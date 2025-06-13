#This is an file maker command prompt
import os;
from colorama import Fore,Style
for i in range(1000000):
    command = input(">>")
    match(command):
        case "mkdir":
            dirName = input("Ente the name of the directory to be made:")
            if(os.path.exists(dirName)):
                print("Folder already found!.Please enter a unique folder name")
            else:
                os.mkdir(dirName)
        case "mtldir":
            baseDirName = input("Enter the base name of the directory:")
            if(os.path.exists(baseDirName)):
                print("Directory name already found same with base dir name!Enter a unique directory name")
            else:
                dirCount = int(input("Enter the number of directories to be made:"))
                i = 1
                for i in range (dirCount):
                    os.mkdir(baseDirName +str(i))
        case "mFile":
            fileName = input("Enter the file name to be made:")
            makeFile = open(fileName,'w')
            makeFile.write("")
            makeFile.close()
        case 'rFile':
            try:
                fileName = input("Enter the file name to read:")
                openFile = open(fileName)
                readFile = openFile.read()
                print(Fore.GREEN,readFile, Style.RESET_ALL)
                openFile.close()
            except(Exception):
                print(f"{Fore.RED}Please enter a valid file name{Style.RESET_ALL}")
        case "aFile":
            try:
                fileName = input(f"{Fore.YELLOW}Enter the file name:{Style.RESET_ALL}")
                openFile = open(fileName,'a')
                appendText = input(f"{Fore.CYAN}Enter the text to append in the file:{Style.RESET_ALL}")
                appendingText = openFile.write(appendText)
                openFile.close()
            except(Exception):
                print(f"{Fore.RED}Invalid Input!{Style.RESET_ALL}")
        case "cFile":
            try:
                existingFileName = input(f"{Fore.YELLOW}Enter the file name to copy:{Style.RESET_ALL}")
                newName = input(f"{Fore.MAGENTA}Enter the new name of the copied file:{Style.RESET_ALL}")
                openExistingFile = open(existingFileName)
                existingFileContent = openExistingFile.read()
                makeNewFile = open(newName,'w')
                writeIntoFile = makeNewFile.write(existingFileContent)
                print(f"{Fore.GREEN}Changes made successfully!{Style.RESET_ALL}")
                openExistingFile.close()
                makeNewFile.close()
            except(FileNotFoundError):
                print(f"{Fore.RED}File not found.Please enter a valid file name!{Style.RESET_ALL}")
        case 'eraseData':
            try:
                fileName = input(f"{Fore.YELLOW}Enter the file name to erase the data:{Style.RESET_ALL}")
                #Confirmation to erase the data
                confirmation = input(f"{Fore.LIGHTRED_EX}Are you sure to remove the data(y/n):{Style.RESET_ALL}")
                match(confirmation):
                    case "y":
                        openFile = open(fileName,'w')
                        eraseData = openFile.write(" ")
                        openFile.close()
                        print(f"{Fore.GREEN}Changes made successfully!{Style.RESET_ALL}")
                    case 'n':
                        print(f"{Fore.LIGHTGREEN_EX}Cancelled the operation!{Style.RESET_ALL}")
                    case default:
                        print(f"{Fore.BLUE}Please enter a valid command{Style.RESET_ALL}")
            except(Exception):
                print(f"{Fore.RED}Invalud Input{Style.RESET_ALL}")
        case default:
            print(f"{Fore.BLUE}Please enter a valid command{Style.RESET_ALL}")
        