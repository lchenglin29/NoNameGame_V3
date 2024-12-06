import curses

def main(stdscr):
    # 初始化
    curses.curs_set(1)  # 显示光标
    stdscr.clear()

    # 创建一个新的窗口
    win = curses.newwin(5, 30, 5, 5)  # 高度5，宽度30，位置（5, 5）
    win.box()  # 绘制边框

    win.addstr(1, 1, "Enter some text: ")
    win.refresh()

    # 接受用户输入
    text = ""
    while True:
        char = win.getch()

        if char == 10:  # Enter 键，结束输入
            break
        elif char == 27:  # ESC 键，退出
            break
        elif char == 127:  # 退格键（删除字符）
            text = text[:-1]  # 删除最后一个字符
        else:
            text += chr(char)  # 添加输入的字符

        # 更新窗口内容
        win.clear()
        win.box()
        win.addstr(1, 1, "Enter some text: " + text)
        win.refresh()

    stdscr.clear()
    stdscr.addstr(0, 0, f"You entered: {text}")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
