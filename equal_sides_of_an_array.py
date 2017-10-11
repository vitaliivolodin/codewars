def find_even_index(arr):
    result = -1
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            result = i
            break

    return result


if __name__ == '__main__':
    print(find_even_index([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]))
