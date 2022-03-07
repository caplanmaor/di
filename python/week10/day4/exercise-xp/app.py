import random

length = input("how long should the sentance be? 2-20: ")
if int(length) > 20 or int(length) < 2:
    print("only 2-20")
    exit()

def get_words_from_file():
    wordList = [] 
    for line in open('/home/maor/projects/di/python/week10/day4/exercise-xp/sowpods.txt','r'):
        line = line.strip('\n')
        wordList.append(line)
    return wordList

wordList = get_words_from_file()

def get_random_sentence(length):
    sentance = ""
    for i in range(int(length)):
        randomWordIndex = random.randint(0, len(wordList))
        sentance += wordList[randomWordIndex] + ' '
    return sentance.lower()

print(get_random_sentence(length))

def main():
    print("this program generates a random sentence")

