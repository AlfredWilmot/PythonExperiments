# -*- coding: utf-8 -*-
"""
Divide and conquer paradiegm:
1) divide into smaller sub-problems
2) use recursion to conquer sub-problems
3) clean-up work to combine together solutions to sub-probllems into overall solution
"""








## Merge-sort Algorithm notes ##

"""
using the "Recursion Tree" method to calculate the amount work done performed by the algorithm.

root level 1: (entire input)
level 1: half on input array
level 2: quarter of input array
...

given that the array length is halved for each recursion level,
size of input array = n = 2^lv, where lv is the base-case level number.

e.g. for arr_len = 8 = 2^3 --> lv = 3, as 8/2 = 4, 4/2 = 2, 2/2 = 1 (basecase),
hence, the maximum level number for any given input array length is:
    lv = log_2(n)

at each level j of the recursion tree, there are 2^j subproblems, as the number of 
subproblems doubles each level (i.e. the number of times the initial array is halved).
The size of the array at level j is original_arr_len / 2^j
"""

"""
The number of sub-problems is doubling with each level of the recursion tree (2^j);
but the amount of work that needs to be done per sub-problem is halving with each
level of the recursion tree n/(2^j). Hence, the total work that needs to be done is 
independent of the number of levels (as these two competing values cancel each other out).

Total number of operations at level j = 2^j x 6(n/(2^j)) = 6n

Hence the total work done by the algorithm is <= 6n(log_2(n) + 1)

i.e. For every input array of length n, the merge-sort algorithm produces
a sorted output array and uses at most 6n*log_2(n) + 6n operations.
"""








## Guiding Principles for Analysis of Algorithms ##

"""
*worst-case analysis* 
-> running time bound holds for every input of length n.
-> no assumptions about nature of input, these solutions are more robust/ general purpose 
-> easier to analyze (due to lack of assumptions)

*average case analysis and benchmarks*
-> requires domain knowledge: an understanding of what the typical inputs are.

*Ignoring small constant factors and lower-order terms*
-> this level of granularity is typically not useful (though epends on context)
-> just makes the analysis easier
-> these factors can "creep in" from various sources, and depend on things like hardware
        architecture/ compiler/ programming language implementation/ etc.

*Asymptotic analysis*
focus on running time for large input sizes n


**Fast Algorithm: worst-case running time grows slowly with input size"**
-> 'sweet spot' for reasoning about algorithms:
    mathematical tractability and predictive power.
    
*Holy grail: as close to linear running time as possible*

"""


        