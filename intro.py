import curses
import random
import math
import time


################################ INITIALIZING THE SCREEN #######################

stdscr = curses.initscr() ###### initializing curses window
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

letters = "abcdefghijklmnopqrstuvwxyz"
falling_letter = letters[random.randint(1, 25)]

x_fall = random.randint(12,max_x-10)
y_fall = 3

rain = "☢ " * (max_x-1)
earth = "⏏_" * (max_x-1)

life = 3
score = 0
difficulty = 0.4
new_level = 10
level = 1

############################# ENVIRONMENT #####################################

def environment():
#Score, life, level
    stdscr.addstr(1, 1, 'SCORE: ✎ %s' %(score), curses.color_pair(3))
    stdscr.addstr(1, int(max_x/2),'LIFE: ♥ %s' %(life), curses.color_pair(3))
    stdscr.addstr(1, int(max_x/4),'LEVEL: ⚔ %s' %(level), curses.color_pair(3))
#Sky, ground
    stdscr.addstr(4, 1, rain, curses.color_pair(4))
    stdscr.addstr(max_y - 3, 1, earth, curses.color_pair(2))

    stdscr.border(0)

############################## IT'S RAINING ##################################

def fall():
    global y_fall
    stdscr.addstr(y_fall,x_fall,str("☣ " + chosen_one.upper()) + "☣", curses.color_pair(4))
    y_fall += 1
    stdscr.refresh()

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
        environment()
    elif s_or_q == "q":
        exit()


intro()



##### Environment:
# stdscr.addstr(1, 1, 'SCORE: ✎ %s' %(score), curses.color_pair(3))
# stdscr.addstr(1, 20,'LIFE: ♥ %s' %(life), curses.color_pair(3))
# stdscr.addstr(1, 40,'LEVEL: ⚔ %s' %(level), curses.color_pair(3))
# stdscr.addstr(1, 60, "Press 'Esc' to exit", curses.color_pair(3))




curses.echo() #usually apps turn off automatic echoing of keys. But .echo turns it back on
stdscr.getch()
curses.endwin()
