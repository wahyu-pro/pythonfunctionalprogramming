def SnakeCase(arg):
    string = arg.split()
    snakeCase = '_'.join(string)
    return snakeCase

hello = SnakeCase("hello world again")
print(hello)