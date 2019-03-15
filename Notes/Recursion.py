# Recursion (Functions calling themselves)

# Functions can call functions
'''
def f():
    print("f")
    g()
def g():
    print("g")

f()


# function calling itself

def f():
    print("f")
    f()


f()
'''
# we can control the recursion depth
