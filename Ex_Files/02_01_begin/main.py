RUN_INDENTED = True

MESSAGE = "running unindented"

if RUN_INDENTED:
    MESSAGE = "running indented"

print(MESSAGE)


def my_function():
    greet = "Hello"
    return greet


print(my_function())
