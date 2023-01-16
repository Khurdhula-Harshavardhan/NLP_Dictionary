

class Dictionary():
    """
    Global Variables.
    """
    file_handler = None

    #Constructor sets up all the global variables.
    def __init__(self) -> None:
        self.file_handler = open("theWarofTheWorlds.txt", encoding='UTF-8')
        print("Successfully opened the file.")
        self.printer()


    def printer(self) -> None:
        
        with open('theWarofTheWorlds.txt',  encoding='UTF-8') as f:
            contents = f.read()
            print(contents)


Dictionary()