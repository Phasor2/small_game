import pygame as pyg
import random as rand

def main():
    '''
    Initialize pygame and pygame parameters.  Note that both player and meteors
    are square.  Thus, player_dim and met_dim are the height and width of the
    player and meteors, respectively.  Each line of code commented.
    '''
    pyg.init()                # initialize pygame

# INIT SECTION
    width = 800               # set width of game screen in pixels
    height = 600              # set height of game screen in pixels

    red = (255,0,0)           # rgb color of player
    yellow = (244,208,63)     # rgb color of meteors
    background = (0,0,156)    # rgb color of sky (midnight blue)

    player_dim = 50           # player size in pixels
    player_pos = [width/2, height-2*player_dim]  # initial location of player
                                                 # at bottom middle; height
                                                 # never changes

    met_dim = 20              # meteor size in pixels

    speed = 0                  #initialize speed

    # Initialize meteors list
    met_list = [[100,100]]


    screen = pyg.display.set_mode((width, height)) # initialize game screen

    game_over = False         # initialize game_over; game played until
                              # game_over is True

    score = 0                 # initialize score
    clock = pyg.time.Clock()  # initialize clock to track time
    my_font = pyg.font.SysFont("monospace", 35) # initialize system font


# CONTROL SECTION
    while not game_over:                       # play until game_over True



        screen.fill(background)                # refresh screen bg color blue in this case

        # FUNCTION SECTION
        drop_meteors(met_list, met_dim, width) # self-explanatory; read prompt

        # Print speed when speed is incremented
        temp_speed = speed
        speed = set_speed(score)               # increase by score
        if speed != temp_speed:
            print('speed:'+str(speed))
            if speed == 20:
                print('It gets a little crazy here')


        # update_meteor_position taking speed, score, met position, height return score

        score = update_meteor_positions(met_list, height, score, speed)


        # score text
        text = "Score: " + str(score)              # create score text
        label = my_font.render(text, 1, yellow)    # render text into label

        # display score
        screen.blit(label, (width-250, height-40)) # blit label to screen at
                                                   # given position; for our 
                                                   # purposes, just think of
                                                   # blit to mean draw


        draw_meteors(met_list, met_dim, screen, yellow)

        player_pos = draw_player(screen,red,player_pos,player_dim)

        #print(player_pos)
        #print(met_list)
        game_over=collision_check(met_list, player_pos, player_dim, met_dim)

    
        clock.tick(30)                             # set frame rate to control
                                                   # frames per second (~30); 
                                                   # slows down game

        pyg.display.update()                       # update screen characters
    print('Final score:', score)                   # final score
    pyg.quit()                                     # leave pygame

def set_speed(score):
    if score <= 25:
        speed = 5
    else:
        speed = score // 5
    return speed

def draw_player(screen,red,player_pos,player_dim):
    x = player_pos[0]  # assign current x position
    y = player_pos[1]  # assign curren y position
    for event in pyg.event.get():  # loop through events in queue
        if event.type == pyg.KEYDOWN:  # checks for key press

            if event.key == pyg.K_LEFT:  # checks if left arrow;
                x -= 20  # if true, moves player left
                if x < 0:           #edge left
                    x = 0
            elif event.key == pyg.K_RIGHT:  # checks if right arrow;
                x += 20  # else moves player right
                if x>750:           #edge right
                    x=750
        player_pos = [x, y]  # reset player position3
    pyg.draw.rect(screen, red, (player_pos[0], player_pos[1], player_dim, player_dim))  # draw player
    return player_pos


def draw_meteors(met_list, met_dim, screen, color):
    for x in range(len(met_list)):                  # for every meteor update position


        # Rect(left, top, width, height)
        pyg.draw.rect(screen, color, (met_list[x][0], met_list[x][1], met_dim, met_dim))

def drop_meteors(met_list, met_size, screenWidth):
    temp = rand.randint(0, 10)
    if temp == 1:                                   # if random time when ==1 drop meteor
        randX = rand.randint(0, screenWidth)        # generate random position for meteor

        # avoid generate random position overlap the current meteor list
        if randX not in met_list or randX + met_size not in met_list or randX - met_size not in met_list:
            met_list.append([randX, 0])                 # get in the meteor list if it satisfy no overlap


def update_meteor_positions(met_list, height, score, speed):
    for i in range(len(met_list)):
        if score < 25:
            met_list[i][1] += 5
        else:
            met_list[i][1] += speed

        if (met_list[i][1] >= height):
                score += 1                  #add score 1
                del met_list[i]             # remove element from the list
                break
    if score == 10:
        print('')
    return score

def collision_check(met_list,player_pos, player_dim, met_dim):          # just a function call detect_collision
    return detect_collision(met_list,player_pos, player_dim, met_dim)


            #randX = detect_collision(player_pos, i, player_dim, met_dim)

def detect_collision(met_list,player_pos, player_dim, met_dim):
    for i in met_list:
        x = i[0]  # assign current x position
        y = i[1]  # assign curren y position
        # hit y area from 475 to 550
        if y >=475 and y<=550:

            # Assume x axis of met_pos = 400
            # then check hit x area of player pos from 350 to 420
            if x<=player_pos[0]+50 and x>=player_pos[0]-20:
                  print('Game Over, buddy !')
                  return True
            else:
                  return False
main()
