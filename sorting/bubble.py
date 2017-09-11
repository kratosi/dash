"""
In bubble sort the largest element bubbles (goes down)
with every pass.

"""


def bubble(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True

        if not swap:
            break


def main():
    a = [5, 1, 4, 2, 8]
    bubble(a)
    print a

main()
