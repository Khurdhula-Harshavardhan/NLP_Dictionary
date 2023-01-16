import re
import os
import time

class Dictionary():
    """
    Global Variables.
    """
    file_handler = None
    british_to_american_text_patterns = dict()
    titles = dict()
    text= None
    log_handler = None
    output_handler = None
    CURRENT_PATH = None
    #total_words_replaced
    #total_characters_discarded
    
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

        self.titles = {
            "Dr\.": "Doctor",
            "Mr\.": "Mister",
            "Ms\.": "Miss",
            "Mrs\.": "Misses"
        }

        #defining a constant for current directory. 
        self.CURRENT_PATH = os.getcwd()+"/"
        self.log_handler = open(self.CURRENT_PATH+ "changes_log.txt", "w+", encoding="UTF-8")

    def read_file(self, filename):
        try:
            self.file_handler = open(self.CURRENT_PATH + filename, "r", encoding = "UTF-8")
            self.text = self.file_handler.read()
        except Exception as e:
            print("The following error occured while trying to read " + filename + str(e))

    def process_regex(self, filename) -> None:
        """
        We shall use the lib "os" module, which provides us with a method: os.getcwd(),
        to eliminate any possible directory/file path errors with the read of the file.

        However, we are setting up the file_handlers within this method rather than the constructor, 
        because the first method to be called, while executing this script is:
        Dictionary.process_regex(filename) 
        Hence the parameter is passed here.
        """

        try:
            self.read_file(filename)
            self.text = self.replace_british_words()
            self.text = self.text.split("\n")
            self.replace_titles()

            if self.flush_output("regex.txt"):
                print("Output stored to 'regex.txt'")
        except:
            print("Failed to process text!")
       

    def replace_british_words(self) -> list():
        """
        Dictionary.replace_british_words() aims to replace words captured by patterns in the dict we have, with counter part American words.
        This is achieved by using re.sub() method.
        The change made is stored to the global variable self.text which is a list that stores all lines read from the file.
        The changes are also noted to changes_log.txt
        """

        try:
            for patternn in self.british_to_american_text_patterns.keys():
                self.text = re.sub(patternn, self.british_to_american_text_patterns[patternn], self.text)
                self.write_log("Replacing British Words using the pattern:", patternn , self.british_to_american_text_patterns[patternn])

            return self.text
        except Exception as e:
            print(str(e))
    

    def replace_titles(self) -> None:
        """
        Dictionary.replace() aims to replace the titles, that we generally address people with
        This is achieved by using re.sub() method.
        The change made is stored to the global variable self.text which is a list that stores all lines read from the file.
        The changes are also noted to changes_log.txt
        """

        try:
            for ind in range(len(self.text)):
                line = self.text[ind]
                for patternn in self.titles.keys():
                    before_change = line
                    after_change = re.sub(patternn, self.titles[patternn], line)

                    if before_change != after_change:
                        self.write_log("Replacing Titles", before_change, after_change)

                    self.text[ind] = after_change
                    
        except Exception as e:
            print(str(e))
    

    def write_log(self, calling_method, original_text, modified_text) -> None:
        """
        write_log method, writes three statements to changes_log.txt everytime it is called,
        the goal of this method is to capture the changes that occur in sentences as we process the lines from self.text.
        """

        try:
            line = "\n" + calling_method + "\n" + original_text +"\n"+ modified_text + "\n"
            self.log_handler.write(line)

        except Exception as e:
            print("The following error occured while trying to write changes to changes_log.txt: " + str(e))


    def flush_output(self, filename) -> bool:
        """
        flush_output method writes all the text that has to be stored in the output file,
        We write all of it once to the file by using handler.writelines() which enables us to pass the iterable, self.text in this case.
        This method returns a boolean value to check that the output has been written to the file without any Tracebacks,
        In the case that there's a unexpected error that arises during the method execution, the error is simply written to console and False is returned.
        """
        try:
            self.output_handler = open(self.CURRENT_PATH + filename, "w+", encoding="UTF-8")
            self.text = "\n".join(self.text)
            self.output_handler.write(self.text)
            return True
        except Exception as e:
            print("The following error occured while writing output to "+ filename+ " " + str(e))
            return False

    #PHASE II - Normalization
    def normalize_text(self, filename) -> None:
        """
        The aim of this Phase is to:
        1. Make all words of same CASE (lower)
        2. Discard duplicates
        3. Strip away all the punctuations
        4. Tokenize
        5. Flush the output to dictionary.txt
        """
        pass

    #Destructor is responsible for closing all file handlers that have been used :)
    def __del__(self) -> None:
        self.file_handler.close()
        self.output_handler.close()

Dictionary().process_regex("theWaroftheWorlds.txt")