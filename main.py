import pygame
import generate
import sys
import link_word
import pickle

pygame.init()
screen = pygame.display.set_mode((800, 600))
selected = []

# Define button properties
button_width = 200
button_height = 50
button_x = 300
button_y = 450
button_color = (0, 255, 0)
button_hover_color = (0, 200, 0)


# Define button font properties
font_size = 25
font = pygame.font.SysFont(None, font_size)
text_color = (255, 255, 255)

def run_game():
    global list_choose
    selected = []

    def refine_list(lst):
        for i in range(len(lst)):
            lst[i]=remove_duplicate(lst[i])
        return lst


    def remove_duplicate(word):
        try:
            s=""
            s+=word[0]
            for i in range(1,len(word)):
                if word[i]!=s[-1]:
                    s+=word[i]
            return s
        except IndexError:
            return 0

    def display_board():
        x_start=0
        y_start=0
        for i in range(15):
            for j in range(15):
                if [x_start,y_start] in guessed_indexes:
                    pygame.draw.rect(screen,"green",(x_start,y_start,40,40),0)
                    pygame.draw.rect(screen,"black",(x_start,y_start,40,40),1)
                elif [x_start,y_start] in selected:
                    pygame.draw.rect(screen,"cyan",(x_start,y_start,40,40),0)
                    pygame.draw.rect(screen,"black",(x_start,y_start,40,40),1)
                    
                else:
                    pygame.draw.rect(screen,"blue",(x_start,y_start,(40),(40)),1)
                x_start+=40
            x_start=0
            y_start+=40
        

    def print_search():
        y=25
        search_format=pygame.font.Font("Quicksilver.ttf",30)
        for line in generate.grid:
            x=21
            for i in range(15):
                search_render=search_format.render(line[i].upper(),True,(0,0,0))
                width=search_render.get_width()
                height=search_render.get_height()
                screen.blit(search_render,(x-width//2,y-height//2))
                x+=40
            y+=40

    def display_words():
        x=625
        y=80
        word_format=pygame.font.Font("freesansbold.ttf", 25)
        title_words_format=pygame.font.Font("freesansbold.ttf", 35)

        title_words=title_words_format.render("WORDS",True,(255,0,255))
        screen.blit(title_words,(x,25))
        for word in generate.words_copy:
            display_word=word_format.render(word,True,(0,0,0))
            screen.blit(display_word,(x,y))
            y+=33
    def game_over_screen(screen,list_copy):
        game_over_format=pygame.font.Font("freesansbold.ttf", 45)
        try:
            if list_copy==[]:
                screen.fill((255,255,255))
                display_word=game_over_format.render(F"{link_word.STD_ID[list_choose[0]]} !!",True,"Green")
                x = (screen.get_width() - display_word.get_width()) // 2
                screen.blit(display_word,(x,320))
                display_word=game_over_format.render(F"Your baby taking is",True,"Green")
                x = (screen.get_width() - display_word.get_width()) // 2
                screen.blit(display_word,(x,200))
                button("FINISHED", button_x, button_y, button_width, button_height, button_color, button_hover_color, rerun_game)
                pygame.display.update()
        except Exception as e:
                game_over_format=pygame.font.Font("freesansbold.ttf", 80)
                display_word=game_over_format.render(F"THANK YOU",True,"Green")
                x = (screen.get_width() - display_word.get_width()) // 2
                screen.blit(display_word,(x,90))
                display_word=game_over_format.render(F"^",True,"Green")
                x = (screen.get_width() - display_word.get_width()) // 2
                screen.blit(display_word,(x,190))
                display_word=game_over_format.render(F"6410110062",True,"Green")
                x = (screen.get_width() - display_word.get_width()) // 2
                screen.blit(display_word,(x,280))
                display_word=game_over_format.render(F"6410110236",True,"Green")
                x = (screen.get_width() - display_word.get_width()) // 2
                screen.blit(display_word,(x,350))
                display_word=game_over_format.render(F"6410110663",True,"Green")
                x = (screen.get_width() - display_word.get_width()) // 2
                screen.blit(display_word,(x,420))
                pygame.display.update()

            



    drag=False
    #guessed=[]
    list_choose= []
    word=""
    running=True
    guessed_indexes=[]
    words_to_guess=refine_list(generate.words_copy[::])
    while(running):
        
        screen.fill((255,255,255))
        
        display_board()
        display_words()
        print_search()
        game_over_screen(screen,words_to_guess)

        for event in pygame.event.get():
            if (event.type!=pygame.MOUSEBUTTONUP):
                if event.type == pygame.QUIT:
                    running = False
                if (event.type == pygame.MOUSEBUTTONDOWN):       
                    drag=True
                    x, y = pygame.mouse.get_pos()
                    if (x>=0 and x<=600) and (y>=0 and y<=600):
                        word+=generate.grid[(y//40)%600][(x//40)%600]
                if event.type==pygame.MOUSEMOTION and drag:
                    x, y = pygame.mouse.get_pos()
                    if (x>=0 and x<=600) and (y>=0 and y<=600):
                        word+=generate.grid[(y//40)%600][(x//40)%600]
                        
                        guessed_indexes.append([(x//40)*40,(y//40)*40])
            else:
                # A variable that is used to determine if the mouse is being dragged.
                drag=False
                if remove_duplicate(word) in words_to_guess:
                    selected+=(guessed_indexes)
                    index=words_to_guess.index(remove_duplicate(word))
                    words_to_guess.remove(remove_duplicate(word))
                    generate.words_copy.pop(index)
                    list_choose.append(remove_duplicate(word))
                    print("CHOOSE = ",list_choose)
                    if len(list_choose) > 0 and len(list_choose) == 1:    
                        with open(r'C:\Users\garoc\Downloads\Word-Search-main\Word-Search-main\words.pkl', 'rb') as f:
                            database_value = pickle.load(f)

                        #Store ID in store_std_id.txt
                        with open('store_std_id.txt', 'a') as f:
                            f.writelines(database_value[list_choose[0]]+"\n")
                            f.close()
                        # Delete the id out from dictionary
                        id_to_delete = list_choose[0]
                        if id_to_delete in database_value:
                            del database_value[id_to_delete]

                        # Write the updated dictionary to a file
                        with open(r'C:\Users\garoc\Downloads\Word-Search-main\Word-Search-main\words.pkl', 'wb') as f:
                            pickle.dump(database_value, f)
                        with open(r'C:\Users\garoc\Downloads\Word-Search-main\Word-Search-main\words.pkl', 'rb') as f:
                            database_value = pickle.load(f)

                            print(database_value)
                        
                        with open("words.txt", "r+") as f:
                            lines = f.readlines()
                            f.seek(0)
                            for line in lines:
                                if list_choose[0] not in line:
                                    f.write(line)
                            f.truncate()

                word=""
                guessed_indexes=[]
        

        if not running:
            kill_game()

        pygame.display.update()
 

def kill_game():
    pygame.quit()
    sys.exit()

def terminate_game():
    pygame.quit()
    run_game()

def rerun_game():
    run_game()

def button(msg, x, y, w, h, ic, ac, action=None):
    """Draws a button on the screen"""
    mouse_pos = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]

    if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if clicked and action:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    text_surf = font.render(msg, True, text_color)
    text_rect = text_surf.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text_surf, text_rect)


background = pygame.image.load("TBG_PROJECT.jpg")
new_size = (800, 600)
scaled_image = pygame.transform.scale(background, new_size)
screen.blit(scaled_image, (0, 0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw button on the screen
    button('START', button_x, button_y, button_width, button_height, button_color, button_hover_color, rerun_game)
    
    # Update screen
    pygame.display.update()