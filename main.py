"""
Author: Koala | lchenglin29
enjoy it:D
"""
import time
import curses
import random
import copy

RUN = True
HELP_MSG = """cool
"""

map_by = 1000
map_bx = 1000
render_by = 10
render_bx = 24
map_info = {
    "buildings": [
        ".",
        "w",
        "m"
    ],
    "colors":{
        ".":0,
        "w":1,
        "m":2
    }
}

def guide(stdscr):
    curses.curs_set(0)
    msgs = [
        "Hi",
        "Hi2",
        "Hi3"
    ]
    for i in range(0,len(msgs)):
        stdscr.addstr(i,0,msgs[i])
        stdscr.refresh()

def generate_map(ly,lx):
    map = []
    for i in range(ly+1):
        cache =[]
        if i == 0 or i == ly:
            for j in range(lx+1):
                cache.append("#")
        else:
            for j in range(lx+1):
                if j == 0 or j == lx:
                    cache.append("#")
                else:
                    cache.append(random.choices(map_info["buildings"], [0.9,0.09,0.01],k=1)[0])
        map.append(cache)
    return map

def render_whole_map(map,stdscr):
    for ly in range(len(map)):
        for lx in range(len(map[ly])):
            cache = map[ly][lx]
            if cache in map_info["buildings"]:
                cp = map_info["colors"][cache]
                stdscr.addstr(ly,lx,cache,curses.color_pair(cp))
            elif cache in ['P','#']:
                if cache == 'P':
                    stdscr.addstr(ly,lx,cache,curses.color_pair(3))
                else:
                    stdscr.addstr(ly,lx,cache,curses.color_pair(4))
            else:
                stdscr.addstr(ly,lx,cache)
    stdscr.refresh()

def render_map(y,x,ly,lx,map,stdscr):
    n_map = map[:]
    cache = []
    y_s = 0 if y-ly<0 else y-ly
    y_e = len(map) if y+ly > len(map) else y+ly
    x_s = 0 if x-lx<0 else x-lx
    x_e = len(map[0]) if x+lx > len(map[0]) else x+lx
    n_map[y][x] = 'P'
    for ry in range(y_s,y_e):
        cache2 = []
        for rx in range(x_s,x_e):
            cache2.append(n_map[ry][rx])
        cache.append(cache2)
    render_whole_map(cache,stdscr)

def main(stdscr):
    map = generate_map(map_by,map_bx)
    stdscr.nodelay(True)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    y, x = 0, 0
    while True:
        stdscr.clear()
        #guide(stdscr)
        render_map(y,x,render_by,render_bx,map,stdscr)

        key = stdscr.getch()
        if key != -1:
            if key == ord('q') or key == ord('Q'):
                break
            elif key == curses.KEY_UP:
                if y != 1:
                    y -= 1
            elif key == curses.KEY_DOWN:
                if y != len(map)-2:
                    y += 1
            elif key == curses.KEY_RIGHT:
                if x != len(map[0])-2:
                    x += 1
            elif key == curses.KEY_LEFT:
                if x != 1:
                    x -= 1

        time.sleep(0.01)


curses.wrapper(main)
