with open("data.txt", 'r') as file:

    array = []
    finalarray = []
    content = file.readlines()
    row = 0

    for line in content:

        row += 1
        array = line.split(",")

        array[-1] = array[-1].strip()

        finalarray.append(array)

for x in finalarray:
    print(x)

#fuck aashish