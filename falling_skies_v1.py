import curses
import random
import math
import time


################################ INITIALIZING THE SCREEN #######################

stdscr = curses.initscr() ###### initialize curses window
curses.noecho()
curses.cbreak() ################ app reacts to keys immediately without pressing enter
curses.curs_set(0) ############# set the cursor state. Can be set to 0,1,or2,for invisible,normal,or very visible
curses.update_lines_cols()

############################### COLORS #####################################

if curses.has_colors():
    curses.start_color()

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)

################################ VARIABLES ####################################

max_y,max_x = stdscr.getmaxyx()

string_list = "abcdefghijklmnopqrstuvwxyz"
chosen_one = string_list[random.randint(1, 25)]

x_fall = random.randint(12,max_x-10)
y_fall = 5

rain = "☢ " * (max_x-1)
earth = "⏏_" * (max_x-1)

life = 3
score = 0
difficulty = 0.4
new_level = 10
level = 1


############################## INTRO #########################################
def intro():
    intro_line1 = "POLLUTION AND WARS HAVE DESTROYED OUR PLANET."
    intro_line2 = "THE LAST REMAINING MEMBERS OF HUMANITY"
    intro_line3 = "HAVE TO FACE DEADLY ACID RAINS"
    intro_line4 = "FALLING FROM THE POISONOUS SKY."
    intro_line5 = "HELP PEOPLE ESCAPE FROM THE RAIN BY"
    intro_line6 = "PRESSING THE SAME LETTER THAT YOU SEE IN THE RAINDROPS!"
    intro_line7 = "Press 'S' to start"
    intro_line8 = "Press 'Q' to exit the game"

    stdscr.addstr(6, int(max_x/7), intro_line1, curses.color_pair(2))
    stdscr.addstr(7, int(max_x/7), intro_line2, curses.color_pair(2))
    stdscr.addstr(8, int(max_x/7), intro_line3, curses.color_pair(2))
    stdscr.addstr(9, int(max_x/7), intro_line4, curses.color_pair(2))
    stdscr.addstr(10,int(max_x/7), intro_line5, curses.color_pair(2))
    stdscr.addstr(11, int(max_x/7), intro_line6, curses.color_pair(2))
    stdscr.addstr(14, int(max_x/7), intro_line7)
    stdscr.addstr(15, int(max_x/7), intro_line8)
    stdscr.chgat(14, (int(max_x/7)+6), 1, curses.color_pair(2))
    stdscr.chgat(14, (int(max_x/7)+7), 1, curses.color_pair(2))
    stdscr.chgat(14, (int(max_x/7)+8), 1, curses.color_pair(2))
    stdscr.chgat(15, (int(max_x/7)+6), 1, curses.color_pair(1))
    stdscr.chgat(15, (int(max_x/7)+7), 1, curses.color_pair(1))
    stdscr.chgat(15, (int(max_x/7)+8), 1, curses.color_pair(1))

    s_or_q = stdscr.getkey()

    if s_or_q == "s":
        stdscr.erase()
        stdscr.refresh()
        stdscr.nodelay(1)
    elif s_or_q == "q":
        curses.endwin()
        quit()


############################# ENVIRONMENT #####################################

def environment():
#Score, life, level
    stdscr.addstr(1, 1, 'SCORE: ✎ %s' %(score), curses.color_pair(3))
    stdscr.addstr(1, int(max_x/2),'LIFE: ♥ %s' %(life), curses.color_pair(3))
    stdscr.addstr(1, int(max_x/4),'LEVEL: ⚔ %s' %(level), curses.color_pair(3))
#Sky, ground
    stdscr.addstr(3, 1, rain, curses.color_pair(4))
    stdscr.addstr(max_y - 3, 1, earth, curses.color_pair(2))

    stdscr.border(0)


########################### FALLING LETTERS ####################################

def fall():
    global y_fall
    stdscr.addstr(y_fall,x_fall,str("☣ " + chosen_one.upper()) + "☣")
    y_fall += 1
    stdscr.refresh()


## SCREEN UPDATE AND TIMEOUT TO LET FUNCTIONS KEEP RUNNING WHILE WAITING TO KEYSTROKE ##

def main():
    running = True
    while running:
        global score
        global life
        global difficulty
        global chosen_one
        global rain
        global earth
        global y_fall
        global x_fall
        global new_level
        global level
        stdscr.nodelay(1)
        environment()
        fall()
        time.sleep(difficulty)
        key = stdscr.getch()
#        clear()
### if keystroke is correct resets the falling letter and updates the score ###
        if key == ord(chosen_one):
             y_fall= 5
             x_fall = random.randint(12,max_x-10)
             chosen_one = string_list[random.randint(0,25)]
             stdscr.erase()
             score += 1
#### level up and difficulty behaviour #######################################
        if score == new_level:
            new_level += 10
            difficulty -= 0.025
            level += 1
        if score == new_level and score > 90:
            new_level += 15
            difficulty -= 0.005
            level += 1
###### if a drop hits the ground life decreases and resets the falling letter ##
        if y_fall == max_y -3 :
            y_fall = 5
            x_fall = random.randint(12,max_x-10)
            chosen_one = string_list[random.randint(0,25)]
            stdscr.erase()
            life -= 1
###### if you die you can choose to quit or restart ###########################
        if life == 0:
            running = False
    while True:
        environment()
        stdscr.addstr(int(max_y/2)-5,int(max_x/2-13), "YOUR FINAL SCORE IS : %s" %(score), curses.color_pair(4))
        stdscr.addstr(int(max_y/2),int(max_x/2-10),"PRESS 'Q' TO QUIT",  curses.color_pair(1))
        stdscr.addstr(int(max_y/2)+5,int(max_x/2-12),"PRESS 'R' TO RESTART", curses.color_pair(2) )
        key = stdscr.getch()
        stdscr.timeout(-1)
        if key == ord("q"):
            break
        if key == ord("r"):
            y_fall= 5
            x_fall = random.randint(12,max_x-10)
            chosen_one = string_list[random.randint(0,25)]
            stdscr.erase()
            life = 3
            score = 0
            difficulty = 0.4
            main()
    curses.endwin()
intro()
main()
