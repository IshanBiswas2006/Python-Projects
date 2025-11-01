def insertion_sort(arr):
    n = len(arr)
    for i in range(n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def main():
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input(f"Enter {n} elements: ").split()))

    insertion_sort(arr)

    print("Sorted array:", *arr)


if __name__ == "__main__":
    main()
