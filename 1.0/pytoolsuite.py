class Phone:
    def __init__(self, hardware, cover):
        self.hardware = hardware
        self.cover = cover

def createPythonDoc():
    
    PythonDoc = open("doc.py", "w")
    PythonDoc.write("")
    
    
    PythonDoc.close
    

def additionCalc():
    
    print("Welcome to this addition calculator!")

    name = input("Enter your name:" )

    age = input("Enter your age:" )

    num1 = input("Enter your first number:" )

    num2 = input("Enter your second number:" )

    result = (float(num1) + float(num2))



    print("Hello, " + name + "!")



    print("You are " + age + " years old")



    print("And this is the answer to your addition:")

    print(result)
    
    
numbers_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    
sampleInput = input("Sample input: ")

helloWorld = print("Hello World")
