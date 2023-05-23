import numpy as np
from collections import defaultdict

# Questions database
easy_questions = [
    {"prompt": "What is 1+1? \nA: 2\nB: 4\nC: 12\nD:11\nAnswer:", "answer": "A"},
    {"prompt": "What is pie in three decimals?\nA: 3.22\nB: 3.12\nC: 3.14\nAnswer:", "answer": "C"}
]

medium_questions = [
    {"prompt": "What is the capital of China?\nA: China\nB: Nanjing\nC: Jiangxie\nAnswer:", "answer": "B"},
    {"prompt": "What is 2 times 3?\nA: 6\nB: 12\nAnswer:", "answer": "A"}
]

class User:
    def __init__(self, name):
        self.name = name

class Teacher(User):
    def __init__(self, name):
        super().__init__(name)
        self.students = {}

    def add_student(self, student):
        if student.name not in self.students:
            self.students[student.name] = student
        else:
            print("Student already exists!")

    def vis_all(self):
        if self.students:
            scores = [student.score for student in self.students.values()]
            print(np.histogram(scores))
        else:
            print("No students to visualize!")

    def vis_one(self, student_name):
        if student_name in self.students:
            print(np.histogram(self.students[student_name].score))
        else:
            print(f"Student {student_name} not found!")

    def change_problem(self, question_index, level, new_prompt, new_answer):
        if level.lower() == "easy":
            if 0 <= question_index < len(easy_questions):
                easy_questions[question_index] = {"prompt": new_prompt, "answer": new_answer}
            else:
                print("Invalid question index!")
        elif level.lower() == "medium":
            if 0 <= question_index < len(medium_questions):
                medium_questions[question_index] = {"prompt": new_prompt, "answer": new_answer}
            else:
                print("Invalid question index!")
        else:
            print("Invalid level!")

class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.score = defaultdict(int)

    def practice(self, level):
        questions = easy_questions if level == "easy" else medium_questions if level == "medium" else None
        if questions is None:
            print("Invalid level!")
            return
        for question in questions:
            answer = input(question['prompt'])
            if answer.upper() == question['answer']:
                self.score[level] += 1

    def vis_self(self):
        print(np.histogram(list(self.score.values())))

def main():
    # Instantiate a Teacher object
    teacher = Teacher("Prof. Snape")

    # Infinite loop until the user decides to quit
    while True:
        user_type = input("Are you a teacher or student? (or type 'quit' to exit): ").lower()
        if user_type == "teacher":
            while True:
                option = input("What would you like to do? \nA: Visualize overall performance from the students "
                               "\nB: Change a problem \nC: Visualize individual performance\nAnswer:  ").upper()
                if option == "A":
                    teacher.vis_all()
                elif option == "B":
                    question_index =
                    question_index = int(input("Enter the question index: "))
                    level = input("Enter level (easy/medium): ").lower()
                    new_prompt = input("Enter the new prompt: ")
                    new_answer = input("Enter the new answer: ").upper()
                    teacher.change_problem(question_index, level, new_prompt, new_answer)
                elif option == "C":
                    student_name = input("Enter the student's name: ")
                    teacher.vis_one(student_name)
                else:
                    print("Invalid option!")

                cont = input("Would you like to continue?[Y/N]: ").upper()
                if cont == "N":
                    break

        elif user_type == "student":
            student_name = input("Enter your name: ")
            if student_name not in teacher.students:
                student = Student(student_name)
                teacher.add_student(student)
            else:
                student = teacher.students[student_name]

            while True:
                choices = input("What would you like to do? \nA: Practice \nB: See progress \nC: Visualize performance\nAnswer:").upper()
                if choices == "A":
                    level = input("Enter level (easy/medium): ").lower()
                    student.practice(level)
                elif choices == "B":
                    for level, score in student.score.items():
                        print(f"Your score at {level} level is {score}")
                elif choices == "C":
                    student.vis_self()
                else:
                    print("Invalid choice!")

                cont = input("Would you like to to continue?[Y/N]: ").upper()
                if cont == "N":
                    break

        elif user_type == "quit":
            break

        else:
            print("That's not a valid response. Please enter 'student' or 'teacher'.")

if __name__ == "__main__":
    main()

