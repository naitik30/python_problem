# Given an array, we need to modify values of this array in such a way that sum of absolute differences between two
# consecutive elements is maximized. If the value of an array element is X, then we can change it to either 1 or X.


# Input  : arr[] = [3, 2, 1, 4, 5]
# Output : 8
# We can modify above array as,
# Modified arr[] = [3, 1, 1, 4, 1]
# Sum of differences =
# |1-3| + |1-1| + |4-1| + |1-4| = 8
# Which is the maximum obtainable value
# among all choices of modification.
#
# Input  : arr[] = [1, 8, 9]
# Output : 14

def maxisum(datalist):
    difflist =[[0,0]for i in range(len(datalist))]

    for i in range(len(difflist)-1):
        difflist[i+1][0]= max(difflist[i][0],difflist[i][1] + abs(1-datalist[i]))
        difflist[i + 1][1] = max(difflist[i][0] + abs(datalist[i + 1] - 1),
                           difflist[i][1] + abs(datalist[i + 1] - datalist[i]));
        print(difflist)
    print(difflist)
if __name__ == "__main__":
    maxisum([1,8,9])