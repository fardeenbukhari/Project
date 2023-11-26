import modules as main
import json
import os
def Retreive(data):
    try:
        with open("users/"+data+".json","r") as file:
            data = json.load(file)
            final = main.pd.Series(data)
            print(final)
            main.pyplot.bar(["math","english","science","urdu","sst"],[data["math"],data["english"],data["science"],data["urdu"],data["sst"]])
            main.pyplot.show()
    except:
        print("data not found")
        main.showCommands()
        main.selectMenu()
            
        
       


        

                    