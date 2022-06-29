#!/usr/bin/env python3
remove_char_at = __import__('101-remove_char_at').remove_char_at
def  remove_char_at(str, n):
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])