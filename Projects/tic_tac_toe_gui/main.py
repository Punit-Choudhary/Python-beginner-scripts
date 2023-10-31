import pygame as pg
import random
import copy
import time

pg.init()
big_font = pg.font.SysFont("monospace", 200)
medium_font = pg.font.SysFont("comicsans", 30)

width = 600
height = 600

leftcl = (255,255,255)
rightcl = (255,255,255)

x_score = 0
o_score = 0
turn = "x"
game_over = False
win_show = False
show_win_count = 0
draw_show = False
show_draw_count = 0
recent_winner = ""
recent_game_pieces = []

pieces = [["","",""],["","",""],["","",""]]

win = pg.display.set_mode((width+300,height))
pg.display.set_caption("Tic tac toe")

def draw_grid(win):
    pg.draw.rect(win,(0,0,0),((width/3)-3,0,6,height))
    pg.draw.rect(win,(0,0,0),((width*2/3)-3,0,6,height))
    pg.draw.rect(win,(0,0,0),(0,(height/3)-3,width,6))
    pg.draw.rect(win,(0,0,0),(0,(height*2/3)-3,width,6))
    pg.draw.rect(win,(0,0,0),(0,0,width,6))
    pg.draw.rect(win,(0,0,0),(0,0,6,height))
    pg.draw.rect(win,(0,0,0),(width-6,0,6,height))
    pg.draw.rect(win,(0,0,0),(0,height-6,width,6))
    pg.draw.rect(win,leftcl,(width+25,500,100,50))
    pg.draw.rect(win,(0,0,0),(width+25,500,100,50),2)

def draw_sidebar(win):
    draw_text(win, "You (X) : ", width+65, 90, medium=True, big=False, color=(255,255,255))
    draw_text(win, "Computer (O) : ", width+25, 180, medium=True, big=False, color=(255,255,255))
    if recent_winner == "x":
        draw_text(win, str(x_score), width+65+150, 90, medium=True, big=False, color=(0,255,0))
        draw_text(win, str(o_score), width+25+230, 180, medium=True, big=False, color=(255,255,255))        
    elif recent_winner == "o":
        draw_text(win, str(o_score), width+25+230, 180, medium=True, big=False, color=(0,255,0))
        draw_text(win, str(x_score), width+65+150, 90, medium=True, big=False, color=(255,255,255))
    else:
        draw_text(win, str(o_score), width+25+230, 180, medium=True, big=False, color=(255,255,255))
        draw_text(win, str(x_score), width+65+150, 90, medium=True, big=False, color=(255,255,255))

    if not win_show:
        if turn == "x":
            draw_text(win, "Your turn", width+75, 360, medium=True, big=False, color=(255,255,255))
        else:
            draw_text(win, "Computer's turn", width+35, 360, medium=True, big=False, color=(255,255,255))
    
    draw_text(win, "Reset", width+25+10, 500, medium=True, big=False)
    pg.draw.rect(win,rightcl,(width+175,500,100,50))
    pg.draw.rect(win,(0,0,0),(width+175,500,100,50),2)
    draw_text(win, "Quit", width+175+15, 500, medium=True, big=False)

def draw_text(win, text, x, y, big=True, color=(0,0,0), medium=False):
    if big:
        text = big_font.render(text, True, color)
        win.blit(text, (x,y))
    elif medium:
        text = medium_font.render(text, True, color)
        win.blit(text, (x,y))

def draw_pieces(pieces, win):
    draw_text(win, pieces[0][0], 42, -21)
    draw_text(win, pieces[1][0], 238, -21)
    draw_text(win, pieces[2][0], 441, -21)
    draw_text(win, pieces[0][1], 42, 175)
    draw_text(win, pieces[1][1], 238, 175)
    draw_text(win, pieces[2][1], 441, 175)
    draw_text(win, pieces[0][2], 42, 371)
    draw_text(win, pieces[1][2], 238, 371)
    draw_text(win, pieces[2][2], 441, 371)

def show_win(winner, screen):
    global show_win_count, win_show, recent_winner
    if show_win_count < 45:
        if recent_winner == "x":
            draw_text(screen, "You win!", width+75, 270, big=False, medium=True, color=(0,255,0))
        else:
            draw_text(screen, "Computer wins!", width+35, 270, big=False, medium=True, color=(0,255,0))
    elif show_win_count == 60:
        win_show = False
        show_win_count = 0
        recent_winner = ""
    show_win_count += 1

def show_draw(screen):
    global show_draw_count, draw_show
    if show_draw_count < 45:
        draw_text(screen, "Draw", width+100, 270, big=False, medium=True, color=(255,255,0))
    elif show_draw_count == 60:
        draw_show = False
        show_draw_count = 0
    show_draw_count += 1

def draw_win(screen):
    global game_over, win_show, recent_winner, recent_game_pieces, x_score, o_score, pieces, draw_show
    screen.fill((255,255,255))
    pg.draw.rect(screen,(100,100,100),(width,0,300,height))
    draw_grid(screen)
    draw_sidebar(screen)
    if win_show or draw_show:
        draw_pieces(recent_game_pieces, screen)
    else:
        draw_pieces(pieces, screen)
    is_win, winner = check_win(pieces)
    if winner == "draw":
        recent_game_pieces = pieces
        pieces = [["","",""],["","",""],["","",""]]
        draw_show = True
    elif is_win and run == True:
        win_show = True
        game_over = True
        if winner == "x":
            x_score += 1
        else:
            o_score += 1
        recent_winner = winner
        recent_game_pieces = pieces
    if win_show:
        show_win(recent_winner, screen)
    elif draw_show:
        show_draw(screen)
    pg.display.update()

def next_move(get_pieces,win):
    all_possible = []
    other_wins = []
    for i in range(3):
        il = get_pieces[i]
        for j in range(3):
            if get_pieces[i][j] == "":
                temp = copy.deepcopy(get_pieces)
                temp[i][j] = "o"
                all_possible.append(copy.deepcopy(temp))
                temp = []
    for i in range(3):
        il = get_pieces[i]
        for j in range(3):
            if get_pieces[i][j] == "":
                temp = copy.deepcopy(get_pieces)
                temp[i][j] = "x"
                if check_win(temp)[0]:
                    other_wins.append([i,j])
                temp = []
    for k in all_possible:
        if check_win(k)[0]:
            time.sleep(0.75)
            return k
    if other_wins != []:
        new = copy.deepcopy(get_pieces)
        i = other_wins[0][0]
        j = other_wins[0][1]
        new[i][j] = "o"
        time.sleep(0.75)
        return new
    else:
        time.sleep(0.75)
        return random.choice((all_possible))
    

def check_win(pieces):
    #vertical
    if pieces[0][0] == pieces [0][1] and pieces[0][0] == pieces [0][2] and pieces[0][0] != "":
        if pieces[0][0] == "x":
            return True, "x"
        else:
            return True, "o"
    elif pieces[1][0] == pieces [1][1] and pieces[1][0] == pieces [1][2] and pieces[1][0] != "":
        if pieces[1][0] == "x":
            return True, "x"
        else:
            return True, "o"
    elif pieces[2][0] == pieces [2][1] and pieces[2][0] == pieces [2][2] and pieces[2][0] != "":
        if pieces[2][0] == "x":
            return True, "x"
        else:
            return True, "o"
    #horizontal
    elif pieces[0][0] == pieces [1][0] and pieces[0][0] == pieces [2][0] and pieces[0][0] != "":
        if pieces[0][0] == "x":
            return True, "x"
        else:
            return True, "o"
    elif pieces[0][1] == pieces [1][1] and pieces[0][1] == pieces [2][1] and pieces[0][1] != "":
        if pieces[0][1] == "x":
            return True, "x"
        else:
            return True, "o"
    elif pieces[0][2] == pieces [1][2] and pieces[0][2] == pieces [2][2] and pieces[0][2] != "":
        if pieces[0][2] == "x":
            return True, "x"
        else:
            return True, "o"
    #diagonal
    elif pieces[0][0] == pieces [1][1] and pieces[0][0] == pieces [2][2] and pieces[0][0] != "":
        if pieces[0][0] == "x":
            return True, "x"
        else:
            return True, "o"
    elif pieces[0][2] == pieces [1][1] and pieces[0][2] == pieces [2][0] and pieces[0][2] != "":
        if pieces[0][2] == "x":
            return True, "x"
        else:
            return True, "o"
    elif pieces[0][0] != "" and pieces[0][1] != "" and pieces[0][2] != "" and pieces[1][0] != "" and pieces[1][1] != "" and pieces[1][2] != "" and pieces[2][0] != "" and pieces[2][1] != "" and pieces[2][2] != "":
            return False, "draw"
    else:
        return False, ""

run = True
clock = pg.time.Clock()
while run:
    clock.tick(30)
    draw_win(win)
    if game_over:
        pieces = [["","",""],["","",""],["","",""]]
        game_over = False

    m_pos = pg.mouse.get_pos()
    if m_pos[0] >= width+25 and m_pos[0] <= width+125 and m_pos[1] >= 500 and m_pos[1] <= 550:
        leftcl = (200,200,200)
    else:
        leftcl = (255,255,255)
    if m_pos[0] >= width+175 and m_pos[0] <= width+275 and m_pos[1] >= 500 and m_pos[1] <= 550:
        rightcl = (200,200,200)
    else:
        rightcl = (255,255,255)

    if turn == "o":
        pieces = next_move(pieces,win)
        turn = "x"
        
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            run = False
            break
        
        if event.type == pg.MOUSEBUTTONUP: #check click - quite hard to understand gg rip
            pos = pg.mouse.get_pos()
            if not win_show and not draw_show and turn == "x":
                if pos[0] >= 6 and pos[0] <= (width/3)-3:
                    if pos[1] >= 6 and pos[1] <= (height/3)-3 and pieces[0][0] == "":
                        if turn == "x":
                            pieces[0][0] = "x"
                            turn = "o"
                        else:
                            pieces[0][0] = "o"
                            turn = "x"
                    elif pos[1] >= (height/3)+3 and pos[1] <= (height*2/3)-3 and pieces[0][1] == "":
                        if turn == "x":
                            pieces[0][1] = "x"
                            turn = "o"
                        else:
                            pieces[0][1] = "o"
                            turn = "x"
                    elif pos[1] >= (height*2/3)+3 and pos[1] <= height-6 and pieces[0][2] == "":
                        if turn == "x":
                            pieces[0][2] = "x"
                            turn = "o"
                        else:
                            pieces[0][2] = "o"
                            turn = "x"
                elif pos[0] >= (width/3)+3 and pos[0] <= (width*2/3)-3:
                    if pos[1] >= 6 and pos[1] <= (height/3)-3 and pieces[1][0] == "":
                        if turn == "x":
                            pieces[1][0] = "x"
                            turn = "o"
                        else:
                            pieces[1][0] = "o"
                            turn = "x"
                    elif pos[1] >= (height/3)+3 and pos[1] <= (height*2/3)-3 and pieces[1][1] == "":
                        if turn == "x":
                            pieces[1][1] = "x"
                            turn = "o"
                        else:
                            pieces[1][1] = "o"
                            turn = "x"
                    elif pos[1] >= (height*2/3)+3 and pos[1] <= height-6 and pieces[1][2] == "":
                        if turn == "x":
                            pieces[1][2] = "x"
                            turn = "o"
                        else:
                            pieces[1][2] = "o"
                            turn = "x"
                elif pos[0] >= (width*2/3)+3 and pos[0] <= width-6:
                    if pos[1] >= 6 and pos[1] <= (height/3)-3 and pieces[2][0] == "":
                        if turn == "x":
                            pieces[2][0] = "x"
                            turn = "o"
                        else:
                            pieces[2][0] = "o"
                            turn = "x"
                    elif pos[1] >= (height/3)+3 and pos[1] <= (height*2/3)-3 and pieces[2][1] == "":
                        if turn == "x":
                            pieces[2][1] = "x"
                            turn = "o"
                        else:
                            pieces[2][1] = "o"
                            turn = "x"
                    elif pos[1] >= (height*2/3)+3 and pos[1] <= height-6 and pieces[2][2] == "":
                        if turn == "x":
                            pieces[2][2] = "x"
                            turn = "o"
                        else:
                            pieces[2][2] = "o"
                            turn = "x"

            if pos[0] >= width+25 and pos[0] <= width+125 and pos[1] >= 500 and pos[1] <= 550:
                pieces = [["","",""],["","",""],["","",""]]
            if pos[0] >= width+175 and pos[0] <= width+275 and pos[1] >= 500 and pos[1] <= 550:
                pg.quit()
                run = False
                break

exit()