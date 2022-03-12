#Q1

def my_func(x1, x2, x3):

    if (x1 + x2 + x3) == 0:
        return "Not a number – denominator equals zero"
    
    if type(x1) != float or type(x2) != float or type(x3) != float:
        return "Eror: parameters should be float"

    return ((x1 + x2 +x3)*(x2 + x3)*3)/(x1 + x2 + x3)



#Q2

def convert(hours=0, minutes=0):

    if hours < 0 or minutes < 0:
        return "Input eror"

    return hours*3600 + minutes*60



