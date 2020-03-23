import random				#to generate random values
import curses 				#The curses library supplies a terminal-independent screen-painting and keyboard-handling facility for text-based terminals

s = curses.initscr()		#intialize a screen to play the game
curses.start_color()
curses.curs_set(0)			#set a start position for the snake
'''
getmaxx() function which returns the maximum X,Y coordinates for current graphics mode and driver.
'''
sh, sw = s.getmaxyx()		#Return the value of maxY(Height) and maxX(Width)

'''
 The newwin() function creates a new window of a given size,
 returning the new window object. 
 Note that the coordinate system used in curses is unusual. 
 Coordinates are always passed in the order y,x, 
 and the top-left corner of a window is coordinate (0,0).

'''
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)			#if you didn't press anykey timeout to close the window
x= 0
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
w.addstr(5,55, "Start!  ",curses.COLOR_WHITE)

'''
The starting position of the snake 
snk_x the X-coordinate position 
snk_y the Y-coordinate position 
'''
snk_x = sw/4					
snk_y = sh/2

'''
snake dimensions declartion
'''
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]
'''
food dimensions declartion
food[0]-> width
food[1]-> height
int() to change from str to integer 

The addch()function place ch(character) into the current or specified window
at the current or specified position, and then advance the window's cursor position.
'''
food = [sh/2, sw/2]
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)		#to show the food in form of Pi character

key = curses.KEY_RIGHT		#to set the key value to the right arrow key pressed

'''comment #1
   getch() is a way to get a user inputted character.
   It can be used to hold program execution, 
   but the "holding" is simply a side-effect of its primary purpose,
   which is to wait until the user enters a character.
   getch() and getchar() are used to read a character from screen.
	
  ''comment #2
   if you clicked any key of arrows so it will move according to it, if not it will wait until you press anykey

  ''comment #3
   Checks if the snake touches any the window edges.

  ''comment #4
   Define the head of the snake, so every time you eat the food it will be incremanted 
   if condition for the motion of the snake and the spacing between the heads

  ''comment #5
   if the head of the snake touches the food, "Food = None" to remove it as it already eaten, then
   Generate a new food in a random postion inside the screen away from the edges.
	
  ''comment #6
	to make sure that the random position of food is not touching the snake, if touching then generate another food 
	in another position, to avoid confusing.

  ''comment #7
    pop() is an inbuilt function in Python that removes and returns last value
    from the list or the given index value. 
    Parameter : index (optional) - The value at index is popped out and removed.
    If the index is not given, then the last element is popped out and removed.
    --which means that the snake will remain as it is no change will accur to its size so adding a " " to the tail

'''

while True:
    next_key = w.getch()															#comment 1
    key = key if next_key == -1 else next_key										#comment 2

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
    	print("GAME OVER !")
    	w.clear()
    	quit()

    new_head = [snake[0][0], snake[0][1]]											#comment 4

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:														   #comment 5
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),										   
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None								   #comment 6
            x=x+1			#add score by one each time you eat the food
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
            w.addstr(5,55, "         ",curses.COLOR_WHITE)
            w.addstr(0,0, "Score: "+str(x), curses.color_pair(1))
            w.refresh()
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()														   #comment 7
        w.addch(int(tail[0]), int(tail[1]), ' ')
    w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
    #to show the snake in form of "haze" character 

    #https://docs.python.org/3/howto/curses.html
