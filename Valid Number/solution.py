class Solution(object):
def isNumber(self, s):
    """
    :type s: str
    :rtype: bool
    """
    #define a DFA
    state = [{}, 
            {'b': 1, 's': 2, 'd':3, '.':4}, 
            {'d':3, '.':4},
            {'d':3, '.':5, 'e':6, 'b':9},
            {'d':5},
            {'d':5, 'e':6, 'b':9},
            {'s':7, 'd':8},
            {'d':8},
            {'d':8, 'b':9},
            {'b':9}]
    currentState = 1
    for c in s:
        if c >= '0' and c <= '9':
            c = 'd'
        if c == ' ':
            c = 'b'
        if c in ['+', '-']:
            c = 's'
        if c not in state[currentState].keys():
            return False
        currentState = state[currentState][c]
    if currentState not in [3,5,8,9]:
        return False
    return True

