def countWordsFromFile():
    filename = input("Please Enter The File Name: ")
    numberOfWords = 0
    file = open(filename,'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords +len(words)
        
    print(numberOfWords)

countWordsFromFile()