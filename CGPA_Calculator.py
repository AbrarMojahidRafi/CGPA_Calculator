import PySimpleGUI as sg
import functions

sg.theme("DarkGreen5")

enterTheCourseName = sg.Text("Enter the Course Code: ", font=("Arial Bold", 10))
courseNameInputBox = sg.Input("", key="courseNameInputBox", do_not_clear=False)

EnterTheCGPAOfThatCourse = sg.Text("Enter the CGPA of that Course: ", font=("Arial Bold", 10))
cgpa_list = ["0.0", "0.7", "1.0", "1.3", "1.7", "2.0", "2.3", "2.7", "3.0", "3.3", "3.7", "4.0"]
CGPAOfThatCourse = sg.Combo(cgpa_list,
                            key="CGPAOfThatCourse",
                            size=(10, 1))
creditOfThatCourse = sg.Text("Credit: ", font=("Arial Bold", 10))
credit_list = ["1", "2", "3", "4", "5"]
creditOfThatCourseCombo = sg.Combo(credit_list, default_value="3", key="creditOfThatCourseCombo", size=(10, 1))

retakeText = sg.Text("Did you retake this course?", font=("Arial Bold", 10))
retakeCombo = sg.Combo(['Yes', 'No'], default_value="No", key="retakeCombo", size=(5, 1))

addButton = sg.Button("Add", font=("Arial Bold", 10))

with open("courses.txt", "r") as courses:
    listBox = sg.Listbox(courses.readlines(), size=(55, 10), font=("Arial Bold", 10), key="list_Box",
                         enable_events=True)

editButton = sg.Button("Edit", font=("Arial Bold", 10))
removeButton = sg.Button("Remove", font=("Arial Bold", 10))

calculate = sg.Button("Calculate the CGPA", font=("Arial Bold", 10))

window = sg.Window("CGPA Calculator",
                   layout=[
                       [enterTheCourseName, courseNameInputBox],
                       [EnterTheCGPAOfThatCourse, CGPAOfThatCourse, creditOfThatCourse, creditOfThatCourseCombo],
                       [retakeText, retakeCombo, addButton],
                       [listBox, editButton, removeButton],
                       [calculate]
                   ]
                   )

while True:
    event = window.Read()
    cases, inputValues = event
    print(event)
    if cases == sg.WINDOW_CLOSED:
        break
    if cases == "list_Box":
        try:
            if len(inputValues["list_Box"][0].split(" || ")) == 2:
                courseName, cgpa = inputValues["list_Box"][0].split(" || ")
                window["courseNameInputBox"].update(courseName)
                window["CGPAOfThatCourse"].update(cgpa.strip("\n"))
                window["retakeCombo"].update("No")
            elif len(inputValues["list_Box"][0].split(" || ")) == 3:
                courseName, cgpa, credit = inputValues["list_Box"][0].split(" || ")
                window["courseNameInputBox"].update(courseName)
                window["CGPAOfThatCourse"].update(cgpa)
                window["creditOfThatCourseCombo"].update(credit.strip("\n"))
                window["retakeCombo"].update("No")
            elif len(inputValues["list_Box"][0].split(" || ")) == 4:
                courseName, cgpa, credit, retake = inputValues["list_Box"][0].split(" || ")
                window["courseNameInputBox"].update(courseName)
                window["CGPAOfThatCourse"].update(cgpa)
                window["creditOfThatCourseCombo"].update(credit)
                window["retakeCombo"].update("Yes")
        except:
            pass
    elif cases == "Add":
        if inputValues["retakeCombo"] == "No":
            if functions.check_course_code_present_or_not(inputValues["courseNameInputBox"]):
                sg.popup_error('Please give the COURSE CODE.')
            elif functions.check_cgpa_is_valid_or_not(inputValues["CGPAOfThatCourse"]):
                if len(inputValues["""CGPAOfThatCourse"""]) != 0:
                    sg.popup_error(
                        f'Please give the CGPA properly of your course.\nYou write "{inputValues["""CGPAOfThatCourse"""]}"'
                    )
                else:
                    sg.popup_error(
                        f'Please give the CGPA properly of your course.\nYou write "noting", which is not correct.'
                    )
            elif functions.check_credit_is_valid_or_not(inputValues["creditOfThatCourseCombo"]):
                sg.popup_error('Your credit is not valid.\nValid Credit is 1-10.')
            elif functions.check_duplicate(inputValues["courseNameInputBox"]):
                sg.popup_error('This course already in the list.')
            else:
                functions.adding_new_course(inputValues["courseNameInputBox"],
                                            inputValues["CGPAOfThatCourse"],
                                            inputValues["creditOfThatCourseCombo"]
                                            )
                window["list_Box"].update(functions.getting_courses())
            window['CGPAOfThatCourse'].update(value='')
            window["creditOfThatCourseCombo"].update(value="3")
            window["retakeCombo"].update("No")
        else:
            functions.adding_retake_course(inputValues["courseNameInputBox"],
                                           inputValues["CGPAOfThatCourse"],
                                           inputValues["creditOfThatCourseCombo"]
                                           )
            window["list_Box"].update(functions.getting_courses())
            window['CGPAOfThatCourse'].update(value='')
            window["creditOfThatCourseCombo"].update(value="3")
            window["retakeCombo"].update("No")
    elif cases == "Calculate the CGPA":
        grade = functions.calculating_cgpa()
        sg.popup_scrolled(grade,
                          title="Your grades")
    elif cases == "Edit":
        if inputValues["retakeCombo"] == "No":
            if functions.check_course_code_present_or_not(inputValues["courseNameInputBox"]):
                sg.popup_error('Please give the COURSE CODE.')
            elif functions.check_cgpa_is_valid_or_not(inputValues["CGPAOfThatCourse"]):
                if len(inputValues["""CGPAOfThatCourse"""]) != 0:
                    sg.popup_error(
                        f'Please give the CGPA properly of your course.\nYou write "{inputValues["""CGPAOfThatCourse"""]}"'
                    )
                else:
                    sg.popup_error(
                        f'Please give the CGPA properly of your course.\nYou write "noting", which is not correct.'
                    )
            elif functions.check_credit_is_valid_or_not(inputValues["creditOfThatCourseCombo"]):
                sg.popup_error('Your credit is not valid.\nValid Credit is 1-10.')
            # elif functions.check_duplicate(inputValues["courseNameInputBox"]):
            #     sg.popup_error('This course already in the list.')
            else:
                functions.editing_a_course_or_its_cgpa(
                    inputValues["list_Box"][0],
                    inputValues["courseNameInputBox"],
                    inputValues["CGPAOfThatCourse"],
                    inputValues["creditOfThatCourseCombo"]
                )
                window["list_Box"].update(functions.getting_courses())
                window['CGPAOfThatCourse'].update(value='')
                window["creditOfThatCourseCombo"].update(value="3")
                window["retakeCombo"].update("No")
        else:
            print(inputValues)
            functions.editing_for_retake(inputValues["list_Box"][0],
                                         inputValues["courseNameInputBox"],
                                         inputValues["CGPAOfThatCourse"],
                                         inputValues["creditOfThatCourseCombo"]
                                         )
            window["list_Box"].update(functions.getting_courses())
            window['CGPAOfThatCourse'].update(value='')
            window["creditOfThatCourseCombo"].update(value="3")
            window["retakeCombo"].update("No")

    elif cases == "Remove":
        try:
            if inputValues["list_Box"][0] != "Course || CGPA\n":
                functions.removing_selected_course(inputValues["list_Box"][0])
                window["list_Box"].update(functions.getting_courses())
            else:
                # give a popup window
                pass
            window['CGPAOfThatCourse'].update(value='')
            window["creditOfThatCourseCombo"].update(value="3")
        except:
            sg.popup_error('Select one course.')
