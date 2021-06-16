
def tallme():
    a = input("enter a")
    a = validateInput(a)
        

    b = input("enter b")
    b= validateInput(b)

    c = input("enter c")
    c= validateInput(c)
    
    tallest = tallMiniMethod(a, b, c)

    print("the tallest is", tallest)
    return a, b, c

def tallMiniMethod(a, b, c):
    if a > b and a > c:
        tallest = a
    elif b > a and b > c:
        tallest = b
    else:
        tallest = c
    return tallest

def validateInput(ins):
    while not ins.isnumeric():
        print("Please provide a number!!")
        ins = input("enter number ")
    return ins

    
t, s, t = tallme()


       

def tall(a=3,b=4,c=10):

    tallest = tallMiniMethod(a, b, c)
    
    print("the tallest is", tallest)

tall(a=4, b=5, c=11)
tall()
tall(15)
tall(12, 17)