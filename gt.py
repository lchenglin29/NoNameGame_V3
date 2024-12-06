import curses
from random import randint

# 生成迷宮
def generate_maze(width, height):
    maze = [['#' if x == 0 or y == 0 or x == width - 1 or y == height - 1 else ' ' for x in range(width)] for y in range(height)]
    for _ in range((width * height) // 4):  # 隨機生成障礙物
        x, y = randint(1, width - 2), randint(1, height - 2)
        maze[y][x] = '#'
    maze[1][1] = 'P'  # 玩家起點
    maze[height - 2][width - 2] = 'E'  # 終點
    return maze

# 畫迷宮
def draw_maze(stdscr, maze):
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            stdscr.addch(y, x, char)

# 主遊戲邏輯
def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    width, height = 20, 10
    maze = generate_maze(width, height)
    player_pos = [1, 1]

    while True:
        stdscr.clear()
        draw_maze(stdscr, maze)
        stdscr.refresh()

        key = stdscr.getch()
        new_pos = player_pos[:]

        if key == curses.KEY_UP:
            new_pos[1] -= 1
        elif key == curses.KEY_DOWN:
            new_pos[1] += 1
        elif key == curses.KEY_LEFT:
            new_pos[0] -= 1
        elif key == curses.KEY_RIGHT:
            new_pos[0] += 1

        # 確認移動是否合法
        if maze[new_pos[1]][new_pos[0]] != '#':
            maze[player_pos[1]][player_pos[0]] = ' '
            player_pos = new_pos
            maze[player_pos[1]][player_pos[0]] = 'P'

        # 判斷是否到達終點
        if player_pos == [width - 2, height - 2]:
            stdscr.addstr(height // 2, width // 2 - 5, "You Win!")
            stdscr.refresh()
            stdscr.getch()
            break

curses.wrapper(main)
