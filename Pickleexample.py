import pickle

ARR = ("DilSe","ManiRatnam","Sharuk","Manisha",1992,
       ((1,"Thaiya Thaiya","sukhwinder Singh"),
        (2,"Ae Ajnabi","Udi Narayan"),
        (3,"Satarangi Re","Kavitha Krishnamurthy")))

even_list = list (range (0,30,2))
odd_list = list (range (1,30,2))

with open ("ARR.pickle","wb") as pickle_file:
    pickle.dump(ARR,file=pickle_file)
    pickle.dump(even_list,file=pickle_file)
    pickle.dump(odd_list,file=pickle_file)

with open ("ARR.pickle","rb") as pickle_read_file:
        ARR2 = pickle.load(pickle_read_file)
        evenlist=pickle.load(pickle_read_file)
        oddlist=pickle.load(pickle_read_file)

print (ARR2)

album, director ,hero ,heroine, year, track_list = ARR2

print (album)
print (director)
print(hero)
print (heroine)
print(year)
for track in track_list:
    track_number,songname,singer = track
    print (track_number)
    print (songname)
    print(singer)

print("*"*50)

for i in evenlist:
    print (i)
print("*" *50)

for i in oddlist:
    print (i)
print("*"*50)



