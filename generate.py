import random
def generate_word_list():
    file=open("words.txt","r")
    words_list=[]
    wordrandlist = []
    for line in file.readlines():
        words_list.append(line.rstrip())
        wordrandlist.append(random.choice(words_list)+"\n")
    return words_list

def check_possiblity(matrice,word,index,fitting_orders,fitting_order):
    x,y=index

    # Assigning the value of the key in the dictionary to the variables ix and iy.
    ix,iy=fitting_orders[fitting_order]

    try:
        # This code is used to check if the word can be placed in the grid.
        for i in range(len(word)):
            if 0<=y<=14 and 0<=x<=14:
                if matrice[y][x]!="0":
                    return False
                x+=ix
                y+=iy
            else :
                return False
    except IndexError:
        return False

    return True

def put_in_word(matrice,word,index,fitting_orders,fitting_order):
    x,y=index
    ix,iy=fitting_orders[fitting_order]
    # This code is used to place the word in the grid.
    for _ in range(len(word)):
        matrice[y][x]=word[_]
        y+=iy
        x+=ix

def generate_words(words):
    for i in range(10): 
        random_word=random.choice(lst_words)
        words.append(random_word)
        lst_words.remove(random_word)
    return words

grid=[]
alphabet="ABCDFEFGHIJKLMNOPQRSTUVWXYZ"
alphabet=list(alphabet)

# This code is used to create a 15x15 grid.
for i in range(15):
    grid.append(list("0"*15))
# Creating a list of words from the file words.txt and then creating a copy of that list.
lst_words=generate_word_list()
words=generate_words([])
words_copy=words[::]


possibilites={"f":(1,0),"b":(-1,0),"u":(0,-1),"d":(0,1)}
moves=["f","b","u","d"]

# This code is used to generate a word search puzzle.
while(True):
    if words==[]:
        break

    # Choosing a random word from the list of words.
    word=random.choice(words)
    words.remove(word)

    # Generating a random number between 0 and 14.
    x_coordinate=random.randint(0,14)
    y_coordinate=random.randint(0,14)
    
    # Creating a tuple of the two values.
    index=(x_coordinate,y_coordinate)
    pattern=random.choice(moves)
    
    # Checking if the word can be placed in the grid.
    while(check_possiblity(grid,word,index,possibilites,pattern)!=1):
        x_coordinate=random.randint(0,14)
        y_coordinate=random.randint(0,14)
        index=(x_coordinate,y_coordinate)
    put_in_word(grid,word,index,possibilites,pattern)
for i in range(15):
    for j in range(15):
        if grid[i][j]=="0":
            grid[i][j]=random.choice(alphabet)

#Swap word position in file words.txt
with open('words.txt', 'r+') as f:
    wordschange = []
    listword = generate_word_list()
    for i in range(len(listword)-1):
        random_word=random.choice(listword)
        #print(random_word)
        wordschange.append(random_word+'\n')
        listword.remove(random_word)
    random_word=random.choice(listword)
    wordschange.append(random_word)
    f.writelines(wordschange)
    f.close()
