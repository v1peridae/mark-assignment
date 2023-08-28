studentName = ["Lia","Allan","Koros","Tayla"]
studentMarks = [
  [90,78,86,92,44], 
  [100,98,100,92,92],
  [60,67,66,53,40], 
  [22,50,35,43,12]
]
classNo = 4
distinctionGrade = 70
meritGrade = 55
passGrade = 40
failGrade = 39

distinctionNo = 0
meritNo = 0
passNo = 0
failNo = 0
for x in range (classNo):
  print("Student Name: ",studentName[x])
  totalMarks = sum(studentMarks[x])
  print("Total Marks: ",totalMarks)
  averageMarks = int(totalMarks / len(studentMarks[x]))
  print("Average Marks: ",averageMarks)
  
  if averageMarks >= distinctionGrade:
    distinctionNo = distinctionNo + 1
    print("Grade Awareded: Distinction \n")
  elif averageMarks >= meritGrade and averageMarks < distinctionGrade:
    meritNo = meritNo + 1
    print("Grade Awareded: Merit \n")
  elif averageMarks >= passGrade and averageMarks < meritGrade:
    passNo = passNo + 1
    print("Grade Awareded: Pass \n")
  else:
    failNo = failNo + 1
    print("Grade Awarded: Fail \n")

print("Out of the", classNo, "that took the exams: \n",distinctionNo, "got Distinction.\n", meritNo, "got Merit.\n",passNo, "got Pass.\n",failNo, "got Fail.")

