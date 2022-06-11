t1 = input("Enter the time: ")

def changeTimeFormat(t1):
    
    if (t1[0:2] >= "0" and t1[0:2] < "12"):
        if "AM" in t1:
            t1 = t1.replace("AM", "")
            return t1
        elif "PM" in t1:
            t1 = t1.replace("PM", "")
            t1 = t1.replace(t1[0:2], str(int(t1[0:2]) + 12))
            return t1
        else:
            return t1

    elif (t1[0:2] >= "12" and t1[0:2] < "24"):
        if "AM" in t1:
            t1 = t1.replace(t1, "this time is not valid, please enter the time in the correct format and try again")
            return t1
        elif "PM" in t1:
            t1 = t1.replace("PM", "")
            return t1
        else:
            return t1

print(changeTimeFormat(t1))
