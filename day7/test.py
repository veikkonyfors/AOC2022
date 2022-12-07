import re

cwd = "//a/e"
print(cwd)
x = cwd.split("/")
cwd='/'.join(cwd.split("/")[:-1])
print(cwd)
