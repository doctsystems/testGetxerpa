def zero(operation=None):
    #your code here
    return 0 if operation is None else f"0{operation}"


def one(operation=None):
    #your code here
    return 1 if operation is None else f"1{operation}"


def two(operation=None):
    #your code here
    return 2 if operation is None else f"2{operation}"


def three(operation=None):
    #your code here
    return 3 if operation is None else f"3{operation}"


def four(operation=None):
    #your code here
    return 4 if operation is None else f"4{operation}"


def five(operation=None):
    #your code here
    return 5 if operation is None else f"5{operation}"


def six(operation=None):
    #your code here
    return 6 if operation is None else f"6{operation}"


def seven(operation=None):
    #your code here
    return 7 if operation is None else f"7{operation}"


def eight(operation=None):
    #your code here
    return 8 if operation is None else f"8{operation}"


def nine(operation=None):
    #your code here
    return 9 if operation is None else f"9{operation}"


def plus(number_right):
    #your code here
    return f"+{number_right}"


def minus(number_right):
    #your code here
    return f"-{number_right}"


def times(number_right):
    #your code here
    return f"*{number_right}"


def divided_by(number_right):
    #your code here
    return f"/{number_right}"


if __name__ == '__main__':
    # imprime 20
    print(f"{eval(four(times(five())))}")
    # imprime 9
    print(f"{eval(one(plus(eight())))}")
    # imprime 4
    print(f"{eval(seven(minus(three())))}")
    # imprime 3
    print(f"{round(eval(nine(divided_by(three()))))}")
