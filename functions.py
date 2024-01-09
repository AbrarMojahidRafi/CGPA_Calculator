def getting_courses():
    """will return a courses list"""
    with open("courses.txt", "r") as file_opening:
        return file_opening.readlines()


def writing_new_course(courses):
    with open("courses.txt", "w") as file:
        for i in courses:
            file.write(i)


# buttons functionality
def adding_new_course(course_name_input_box, cgpa_of_that_course, credit_of_that_course_combo):
    courses = getting_courses()
    courses.append(f"{course_name_input_box} || {cgpa_of_that_course} || {credit_of_that_course_combo}\n")
    writing_new_course(courses)


def adding_retake_course(course_name_input_box, cgpa_of_that_course, credit_of_that_course_combo):
    courses = getting_courses()
    for i in range(len(courses)):
        if courses[i].split(" || ")[0] == course_name_input_box:
            courses[i] = (f"{course_name_input_box} || {cgpa_of_that_course} || {credit_of_that_course_combo}"
                          f" || Before Retake, CGPA was {courses[i].split(' || ')[1]}\n"
                          )
    writing_new_course(courses)


def calculating_cgpa_for_all_course():
    courses = getting_courses()
    denominator_number_of_credit = 0
    numerator = 0
    grade = "COURSE || CGPA\n"
    for i in range(1, len(courses)):
        course, cgpa, credit = None, None, None
        if len(courses[i].split(" || ")) == 3:
            course, cgpa, credit = courses[i].split(" || ")
        elif len(courses[i].split(" || ")) == 4:
            temp = courses[i].split(" || ")
            course = temp[0]
            cgpa = temp[1]
            credit = temp[2]
        denominator_number_of_credit += int(credit)
        numerator += (float(cgpa) * int(credit))
        grade = grade + f"{course} || {cgpa}\n"

    grade = grade + "--------------------------------------------------\n"
    cg = numerator / denominator_number_of_credit
    grade = grade + f"Your current CGPA:- {cg}\n"
    grade = grade + f"Total Completed Credit:- {denominator_number_of_credit}"
    return grade


def calculating_cgpa_selected_course(list_box_courses):
    denominator_number_of_credit = 0
    numerator = 0
    grade = "COURSE || CGPA\n"
    for i in range(len(list_box_courses)):
        if list_box_courses[i] != "COURSE || CGPA\n":
            course, cgpa, credit = None, None, None
            if len(list_box_courses[i].split(" || ")) == 3:
                course, cgpa, credit = list_box_courses[i].split(" || ")
            elif len(list_box_courses[i].split(" || ")) == 4:
                temp = list_box_courses[i].split(" || ")
                course = temp[0]
                cgpa = temp[1]
                credit = temp[2]
            denominator_number_of_credit += int(credit)
            numerator += (float(cgpa) * int(credit))
            grade = grade + f"{course} || {cgpa}\n"
    grade = grade + "--------------------------------------------------\n"
    cg = numerator / denominator_number_of_credit
    grade = grade + f"Your current CGPA:- {cg}\n"
    grade = grade + f"Total Completed Credit:- {denominator_number_of_credit}"
    return grade


def calculating_cgpa(list_box_courses):
    # print(list_box_courses)
    if len(list_box_courses) == 0:
        return calculating_cgpa_for_all_course()
    else:
        return calculating_cgpa_selected_course(list_box_courses)


def editing_a_course_or_its_cgpa(course_prev, course_name_update, cgpa_update, credit_of_that_course_combo):
    courses = getting_courses()
    for i in range(len(courses)):
        if courses[i].split(" || ")[0] == course_prev.split(" || ")[0]:
            courses[i] = f"{course_name_update} || {cgpa_update} || {credit_of_that_course_combo}\n"
            break
    writing_new_course(courses)


def editing_for_retake(course_prev, course_name_update, cgpa_update, credit_of_that_course_combo):
    courses = getting_courses()
    for i in range(len(courses)):
        if courses[i].split(" || ")[0] == course_prev.split(" || ")[0]:
            courses[i] = (f"{course_name_update} || {cgpa_update} || {credit_of_that_course_combo} "
                          f"|| Before Retake, CGPA was {course_prev.split(' || ')[1]}\n")
    writing_new_course(courses)


def removing_selected_course(course):
    courses = getting_courses()
    for i in range(len(courses)):
        if courses[i] == course:
            courses.remove(course)
            break
    writing_new_course(courses)


# Error handling of Add button
def check_course_code_present_or_not(course):
    if len(course) == 0:
        return True  # means user didn't give the course code.


def check_cgpa_is_valid_or_not(cgpa):
    if len(cgpa) == 0:
        return True
    elif "0.0" > cgpa or "4.0" < cgpa:
        return True
    else:
        flag = False
        for i in cgpa:
            if i not in ".0123456789":
                flag = True

        if flag == True:
            return True
        else:
            return False


def check_credit_is_valid_or_not(credit):
    if int(credit) < 1 or int(credit) > 10:
        return True


def check_duplicate(course):
    courses = getting_courses()
    for i in courses:
        if i.split(" || ")[0] == course:
            return True
