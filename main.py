"""
Author: Koala | lchenglin29
enjoy it owo
"""
import time
import curses

RUN = True
HELP_MSG = """cool
"""
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

def main(stdscr):
    while True:
        stdscr.clear()
        guide(stdscr)
        time.sleep(0.01)

curses.wrapper(main)
