# if works
# example two
def calculator(a,d,c= "mult"):
    
    if c=="mult":
        return a*d
    
    elif c=="add":
       return a+d

    if c=="sub":
      return a-d
  
    elif c=="div":
        return a/d
    else:
        return"invalid"
    
print(calculator(954,7,"mult"))

