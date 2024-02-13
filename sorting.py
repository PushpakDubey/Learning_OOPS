# WAP to quicksort in python

list = [3,5,67,8,9,4,3,2,4,6,8,9,9,24]

def quicksort(list):
    if len(list) <= 1:
        return list

    pivot = list[len(list) // 2]
    left = [x for x in list if x < pivot]
    middle = [x for x in list if x == pivot]
    right = [x for x in list if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort(list))

# WAP to bubblesort in python
def bubblesort_basic(list):
    length_of_list = len(list)
    for n1 in range(length_of_list): # This line will repeat for every index of list
        for n2 in range(0, length_of_list - n1 - 1): # This line will repeat for consequtive one less
            if list[n2] > list[n2+1]:
                list[n2], list[n2+1] = list[n2+1], list[n2]
    return list

list1 = [2,5,4,3,6,5,5,8,9,8,6,7,5,8,5,4,6]
print(bubblesort_basic(list1))

# WAP to selection sort in python
def selectionsort_basic(list):
    length_of_list = len(list)
    for n1 in range(length_of_list - 1):
        min_index = n1
        for n2 in range(n1 + 1, length_of_list):
            if list[n2] < list[min_index]:
                min_index = n2
        list[n1], list[min_index] = list[min_index], list[n1]
    return list

list2 = [5, 2, 9, 1, 6, 8, 3, 10, 7, 4]
print(selectionsort_basic(list2))