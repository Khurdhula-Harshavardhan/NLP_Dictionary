

class Dictionary():
    """
    Global Variables.
    """
    file_handler = None

    #Constructor sets up all the global variables.
    def __init__(self) -> None:
        try:
            self.file_handler = open("theWarofTheWorlds.txt", encoding='UTF-8')
            print("Successfully opened the file.")
            self.printer()
        except Exception as e:
            print("The following error occured while trying to read the file: "+str(e))



Dictionary()