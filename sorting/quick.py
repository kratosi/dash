

def sort(arr, l, h):
    if l < h:
        p = partition(arr, l, h)
        sort(arr, l, p-1)
        sort(arr, p+1, h)


def partition(arr, l, h):
    """
    1) take first element as the pivot
    2) incremnt i till arr[i] > arr[o]
    3) decrement j till arr[j] < arr[0]


    """
    p = arr[l]
    i = l + 1
    j = h

    while True: 
        while arr[i] <= p:
            i += 1

        while arr[j] > p:
            j -= 1

        if i > j:
            break

        # swap
        arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[l] = arr[l], arr[j]
    return j

def main():
    a = [2,6,3,8,5,7,9,7,4,2,4,6,3,7]
    sort(a, 0, len(a)-1)
    print a

main()
