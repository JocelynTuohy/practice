# Scores and Grades Assignment (Coding Dojo)
# Write a function that generates ten scores between 60 and 100. Each time a score is generated,
# your function should display what the grade is for a particular score.

# import random module
import random

def scoresAndGrades():
  print 'Scores and Grades'
  for student in range(0,11):
    score = random.randint(60,101)
    if score >= 90:
      grade = 'A'
    elif score >= 80:
      grade = 'B'
    elif score >= 70:
      grade = 'C'
    elif score >= 60:
      grade = 'D'
    print 'Score: ' + str(score) + '; Your grade is ' + grade
  print 'End of the program. Bye!'

scoresAndGrades()