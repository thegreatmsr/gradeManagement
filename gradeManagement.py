#Initialising Dictionary
studentGrade = { }
#Add a new student 
def addStudent(name,grade):
    studentGrade[name]=grade
    print(f"Added {name} with a {grade}")
    
#Update a Student

def updateStudent(name,grade):
    if name in studentGrade:#Member Ship Operator is being used in this
        studentGrade[name]=grade
        print(f"{name} with marks are updated {grade}")  
    else:
        print(f"{name} is not found") 


#Delete a student
def deleteStudent(name): #To delete the student name we only need key we don't require a value of it
    if name in studentGrade:
        del studentGrade[name]
        print(f"{name} has been successflly deleted")
    else:
        print(f"{name} is not found") 
        
#View a Student
def viewStudent():
    if studentGrade:
        for name, grade in studentGrade.items():
          print(f"{name}")
    else:
        print("No Students Found")
def main():
    while True:
        print("\n Student Grade Management System:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit Progrsm it is just a python program for practising")
        
        
        choice= int(input("Enter Your Choice"))
        if choice==1:
            name=input("Enter student name")
            grade=int(input("Enter the grade of the student"))
            addStudent(name,grade)
        elif choice ==2:
            name=input("Enter student name")
            grade=int(input("Enter the grade of the student"))
            updateStudent(name,grade)
        elif choice ==3:
            name=input("Enter student name")
            deleteStudent(name)
        elif choice==4:
            viewStudent()
        elif choice==5:
            print("Closing the program")
        else:
            print("Enter a valid choice")
            
main()



            
            
            
        

        
    