คำสั่ง run web
---------------
python main.py ; ธรรมดาบนเทอร์มินัล

python generate.py | pygbag main.py ; รันบนเว็ป

---------------
Test URL
---------------
localhost:8000


---------------
การดัมป์
---------------
with open(r"C:\Users\garoc\Downloads\Word-Search-main\Word-Search-main\words.pkl", 'rb') as f:
    STD_ID = pickle.load(f)
    print(STD_ID)


---------------
จัดการ database
---------------
import pickle
import link_word

#set default
#with open('words.pkl', 'wb') as f:
#    pickle.dump(link_word.STD_ID, f)

#Read pickle database
with open("words.pkl", 'rb') as f:
    STD_ID = pickle.load(f)
    print((STD_ID))

    print("N = ",len(STD_ID))