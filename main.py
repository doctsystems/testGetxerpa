def zero(operation=None):
    #your code here
    if operation is None:
        return 0
    else:
        return f"0{operation}"


def one(operation=None):
    #your code here
    if operation is None:
        return 1
    else:
        return f"1{operation}"


def two(operation=None):
    #your code here
    if operation is None:
        return 2
    else:
        return f"2{operation}"


def three(operation=None):
    #your code here
    if operation is None:
        return 3
    else:
        return f"3{operation}"


def four(operation=None):
    #your code here
    if operation is None:
        return 4
    else:
        return f"4{operation}"


def five(operation=None):
    #your code here
    if operation is None:
        return 5
    else:
        return f"5{operation}"


def six(operation=None):
    #your code here
    if operation is None:
        return 6
    else:
        return f"6{operation}"


def seven(operation=None):
    #your code here
    if operation is None:
        return 7
    else:
        return f"7{operation}"


def eight(operation=None):
    #your code here
    if operation is None:
        return 8
    else:
        return f"8{operation}"


def nine(operation=None):
    #your code here
    if operation is None:
        return 9
    else:
        return f"9{operation}"


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