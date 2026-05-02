#task six
#caculator work
def caculator(a,b,c="add"):
    
    
    if c=="add":
     return a+b
 
    elif c=="sub":
     return a-b
    
    elif c=="dev":
     return a/b
    else:
     return "invalid"
print(caculator(8,6,"sub"))     
     