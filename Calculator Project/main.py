def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1-n2
def mul(n1, n2):
    return n1*n2
def div(n1, n2):
    return n1/n2
mathsops = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
n1 = int(input("Enter the n1 : "))
S_continue = True
while S_continue:
    opration = input("Choose one Opreation :\n 1. + \n 2. - \n 3. *\n 4. /")
    n2 = int(input("Enter the n2 : "))
    result = mathsops[opration](n1,n2)
    print(result)
    choice=input("if you continue with answer prees 'y' else 'n' ")
    if  choice=="y":
        n1=result
    else:
        S_continue=False
