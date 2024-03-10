import sys


def compute_list_average(numbers_list):
    """
    :param numbers_list: list of numbers
    :return: average of the list of numbers
    """
    return sum(numbers_list) / len(numbers_list)


if __name__ == '__main__':
    print('Enter some numbers. Type "finish" when you are done.')
    numbers = []
    for line in sys.stdin:
        user_input = line.strip()
        if user_input == 'finish':
            break
        else:
            numbers.append(user_input)

    average = compute_list_average(numbers)
    print(f'The average of the list of numbers {numbers} is: {average}')
