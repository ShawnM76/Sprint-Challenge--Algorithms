'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, count=0):
    # Base Case
    if len(word) < 2:
        return count
    if word[0:2] == 'th':
        count += 1
    # recursively call the function with word[1:]
    # Move up one letter and check if the new [0:2] are 'th'
    return count_th(word[1:], count)


print(count_th("abcthefthghith"))
