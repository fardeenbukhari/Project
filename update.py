import json
import os
import modules as main
def Update(data): 
        try:
             if(not(os.path.isfile("users/"+data["name"]+".json"))):
                  print("User Doesnt Exist")  
                  main.showCommands()
                  main.selectMenu()

             else:   
                  with open("users/"+data["name"]+".json","w") as file:
                        json.dump(data,file)
                        print("data Updated")
                        os.wait(3)
                        main.showCommands()
                        main.selectMenu()
        except:
              print("Couldnt Update")
              main.showCommands()
              main.selectMenu() 
                  
        
            

            
    