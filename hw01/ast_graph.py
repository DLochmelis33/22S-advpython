import matplotlib.pyplot as plt
import networkx as nx
import ast

node_map = {}
cnt = 0


def map_name(cnt, node):
    # v1
    if isinstance(node, ast.Constant):
        return ast.unparse(node)
    if isinstance(node, ast.Name):
        return ast.unparse(node)
    if isinstance(node, ast.BinOp):
        return node.op.__class__.__name__
    if isinstance(node, ast.Lt):
        return "<"
    if isinstance(node, ast.Gt):
        return ">"
    return str(node.__class__.__name__)


def iterate_node(node, parent_cnt, g, depth=0):
    global cnt, node_map

    cnt += 1
    mycnt = cnt
    g.add_node(cnt)
    if parent_cnt != -1:
        g.add_edge(parent_cnt, cnt)

    node_map[cnt] = map_name(mycnt, node)

    if node is ast.Name:
        return

    for child in ast.iter_child_nodes(node):
        iterate_node(child, mycnt, g, depth + 1)


if __name__ == '__main__':
    g = nx.DiGraph()
    with open('fib.py', 'r') as f:
        tree = ast.parse(f.read())
        iterate_node(tree, -1, g)

    nx.draw_planar(g, with_labels=True, labels=node_map)
    plt.show()
