import re
from ApproximateSearch import ApproximateSearch
import numpy as np
import time


class CDPMatcher(object):
    pattern = ""
    string = []
    nonSolid = {}
    location = []
    fakematch = True
    Occurrence = []
    
"""The String Pair is a representation of the sequence, pattern and the upper bound as one object with these three variables"""


class String_pair(object):
    pattern = ""
    string = []
    variable = 0

    def __init__(self, pattern, string, variable):
        self.pattern = pattern
        self.string = string
        self.variable = variable


"""Constructs a pattern, sequence and variable object"""
def make_pair(pattern, string, variable):
    pair = String_pair(pattern, string, variable)
    return pair

"""The method 'find_pattern' searches the pattern given in O(n)time to find any degeneracys. It then stores the index of the non-solid in 'location' and the non-solid options in 'nonSolid'then returns the new patterns with character '%' at the location of degeneracy"""
def find_pattern(pattern):

    pattern = pattern
    l = list(pattern)
    nonSolid = {}
    location = []

    prog = re.compile('\[(.+?)]')

    i = 0
    j = 0
    for h in re.finditer(prog, pattern):
            # print h.group(0), h.start(), h.end()
            nonSolid[h.start()-j] = cleanup(''.join(l[h.start()-j+1:h.end()-j-1]))
            location.append(h.start()-j)
            location.sort()
            l[h.start()-j:h.end()-j] = "$"
            j = j + h.end() - 1 - h.start()
            i += 1
    CDPMatcher.nonSolid = nonSolid
    CDPMatcher.location = location
    #print nonSolid
    return ''.join(l)

"""This method takes the parameter as a string and returns a list of characters"""
def cleanup(set):
    setList = list(set)
    return setList

"""This method creates a string_pair from the parameters and goes on to output the indexes of any successful matchesfrom the algorithm"""


def patternMatcher(pattern, string, variable):

    Occ = CDPMatcher.Occurrence = []
    pair = make_pair(pattern, string, variable)
    pattern = pair.pattern
    string = pair.string
    sLength = len(string)
    l = find_pattern(pattern)
    print pattern
    location = CDPMatcher.location
    nonSolid = CDPMatcher.nonSolid
    pLength = l.__len__()
    k = pair.variable
    _concat = string+l+'#'
    tree = ApproximateSearch(_concat)

    approxmatch = []

    Mismatch = np.zeros((sLength-pLength+1, k+1), dtype=np.int32)

    """"This fills our mismatch array to find instances of approximate matches"""
    for i in range(sLength-pLength+1):
        f = 0
        for j in range(0, k+1):
            Mismatch[i][j] = f + tree.lcpair(tree.suffixes[i+f], tree.suffixes[sLength + f])
            f = Mismatch[i][j] + 1
        if Mismatch[i][k] == pLength:
            approxmatch.append(i)
    #print approxmatch
    if not approxmatch:
        print "NO MATCH"

    del Mismatch

    """Based on the results of approximate match, this segment searches the locations of non-solid positions to identify if the mismatch was in fact a correct match, to finally output the indexes"""
    for i in approxmatch.__iter__():
        testPostion = i
        fake_match = True
        for j in range(k):
            print k
            sequencePosition = location[j]
            letter = string[sequencePosition + testPostion]
            this = nonSolid.__getitem__(sequencePosition)
            if letter not in this:
                fake_match = False

        if fake_match:
            Occ.append(testPostion+1)

    print approxmatch
    del approxmatch
    print Occ

    if Occ.__sizeof__() < 1:
        print 'NEGATIVE MATCH'

    return Occ
