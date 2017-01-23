import curses

class CursesMixin(object):
    def cursesStart(self, colour = False):
        self.window = curses.initscr()
        curses.noecho()
        if colour:
            curses.start_color()
            curses.use_default_colors()
            for i in range(0, curses.COLORS):
                curses.init_pair(i + 1, i, -1)

    def cursesEnd(self):
        curses.endwin()

    def drawCursesMessage(self, *args):
        self.window.addstr(*args)
        self.window.refresh()
