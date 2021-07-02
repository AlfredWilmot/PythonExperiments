# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 00:19:59 2021

Comparing the Merge Sort algorithm against other more basic sorting algorithms.
This demonstrates the benefit of the "divide and conquer" paradigm.

implement insertion, selection, and bubble sort algorithms, and compare these to merge sort.

@author: alfred
"""





"""
An implementation of a type of insertion sorting algorithm
whereby each value in the unsorted part of the list is compared against
the last value (tail) of the sorted part of the list which is gradually grown
as the algorithm proceeds until all parts of the list have been sorted.

Scales exponentially with list size: O(n^2).
"""
def insertion_sort(in_arr, debug = False):
    
    # points to the tail of the sorted part of the list
    swap_idx = 0
    
    # indicates whether values were swapped around
    swap = True
    
    # Only measure array length once then store value for future reference
    len_arr = len(in_arr)
    
    # containers for swapping values in the list
    tmp0 = 0
    tmp1 = 0
    
    # keep traversing list until the sorted list tail passess through the whole list
    while swap_idx < (len_arr-1):
        
        # visualizing the list as it is being sorted.
        if debug: print(in_arr)
        
        # keep going through the list from the tail of the sorted part until no swaps are made
        while swap:
            
            swap = False
            
            for i in range(swap_idx,len_arr):
                
                # swap value from the sorted list tail with the new smaller value
                if in_arr[swap_idx] > in_arr[i]:
                    tmp0 = in_arr[swap_idx]
                    tmp1 = in_arr[i]
                    in_arr[swap_idx] = tmp1
                    in_arr[i] = tmp0
                    
                    # indicate that a swap occured
                    swap = True
        
        # increment the pointer to the sorted list tail until while input list is traversed
        swap_idx+=1
        swap = True
        
    return(in_arr)
                
         

"""
An implementation of a merge-sort algorithm that utilizes the "divide and conquer technique".
divide:
 - The input list is recursively split into halves until each sub-list consists of individual elements.
conquer:
 - the sub-lists are then sorted into ascending order and then recursively merged to give the final sorted array.
 
 
Useful resource: https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm

"""
def merge_sort(arr,debug=False):
    
    if debug: print("Sublist: " + str(arr))
    
    # split the input array into two halves 
    n = int(len(arr)/2)
    
    # Once the array has been halved enough times that only 
    if len(arr) == 1:
        
        return arr
    
    elif len(arr) > 1:
        
        arr0 = merge_sort(arr[:n])
        arr1 = merge_sort(arr[n:])
          
        return merge(arr0,arr1,debug)
    

def merge_v0(arr0,arr1,debug=False):
    """
    my first version of the merge algorithm: here I'm trying to utilize the memory 
    already used for the input arrays instead of making new variables to hold data.s
    """
    
    merged_arr = []
    
    while(len(arr0) > 0 and len(arr1) > 0):

        if arr0[0] > arr1[0]:
            merged_arr.append(arr1.pop(0))
        else:
            merged_arr.append(arr0.pop(0))
    
    while(len(arr0) >0):
        merged_arr.append(arr0.pop(0))
        
    while(len(arr1) > 0):
        merged_arr.append(arr1.pop(0))
    
    if debug: print("Merged: " + str(merged_arr))
    
    return merged_arr



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
    
    # single for-loop, linear time O(n) #
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


"""
Here I will compare the efficiencies of each sorting algorithm impementation with respect to execution time.

Resource covering the timeit module: https://www.geeksforgeeks.org/timeit-python-examples/
"""
import timeit
import cProfile
import random as rand
    

if __name__ == "__main__":

    # creating a random array of numbers that needs to be sorted
    n=100
    # C = [round(rand.random()*n) for x in range(1,n+1)]
    
    print("For an unsorted input array of length " + str(n))
    
    SETUP_CODE  = """
from __main__ import insertion_sort
from __main__ import merge_sort
import random as rand
    """
    
    TEST_CODE   = """
n=100
C = [round(rand.random()*n) for x in range(1,n+1)]    
insertion_sort(C)
    """
    solving_latency0 = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 3, number = 1000)
    print("Solving latency of Insertion-sort: {}".format(min(solving_latency0)))
    
    
    TEST_CODE   = """
n=100
C = [round(rand.random()*n) for x in range(1,n+1)]    
merge_sort(C)
    """
    solving_latency1 = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE, repeat = 3, number = 1000)
    print("Solving latency of Merge-sort: {}".format(min(solving_latency1)))
    
    print("Merge-sort is " + "%.2f"%(min(solving_latency0)/min(solving_latency1)) + " times faster than Insertion-sort.")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
