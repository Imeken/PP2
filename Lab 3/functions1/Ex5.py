def permutation(word):
    if len(word) == 1:
        return [word]
    
    perms = permutation(word[1:])
    char = word[0]
    result = []

    for per in perms:
        for i in range(len(per)+1):
            result.append(per[:i] + char + per[i:])
    
    return result

word = input()
print(permutation(word))