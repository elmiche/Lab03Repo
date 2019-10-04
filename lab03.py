#lab03.py
#Grading

#version 1
user_score = input("Find out your letter grade, enter your score:")
user_grade = int(user_score)

#this is the code that converts numeric ranges to symbolic letters
if user_grade >= 90 and user_grade <=100:
    print("A")
elif user_grade >= 80 and user_grade <=89:
    print("B")
elif user_grade >= 70 and user_grade <=79:
    print("C")
elif user_grade >= 60 and user_grade <=69:
    print("D")
elif user_grade >= 0 and user_grade <=59:
    print("F")
else: done


#version
