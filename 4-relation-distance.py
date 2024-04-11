from typing import Tuple, List, Dict

amount = int(input())

members = [(int(member[0]), int(member[1])) for member in [input().split() for _ in range(amount - 1)]]


def find_root_node(relations: List[Tuple[int, int]]):
    parents = set()
    children = set()

    for parent, child in relations:
        parents.add(parent)
        children.add(child)

    return parents.difference(children).pop()


def build_family_tree(relations: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    tree = {}

    for parent, child in relations:
        if parent not in tree:
            tree[parent] = []

        if child not in tree:
            tree[child] = []

        tree[parent].append(child)
        tree[child].append(parent)

    return tree


def bfs(tree: Dict[int, List[int]], start: int) -> Tuple[int, int]:
    visited = set()
    queue = [(start, 0)]

    furthest_node = start
    max_distance = 0

    while queue:
        node, distance = queue.pop()

        if distance > max_distance:
            furthest_node = node
            max_distance = distance

        for neighbor in tree[node]:
            if neighbor in visited:
                continue

            visited.add(node)
            queue.append((neighbor, distance + 1))

    return furthest_node, max_distance


family_tree = build_family_tree(members)

furthest_node, _ = bfs(family_tree, find_root_node(members))
_, max_distance = bfs(family_tree, furthest_node)

print(max_distance)
