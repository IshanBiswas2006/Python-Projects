def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    arr3 = []
    i = j = 0

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1

    while i < n:
        arr3.append(arr1[i])
        i += 1

    while j < m:
        arr3.append(arr2[j])
        j += 1

    return arr3


def main():
    n = int(input("Enter size of first array: "))
    arr1 = list(map(int, input(f"Enter {n} sorted elements for first array: ").split()))

    m = int(input("Enter size of second array: "))
    arr2 = list(map(int, input(f"Enter {m} sorted elements for second array: ").split()))

    arr3 = merge(arr1, arr2)

    print("Merged sorted array:", *arr3)


if __name__ == "__main__":
    main()
