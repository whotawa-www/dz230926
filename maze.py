import random
def mazegen(size):
    maze = []
    for j in range(size):
        maze.append(['██']*size)
    for y in range(1, size-1, 2):
        for x in range(1, size-1, 2):
            maze[y][x] = '  '
    start = (random.randrange(1, size-1, 2), random.randrange(1, size-1, 2))
    in_maze = {start}
    unvisited = []
    for y in range(1, size-1, 2):
        for x in range(1, size-1, 2):
            if (x, y) != start:
                unvisited.append((x, y))
    while unvisited:
        current = random.choice(unvisited)
        mecto = [current]
        max_steps = len(unvisited) * 10
        steps = 0
        while current not in in_maze and steps < max_steps:
            steps += 1
            x, y = current
            directions = []
            for dx, dy in [(2,0), (-2,0), (0,2), (0,-2)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < size-1 and 0 < ny < size-1:
                    directions.append((nx, ny, x+dx//2, y+dy//2))
            if not directions:
                break
            nx, ny, wx, wy = random.choice(directions)
            index_in_path = -1
            for i in range(len(mecto)):
                if mecto[i] == (nx, ny):
                    index_in_path = i
                    break
            if index_in_path != -1:
                mecto = mecto[:index_in_path + 1]
                current = (nx, ny)
            else:
                mecto.append((wx, wy))
                mecto.append((nx, ny))
                current = (nx, ny)
        if current in in_maze:
            for i in range(0, len(mecto), 2):
                node = mecto[i]
                maze[node[1]][node[0]] = '..'
                if i + 1 < len(mecto):
                    proxod = mecto[i+1]
                    maze[proxod[1]][proxod[0]] = '..'
                in_maze.add(node)
            for u in list(in_maze):
                if u in unvisited:
                    unvisited.remove(u)
    maze[1][0] = 'S.'
    maze[size-2][size-1] = '.F'
    return maze
maze = mazegen(25)
stroka = ''
for v in range(len(maze)):
    for g in range(len(maze)):
        stroka += maze[v][g]
    stroka+= '\n'
filee = open("лабиринт.txt", "w", encoding="utf-8")
filee.write(stroka)
filee.close()
