import curses
import random
import math
import time


# INITIALIZING THE SCREEN #####################################################

stdscr = curses.initscr()  # initialize curses window
curses.noecho()
curses.cbreak()  # app reacts to keys immediately without pressing enter
# set the cursor state. Can be set to 0,1,or2,for invisible,normal,or very
# visible
curses.curs_set(0)
curses.update_lines_cols()

# COLORS ######################################################################

if curses.has_colors():
    curses.start_color()

curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)

# VARIABLES ###################################################################

max_y, max_x = stdscr.getmaxyx()

string_list = "abcdefghijklmnopqrstuvwxyz"
chosen_one = string_list[random.randint(1, 25)]
possible_letters = [ord(i) for i in string_list]

x_fall = random.randint(12, max_x - 10)
y_fall = 5

rain = "☢ " * (max_x - 1)
earth = "⏏_" * (max_x - 1)

life = 3
score = 0
difficulty = 0.4
new_level = 10
level = 1
new_life = 5


# INTRO #######################################################################

# prints the intro line by line with associated colore scheme #################
def printer(intro_line):
    y = 6
    x = int(max_x / 7)
    for i in range(0, len(intro_line)):
        if i >= 6:
            stdscr.addstr(y, x, intro_line[i])
            stdscr.refresh()
            time.sleep(2)
            y += 1
        else:
            stdscr.addstr(y, x, intro_line[i], curses.color_pair(2))
            stdscr.refresh()
            time.sleep(2)
            y += 1
    while True:
        s_or_q = stdscr.getkey()

        if s_or_q == "s":
            stdscr.erase()
            stdscr.refresh()
            stdscr.nodelay(1)
            break
        elif s_or_q == "q":
            curses.endwin()
            quit()


def intro():
    intro_line = ["POLLUTION AND WARS HAVE DESTROYED OUR PLANET.",
                  "THE LAST REMAINING MEMBERS OF HUMANITY",
                  "HAVE TO FACE DEADLY ACID RAINS",
                  "FALLING FROM THE POISONOUS SKY.",
                  "HELP PEOPLE ESCAPE FROM THE RAIN BY",
                  "PRESSING THE SAME LETTER THAT YOU SEE IN THE RAINDROPS!",
                  "Press 'S' to start",
                  "Press 'Q' to exit the game"]

    printer(intro_line)


# ENVIRONMENT #################################################################

def environment():
    # Score, life, level
    stdscr.addstr(1, 1, 'SCORE: ✎ %s' % (score), curses.color_pair(3))
    stdscr.addstr(1, 20, 'LIFE: ♥ %s' % (life), curses.color_pair(3))
    stdscr.addstr(1, 40, 'LEVEL: ⚔ %s' % (level), curses.color_pair(3))
    stdscr.addstr(1, 60, "Press 'Esc' to exit", curses.color_pair(3))
# Sky, ground
    stdscr.addstr(3, 1, rain, curses.color_pair(4))
    stdscr.addstr(max_y - 3, 1, earth, curses.color_pair(2))

    stdscr.border(0)


# FALLING LETTERS #############################################################

def fall():
    global y_fall
    stdscr.addstr(y_fall, x_fall, str("☣ " + chosen_one.upper()) + "☣")
    y_fall += 1
    stdscr.refresh()


# SCREEN UPDATE AND TIMEOUT TO LET FUNCTIONS KEEP RUNNING WHILE WAITING TO
# KEYSTROKE ##

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
        global new_life
        stdscr.nodelay(1)
        environment()
        fall()
        time.sleep(difficulty)
        key = stdscr.getch()
        # stdscr.erase()


# if keystroke is correct resets the falling letter and updates the score
# if keystroke is not correct, score decreases by 1 and
# in case of negative score player loses 1 life

        if key in possible_letters:
            if key == ord(chosen_one):
                y_fall = 5
                x_fall = random.randint(12, max_x - 10)
                chosen_one = string_list[random.randint(0, 25)]
                stdscr.erase()
                score += 1
            else:
                score -= 1
                if score < 0:
                    life -= 1


# press ESC to end the game ###################################################

        if key == ord('\x1b'):
            break

# level up and difficulty behaviour ###########################################
        if score == new_level:
            new_level += 10
            difficulty -= 0.025
            level += 1
        if score == new_level and score > 90:
            new_level += 15
            difficulty -= 0.005
            level += 1
# if a drop hits the ground resets the falling letter ##
        if y_fall == max_y - 3:
            y_fall = 5
            x_fall = random.randint(12, max_x - 10)
            chosen_one = string_list[random.randint(0, 25)]
            stdscr.erase()
            life -= 1

# life increases by one in every 5 level

        if level == new_life:
            new_life += 5
            life += 1

# if you die you can choose to quit or restart ################################
        if life == 0:
            running = False
    while True:
        environment()
        stdscr.addstr(int(max_y / 2) - 5, int(max_x / 2 - 13),
                      "YOUR FINAL SCORE IS : %s"
                      % (score), curses.color_pair(4))
        stdscr.addstr(int(max_y / 2), int(max_x / 2 - 10),
                      "PRESS 'Q' TO QUIT",  curses.color_pair(1))
        stdscr.addstr(int(max_y / 2) + 5, int(max_x / 2 - 12),
                      "PRESS 'R' TO RESTART", curses.color_pair(2))
        key = stdscr.getch()
        # stdscr.timeout(-1)
        if key == ord("q"):
            break
        if key == ord("r"):
            y_fall = 5
            x_fall = random.randint(12, max_x - 10)
            chosen_one = string_list[random.randint(0, 25)]
            stdscr.erase()
            life = 3
            score = 0
            difficulty = 0.4
            main()
    curses.endwin()
intro()
main()
