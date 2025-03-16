# Задание 0
def greater_than_previous(lst):
    result = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]
    return result


n = [1, 2, 1, 3, 5, 4]
print(greater_than_previous(n))


# Задание 1
def swap_min_max(lst):
    if not lst:
        return lst
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
    return lst


n = [3, 5, 1, 2, 4]
print(swap_min_max(n))


# Задание 2
def count_common_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return len(set1 & set2)


lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]
print(count_common_elements(lst1, lst2))


# Задание 3
def count_string_repetitions(lst):
    counts = {}
    for string in lst:
        if string in counts:
            counts[string] += 1
        else:
            counts[string] = 1
    return list(counts.values())


s1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
print(*count_string_repetitions(s1))

s2 = ['aaa', 'bbb', 'ccc']
print(*count_string_repetitions(s2))

s3 = ['abc', 'abc', 'abc']
print(*count_string_repetitions(s3))