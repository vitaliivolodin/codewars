def remove_smallest(numbers):
    input_list = numbers
    if not input_list:
        return []
    else:
        smallest = min(input_list)

        for i in range(len(input_list)):
            if input_list[i] == smallest:
                del input_list[i]
                break

        return input_list

print(remove_smallest([1, 2, 3, 5, 3, 2, 1]))
