'''
Function to convert first letter of string to lower case, unless all other
letters are upper case
'''


def lower_first(string):
    '''
    Converts first letter of string to lower case, unless all other letters
    in the string are uppercase.

    Parameters
    ----------
    string : string
        The string to be modified

    Returns
    -------
    new_string : string
        The modified string
    '''
    if string.isupper():
        new_string = string
    else:
        new_string = string[0].lower() + string[1:]
    return new_string
