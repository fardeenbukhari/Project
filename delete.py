import json
import os
import modules as main
def Delete(data):
        try:
               os.remove("users/"+data+".json")
               main.showCommands()
               main.selectMenu()
                       
        except:
              print("Couldnt delete")
              main.showCommands()
              main.selectMenu()

                  
        
            

            
    