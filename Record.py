import json
import os
import modules as main
def Record(data): 
        try:
             if(os.path.isfile("users/"+data["name"]+".json")):
                  print("User Already Exists Try Updating")  
                  main.showCommands()
                  main.selectMenu()

             else:   
                  with open("users/"+data["name"]+".json","w") as file:
                        json.dump(data,file)
                        print("data recorded")
                        os.wait(3)
                        main.showCommands()
                        main.selectMenu()
        except:
              print("Couldnt Record")
              main.showCommands()
              main.selectMenu() 
                  
        
            

            
    