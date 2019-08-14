# Given an array of different lengths of rods and a number of desired equal length cuts (a, k),
# determine the maximum length of equal cuts that can satisfy the desired number of
# equal length cuts

# Example : Given lengths of 1,2,5,9 and number of desired cuts to be 4,
# the answer is 3. This is because you can create:

# - 1 cut of length 3 from rod of length 5
# - 3 cuts of length 3 from rod of length 9

# As a result, 1+3 = 4 which satisfies the number of cuts, and therefore is also 
# max length we can use to satisfy the desired cuts.

# Notice if we try lengths of 4, we can not satisfy the desired number of equal 
# cuts of 4. This is because you can only create:
# - 1 cut of length 4 from rod of length 5
# - 2 cuts of length 4 from rod of length 9

# As a result, 1 + 2 = 3 which does not satisfy k=4 which is the required 
# number of equal cuts.


def longestLengthOfRibbon(a, k):
    # use dyanmic programming to have a dictionary
    # given a length of a rod, we keep track of how many cuts it
    # can give when required to have cuts of length: 0 - its own length
    vals = {}; answer = 0
    #iterate through array of different length rods
    for num in a:
        #iterate throught different length values to cut
        for length in range(1, num + 1):
            #determine number of equal rods it can provide given a length of cut
            #add it to the previous length existing in dictionary so
            #at the end, we know how many cuts of that length can be provided
            #from the entire array
            cuts = vals.get(length, 0) + num // length
            vals[length] = cuts
            #when the number of cuts for a given length is greater or equal
            # to the desired number of cuts, then we know that length is a possible solution
            if cuts >= k:
                # we compare the possible solution to an existing one
                # and take the largest length value
                answer = max(answer, length)
    return answer

print(longestLengthOfRibbon([8,4,2,1,9,7], 14))
print(longestLengthOfRibbon([8,4,2,1,9,7], 6))
print(longestLengthOfRibbon([100,99],4))
print(longestLengthOfRibbon([1,2,3,4,9],5))
print(longestLengthOfRibbon([1,2,3,4,9],6))