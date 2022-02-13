list = []
for i in range(3):
    word = input(f"{i} type a word: ")
    list.append(str(word))

list.sort()
print(list)