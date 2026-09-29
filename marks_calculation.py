def marks_converted(CAT_score):
     return 15*CAT_score/50

#Determines the letter grade based on class average and standard deviation
def calculate_grade(t,e,f):
   if t >= e+1.5*f:
      grade="S"
   elif t >= e+0.5*f:
        grade="A"
   elif t >=e-0.5*f:
       grade="B"
   elif t >= e-1.0*f:
        grade="C"
   elif t >= e-1.5*f:
        grade="D"
   else:
       grade="E"

   return grade

