'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    found = word.find('th')

    if found == -1:
        return 0
    else:
        return 1 + count_th(word[found + 1:])
    


# my_word = 'this'
# print(my_word[1])
# print('this is it'.find('is'))
