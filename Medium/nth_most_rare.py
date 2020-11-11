"""
Created by  Ege of the House Hoşgüngör, the First of His Name  at 01:59 10.11.2020
"""


def nth_most_rare(elements, n):
    """
    :param elements: (list) List of integers.
    :param n: (int) The n-th element function should return.
    :returns: (int) The n-th most rare element in the elements list.
    """
    element_dict = {}
    for element in elements:
        if element in element_dict:
            element_dict[element] += 1
        else:
            element_dict[element] = 1

    for i in range(n - 1):
        min_val = 10000
        choose_for_remove= None
        for element in element_dict.values():
            if element < min_val:
                choose_for_remove = element
                min_val = element
        del element_dict[choose_for_remove]

    min_val = 10000
    for element in element_dict.values():
        if element < min_val:
            min_val = element
    return min_val

if __name__ == '__main__':
    print(nth_most_rare([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))
