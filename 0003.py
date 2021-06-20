def length_of_longest_substring(s):
    '''
    Leetcode 0003
    Difficulty: Medium
    Longest Substring Without Repeating Character
    '''
    letters = set()
    max_len = 0

    j = 0
    for i in range(len(s)):
        while s[i] in letters:
            letters.remove(s[j])
            j += 1
        letters.add(s[i])
        max_len = max(max_len, len(letters))

    reurn max(max_len, len(letters))
