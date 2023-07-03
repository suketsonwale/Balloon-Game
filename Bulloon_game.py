import pygame          # import pygame library to create window,keys,images,etc(whole game)
import random          # import random library to generate random numbers
pygame.init()          # initialize mobules of pygame

#create variables to set game window weidth and height
screen_weidth = 600
screen_height = 650

# create game window (display) and give name to it
game_window = pygame.display.set_mode((screen_weidth,screen_height))
pygame.display.set_caption("Bulloon Game")

background = pygame.image.load('background.png')
# load balloon images
Red_balloon = pygame.image.load('red_balloon.png')
Blue_balloon = pygame.image.load('blue_balloon.png')
Green_balloon = pygame.image.load('green_balloon.png')
Yellow_balloon = pygame.image.load('yellow_balloon.png')
Orange_balloon = pygame.image.load('orange_balloon.png')

# load bomb image
Bomb = pygame.image.load('bomb.png')
# load sword images
Sword = pygame.image.load('sword.png')

# resize the balloon inage size
image_x = 40            # weidth of image
image_y = 100            # height of image
Red_balloon = pygame.transform.scale(Red_balloon, (image_x,image_y))
Blue_balloon = pygame.transform.scale(Blue_balloon, (image_x,image_y))
Green_balloon = pygame.transform.scale(Green_balloon, (image_x,image_y))
Yellow_balloon = pygame.transform.scale(Yellow_balloon, (image_x,image_y))
Orange_balloon = pygame.transform.scale(Orange_balloon, (image_x,image_y))
Bomb = pygame.transform.scale(Bomb, (50,50))

# resize the sword inage size
Sword = pygame.transform.scale(Sword, (30,60))
background = pygame.transform.scale((background), (screen_weidth,screen_height))

# include the clock to run 30 phots pre second
clock = pygame.time.Clock()


def welcome():
    welcome = True
    font = pygame.font.SysFont(None, 25)
    main_font = pygame.font.SysFont(None, 35)
    while welcome:
        for event in pygame.event.get():                 # load the pygame events in variable event 
            if event.type == pygame.QUIT:                # quit the game if user press cross button
                welcome = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
        game_window.blit(background, (0,0))
        
        title_label = main_font.render('"The Balloons"', True, (156,29,150))
        discription_label = font.render("Discription :- ", True, (0,0,255))
        discription_label1 = font.render("The game will end if your", True, (0,0,255))
        discription_label2 = font.render("Lives reach to 0 or", True, (0,0,255))
        discription_label3 = font.render("Balloon reach to 30", True, (0,0,255))
        continue_label = font.render("Press enter to continue...", True, (0,0,0))
        game_window.blit(continue_label, (200,600))
        game_window.blit(title_label, (200,280))
        game_window.blit(discription_label, (100,340))
        game_window.blit(discription_label1, (220,340))
        game_window.blit(discription_label2, (220,360))
        game_window.blit(discription_label3, (220,380))

        pygame.display.update()


    quit()

def game_loop():
    # create a variable to keep game continue running
    run_game = True
    game_over = False

    # create variables that are going to use in game 
    mouse_possition  = []
    sword_x_poss = screen_weidth/2
    sword_y_poss = screen_height/2
    score = 0
    lives = 3
    balloon_loss = 0

    red_x_poss = random.randint(50,500)
    red_y_poss = random.randint(700,1500)

    blue_x_poss = random.randint(50,500)
    blue_y_poss = random.randint(700,1500)

    green_x_poss = random.randint(50,500)
    green_y_poss = random.randint(700,1500)

    yellow_x_poss = random.randint(50,500)
    yellow_y_poss = random.randint(700,1500)

    orange_x_poss = random.randint(50,500)
    orange_y_poss = random.randint(680,1200)

    red2_x_poss = random.randint(50,500)
    red2_y_poss = random.randint(700,1500)

    blue2_x_poss = random.randint(50,500)
    blue2_y_poss = random.randint(700,1500)

    green2_x_poss = random.randint(50,500)
    green2_y_poss = random.randint(700,1500)

    yellow2_x_poss = random.randint(50,500)
    yellow2_y_poss = random.randint(700,1500)

    orange2_x_poss = random.randint(50,500)
    orange2_y_poss = random.randint(680,1200)

    bomb_x_poss = random.randint(50,500)
    bomb_y_poss = random.randint(680,1200)

    # create a font 
    font = pygame.font.SysFont(None, 25)

    while run_game:
        if game_over:
            for event in pygame.event.get():                 # load the pygame events in variable event 
                if event.type == pygame.QUIT:                # quit the game if user press cross button
                    run_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
            game_window.fill((0,0,0))
            score_label = font.render("Score = "+str(score), True, (255,255,255))
            lives_label = font.render("Lives = "+str(lives), True, (255,255,255))
            balloon_loss_label = font.render("Balloon loss = "+str(balloon_loss), True, (255,255,255))
            dead_label = font.render("You Dead!!!", True, (255,255,255))
            replay_label = font.render("Press enter to play again...", True, (255,255,255))
            game_window.blit(score_label, (200,150))
            game_window.blit(lives_label, (200,190))
            game_window.blit(balloon_loss_label, (200,230))
            game_window.blit(dead_label, (250,450))
            game_window.blit(replay_label, (200,600))

        else:
            for event in pygame.event.get():                 # load the pygame events in variable event 
                if event.type == pygame.QUIT:                # quit the game if user press cross button
                    run_game = False
                if event.type == pygame.MOUSEMOTION:
                    mouse_possition = pygame.mouse.get_pos()
                    sword_x_poss = (mouse_possition[0] - 20)
                    sword_y_poss = (mouse_possition[1] - 40)

            
            red_y_poss -= 2
            blue_y_poss -= 2
            green_y_poss -= 2
            yellow_y_poss -= 2
            orange_y_poss -= 2
            red2_y_poss -= 2
            blue2_y_poss -= 2
            green2_y_poss -= 2
            yellow2_y_poss -= 2
            orange2_y_poss -= 2
            bomb_y_poss -=1.5

            if red_y_poss < -100:
                red_x_poss = random.randint(50,500)
                red_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if blue_y_poss < -100:
                blue_x_poss = random.randint(50,500)
                blue_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if green_y_poss < -100:
                green_x_poss = random.randint(50,500)
                green_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if yellow_y_poss < -100:
                yellow_x_poss = random.randint(50,500)
                yellow_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if orange_y_poss < -100:
                orange_x_poss = random.randint(50,500)
                orange_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if red2_y_poss < -100:
                red2_x_poss = random.randint(50,500)
                red2_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if blue2_y_poss < -100:
                blue2_x_poss = random.randint(50,500)
                blue2_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if green2_y_poss < -100:
                green2_x_poss = random.randint(50,500)
                green2_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if yellow2_y_poss < -100:
                yellow2_x_poss = random.randint(50,500)
                yellow2_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if orange2_y_poss < -100:
                orange2_x_poss = random.randint(50,500)
                orange2_y_poss = random.randint(680,1200)
                balloon_loss +=1
            if bomb_y_poss < -100:
                bomb_x_poss = random.randint(50,500)
                bomb_y_poss = random.randint(800,1000)


            if sword_x_poss > red_x_poss and sword_x_poss < red_x_poss+40 and sword_y_poss > red_y_poss and sword_y_poss < red_y_poss+40:
                red_x_poss = random.randint(50,500)
                red_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > blue_x_poss and sword_x_poss < blue_x_poss+40 and sword_y_poss > blue_y_poss and sword_y_poss < blue_y_poss+40:
                blue_x_poss = random.randint(50,500)
                blue_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > green_x_poss and sword_x_poss < green_x_poss+40 and sword_y_poss > green_y_poss and sword_y_poss < green_y_poss+40:
                green_x_poss = random.randint(50,500)
                green_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > yellow_x_poss and sword_x_poss < yellow_x_poss+40 and sword_y_poss > yellow_y_poss and sword_y_poss < yellow_y_poss+40:
                yellow_x_poss = random.randint(50,500)
                yellow_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > orange_x_poss and sword_x_poss < orange_x_poss+40 and sword_y_poss > orange_y_poss and sword_y_poss < orange_y_poss+40:
                orange_x_poss = random.randint(50,500)
                orange_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > red2_x_poss and sword_x_poss < red2_x_poss+40 and sword_y_poss > red2_y_poss and sword_y_poss < red2_y_poss+40:
                red2_x_poss = random.randint(50,500)
                red2_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > blue2_x_poss and sword_x_poss < blue2_x_poss+40 and sword_y_poss > blue2_y_poss and sword_y_poss < blue2_y_poss+40:
                blue2_x_poss = random.randint(50,500)
                blue2_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > green2_x_poss and sword_x_poss < green2_x_poss+40 and sword_y_poss > green2_y_poss and sword_y_poss < green2_y_poss+40:
                green2_x_poss = random.randint(50,500)
                green2_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > yellow2_x_poss and sword_x_poss < yellow2_x_poss+40 and sword_y_poss > yellow2_y_poss and sword_y_poss < yellow2_y_poss+40:
                yellow2_x_poss = random.randint(50,500)
                yellow2_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > orange2_x_poss and sword_x_poss < orange2_x_poss+40 and sword_y_poss > orange2_y_poss and sword_y_poss < orange2_y_poss+40:
                orange2_x_poss = random.randint(50,500)
                orange2_y_poss = random.randint(680,1200)
                score+=1
            if sword_x_poss > bomb_x_poss+10 and sword_x_poss < bomb_x_poss+40 and sword_y_poss > bomb_y_poss+10 and sword_y_poss < bomb_y_poss+40:
                bomb_x_poss = random.randint(50,500)
                bomb_y_poss = random.randint(680,1200)
                lives-=1

            if lives == 0 or balloon_loss >= 30:
                lives = 0
                game_over = True
            game_window.fill((0,0,0))                    # fill the display or game window with black color

            game_window.blit(Bomb, (bomb_x_poss,bomb_y_poss))
            game_window.blit(Red_balloon, (red_x_poss,red_y_poss))
            game_window.blit(Blue_balloon, (blue_x_poss,blue_y_poss))
            game_window.blit(Green_balloon, (green_x_poss,green_y_poss))
            game_window.blit(Yellow_balloon, (yellow_x_poss,yellow_y_poss))
            game_window.blit(Orange_balloon, (orange_x_poss,orange_y_poss))
            game_window.blit(Red_balloon, (red2_x_poss,red2_y_poss))
            game_window.blit(Blue_balloon, (blue2_x_poss,blue2_y_poss))
            game_window.blit(Green_balloon, (green2_x_poss,green2_y_poss))
            game_window.blit(Yellow_balloon, (yellow2_x_poss,yellow2_y_poss))
            game_window.blit(Orange_balloon, (orange2_x_poss,orange2_y_poss))
            
            game_window.blit(Sword, (sword_x_poss,sword_y_poss))

            score_label = font.render("Score = "+str(score), True, (255,255,255))
            lives_label = font.render("Lives = "+str(lives), True, (255,255,255))
            balloon_loss_label = font.render("Balloon loss = "+str(balloon_loss), True, (255,255,255))
            game_window.blit(score_label, (5,10))
            game_window.blit(lives_label, (500,10))
            game_window.blit(balloon_loss_label, (180,10))

        pygame.display.update()                      # update th game window
        clock.tick(80)


    pygame.quit()            # end the pygame library
    quit()                   # end the python code/program

welcome()