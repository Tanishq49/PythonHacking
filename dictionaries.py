#This is an example of dictionaries in python

try:
    languageComplexityRating = {
        "HTML": 2,
        "Css" : 5,
        "JavaScript": 9,
        "C++": 10,
        "C": 10,
    }

    languageName = input("Enter any language (HTML,Css,JavaScript,C++,C):")
    print("The complexity in language "+ languageName + " is" , languageComplexityRating[languageName])
except(Exception):
    print("Some error occured in the code")
finally:
    #Creating the keys by assignment
    bioData = {}
    bioData["Name"] = "Tanishq"
    bioData["Age"] = 13
    bioData["OS"] = "Kali Linux"
    #This will add the data in to the bio data dictionary
    print(bioData)
    #Converting the dictionary keys/values into the list
    request = input("Which type of data you want from the dictionary(keys,values)?:")
    match(request):
        case "keys":
            newList = list(bioData.keys())
            print(newList)
        case "values":
            newList = list(bioData.values())
            print(newList)
        case default:
            print("Invalid Input")

        #Printing all the key values of dictionary one by one using for loop
    for dictKey in bioData:
        print(dictKey + ":" , bioData[dictKey])