import argparse
import sys

class Script(object):
    def __init__(self):
        self.config = None

    def fetchArgParser(self, description=""):
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


    def _main(self):
        pass
