import os

dirpath = "C:\\users\\Bhuvan_Nithya\\PycharmProjects\\Geeks"


def printdircontents(dirpath):
    for spath in os.listdir(dirpath):
        childpath  = os.path.join(dirpath,spath)
        if os.path.isdir(childpath):
            printdircontents(childpath)
        else:
            print(childpath)



if __name__ == '__main__':
    for root,dirs,files in os.walk(dirpath,topdown=True  ):
        for name in files:
            print(os.path.join(root,name))
        for name in dirs:
            print(os.path.join(root,name))

    fruit = {'Apple':'Sweet','Orange':'Sour','Lemon':'Citrus'}
    fruit1 = {}
    #print(fruit.keys())
   # print(fruit.values())


  #  for x in fruit:
   #     fruit1[fruit[x]] = x
        #fruit1[x] = x
   # fruit1={fruit.values():fruit.keys()}
    #print(fruit1)
   # printdircontents(dirpath)
    #print(fruit1)