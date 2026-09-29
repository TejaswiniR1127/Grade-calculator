#GRADE CALCULATOR FOR VIT.

import marks_calculation     #importing module
import helper_module         #importing module

students=[]
while True:
    name=input("Enter student name:")
    subject=input("Enter the subject =")
    
    CAT1_score=float(input("Marks in CAT1="))
    CAT2_score=float(input("Marks in CAT2="))
    TEE=float(input("Marks in TEE="))

    x=marks_calculation.marks_converted(CAT1_score)
    print("cat1 marks_calculation to 15 =",x)

    y=marks_calculation.marks_converted(CAT2_score)
    print("cat2 marks_calculation to 15=",y)

    z=TEE*30/100
    print("TEE marks converted into 30=",z)
    print("\n")

    b=float(input("enter internal marks(out of 35)="))
    print("\n")
    
    d,is_eligible = helper_module.check_attendence()
    if not is_eligible:
            continue
    e=float(input("class average="))
    f=float(input("standard deviation of the subject="))

    total=x+y+z+b+d
    t=int(total)

    print("\n")
    print("total marks of semester out of 100=",t)

    grade=marks_calculation.calculate_grade(t,e,f)

    print("\n")
    print(" Grade of this student is",grade,".")

    (students.append([name,subject,t,grade]))
    
    more=input("\n Add another student? YES/NO:")
    if more.lower()=="no":
        break
    print("\n")

    
  
