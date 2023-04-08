#!/usr/bin/python2
# -*- coding: utf-8 -*-
import datetime
import sys
sys.path.append("../lib/")
import Script

class  WordClock(Script.Script):
    STRUCTURE = (("IT", "IS", "HALF", "TEN", ""),
                 ("QUARTER", "TWENTY", ""),
                 ("FIVE", "MINUTES", "TO"),
                 ("PAST", "TWO", "THREE", ""),
                 ("", "ONE", "FOUR", "FIVE", ""),
                 ("SIX", "SEVEN", "EIGHT"),
                 ("NINE", "TEN", "ELEVEN"),
                 ("", "TWELVE", "O'CLOCK"),
                 )

    def __init__(self):
        super(WordClock, self).__init__()

    def fetchArgParser(self, description=""):
        parser = super(WordClock, self).fetchArgParser(description = description)
        parser.add_argument("-c", "--colour", type = str, default = None)
        return parser

    def _main(self):
        time = datetime.datetime.now()
        texttime = self.getTextTime(time)
        self.printTime(texttime)

    def printTime(self, texttime):
        for line in self.STRUCTURE:
            text = []
            for word in line:
                if not word:
                    text.append(word)
                    continue
                colour = "black"
                bold = 0
                if word == texttime[0]:
                    colour = self.config.colour
                    bold = 1
                    texttime = texttime[1:]
                text.append(self.highlight(word, colour = colour, bold = bold))
            print " ".join(text)
            

    def getTextTime(self, time):
        texttime = ["IT", "IS"]
        texttime.extend(self.textMinute(time.minute))
        texttime.append(self.textHour(time.hour))
        texttime.append("O'CLOCK")
        return texttime

    def textMinute(self, m):
        minutes = []
        m = m // 5
        if m:
            if m == 6:
                minutes.append("HALF")
            elif m % 3 == 0:
                minutes.append("QUARTER")
            else:
                fives = m
                if m > 6:
                    fives = 12 - m
                if fives >= 4:
                    minutes.append("TWENTY")
                elif fives >= 2:
                    minutes.append("TEN")
                if not fives % 2 == 0:
                    minutes.append("FIVE")
                minutes.append("MINUTES")

            if m < 7: # 35m
                minutes.append("PAST")
            else:
                minutes.append("TO")
        return minutes


    def textHour(self, h):
        h = h%12
        return {1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT", 9: "NINE", 10: "TEN", 11: "ELEVEN", 0: "TWELVE"}.get(h, h)

if __name__ == "__main__":
    clock = WordClock()
    clock.main()
