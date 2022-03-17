def permutate(s):
    if len(s) <= 1:
        return [s]
    else:
        temp = []
        for i in range(len(s)):
            p = s[:i] + s[i+1:]
            for j in permutate(p):
                temp.append(s[i:i+1] + j)
        return temp    
