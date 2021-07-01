# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:21:09 2021

@author: alfre

A collection of my notes from the kaggle Python course:
    https://www.kaggle.com/learn


**Formatting strings in Python:**
    https://pyformat.info/
    https://docs.python.org/3/library/string.html#formatstrings
    
    
An "item" is a key-value pair.

**Dictionaries in Python:**
    https://docs.python.org/3/library/stdtypes.html#dict

"""

import this

"""
These are solutions to problems presented by the author of this course (Colin Morris)
that I felt were particularly elegant and so worth noting down.

"""

"""
## Silly Strings ##
Identifies which of the substrings in the list of strings "documents" contains 
a valid version of the "keyword" string.
"""
def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices










# Examples of string formatting from the Kaggle Python crash-course

planet = "Pluto"
position = 9

print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)