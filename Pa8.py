import pygame as pyg
import random as rand

def main():
    '''
    Initialize pygame and pygame parameters.  Note that both player and meteors
    are square.  Thus, player_dim and met_dim are the height and width of the
    player and meteors, respectively.  Each line of code commented.
    '''
    pyg.init()                # initialize pygame

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
    met_list = [[100,100]]             # initialize list of two-element lists
                              # giving meteor positions

    screen = pyg.display.set_mode((width, height)) # initialize game screen

    game_over = False         # initialize game_over; game played until
                              # game_over is True

    score = 0                 # initialize score

    clock = pyg.time.Clock()  # initialize clock to track time

    my_font = pyg.font.SysFont("monospace", 35) # initialize system font

    while not game_over:                       # play until game_over True
        for event in pyg.event.get():          # loop through events in queue
            if event.type == pyg.KEYDOWN:      # checks for key press
                x = player_pos[0]              # assign current x position
                y = player_pos[1]              # assign curren y position
                if event.key == pyg.K_LEFT:    # checks if left arrow;
                    x -= player_dim            # if true, moves player left
                elif event.key == pyg.K_RIGHT: # checks if right arrow;
                    x += player_dim            # else moves player right
                player_pos = [x, y]            # reset player position
            
        screen.fill(background)                # refresh screen bg color
        drop_meteors(met_list, met_dim, width) # self-explanatory; read prompt
        speed = set_speed(score)               # self-explanatory; read prompt
        score = update_meteor_positions(met_list, height, score, speed)
                                               # read prompt
        text = "Score: " + str(score)              # create score text
        label = my_font.render(text, 1, yellow)    # render text into label
        screen.blit(label, (width-250, height-40)) # blit label to screen at
                                                   # given position; for our 
                                                   # purposes, just think of
                                                   # blit to mean draw
        draw_meteors(met_list, met_dim, screen, yellow) # self-explanatory;
                                                        # read prompt

        pyg.draw.rect(screen, red, (player_pos[0], player_pos[1], player_dim, player_dim))                                        # draw player

        if collision_check(met_list, player_pos, player_dim, met_dim):
            game_over = True                       # read prompt
    
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

def draw_meteors(met_list, met_dim, screen, color):
    for x in range(len(met_list)):
        pyg.draw.rect(screen, color, (met_list[x][0], met_list[x][1], met_dim, met_dim))

def drop_meteors(met_list, met_size, screenWidth):
    if rand.randint(0, 10) == 1:
        randX = rand.randint(0, screenWidth)
        if randX not in met_list or randX + met_size not in met_list or randX - met_size not in met_list:
            met_list.append([randX, 0])
    print(met_list)

def update_meteor_positions(met_list, height, score, speed):
    for i in range(len(met_list)):
        met_list[i][1] += 5 
        if (met_list[i][1] == height):
                score += 1
    

    return score
def collision_check(met_list,player_pos, player_dim, met_dim):
    for i in met_list:
        randX = detect_collision(player_pos, i, player_dim, met_dim)
        if randX == True:
            return True
        else:
            return False

def detect_collision(player_pos, met_list, player_dim, met_dim):
    player_touch = pyg.rect(player_pos[0], player_pos[1], player_dim,player_dim)
    meteor_touch = pyg.rect(met_list[0], mis_list[1], met_dim, met_dim)
    if player_touch.collision_check(meteor_rec) == True:
        return True
    else:
        return False
main()
