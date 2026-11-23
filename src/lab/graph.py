"""Deterministic traversal on unweighted adjacency lists."""
from collections import deque


def breadth_first(graph: dict[str, list[str]], start: str) -> list[str]:
    seen = {start}
    pending = deque([start])
    order = []
    while pending:
        node = pending.popleft()
        order.append(node)
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append(neighbor)
    return order


def shortest_path(graph: dict[str, list[str]], start: str, target: str) -> list[str] | None:
    pending = deque([(start, [start])])
    seen = {start}
    while pending:
        node, route = pending.popleft()
        if node == target:
            return route
        for neighbor in sorted(graph.get(node, [])):
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append((neighbor, route + [neighbor]))
    return None
