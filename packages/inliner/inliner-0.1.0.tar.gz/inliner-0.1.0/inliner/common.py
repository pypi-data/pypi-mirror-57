import astor
from astor.code_gen import SourceGenerator
import textwrap
import itertools
import ast
import re

SEP = '___'
COMMENTS = False


def parse_stmt(s):
    return ast.parse(s).body[0]


def parse_expr(s):
    return parse_stmt(s).value


class RemoveSuffix(ast.NodeTransformer):
    def visit_Name(self, name):
        parts = name.id.split(SEP)
        if len(parts) > 1:
            name.id = parts[0]
        return name


class SourceGeneratorWithComments(SourceGenerator):
    def visit_Str(self, node):
        global COMMENTS
        if COMMENTS and \
           '__comment' in node.s:
            s = node.s[10:]
            call = parse_expr(textwrap.dedent(s))
            RemoveSuffix().visit(call)
            s = a2s(call)
            indent = self.indent_with * self.indentation
            comment = '\n'.join([f'{indent}# {part}'
                                 for part in s.split('\n')][:-1])
            self.write('#\n' + comment)
        else:
            super().visit_Str(node)


def a2s(a, comments=False):
    global COMMENTS
    COMMENTS = comments
    outp = astor.to_source(a,
                           source_generator_class=SourceGeneratorWithComments)
    return re.sub(r'^\s*#\s*\n', '\n', outp, flags=re.MULTILINE)


# https://stackoverflow.com/questions/3312989/elegant-way-to-test-python-asts-for-equality-not-reference-or-object-identity
def compare_ast(node1, node2):
    if type(node1) is not type(node2):
        return False
    if isinstance(node1, ast.AST):
        for k, v in vars(node1).items():
            if k in ('lineno', 'col_offset', 'ctx'):
                continue
            if not compare_ast(v, getattr(node2, k)):
                return False
        return True
    elif isinstance(node1, list):
        return all(itertools.starmap(compare_ast, zip(node1, node2)))
    else:
        return node1 == node2


class ObjConversionException(Exception):
    pass


def obj_to_ast(obj):
    if isinstance(obj, tuple):
        return ast.Tuple(elts=tuple(map(obj_to_ast, obj)))
    elif isinstance(obj, dict):
        k, v = unzip([(obj_to_ast(k), obj_to_ast(v)) for k, v in obj.items()])
        return ast.Dict(k, v)
    elif isinstance(obj, list):
        return ast.List(list(map(obj_to_ast, obj)))
    elif isinstance(obj, type):
        return ast.Name(id=obj.__name__)
    elif isinstance(obj, int):
        return ast.Num(obj)
    elif isinstance(obj, str):
        return ast.Str(obj)
    elif obj is None:
        return ast.NameConstant(None)
    elif isinstance(obj, (typing._GenericAlias, typing._SpecialForm)):
        # TODO: types
        # issue was in pandas, where importing pandas._typing.Axis would
        # resolve module to typing, attempt to do "from typing import Axis"
        return ast.NameConstant(None)
    elif callable(obj):
        return ast.NameConstant(None)
    else:
        raise ObjConversionException(f"No converter for {obj}")


def can_convert_obj_to_ast(obj):
    try:
        obj_to_ast(obj)
        return True
    except ObjConversionException:
        return False


def robust_eq(obj1, obj2):
    import pandas as pd
    import numpy as np

    if isinstance(obj1, pd.DataFrame) or isinstance(obj1, pd.Series):
        return obj1.equals(obj2)
    elif isinstance(obj1, np.ndarray):
        return np.array_equal(obj1, obj2)
    elif isinstance(obj1, tuple) or isinstance(obj1, list):
        return all(map(lambda t: robust_eq(*t), zip(obj1, obj2)))
    else:
        return obj1 == obj2
