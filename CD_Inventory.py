#------------------------------------------#
# Title: CD_Inventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Mlist, 2020-March-14, added fucntions from previous assignments
# Mlist, 2020-March-15, build out all functionalities and tested
# Mlist, 2020-March-15, updated docstrings, cleaned up code, added comments
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD():
    """Stores data about a CD:

    properties:
        position: (int) with CD ID
        album: (string) with the title of the CD
        artist: (string) with the artist of the CD
    methods:
        append_cd_inventory_memory_list(objCD, table): -> None
    """
    # -- Fields -- #
    # -- Constructer -- #
    def __init__(self):
        self.__intPosition = 1
        self.__strAlbum = ""
        self.__strArtist = ""

    @property
    def position(self):
        return self.__intPosition
    @position.setter
    def position (self, ps):
        self.__intPosition = ps

    @property
    def album (self):
        return self.__strAlbum
    @album.setter
    def album (self, alb):
        self.__strAlbum = alb

    @property
    def artist (self):
        return self.__strArtist
    @artist.setter
    def artist (self, ar):
        self.__strArtist = ar

    def __str__(self):
        return str(self.__intPosition) + "\t" + str(self.__strAlbum) + "\tby: " + str(self.__strArtist)

    @staticmethod
    def append_cd_inventory_memory_list(objCD, table):
        """Function to append a newly created CD object (user input or file reading) to the global list of CD objects

        Uses passed arguements of CD information to create a new CD entry as a dictionary and adds dictionary as a new line to global 2D table

        Args:
            objCD (object): CD Object that needs to be added to the list 
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """
        table.append(objCD)
# -- PROCESSING -- #

class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        write_file(file_name, table): -> None
        load_inventory(file_name): -> cdObjLst (a list of CD objects)

    """
    # -- Methods --#
    @staticmethod
    def write_file(file_name, table):
        """Function to write added data to file

        Reads the data of objects stored in 2D table. 
        Casts each object into a string, adds a new line at the end of each string and overrides any data in file.

        Args:
            file_name (string): name of file used to read the data to
            table (list of objects): 2D data structure (list of objects) that holds the data during runtime

        Returns:
            None.
        """
        objFile = open(file_name, 'w')
        for obj in table:
            cd_string = str(obj.position)+ ',' + obj.album + ',' + obj.artist
            objFile.write(cd_string + '\n')
        objFile.close()

    @staticmethod
    def load_inventory(file_name):

        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a global 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            cdObjLst (list): list of objects
        """
        cdObjLst = []
        try:
            with open(file_name, 'r') as objFile:
                for line in objFile:
                    cdObjName = CD()
                    data = line.strip().split(',')
                    cdObjName.position = data[0]
                    cdObjName.album = data[1]
                    cdObjName.artist = data[2]
                    cdObjLst.append(cdObjName)
        except IOError: 
            print('\nThere is currently no existing inventory file\n')
        return cdObjLst

# -- PRESENTATION (Input/Output) -- #

class IO:
    """Presents menu, data and requests data from the user:

    properties:

    methods:
        cd_user_input(): -> CD (list)
        print_menu(): -> None
        menu_choice(): -> choice(string)
        show_inventory(table): -> None
    """
    # -- Methods --#
    @staticmethod
    def cd_user_input():
        """Gets user input to add new CD

        Catches ValueError in case the entered ID for the CD is not an integer. 
        If this exception is caught the program keeps asking the user to enter a numerical ID
        until an integer has been entered.

        Args:
            None.

        Returns:
            CD (list): Returns list with the 3 values: ID, Title and Artist

        """
        while True:
            try:
                strID = input('Enter a numerical ID: ').strip()
                intID = int(strID)
                break
            except ValueError:
                print ('The entered ID is not an integer. Please enter a number')
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        CD = [intID, strTitle, strArtist]
        return CD
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, ,s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of CD objects): 2D data structure (list of CD objects) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for obj in table:
            print(obj) #printing out __str__ for each CD object
        print('======================================')

# -- Main Body of Script -- #

# Load data from file into a list of CD objects on script start
initial_Load = FileIO.load_inventory(strFileName)
#assigning loaded data to list of CD objects
lstOfCDObjects = initial_Load 

while True:
    # Display menu to user
    IO.print_menu()
    strChoice = IO.menu_choice()
    # let user exit program
    if strChoice == 'x':
        break
    # let user load inventory from file
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            #FileProcessor.read_file(strFileName, lstTbl)
            lst = FileIO.load_inventory(strFileName)
            lstOfCDObjects = lst
            IO.show_inventory (lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory (lstOfCDObjects)
        continue  # start loop back at top.
    # let user add data to the inventory
    elif strChoice == 'a':
        UserInputLst = IO.cd_user_input() #requests the user input of the new CD object and temprorarly stores it into a list object
        cdObjName = CD() # initiate an empty CD object
        #Writing the user input into the initialized CD object
        cdObjName.position = UserInputLst[0]
        cdObjName.album = UserInputLst[1]
        cdObjName.artist = UserInputLst[2]
        #Appending the newly created CD to the CD object list
        CD.append_cd_inventory_memory_list(cdObjName, lstOfCDObjects)
        IO.show_inventory (lstOfCDObjects)
    # show user current inventory
    elif strChoice == 'i': 
        IO.show_inventory (lstOfCDObjects)
        #print('Length of CD object list :', len(lstOfCDObjects))
        continue
    # let user save inventory to file
    elif strChoice == 's':
        # Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower() #No Error handling required
        # Process choice
        if strYesNo == 'y':
            # save data
            FileIO.write_file(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    # catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
