#Prompt the user to enter the student's average.

stu_avg = float(input("Please enter student's average: "))

#Validate the input by using a while loop till the value

#entered by the user is out of range 0 and 100.

while(stu_avg < 0 or stu_avg > 100):

    #Display an appropriate message and again, prompt

    #the user to enter a valid average value.

    print("Invalid average! Please enter a valid " +

    "average between 0 - 100:")

    stu_avg = float(input("Please enter student's " +

   "average: "))

#Prompt the user to enter the number of days missed.

num_days_missed = int(input("Please enter the number " +

"of days missed: "))

#Validate the input by using a while loop till the

#value entered by the user is less than 0.

while(num_days_missed < 0):

    #Display an appropriate message and again, prompt

    #the user to enter a valid days value.

    print("Invalid number of days! Please enter valid " +

    "number of days greater than 0:")

    num_days_missed = int(input("Please enter the " +

    "number of days missed: "))

#If the student's average is at least 96, then the

#student is exempt.

if(stu_avg >= 96):

    print("Student is exempt from the final exam. " +

    "Because, the student's average is at least 96.")

#If the student's average is at least 93 and number of

#missing days are less than 3, then the student is

#exempt.

elif(stu_avg >= 93 and num_days_missed < 3):

    print("Student is exempt from the final exam. " +

    "Because, the student's average is at least 93 " +

    "and number of days missed are less than 3.")

#If the student's average is at least 90 and there is a

#perfect attendence i.e., number of missing days is 0,

#then the student is exempt.

elif(stu_avg >= 90 and num_days_missed == 0):

    print("Student is exempt from the final exam. " +

    "Because, the student's average is at least 90 " +

    "and student has perfect attendence.")

#Otherwise, student is not exempt.

else:

    print("Student is not exempt from the final exam.")