import curses

def main(stdscr):
    curses.curs_set(1)  # 显示光标

    # 创建一个新的窗口
    win = curses.newwin(5, 30, 5, 5)  # 高度5，宽度30，位置（5, 5）
    win.box()  # 绘制边框

    win.addstr(1, 1, "Enter some text: ")

    win.refresh()

    # 接受用户输入
    text = ""
    while True:
        char = win.getch()

        if char == 10:  # Enter 键
            break
        elif char == 27:  # ESC 键
            break
        else:
            text += chr(char)
            win.clear()
            win.box()
            win.addstr(1, 1, "Enter some text: " + text)
            win.refresh()

    stdscr.clear()
    stdscr.addstr(0, 0, f"You entered: {text}")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
