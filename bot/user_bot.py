def script(check, x, y):
    from collections import deque

    if check("gold", x, y) > 0:
        return "take"

    start = (x, y)
    queue = deque([(x, y, None)])
    visited = {start}
    dirs = [("up", 0, -1), ("down", 0, 1), ("left", -1, 0), ("right", 1, 0)]

    while queue:
        cx, cy, first = queue.popleft()
        if (cx, cy) != start and check("gold", cx, cy) > 0:
            return first
        for name, dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if (nx, ny) in visited:
                continue
            if check("wall", nx, ny):
                continue
            visited.add((nx, ny))
            nf = first if first is not None else name
            queue.append((nx, ny, nf))

    return "pass"