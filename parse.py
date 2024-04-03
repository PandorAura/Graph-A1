import graph


class Tree:
    """
    A tree represented as a dictionary mapping a vertex to a tree node
    """


class TreeNode:
    """
    A tree node with three members: parent: TreeNode or None, children: list of TreeNode, level
    """


def bfs(g, s):
    """
    Performs a Breadth-First search of the graph g, starting from vertex s, in forward direction
    :param g: the graph to be searched
    :param s: the vertex
    :return: a dictionary mapping accessible vertices to the corresponding TreeNode information
    """
    tree = {}
    q = [s]
    tree[s] = TreeNode()
    tree[s].parent = None
    tree[s].level = 0
    tree[s].children = []
    head = 0
    tail = 1
    while head < tail:
        x = q[head]
        head += 1
        for y in g.parse_nout(x):
            if y not in tree.keys():
                q.append(y)
                tree[y] = TreeNode()
                tree[s].parent = x
                tree[s].level = tree[x].level + 1
                tree[s].children = []
    pass


def shortest_path(g, s, t):
    bfs(g, s)


def main():
    # g = graph.
    pass


if __name__ == "__main__":
    main()
