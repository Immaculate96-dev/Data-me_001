# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    lst.reverse()
    return lst

def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    count = 0
    if element in lst:
        count += 1
    return count

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    dict.keys(value)
    return list[keys]

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    merge_lst = sorted(lst1 + lst2)
    return merge_lst


def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    largest = 0
    second_largest = 0
    my_list = [0]

    for number in my_list[1:]:
        if number > largest:
            second_largest = largest
            largest = number
        elif number == second_largest and number != largest:
            second_largest = number
    print(second_largest)

def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    if sorted (str1) == sorted (str2):
        return True
    else:
        return False
    
    str1 = "listen"
    str2 = "silence"



def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    pass  # Implement this


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    my_lst = lst(set(my_lst))
    return my_lst

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    new_lst = lst1 + lst2
    return new_lst