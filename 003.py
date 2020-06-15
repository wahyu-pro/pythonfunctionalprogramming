def KebabCase(arg):
    string = arg.split()
    kebabCase = '-'.join(string)
    return kebabCase

hello = KebabCase("hello world again")
print(hello)