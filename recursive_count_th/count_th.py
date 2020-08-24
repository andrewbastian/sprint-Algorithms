'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC - check if there are 2 letters in our word
    if len(word) <= 1:
        return 0
    # check if the letters at the front of the line are `th`
          # if so, run this function on the next two spaces
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    # if `th` was not found on the if statment, run the function on the next letter.
    else:
        return count_th(word[1:])
