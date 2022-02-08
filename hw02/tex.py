from typing import List, Any
from functools import reduce


def _gen_tex_table_row(row: List[Any]) -> str:
    return reduce(lambda s, e: s + " & " + str(e), row)


def _gen_tex_table_of_width(table: List[List[Any]], width: int) -> str:
    return "\\begin{tabular}{ " + ("c " * width) + "}\n" + \
           reduce(lambda s, e: s + " \\\\\n" + e, map(_gen_tex_table_row, table)) + \
           "\n\\end{tabular}"


def _get_table_width(table: List[List[Any]]) -> int:
    return max(map(len, table))


def gen_tex_table(table: List[List[Any]]) -> str:
    return _gen_tex_table_of_width(table, _get_table_width(table))


if __name__ == '__main__':
    test = [
        ['a', 'bb', 'ccc'],
        ['dddd', 'eeeee', 'ffffff']
    ]
    result = gen_tex_table(test)
    print(result)
    open('artifacts/table.tex', 'w').write(result)
