# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 17:09:26 2021

@author: Alfred

Algorithms for couting the number of inversions in an input array.


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

# General claim#
The spilit inversions involving an element y of the 2nd array C equals 
the number left in the first array B when y is copied to the output array D.

"""









## --------------------------------------------------------------------------#
## A simple O(n^2) algorithm for counting inversions using nested for loops ##
## --------------------------------------------------------------------------#
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









## ----------------------------------------------------------------------------------------------------#
## A more complext implementation, but much more efficient O(nlogn) Algorithm for counting inversions ##
## ----------------------------------------------------------------------------------------------------#
def merge_and_countSplitInv(A,B):
    """
    Same as the merge function from merge-sort, 
    except now counting the nubmer of split inversions too.
    """
    # defining lengths of arrays
    n_a = len(A)
    n_b = len(B)
    n_c = n_a+n_b
    
    # output array of length n_c
    C = []
    
    # tracks the number of split-inversions
    split_inv_cnt = 0
    
    # indicese used to traverse through A and B arrays, respecitvely
    idx_a = 0
    idx_b = 0
    
    # single for-loop, linear time O(n) #
    for k in range(n_c):
        
        # basic element wise comparison of either sub-array
        if A[idx_a] > B[idx_b]:
            C.append(B[idx_b])
            idx_b += 1
            
            # in this condition there is at least one split inversion,
            # corresponding to the number of elements remaining in array A
            split_inv_cnt += len(A) - idx_a
            
        else:
            C.append(A[idx_a])
            idx_a += 1
        
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
    
    return split_inv_cnt, C




def div_con_inv_cnt(in_arr):
    """
    Recursive method for couting inversions via divide and conquer, efficient: O(nlogn)
    {logarithmic-linear time due to recursion}

    """
    
    n = len(in_arr)
    inv_cnt = 0
    
    if n <= 1:
        return inv_cnt, in_arr
    
    else:
        c0, A = div_con_inv_cnt(in_arr[:n//2])
        c1, B = div_con_inv_cnt(in_arr[n//2:])
        
        inv_cnt += c0 + c1
        
        
        c2, C = merge_and_countSplitInv(A, B)
        
        inv_cnt += c2
        
        return inv_cnt, C
