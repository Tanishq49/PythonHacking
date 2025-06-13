#This is an example of fileSystem in python

#Writing into an file
openFile = open("helloToPython.txt",'w')
openFile.write("This is an text written inside the helloToPython.txt file")
openFile.close()

#Reading the content of the file
readingFile = open("learning/newFile.md")
fileContent = readingFile.read()
print(fileContent)