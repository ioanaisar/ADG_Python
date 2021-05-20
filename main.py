# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
    copy_list = sorted(my_list)
    copy_list_reversed = sorted(my_list, reverse=True)
    even_list = copy_list[1::2]
    odd_list = copy_list[::2]
    multiple_list = copy_list[2::3]
    print(my_list)
    print(copy_list)
    print(copy_list_reversed)
    print(even_list)
    print(odd_list)
    print(multiple_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
