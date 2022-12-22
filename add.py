x = 10 #Global Variable
y = 100

def addFunction():
    global x
    x = 500 #Local Variable
    print(x+y)
addFunction()
print(x)