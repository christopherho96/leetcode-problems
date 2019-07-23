def anagramSolution4(s1,s2):
    s1 = list(s1)
    s2 = list(s2)
    for char in s1:
        index = s2.index(char)
        if s2.pop(index) == None:
            return False
    return not s2

print(anagramSolution4('apple','pleap'))