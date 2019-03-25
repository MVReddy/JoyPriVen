"""
Homework Assignment #8
"""


def main():
    """
    main() Function
    :return:
    """
    names = get_names_from_input_file()
    names = [''.join(s.split(',')) for s in names]
    print_names(names)
    names.sort()
    print_names(names)
    write_names_to_output_file(names)
    print(is_name_in_list(names))


def get_names_from_input_file(file_name='names.txt'):
    """
    Function to read names from file as list
    :param file_name: name of the input file containing names
    :return: List of names
    """
    data = []
    try:
        with open('names.txt') as f:
            data = f.readlines()
            return data
    except Exception as e:
        print('Error while reading file: {}'.format(file_name))
        print(e)
        return data


def print_names(data):
    """
    Function to print data in the list of names
    :param data: list of names
    :return: N/A
    """
    for item in data:
        print(item)


def write_names_to_output_file(data):
    """
    Function to write names to output file.
    :param data: list of names
    :return: N/A
    """
    data = '\n'.join(data)
    with open('output_data.txt', 'w') as f:
        f.write(data)


def is_name_in_list(data):
    """
    Function to check if name exists in list of not
    :param data: list of names
    :return: name and index if found else error message.
    """
    name = input('who are you looking for?(case sensitive)')
    if name in data:
        return name, data.index(name)
    else:
        return 'Given name: '{}' not found in list'.format(name)


if __name__ == '__main__':
    main()
