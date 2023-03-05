# python3
import numpy
import sys
import threading


def compute_height(n, parents):
    levels = [0]*n
    max_height = 0

    def heights(element):
        if element == -1:
            return 0
        if levels[element] != 0:
            return levels[element]
        level = heights(parents[element]) +1
        levels[element] = level
        return level

    for i in range(n):
        max_height = max(max_height, heights(i))
        
    return max_height


def main():
    n = input()
    parents = input()
    #parents = parents.split()
    #parents = map(int, parents)
    #parents = list(parents)

    if "I" in n:
        n = int(input())
        parents = input()
        parents = parents.split()
        parents = map(int, parents)
        parents = list(parents)
        print(parents)
        print(compute_height(n, parents))
        
        
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    ## input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
