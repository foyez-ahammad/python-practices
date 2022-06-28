def student_exam_info():
  # Input: Student Info
  student_Name  = input("Enter Your Name     : ")
  student_Class = input("Enter your Class    : ")
  student_Roll  = input("Enter Your Roll No  : ")

  # Input: Student Exam Marks Info
  arb_Mark = int(input("Enter Arabic Mark   : "))
  ban_Mark = int(input("Enter Bangla Mark   : "))
  eng_Mark = int(input("Enter English Mark  : "))
  mat_Mark = int(input("Enter Math Mark     : "))
  agr_Mark = int(input("Enter Agr Mark      : "))
  ict_Mark = int(input("Enter ICT Mark      : "))

  # Calculate: Total and Avarage Of Exam Marks
  totalNum = (arb_Mark + ban_Mark + eng_Mark + mat_Mark + agr_Mark + ict_Mark)
  totalAvg = int(totalNum / 6)

  # Print: Student info and Exam Result
  print('____________________________')
  print('Your Name        : ' + student_Name)
  print('Your Class       : ' + student_Class)
  print('Class Roll       : ' + student_Roll)
  print('Total Number     : ' , totalNum)
  print('Subject Avarage  : ' , totalAvg)

  # Calculate: Grade and GPA
  def grade(level):
    print(f"You Grade is: {level}")

  def gpa(level):
    print(f"You GPA is  : {level}")

   # This Codnditional Statements
  if totalAvg >= 80:
    grade("A+")
  elif totalAvg >= 70:
    grade("A")
  elif totalAvg >= 60:
    grade("A-")
  elif totalAvg >= 50:
    grade("B")
  elif totalAvg >= 40:
    grade("C")
  elif totalAvg >= 33:
    grade("D")
  else:
    grade("Failed")
  print('--------------------')

while True:
  student_exam_info()