specials = [".", "?", "!", "&", "#", ",", ";", ":", "-", "_", "*"]

def passcheck(pw):
    lower = [x for x in pw if x.islower()]
    upper = [x for x in pw if x.isupper()]
    number = [x for x in pw if x.isdigit()]
    if len(lower) == 0 or len(upper) == 0 or len(number) == 0:
        return "Password doesn't meet threshold."
    else:
        return "Password meets threshold."

#print(passcheck("cool"))
#print(passcheck("coolbeAns"))
#print(passcheck("coolbeAns15"))

def rating(pw):
    lower = [x for x in pw if x.islower()]
    upper = [x for x in pw if x.isupper()]
    number = [x for x in pw if x.isdigit()]
    specialsHere = [x for x in pw if x in specials]
    rating = 1
    if(len(lower) > 0):
        rating += 1
    if(len(upper) > 0):
        rating += 1
    if(len(lower) > 0 and len(upper) > 0):
        rating += 1
    if(len(pw) > 5 and len(pw) < 9):
        rating += 1
    if(len(pw) > 8):
        rating += 2
    if(len(number) > 0):
        rating += 1
    if(len(number) > 1):
        rating += 1
    if(len(specialsHere) == 1):
        rating += 1
    if(len(specialsHere) > 1):
        rating += 2
    return rating

#print(rating("cool"))
#print(rating("COOL"))
#print(rating("Cool"))
#print(rating("Coolio"))
#print(rating("Coolbeans"))
#print(rating("Coolbeans1"))
#print(rating("C00lbeans1"))
#print(rating("C00lbeans1*"))
#print(rating("C00lbeans1**"))

