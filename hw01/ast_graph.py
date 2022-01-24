import matplotlib.pyplot as plt
import networkx as nx
import ast


node_map = {}
cnt = 0


def map_name(cnt, node):
    # v1
    return str(node.__class__.__name__)[0:10]


def iterate_node(node, parent_cnt, g, off=0):
    global cnt, node_map

    cnt += 1
    mycnt = cnt
    g.add_node(cnt)
    if parent_cnt != -1:
        g.add_edge(parent_cnt, cnt)

    node_map[cnt] = map_name(mycnt, node)

    for child in ast.iter_child_nodes(node):
        print("-"*off + str(child))
        iterate_node(child, mycnt, g, off+2)


if __name__ == '__main__':
    g = nx.DiGraph()
    with open('fib.py', 'r') as f:
        tree = ast.parse(f.read())
        iterate_node(tree, -1, g)

    nx.draw_planar(g, with_labels=True, labels=node_map)
    plt.show()


