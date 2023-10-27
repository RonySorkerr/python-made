'''result = 60
if result>=80:
    print("A+")
if result>=70:
    print("A")
if result>=60:
    print("A-")
if result>=50:
    print("B")
if result>=40:
    print("B-")
if result>=35:
    print("C")
if result>=33:
    print("D")
if result<33:
    print("Fail")
else:
    print("FSAL")'''

#Lets work properly

result = 60
if result>=80:
    print("A+")
elif result>=70:
    print("A")
elif result>=60:
    print("A-")
elif result>=50:
    print("B")
elif result>=40:
    print("B-")
elif result>=35:
    print("C")
elif result>=33:
    print("D")
else:
    print("Fail")