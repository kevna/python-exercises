import argparse
import sys

class Script(object):
    def __init__(self):
        self.config = None

    def fetchArgParser(self, description = ""):
        parser = argparse.ArgumentParser(description = "%s: %s"%(self.__class__.__name__, description))
        return parser

    def validateConfig(self):
        pass

    def main(self):
        self.config = self.fetchArgParser().parse_args()
        self.validateConfig()
        try:
            self._main()
        except KeyboardInterrupt:
            sys.exit(0)

    def highlight(self, message, colour = None, bold = 0):
        text = message
        colourMap = {"black": 0,
                     "red": 1,
                     "green": 2,
                     "yellow": 3,
                     "blue": 4,
                     "purple": 5,
                     "bright": 7,
                     }
        if colour in colourMap or bold:
            colourCode = "3%d"%colourMap.get(colour, 7)
            if bold:
                colourCode = "%s;%d"%(colourCode,bold)
            text = "\033[%sm%s\033[m"%(colourCode, message)
        return text

    def _main(self):
        raise NotImplementedError()
