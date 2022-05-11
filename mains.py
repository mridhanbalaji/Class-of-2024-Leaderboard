import random
from Variables import names,gender,grades


 #Creates the studentdata_Final list here, so all of the functions in the class can acess it
studentdata_Final = []


# Constantly update that file with the new data points from the input



#Function to get the inputed data, and sort it into a list, so the users data can be accesed with their name, and gender
def getgrades(names,grades,gender):
    studentdata1 = [names, grades, gender]
    for i in range(len(names)):
        sticks = [studentdata1[0][i], studentdata1[1][i], studentdata1[2][i]]
        studentdata_Final.append(sticks)


# GEts the User Input data, and makes t lower case, so all the data is uniform,, to acess later, then appends them to their corresponding data lists
def userdata():
    user_name = input("What is your name(First Last): ")
    user_name = user_name.lower()

    user_grade = input("What is your GPA: ")

    user_gender = input("What  is your gender: ")
    user_gender = user_gender.lower()
    names.append(user_name)
    grades.append(user_grade)
    gender.append(user_gender)



#Calls the fucntion to recive all the user data.
userdata()

#Calls the function  with the peramiters in which the students data is combined together into a list, which is placed into a large nested list 
#(The list of the data)
#Called before the get_studentdata dunction, because that function uses thedata processed in
#this function
getgrades(names,grades,gender)



#Function to pull the data of the requested student, First takes the input of the desired student.
# Then findes the index of the student in the names data list, then finds the corrwesponding data of,
#the index in the studentdata_Fianl nested list, to pull akll of the student data infomaition.
def get_studentdata():
    desiredStudent = input("Who would you like to find: ")
    desiredStudent = desiredStudent.lower()
    
    wanted = 0
    
    for i in names:
        if i == desiredStudent:
            wanted = names.index(i)
        # else:
        # return "Sadley User Was Not Found :( /n Please Try a different Name"
    

    found = studentdata_Final[wanted]
    print("Name: " + str(found[0]).upper())
    print("GPA: " + str(found[1]))
    print("Gender: " + str(found[2]).upper())


# Calls the function, to pull the data, of the requested student
get_studentdata()












# ----------------> TO DO LIST <-----------------------
# 1. Create a seperate file, with the list of data, and contantly update the list (Create a text file, and constantly update it, then call the text file as the list)
# 3. Create the leaderboard
# 4. CReate the option for the useer to make their data pubnlicly or privatly visabele
# 5. Create the app interface