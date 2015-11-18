# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        return 'Number of donuts: '+str(count)
    else:
        return 'Number of donuts: many'


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        return ''
    else: 
        first2 = s[:2]
        last2 = s[-2:]
        return first2+last2


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    word = s[0]
    for x in range(1, len(s)):
        letter = s[x]
        if s[x] == s[0]:
            letter = '*'
        word = word + letter
    return word


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    
    a_start = a[:2]
    b_start = b[:2]
    alist = list(a)
    blist = list(b)
    alist[:2] = b_start
    blist[:2] = a_start
    str_a = ''.join(alist)
    str_b = ''.join(blist)
    return str_a + ' ' + str_b


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    
    if len(s) < 3:
        return s
    else:
        if s[-3:] == 'ing':
            new = s + 'ly'
            return new
        else:
            new = s + 'ing'
            return new


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    notsub = s.find('not')
    badsub = s.find('bad')
    if badsub > notsub:
        chop = s[:notsub]
        new = chop + 'good'
        return new
    else:
        return s

def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    def splitter(x):
        if len(x) % 2 == 0: # string is even
            xfront, xback = x[:len(x)/2], x[-len(x)/2:]
        else:
            xfront, xback = x[:(len(x)/2)+1], x[-(len(x)/2):]
        return xfront, xback

    afront, aback = splitter(a)
    bfront, bback = splitter(b)

    return afront+bfront+aback+bback


