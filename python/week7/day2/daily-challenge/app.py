from cgitb import reset


code = [
    [7,"i",3],
    ["T","s","i"],
    ["h", "%", "x"],
    ["i"," ", "#"],
    ["s", "M", " "],
    ["$","a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"]
]

# The matrix is a grid of strings (alphanumeric characters and spaces) 
# with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, 
# starting from the leftmost column, select only the alpha characters and connect them,
# then he replaces every group of symbols between two alpha characters by a space.
# Using his technique, try to decode this matrix

result = ""
for index in range(len(code[0])):
    for row in code:
        if str(row[index]).isalpha():
            result += str(row[index])
        else:
            result += " "

print(result)
