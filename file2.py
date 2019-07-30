import mainexample

print ("File2 __name__ = %s" %__name__ )

if __name__ == '__main__':
    print ("File2 is being run directly")
else:
    print("File2 is being Imported")

question = ['name','color','shape']
answers = ['Apple','Red','Round']

for quest,ans in zip(question,answers):
    print("What is your {0} : I am {1}".format(quest,ans))

for key,value in enumerate(question):
          print(key,value)


for k in reversed(range(1,10)):
    print(k)

for i in range(0,6):
    for j in range(0,i):
        print("* ",end="")
    print()
