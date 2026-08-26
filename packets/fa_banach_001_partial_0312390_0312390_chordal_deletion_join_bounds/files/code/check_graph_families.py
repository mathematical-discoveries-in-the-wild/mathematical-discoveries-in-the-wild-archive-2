"""Brute-force chordal-deletion checks for small cycle examples."""

from itertools import combinations


def cycle(n):
    return set(range(n)), {
        frozenset((i, (i + 1) % n)) for i in range(n)
    }


def join(graphs):
    vertices = set()
    edges = set()
    blocks = []
    offset = 0
    for old_vertices, old_edges in graphs:
        mapping = {v: v + offset for v in old_vertices}
        block = {mapping[v] for v in old_vertices}
        blocks.append(block)
        vertices |= block
        edges |= {
            frozenset((mapping[u], mapping[v]))
            for u, v in map(tuple, old_edges)
        }
        offset += len(old_vertices)
    for i, left in enumerate(blocks):
        for right in blocks[i + 1 :]:
            edges |= {frozenset((u, v)) for u in left for v in right}
    return vertices, edges


def induced(edges, keep):
    keep = set(keep)
    return keep, {edge for edge in edges if edge <= keep}


def chordal(vertices, edges):
    """Directly exclude induced cycles; intended only for tiny test graphs."""
    vertices = set(vertices)
    for size in range(4, len(vertices) + 1):
        for subset_tuple in combinations(sorted(vertices), size):
            subset = set(subset_tuple)
            selected = [edge for edge in edges if edge <= subset]
            degree = {vertex: 0 for vertex in subset}
            neighbors = {vertex: set() for vertex in subset}
            for edge in selected:
                left, right = tuple(edge)
                degree[left] += 1
                degree[right] += 1
                neighbors[left].add(right)
                neighbors[right].add(left)
            if len(selected) != size or any(value != 2 for value in degree.values()):
                continue
            start = next(iter(subset))
            reached = {start}
            frontier = [start]
            while frontier:
                current = frontier.pop()
                fresh = neighbors[current] - reached
                reached |= fresh
                frontier.extend(fresh)
            if reached == subset:
                return False
    return True


def chordal_vertex_deletion_number(vertices, edges):
    for k in range(len(vertices) + 1):
        for deleted in combinations(sorted(vertices), k):
            keep = vertices - set(deleted)
            if chordal(*induced(edges, keep)):
                return k
    raise AssertionError("unreachable")


for length in (4, 5, 7):
    graph = cycle(length)
    assert not chordal(*graph)
    value = chordal_vertex_deletion_number(*graph)
    assert value == 1, (length, value)
    print(f"cycle C_{length}: cvd={value}")

joined = join([cycle(4), cycle(4)])
joined_value = chordal_vertex_deletion_number(*joined)
assert joined_value == 3, joined_value
print(f"join C_4 vee C_4: cvd={joined_value} (not 2)")
