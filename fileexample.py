 #
 # values = [1234,5678,9012]
 #
 #
 # with open("C:\\Users\\vp40614\\PycharmProjects\\Venky\\cities.txt","a+") as f:
 #
 # #f = open("C:\\Users\\vp40614\\PycharmProjects\\Venky\\cities.txt","r+")
 #     print(f.name)
 #     f.write("Belfast\n")
 #     f.write("London\n")
 #     for value in values:
 #         f.write(str(value))
 #         f.write("\n")
 #     f.close()
#
#
# with open("C:\\Users\\vp40614\\PycharmProjects\\Venky\\cities.txt","r+") as f:
#     for line in f:
#         print(line,end='')
#
# print("*" *50)


with open("C:\\Users\\vp40614\\PycharmProjects\\Venky\\cities.txt","r+") as f:
     data_contents = f.readlines()

print("Content of file before Insert" + str(data_contents))
data_contents.insert(1,"Belfast")

with open("C:\\Users\\vp40614\\PycharmProjects\\Venky\\cities.txt","w+") as f:
    data_contents = "".join(data_contents)
    f.write(data_contents)


with open("C:\\Users\\vp40614\\PycharmProjects\\Venky\\cities.txt","r+") as f:
    print("Print the lines after write")
    for line in f:
        print(line)

