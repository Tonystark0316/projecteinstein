#tuesday
#practicals
def calculator(a,b,c="dev"):
    
    if c=="dev":
        return a-b
    
    elif c=="mult":
        return a*b
    
    if c=="sub":
        return a-b
    
    elif c=="add":
        return a+b
    
    if c=="esponent":
        return a**b
    
    elif c=="modulo":
        return a%b
print(calculator(5,6,"esponent"))    
    