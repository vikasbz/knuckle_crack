def find_duplicate_number(array: list[int]) -> int | None:
    """
    Write a function that finds the duplicate number in an unsorted array containing
    every number from 1 to 100.

    Only one of the numbers will appear twice.

    :return:
        Return the duplicate number or None if there is no duplicate number.
    """
    expected_array = set(range(min(array), max(array) + 1))
    try:
        return expected_array.difference(array).pop()
    except KeyError:
        return None


if __name__ == "__main__":
    # List: 1...100
    input_array = list(range(1, 101))
    # Replace 14 with 13. 13 is the duplicate number
    input_array[13] = 13

    missing_number = find_duplicate_number(input_array)
    print(f"Duplicate number: {missing_number}")
