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

    def process_regex(self, filename) -> None:
        """
        We shall use the lib "os" module, which provides us with a method: os.getcwd(),
        to eliminate any possible directory/file path errors with the read of the file.
        """
        try:
            self.file_handler = open(os.getcwd() +"/"+ filename, "r", encoding = "UTF-8")

            for line in self.file_handler:
                for patternn in self.british_to_american_text_patterns.keys():
                    before_change = line
                    after_change = re.sub(patternn, self.british_to_american_text_patterns[patternn], line)
                    if before_change != after_change:
                        print(before_change)
                        print(after_change)
                        time.sleep(1)

            

        except Exception as e:
            print("The following error occured while trying to read the file: " + str(e))


Dictionary().process_regex("theWaroftheWorlds.txt")