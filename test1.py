import curses

def main(stdscr):
    curses.curs_set(0)  # 隱藏游標
    stdscr.nodelay(True)  # 設置為非阻塞模式
    stdscr.timeout(100)  # 設置輸入超時（毫秒）

    stdscr.addstr(0, 0, "Press any key (or 'q' to quit):")

    while True:
        key = stdscr.getch()  # 非阻塞檢測按鍵
        if key == ord('q'):  # 偵測 'q'
            break
        elif key != -1:  # 若有按鍵輸入
            stdscr.addstr(1, 0, f"Key pressed: {chr(key)}          ")

curses.wrapper(main)
