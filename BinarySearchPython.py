# Binary Search In Python
def binarysearch(a, element, start, end):
    mid = int((start + end) / 2)  # Gets the mid point of the list
    if (a[mid] > element):  # checks if the mid point is greater than the element required or not
        return binarysearch(a, element, start, mid - 1)
    elif (a[mid] < element):
        return binarysearch(a, element, mid + 1, end)
    else:
        return mid


a = [1, 2, 3, 4, 5, 6, 7]
a.sort()
print(binarysearch(a, 7, 0, len(a) - 1))
