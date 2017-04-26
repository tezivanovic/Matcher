from CDPMatcher import *
import sys
from multiprocessing import *
from CDPMatcher import patternMatcher

"""DNA Match is an separate class containing the dictionary of DNA sequences and performs multiple pattern matcher functions"""

class DNAMatch(object):
    results = {}
    fullset = []
    indexset = []
    onlymatch = []

    def __init__(self, string):
        for i in range(len(string)):
            self.fullset.append(None)
            self.indexset.append(i)
        self.string = string.upper()
        if string == file:
            f = open(string, "r")
            self.string = f.read().upper()
        self.matchAll()
        
    """matchAll creates a Pool to run mulitple pattern matchers in parallel"""
    def matchAll(self):
        results = self.results
        fullset = self.fullset
        indexset = self.indexset
        for it in codonPatterns.iterkeys():
            pm = patternMatcher(it, self.string, 1)
            pool = Pool(22)
            pool.apply_async(pm)
            if pm:
                results.__setitem__(codonPatterns[it], pm)
                for i in pm:
                    self.onlymatch.append(i)
                    match = codonPatterns[it]
                    fullset[i] = match
                    indexset[i] = match
                print 'POSITIVE MATCH FOR '+codonPatterns[it]


        '''for i in nonDegenPatterns.iterkeys():
            pool = Pool()
            pm = patternMatcher(i, self.string, 0)
            pool.apply_async(pm)
            if pm:
                print 'POSITIVE MATCH FOR '+nonDegenPatterns[i]'''

        self.onlymatch.sort()
        print self.indexset

        print self.results


codonTest = ['TT[TC]', 'TT[AG]', 'GC[TCAG]']

codonPatterns = {
        'TT[TC]': 'Phenylalanine',
        'TT[AG]': 'Leucine',
        'CT[TCAG]': 'Leucine',
        'AT[TCA]': 'Isoleucine',
        'GT[CTAG]': 'Valine',
        'TC[TCAG]': 'Serine',
        'CC[TCAG]': 'Proline',
        'AC[CTAG]': 'Threonine',
        'GC[TCAG]': 'Alanine',
        'TA[TC]': 'Tyrosine',
        'CA[TC]': 'Histidine',
        'CA[AG]': 'Glutamine',
        'AA[AT]': 'Asparagine',
        'AA[AG]': 'Lysine',
        'GA[TC]': 'Aspartic Acid',
        'GA[AG]': 'Glutamic Acid',
        'TG[TC]': 'Cysteine',
        'CG[CATG]': 'Arginine',
        'AG[TC]': 'Serine',
        'AG[GA]': 'Arginine',
        'GG[TCAG]': 'Glycine',
        'TA[AG]': 'Stop'
}

nonDegenPatterns = {
    'ATG': 'Methionine',
    'TGG': 'Tryptophan',
    'TGA': 'Stop'
}

"""The following were used during implementation for testing purposes"""
pattern2 = 'ab[ac]d[abc]'
string3 = 'abadaabcdcabadaabcdcabadaabcdcabadaabcdcabadaabcdcabadaabcdc' \
    'abadaabcdcabadaabcdcabadaabcdcabadaabcdcabadaabcdcabadaabcdc' \
    'abadaabcdcabadaabcdcabadaabcdcabadaabcdc'

pattern1 = 'ab[ac]d'
pattern3 = 'ab[ac]d[abc][ab]'

string1 = 'abadaabcdcabadaabcdcabadaabcdcabadaabcdcabadaabcdcabadaabcdc'
string2 = 'abadaabcdcabadaabcdcabadaabcdcabadaabcdcabadaabcdcabadaabcdca' \
    'badaabcdcabadaabcdc'

'''start_time = time.time()
patternMatcher(pattern1, string1, 1)
print string1.__len__()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
patternMatcher(pattern2, string1, 2)
print string1.__len__()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
patternMatcher(pattern3, string1, 3)
print string1.__len__()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
patternMatcher(pattern1, string2, 1)
print string2.__len__()
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

patternMatcher(pattern2, string2, 2)
print string2.__len__()
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()

patternMatcher(pattern3, string2, 3)
print string2.__len__()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
patternMatcher(pattern1, string3, 1)
print ("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
patternMatcher(pattern2, string3, 2)
print string3.__len__()
print("--- %s seconds ---" % (time.time() - start_time))'''

'''start_time = time.time()
patternMatcher(pattern3, string3, 3)
print("--- %s seconds ---" % (time.time() - start_time))'''

