import re
def repl_func(m):
    return m.group(1) + m.group(2).upper()

def Capitalize(arg):
    s = arg
    s = re.sub("(^|\s)(\S)", repl_func, s)
    return s

hello = Capitalize("hello world again")
print(hello)
