"""The suffix represents a node on the tree.
The method that follows actually creates a 'Suffix Array'"""

class Suffix(object):
    index = 0
    string = ""

    def __init__(self, string, index):
        self.string = string
        self.index = index

    def length(self):
        return len(self.string) - self.index

    def charAt(self, index):
        return self.string[self.index + index]

    def substring(self):
        return self.string[self.index:]

    def __str__(self):
        return 'index '+str(self.index)+', String ' +self.string

"""Approximate search uses a modified Ukkenens algorithm to construct a Suffix-Array"""
class ApproximateSearch(object):
    LCPCAPACITY = 5000
    string = ''
    suffixes = [LCPCAPACITY]
    lcp = []

    def __init__(self, string):
        self.string = string
        self.buildSA(string)

    def __repr__(self):
        print self.string

    """This method constructs the array from the parameter 'string'"""
    def buildSA(self, string):

        self.N = len(string)
        self.suffixes = []
        for i in range(0, self.N):
            self.suffixes.append(Suffix(string, i))
            #print self.suffixes.__getitem__(i)
        self.suffixes.sort()
        self.buildLCP(string)
        #print self.lcp

    """This returns the LCP of a single suffix using the--><--"""
    def getLCP(self, i):
        return self.lcpair(self.suffixes[i], self.suffixes[i-1])

    """build LCP construct the LCP array"""
    def buildLCP(self, string):
        for i in range(1, len(string)):
            if i < 1:
                raise IndexError
            self.lcp = [1]*len(string)
            self.lcp[i] = self.lcpair(self.suffixes[i], self.suffixes[i-1])
            return self.lcp[i]
        #print self.lcp

    """LCPair constructs the LCP from two suffix parameters"""
    @staticmethod
    def lcpair(suffix1, suffix2):
        n = min(suffix1.length(), suffix2.length())
        for i in range(n):
            if not suffix1.charAt(i) == suffix2.charAt(i):
                return i
        return n
