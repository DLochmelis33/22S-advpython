import time, os
from my_package import ast_graph

#"\\usepackage[margin=0pt]{geometry}\n"

def gen_tex_header() -> str:
    return  ("\\documentclass[a4paper]{article}\n"
            "\\usepackage{graphicx}\n"
            "\n"
            "\\begin{document}\n"
            "\n")

def gen_tex_footer() -> str:
    return  ("\n"
            "\\end{document}\n")


def gen_image_tex(image_path: str) -> str:
    return ('\\begin{center}\n'
            '\\includegraphics[width=\\textwidth]{' + image_path + '}\n'
            '\\end{center}\n')


def image_to_tex_pdf(image_path: str):
    fname = 'artifacts/result'
    with open(fname, "w") as f:
        f.write(gen_tex_header() + gen_image_tex(image_path) + gen_tex_footer())
    # file is written for sure
    os.system(f'pdflatex -halt-on-error -interaction=nonstopmode {fname}')
    os.remove(fname)


if __name__ == '__main__':
    ast_graph.generate_ast(open('a.py', 'r'))
    image_to_tex_pdf('artifacts/ast.png')
