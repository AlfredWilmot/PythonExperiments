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








## O(nlogn) Algorithm for counting inversions I ##
"""

# inversion def #
Number of inversion = number of array indices pairs (i,j) with i < j and A[i] > A[j].

e.g. 
[1,2,3,4,5] has 0 inversions
[5,4,3,2,1] has 4+3+2+1 = 10 inversions (5>4>3>2>1), (4>3>2>1), (3>2>1), (2>1)

[1,3,5,2,4,6] has 3 inversions: (3,2), (5,2), (5,4)

# motivation #
This algorithm is useful for establishing a "numerical similarity measure
between two ranked lists" (e.g. collaborative filtering)

# defs #
The largest number of inversions that a 6-element array can have is 5+4+3+2+1 = 15
in general, if the array length is n, then the maximum number of inversions 
possible is "n choose 2": n(n-1)/2


# observation #
If an input array A with no split inversions, is split in half into sub arrays
B and C, 
e.g. A:[1,2,3,4,5] --> B:[1,2], C:[3,4,5],
then all elements in B will be less than C, and the merge algorithm will simply
concatenate the two sub-arrays together B+C. Therefore there is a relationship
between the number of split-inversions in the input array A and the number 
of times an element from C is appended to the output array.

"""

## SoMe CoDe ##
def brute_inversion_count(in_arr):
    """
    Brute-force method for counting inversions, inefficient: O(n^2) 
    {quadratic time due to nested for-loop}
    """
    
    inv_cnt = 0
    for i in range(len(in_arr)):
        for j in range(i+1,len(in_arr)):            
            if in_arr[i] > in_arr[j]:
                inv_cnt +=1
                print("A[{}] = {} > A[{}] = {}".format(i,in_arr[i],j,in_arr[j]))
    return inv_cnt


def merge(A,B):
    """
    Merge two sub-arrays together such that the output array contains their 
    sorted values. Note: the sub-arrays must already be in sorted order! 
    """  
    # defining lengths of arrays
    n_a = len(A)
    n_b = len(B)
    n_c = n_a+n_b
    
    # output array of length n_c
    C = []
    
    # indicese used to traverse through A and B arrays, respecitvely
    idx_a = 0
    idx_b = 0
    
    for k in range(n_c):
        
        # basic element wise comparison of either sub-array
        if A[idx_a] < B[idx_b]:
            C.append(A[idx_a])
            idx_a += 1
        else:
            C.append(B[idx_b])
            idx_b += 1
        
        # managing end-cases:    
        # simply append the remainder of the untraversed sub-array
        # when the other sub-array has been fully traversed, 
        # then exit the loop
        if idx_a > n_a-1:
            C+= B[idx_b:]
            break
        elif idx_b > n_b-1:
            C+= A[idx_a:]
            break
    
    return C
    
            

# 
def div_con_inv_cnt(in_arr):
    """
    Recursive method for couting inversions via divide and conquer, better: O(nlogn)
    
    Classify the inversions of an array into three types for form c(i,j) where i < j:
        1) "left-inversion":    {i,j} <= n/2
        2) "right-inversion":   {i,j} > n/2
        3) "split-inversion":   i <= n/2 < j
    
            ("split" --> i is located at the tail of the left array, 
             j is located at the head of the right array)
    
    After the recursion, need to do clean-up and count the number of "split inversions"
    """
    
    n = len(in_arr)
    inv_cnt = 0
    
    if n > 1:
        #inv_cnt += count(1st_half_of_in_arr, n//2)
        #inv_cnt += count(2nd_half_of_in_arr, n//2)
        #inv_cnt += count_split_inv(1st_half_of_in_arr, n//2)
        pass
    
    """
    use merge subroutine (from merge-sort algorithm) to count the number of 
    split inversions.
    "merging two sorted sub-arrays naturally uncovers all the split inversions"
    
    perform sort_and_count on two halves of input array,
    then pass these as inputs to the thirds merge_and_countSplitInv subroutine
    to deal with split-inversion cases
    """
    
    return inv_cnt
        