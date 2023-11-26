import modules as main
def selectMenu():
    option = int(input("Please enter an option : "))
    if option==1:
        print("Recording new user to database")
        recordName = input("Enter name : ")
        mathMarks = int(input("Enter Math marks : "))
        englishMarks = int(input("Enter English marks : "))
        scienceMarks = int(input("Enter Science marks : "))
        urduMarks = int(input("Enter Urdu marks : "))
        sstMarks = int(input("Enter Sst marks : "))
        finalRecord = {"name":recordName,"math":mathMarks,"english":englishMarks,"science":scienceMarks,"urdu":urduMarks,"sst":sstMarks}
        main.Record(finalRecord)


    elif option == 2:
       recordName = input("Enter name : ")
       main.Retreive(recordName)
       
    elif option == 3:
        recordName = input("Enter name : ")
        mathMarks = int(input("Enter Math marks : "))
        englishMarks = int(input("Enter English marks : "))
        scienceMarks = int(input("Enter Science marks : "))
        urduMarks = int(input("Enter Urdu marks : "))
        sstMarks = int(input("Enter Sst marks : "))
        finalRecord = {"name":recordName,"math":mathMarks,"english":englishMarks,"science":scienceMarks,"urdu":urduMarks,"sst":sstMarks}
        main.Update(finalRecord)
    elif option == 4:
        print("deleting user from database")
        recordName = input("Enter name : ")
        main.Delete(recordName)

    else:
        print("Not a Valid Option")
        main.showCommands()
        main.selectMenu()
        


    