import re
import os
import time

class Dictionary():
    """
    Global Variables.
    """
    file_handler = None
    british_to_american_text_patterns = dict()
    text= None
    log_handler = None
    CURRENT_PATH = None

    #Constructor sets up all the global variables.
    def __init__(self) -> None:

        #storing all the matching words inorder to make it easier for retrival with a dict()
        self.british_to_american_text_patterns ={
            "[Cc]olour":"color",
            "[Nn]eighbour":"neighbor",
            "[Hh]omour": "humor",
            "[Ll]abour": "labor",
            "[Ff]lavour": "flavor",
            "[aA]nalyse": "analyze",
            "[pP]aralyse": "paralyze",
            "[dD]efence": "defence",
            "[lL]icence": "license",
            "[oO]ffence": "offense",
            "[pP]retence": "pretense"
        }

        #defining a constant for current directory. 
        self.CURRENT_PATH = os.getcwd()+"/"


    def process_regex(self, filename) -> None:
        """
        We shall use the lib "os" module, which provides us with a method: os.getcwd(),
        to eliminate any possible directory/file path errors with the read of the file.
        """
        try:
            self.file_handler = open(self.CURRENT_PATH + filename, "r", encoding = "UTF-8")
            self.log_handler = open(self.CURRENT_PATH+ "changes_log.txt", "w+", encoding="UTF-8")
            for line in self.file_handler:
                for patternn in self.british_to_american_text_patterns.keys():
                    before_change = line
                    after_change = re.sub(patternn, self.british_to_american_text_patterns[patternn], line)
                    if before_change != after_change:
                        self.write_log("Replacing British Words", before_change, after_change)
                        print(before_change)
                        print(after_change)
                        

            

        except Exception as e:
            print("The following error occured while trying to read the file: " + str(e))

    

    def write_log(self, calling_method, original_text, modified_text):
        try:
            line = "\n" + calling_method + "\n" + original_text + "\n" + modified_text + "\n"
            self.log_handler.write(line)
        except Exception as e:
            print("The following error occured while trying to write changes to changes_log.txt: " + str(e))
            
Dictionary().process_regex("theWaroftheWorlds.txt")