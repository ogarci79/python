#!/usr/bin/env python

import sys, time
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg 

class PatMatch :
    def __init__(self) :
        self.patterns = []      # To match against
        self.matches  = []      # matches (pattern,nchar) found so far
        self.working  = [0]*50  # Partial matches -> [0]*50 creates a list, len(50), instantiated with zero's
        self.worktop  = 0       # Limit for partials
        self.chars    = ""

    def addPattern(self, pattern) :
        # Add a pattern with its call back function
        self.patterns.append(pattern)

    def seeChar (self,ch) :
        # a new char to be handled
        # if char starts a pattern - add it to top of workspace
        pos=len(self.chars)
        self.chars += ch
        for p in self.patterns :
            if ch == p[0][0] :  # Check the first letter of patterns to see if the char matches, if so potential partial
                # partial match has pattern pointer and # chars matched
                self.working[self.worktop]=(p, pos, 0, "partial")
                self.worktop += 1
                print("self.working: " , self.working)
                print("self.worktop: " , self.worktop)
                #time.sleep(15)

        wp=wkeep = 0            # work-pointer, work-keepers
        while wp < self.worktop :
            # wpat is pattern, wcp chars matched so far
            wpat,wpos,wcp,wsts = self.working[wp]
            if wsts == "complete" : wkeep += 1 # leave in workspace
            elif wpat[wcp] == ch :
                # new character continues the match
                wcp += 1 
                if wcp >= len(wpat) :
                    # Oh. the new char has completed match 
                    self.matches.append((wpat,self.chars))
                    self.working[wkeep] = (wpat,wpos,wcp,"complete")
                    wkeep += 1
                else :
                    # Still more to match.  tuck partila match in 
                    self.working[wkeep]=(wpat,wpos,wcp,"parital ")
                    wkeep += 1 # Adjust new worktop, keeping partial 
            else : pass     # don't advance wkeep (drop failed partial)
            wp += 1
        self.worktop = wkeep    # set worktop to matches kept

    def dump (self) :
        print "Patterns: %s" % " ".join(self.patterns)
        print "Chars seen: ", self.chars
        for wp in range (self.worktop) :
            wpat,wpos,wcp,wsts = self.working[wp]
            print "Found %s %s={%s-%s}" % (wsts,wpat,wpos,wpos+wcp-1)



def main():
    pm=PatMatch()
    text=sys.argv[1]
    for pat in sys.argv[2:] : pm.addPattern(pat)

    for ch in text :
        pm.seeChar(ch)
        sys.stdout.write('\033[1;1H\033[J\n') # clear screen
        pm.dump()                             # produce animation frame
        time.sleep(.5)
    print "Done", len(pm.matches),"matches:"

if __name__ == "__main__":
    main()

