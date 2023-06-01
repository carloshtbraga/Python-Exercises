x = 1

def escopo():
    global x
    x = 10
    print(x)

print(x)
escopo()
print(x)
