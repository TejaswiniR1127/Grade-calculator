def check_attendence ():
    #tell about the marks out of 5 for attendence
    c=str(input("attendence above 75% or not 'YES'/'NO'="))
    print("/n")
    if c.lower()=="yes":
        print("marks for attendence is 5/5")
        return 5,True
    else:
        print("marks for attendence is 0/5. NOT ELIGABLE FOR ANY EXAM")
        return 0, False
