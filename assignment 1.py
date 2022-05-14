#CMPUT 175 Assignment 1: Anietie Akpanusoh (1628270)

#firstly I will create dictionaries for all the three text files to allow for easier manipulation
students = {} #this is for the students
courses = {} #this is for the courses
enrollment = {}

def menu():
    #this will the display the menu for selection
    print ('What would you like to do?')
    print ('1. Print timetable')
    print ('2. Enroll in course')
    print ('3. Drop course')
    print ('4. Quit')

def welcome():
    #the welcome to beartracks message will be displayed with this function
    print("== == == == == == == == == == == == ==")
    print("Welcome to Mini - BearTracks")
    print("== == == == == == == == == == == == ==")

def courses_data():
    #this will read the contents of the courses.txt file and create the dictionary
    with open("courses.txt", "r") as f:
        for line in f:
            stripLine = line.strip()
            stripLineItems = stripLine.split(';') #this will remove all the spaces around the contents
            for index in range(len(stripLineItems)):
                stripItem = stripLineItems[index].strip()
                stripLineItems[index] = stripItem
            #using the course name as the key of the dictionary
                courses[stripLineItems[0]] = stripLineItems

def student_data():
    #this will read the contents of the students.txt file and create the dictionary
    with open("students.txt", "r") as f:
        for line in f:
            stripLine = line.strip()
            stripLineItems = stripLine.split(',') #this will remove all the spaces around the contents
            for index in range(len(stripLineItems)):
                stripItem = stripLineItems[index].strip()
                stripLineItems[index] = stripItem
            #using the student ID as the key of the dictionary
                students[stripLineItems[0]] = stripLineItems


def enrollment_data():
    #this will read the data from the enrollment.txt file and create its dictionary
    with open("enrollment.txt") as f:
        for line in f:
            stripLine = line.strip()
            stripLineItems = stripLine.split(':')
            for index in range(len(stripLineItems)):
                stripItem = stripLineItems[index].strip()
                stripLineItems[index] = stripItem
            #using the IDs keys to store the enrollment. 
            if stripLineItems[1] not in enrollment:
                enrollment[stripLineItems[1]] = []
            #appending the course names to the list of the enrolled students
            enrollment[stripLineItems[1]].append(stripLineItems[0])

def writeEnrollment():
    #this function updates the enrollment.txt
    with open("enrollment.txt", "w") as myfile:
        #go through the enrollment data
        for key,value in enrollment.items():
            for course in value:
                myfile.write(f"{course}: {key}\n")

def writeCourse():
    #this function updates the courses.txt
    with open("courses.txt", "w") as myfile:
        #iterate through enrollment data
        for key,value in courses.items():
            myfile.write(f"{value[0]}; {value[1]}; {value[2]}; {value[3]}\n")

def drawTimetable():
    #this will ask the user to enter the student ID and draw the timetable for that student
    studentID = input("Student ID:")
    if studentID not in students.keys(): #validity check
        print("Invalid ID. Cannot Print timetable.")
    else:
        studentInfo = students[studentID]
        print(
            f"Timetable for {studentInfo[2].upper()}, in the faculty of {studentInfo[1].upper()}")
        print ("{space:>13}".format(space=''), end='')
        for hours in [8, 9, 10, 11, 12, 13, 14, 15, 16]:
               print("{hours:^13}".format(hours=f'{hours}:00'), end='')
        print()
        print("{space:>13}".format(space=''), end='')
        for hours in [8, 9, 10, 11, 12, 13, 14, 15, 16]:
               print ("+------------", end='')
        print("+")
        if studentID in enrollment.keys():
            student_enrollments = enrollment[studentID]
            TRcourses = {}
            MWFcourses = {}
            for course_code in student_enrollments:
                course_day_time = courses[course_code][1]
                course_day_time_list = course_day_time.split()
                course_code_items = course_code.split()
                formatted_course_code = course_code
                if len(course_code_items[0]) > 4:
                    formatted_course_code = f"{course_code[0:3]}* {course_code_items[1]}"
                if course_day_time_list[0] == 'TR':  # check if a TR course
                    # add name and the number of open seats
                    TRcourses[course_day_time_list[1]] = [formatted_course_code, courses[course_code][2]]
                else:
                    MWFcourses[course_day_time_list[1]] = [formatted_course_code, courses[course_code][2]]
            # sort courses using keys
            TRcourses_keys = sorted(TRcourses.items())
            MWFcourses_keys = sorted(MWFcourses.items())
            print("{space:^13}".format(space='Mon/Wed/Fri'), end='')
            for hours in [8, 9, 10, 11, 12, 13, 14, 15, 16]:
                if f"{hours}:00" in MWFcourses.keys():
                    print("|{course:^12}".format(course=MWFcourses[f"{hours}:00"][0]), end='')
                else:
                    print("|{course:^12}".format(course=''), end='')
            print('|')
            print("{space:^13}".format(space=''), end='')
            for hours in [8, 9, 10, 11, 12, 13, 14, 15, 16]:
                if f"{hours}:00" in MWFcourses.keys():
                    print("|{course:^12}".format(course=MWFcourses[f"{hours}:00"][1]), end='')
                else:
                    print("|{course:^12}".format(course=''), end='')
            print('|')
            print("{space:>13}".format(space=''), end='')
            print(
                "+--------------------------------------+--------------------------------------+--------------------------------------+")
            print("{space:^13}".format(space='Tues/Thurs'), end='')
            index = 1
            separator = '|'
            print('|', end='')
            for hours in ['8:00', '9:30', '11:00', '12:30', '14:00', '15:30']:
                if index % 2 == 1:
                    separator = '||'
                else:
                    separator = '|'
                if hours in TRcourses.keys():
                    print("{course:^18}{separator}".format(course=TRcourses[f"{hours}"][0], separator=separator),
                          end='')
                else:
                    print("{course:^18}{separator}".format(course='', separator=separator), end='')
                index = index + 1
            print()
            print("{space:^13}".format(space=''), end='')
            separator = '|'
            print('|', end='')
            for hours in ['8:00', '9:30', '11:00', '12:30', '14:00', '15:30']:
                if index % 2 == 1:
                    separator = '||'
                else:
                    separator = '|'
                if hours in TRcourses.keys():
                    print("{course:^18}{separator}".format(course=TRcourses[f"{hours}"][1], separator=separator),
                          end='')
                else:
                    print("{course:^18}{separator}".format(course='', separator=separator), end='')
                index = index + 1
            print()
            print("{space:>13}".format(space=''), end='')
            print(
                "+--------------------------------------+--------------------------------------+--------------------------------------+")
        else:
            print("The student hasn't enrolled to any course")


                
def enrollcourse():

    studentID = input("Student ID: ")
    courseName = input("Course name: ")
    # check if the student id is valid
    if studentID not in students.keys():
        print("Invalid student ID. Cannot print timetable.")
    # check if course name is valid
    elif courseName not in courses.keys():
        print("The course name is invalid")
    # check if student is already registered for course
    elif studentID in enrollment.keys() and courseName in enrollment[studentID]:
        print("The student is already registered in the course")
    # check if the selected course is full and if there are any empty seats
    elif courses[courseName][1] == 0:
        print("The selected course is full")
    else:
        if studentID not in enrollment.keys():
            enrollment[studentID] = []
        # enroll student
        enrollment[studentID].append(courseName)
        # decrease the number of open seats
        courses[courseName][2] = int(courses[courseName][2]) - 1
        # print message
        print(
            f"{students[studentID][2]} has successfully been enrolled in {courseName}, on {courses[courseName][1]}")        


def dropcourse():
    studentID = input("Student ID: ")
    # check if the student id is valid
    if studentID not in students.keys():
        print("Invalid student ID. Cannot print timetable.")
    else:
        print("Select course to drop:")
        if studentID in enrollment.keys():
            enrolled_courses = enrollment[studentID]
            # sort courses
            enrolled_courses.sort()
            # display courses
            for course in enrolled_courses:
                print(f"- {course}")
            # prompt user for course
            the_course_to_drop = input("> ")
            # check if enrolled for the course
            if the_course_to_drop in enrolled_courses:
                # remove the course
                enrolled_courses.remove(the_course_to_drop)
                # update enrolled courses for the students
                enrollment[studentID] = enrolled_courses
                # increase the number of open seats
                courses[the_course_to_drop][2] = int(courses[the_course_to_drop][2]) + 1
                # display message
                print(f"{students[studentID][2]} has successfully dropped {the_course_to_drop}")
            else:
                print("The student hasn't enrolled in the course selected")
        else:
            print("Student hasn't enrolled in any course")


def mini_bear_tracks():
    """
    this function allows user to perform several options on the mini-bear tracks
    """
    userChoice = ''
    validOptions = ('1', '2', '3', '4')
    # while user choice is not exit(4)
    while userChoice != '4':
        userChoice = ''
        menu()
        # prompt user to select an option and check whether it is either 1, 2, 3, 4
        while userChoice not in validOptions:
            userChoice = input("> ")
            if userChoice not in validOptions:
                print("Sorry, invalid entry. Please enter a choice from 1 to 4.")
        print()
        if userChoice == '1':
            # print timetable for a student
            drawTimetable()
        elif userChoice == '2':
            enrollcourse()
        elif userChoice == '3':
            # drop course
            dropcourse()
        elif userChoice == '4':
            writeEnrollment()
            writeCourse()
            print("Goodbye")
        else:
            quit()


if __name__ == '__main__':
    # load data first
    courses_data()
    student_data()
    enrollment_data()
    # display welcome message
    welcome()
    print()
    mini_bear_tracks()
            
