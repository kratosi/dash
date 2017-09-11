"""
In insertion sort the elements on the left are sorted and
the elements of the right are __inserted__ to the right
position one by one on the left
"""


def insertion(arr):

    for i in range(len(arr)):
        elem = arr[i]

        j = i - 1 
        while j >= 0 and arr[j] > elem:
            arr[j+1] = arr[j]
            j = j - 1

        arr[j + 1] = elem

        print "-" * 50
        print arr


def main():
    a = [5,4,7,9,2,1,3,5,6,8,2,1]
    insertion(a)
    print a

main()

