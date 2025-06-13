#This code contains all the basic code of the lists in python
marks = [10,10,9.5,5,7]
print(marks)
newList = marks + [4,67,3]
print(newList)

#Appending the data in the list
programmingLanguage = ["C++","C","Python"]
print(programmingLanguage)
#Think if we have to add another language Java after python
#Solution
programmingLanguage.append("Java");
print(programmingLanguage)

programmingLanguage.append("C#")
programmingLanguage.append("Ruby")
programmingLanguage.append("Rust")
programmingLanguage.append("PHP")
programmingLanguage.append("JavaScript")

print(programmingLanguage)

programmingLanguage.pop(-1)
print(programmingLanguage)

#Printing all the values inside the array using the loop
i = 0
for i in range (len(programmingLanguage)):
    print(programmingLanguage[i])
    
#Sorting the strings in the List
programmingLanguage.sort()
print(programmingLanguage)

#Reversing the data in the list
programmingLanguage.reverse()
print(programmingLanguage)