import numpy

# Maybe hash Map??
all_students = () #global variable so in all caps, snapescript, used to access old inputs of students
easy_questions = [
    "What is 1+1? \nA: 2\nB: 4\nC: 12\nD:11\nAnswer:",
    "What is pie in three decimals?\nA: 3.22\nB: 3.12\nC: 3.14\nAnswer:"
    ]
medium_questions = [
    "What is the captial of China?\nA: China\nB: Nanjing\nC: Jiangxie\nAnswer:",
    "What is 2 times 3?\nA: 6\nB: 12\nAnswer:"
]

# Class object for quesion and answeer
class questions:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Store the questions the answers in an object in an array
e_prmopts = [
    questions(easy_questions[0], "A"),
    questions(easy_questions[1], "C"),

]

m_prmopts = [
    questions(medium_questions[0], "A"),
    questions(medium_questions[1], "A")
]

# Keep track of the socre at different levels
level_score = {}

# practice set easy
def p():
    easy_score = 0
    for prompt in e_prmopts:
        e_answer = input(prompt.prompt)
        if e_answer.upper() == prompt.answer:
            easy_score += 1
    level_score["easy"] = easy_score
    return easy_score

def p2():
    m_score = 0
    for m_prompt in m_prmopts:
        m_answer = input(m_prompt.prompt)
        if m_answer == m_prompt.answer:
            m_score += 1
    level_score["medium"] = m_score
    return m_score

class User:

    class Teacher:

        def __init__(self, name, class, score):
            self.name = name       #teacher's name
            self.class = class    #dataset of student names and scores, as objects within a list


        def add_student(self, student_object):
            if self.student in self.class == False:
                all_students.append(student_object)
            elif self.student in self.class == True:

        def vis_all(self):
            # All performance check
            numpy.histogram(all_students)

        def vis_one(self,score):
            # Indidvual performance
            numpy.histogram()

        def change_problem(student):



    class Student:
        def __init__(self, name, index, level):
            student.self = name #IDK
            student.index = index #IDK
            student.level = level #IDK

        def pratice():





        def record_score():

        def vis_self(self,score)
            #see own score and progress overtime
            numpy.histogram()

def main():
    # Ask the user for their role
    while True:
        answer = input("Are you a teacher or student?: ")

        # If the user is a teacher
        if answer.lower() == "teacher":

            # Reprompt the user if the answer don't match
            while True:
                options = input("What would you like to do? \nA: Visualize overall perfromance from the students \nB: Change a problem \nC: Visualize indidvual perfromace\nAnswer:  ")
                if options.upper() in ["A", "B", "C"]: # Check the user's answer
                    break
                else:
                    print("Answer must be A, B or C")
                    # Make sure the user input the correct response

            # Uppercase the input
            options = options.upper()

            # If the user chose option A
            if options == "A":
                # Visualize the performance for all students
                pass

            # If the user chose option B
            elif options== "B":
                # Change a problem from the problem sets
                pass
            # IF the user chose option C
            elif options == "C":
                # Visualize indivudal performance
                pass

            # Ask the user if they would like to continue
            while True:
                des = input("Would you like to to continue?(Y/N): ")
                if des.upper not in ["Y", "N","YES","NO"]
                    print("Answer must be Y or N")
                else:
                    break

            # Break out the entire while loop
            if des.upper() == "N":
                break



        # If the user is a student
        elif answer.lower() == "student":

            # Prompt the user with their choices
            while True:
                choices = input("What would you like to do? \nA: Pratice \nB: See progress \nC: Visualize performace\nAnswer:")
                if choices.upper() in ["A","B","C"]:
                    break
                else:
                    print("Answer must be A, B or C")

            # Uppercase the input
            choices = choices.upper()

            if choices == "A":
                # Practice problems
                if p() == 2:
                    p2()
                else:
                    print("More practice!!")
                    p()
            elif choices == "B":
                # See your progress
                for k, v in level_score.items():
                    print("Your level at " + k + " score is " + str(v))

                # Visualize the student performance
                pass

            # Ask the user if they would like to continue
            while True:
                des = input("Would you like to to continue?[Y/N]: ")
                if des.upper not in ["Y", "N","YES","NO"]
                    print("Answer must be Y or N")
                else:
                    break

            # Break out the while loop
            if des.upper() == "N":
                break

        else:
            print("That's not a valid response. Please enter 'student' or 'teacher'. ")
            # can just print things out in terminals to make visualization, don't have to import libraries
            # or can use numpy from data science lab
            # can make private ed posts with code-specific questions

            # ask, have you used this before and if not, create a new variable
            # can also have student object and add student ass object to a list that can be accessed from the teacher class


if __name__ == "__main__":
    main()
