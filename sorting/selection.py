"""
In selection sort the minimum element is selected from the
right portion of the array and then swapped with the current
element
"""


def selection(arr):

    for i in range(len(arr)):
        min = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[min], arr[i]  = arr[i], arr[min]



def main():
    a = [4,6,2,3,4,7,9,6,3,6,1]
    selection(a)
    print a

main()
