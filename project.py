USER_NAME= "AHMET DINCER"
is_login = 0
login_try = 0
courses = []
selected_courses = []
grades = []

def login():
    print("Please type your full name: ", end="")
    inp = input()
    if inp.upper() == USER_NAME:
        global is_login
        is_login = 1
        print(f"Welcome {USER_NAME}")
    else:
        print("Name did not matched. Please try again.")
        global login_try
        login_try += 1
        
def create_course():
    global courses
    print("Please type a new lesson:", end=" ")
    new_course = input()
    if new_course in courses:
        print("This course already exist.")
    else:
        courses.append(new_course)
        print("Course created successfully.")
    
def select_course():
    print("\n\nThese are available courses. You can choose whatever you want. Type number of lesson and use comma(,) to separate courses.")
    for i in enumerate(courses, 1):
        print(i[0], "->", i[1])

    select = input()
    select = select.split(",")
    for i in select:
        selected_courses.append(courses[int(i)-1])

    print("You chose these courses successfully ->", end=" ")
    for i in selected_courses:
        print(i, end=" ")
    print("\n")

def take_exam():
    print("You can take an exam. There are your enrolled courses. Type number of lesson to take exam.")
    for i in enumerate(selected_courses, 1):
        print(i[0], "->", i[1])

    selection = input()
    selected_exam = selected_courses[int(selection)-1]
    print(f"Type grades for {selected_exam}")
    
    print("Midterm grade: ", end="")
    midterm_grade = int(input())

    print("Final grade: ", end="")
    final_grade = int(input())

    print("Project grade: ", end="")
    project_grade = int(input())

    grades.append({selected_exam: {"midterm": midterm_grade, "final": final_grade, "project": project_grade}})
    final_point = (midterm_grade * 3/10) + (final_grade * 5/10) + (project_grade * 2/10)
    
    print(f"Your final point is {final_point}.", end=" ")
    if final_point>90:
        print("You get AA from exam.")
    elif final_point>70 and final_point<90:
        print("You get BB from exam.")
    elif final_point>50 and final_point<70:
        print("You get CC from exam.")
    elif final_point>30 and final_point<50:
        print("You get DD from exam.")
    elif final_point<30:
        print("You get FF from exam. You failed the course.")

while(1):
    if is_login==1:
        while(len(courses)<5):
            create_course()

        print("These are created courses -> ", end="")
        for i in courses:
            print(i, end=" ")
        
        select_course()
        if len(selected_courses)<3:
            print("You failed in class because you chose less than 3 course. You must select more than 3 course to pass class.")
            break
        
        take_exam()
        break

    elif is_login==0:
        if login_try<3:
            login()
        else:
            print("You did all attempts. Please try again later.")
            break