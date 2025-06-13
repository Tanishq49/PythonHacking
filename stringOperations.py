#This code contains all the string operations

operatingSystem = "Kali Linux"

print(len(operatingSystem))#To take out the length of the string

#Loop to print all the charachters of the strings one by one
lengthOperatingSystem = len(operatingSystem)
for i in range (lengthOperatingSystem):
    print(operatingSystem[i])

#Negative indexing in python:
languageName = "python"
#Printing the last letter of string "langaugeName" i.e. python :
print("The last letter of string languageName is :",languageName[-1]);#Starts from last place

#Printing the letters using sign ':'
print("The letter between 1 - 3 in string language name is:",languageName[1:3])

#String concatination in python:
string1 = "This is an example"
blank = " "
string2 = "of string concatination"
result = string1+blank+string2
print(result)

#String repetetion
#Printing the same string 10 times

newString = "Hello "
print(newString * 10)

changingString = "Java"
changingString = 'H' + changingString[1:] #Result -> Hava
print(changingString)

#Find method 
#This is used to find the index of given character in the string
programmingLanguage = "C++"
findTheLocationOfC = programmingLanguage.find("C")
print(findTheLocationOfC);
#The result will be 0

#replace method ->
programmingLanguage2 = "C#"
cPlus = programmingLanguage2.replace("#","++")
print(cPlus)  


#converting the string into upper case
sentence1 = "This is an sentence which will be converted into uppercase"
sentence1Uppercase = sentence1.upper();
print(sentence1Uppercase)

#Capitalize method in python:
sentence2 = "this is an sentence which will be capitalized"
sentence2Capitalized = sentence2.capitalize();
print(sentence2Capitalized)

#Split method in python
line1 = "This is an example of sentence"
splittedLine1 = line1.split(" ")
print(splittedLine1) 
print(type(splittedLine1)) 