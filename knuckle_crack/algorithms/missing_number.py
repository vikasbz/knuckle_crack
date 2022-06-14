def find_missing_number(array: list[int]) -> int | None:
    """
    Finds the missing number in an unsorted array containing every one of the other 99
    numbers ranging from 1 to 100.

    :return:
        Return the missing number or None if there is no missing number.
    """
    array_sum = sum(array)
    expected_sum = (1 + 100) * 100 / 2
    return int(expected_sum - array_sum) or None


if __name__ == "__main__":
    # List: 1...100
    input_array = list(range(1, 101))
    # Remove 13 from the list
    input_array.remove(13)

    missing_number = find_missing_number(input_array)
    print(f"Missing number: {missing_number}")
