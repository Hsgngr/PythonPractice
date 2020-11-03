"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 16:54 3.11.2020
"""


def maxPower(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0: return 0
    arr = []
    for character in s:
        arr.append(character)
    print(arr)
    prev_char = ''
    max_power = 0
    result = 0
    for i in range(len(arr)):

        if (arr[i] == prev_char):
            max_power += 1
        else:
            max_power = 1

        prev_char = arr[i]
        if result < max_power: result = max_power

    return result


s = ''
result = maxPower(s)
print(result)
