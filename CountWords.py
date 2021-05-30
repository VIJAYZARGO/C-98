def CountWordsFromFile():
    fileName = input("Enter The File Name : ")
    numberofWords = 0
    file = open(fileName, "r")
    for line in file:
        words = line.split()
        numberofWords += len(words)
    print("Number Of Words : ")
    print(numberofWords)

CountWordsFromFile()