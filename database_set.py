import pickle
import link_word

#set default
with open('words.pkl', 'wb') as f:
    pickle.dump(link_word.STD_ID, f)

#Read pickle database
with open("words.pkl", 'rb') as f:
    STD_ID = pickle.load(f)
    print((STD_ID))

    print("N = ",len(STD_ID))


#Cut off words.txt
"""with open("words.txt", "r+") as f:
    lines = f.readlines()
    f.seek(0)
    for line in lines:
        if 'coconut' not in line:
            f.write(line)
    f.truncate()"""

        