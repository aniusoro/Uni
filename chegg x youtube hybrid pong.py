# Pong Game from Atari (Python code)



import pygame





# User-defined functions



def main():

    # initialize all pygame modules (some need initialization)

    pygame.init()

    # create a pygame display window

    pygame.display.set_mode((500, 400))

    # set the title of the display window

    pygame.display.set_caption('Pong')

    # get the display surface

    w_surface = pygame.display.get_surface()

    # create a game object

    game = Game(w_surface)

    # start the main game loop by calling the play method on the game object

    game.play()

    # quit pygame and clean up the pygame window

    pygame.quit()



# User-defined classes        

class Game:

    # An object in this class represents a complete game.

    

    def __init__(self, surface):

        # Initialize a Game.

        # - self is the Game to initialize

        # - surface is the display window surface object

        

        # Colour for the game surface

        self.surface = surface

        self.bg_color = pygame.Color('black') #bg = background color

        self.fg_color = pygame.Color('dark blue')

        

        self.FPS = 60

        self.game_Clock = pygame.time.Clock()

        self.close_clicked = False

        self.continue_game = True

        

        # sets the scores for the left and right paddles

        self.left_score = 0

        self.right_score = 0

       

        # computes the centre of the window

        y_window = int(self.surface.get_height()/2)

        

        self.l_paddle = y_window - 20

        self.r_paddle = y_window - 20

        

        # sets the paddles velocity

        self.l_paddle_v = 0

        self.r_paddle_v = 0

        

        # === game specific objects

        self.left_paddle = Paddle('green', pygame.Rect(100, self.l_paddle, 10, 40), 5, self.surface)

        self.right_paddle = Paddle('green', pygame.Rect(self.surface.get_width() - 100, self.r_paddle,10, 40), 5, self.surface)

        self.ball = Ball('white', 5, [int(self.surface.get_width()/2) - 3,y_window - 3], [6, 2], self.surface) 

        self.max_frames = 150

        self.frame_counter = 0



    def play(self):

        # Play the game until the player presses the close box.

        # - self is the Game that should be continued or not.

        

        while not self.close_clicked:  # until player clicks close box

            self.handle_events()

            self.draw()

            if self.continue_game:

                self.update()

                self.decide_continue()

            self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second

    

    def handle_events(self):

        # Handle each user event by changing the game state appropriately.

        # - self is the Game whose events will be handled

        

        events = pygame.event.get()

        for event in events:

            if event.type == pygame.QUIT:

                self.close_clicked = True

            elif event.type == pygame.KEYDOWN:

                # modifies left paddle velocity when Q/A is pressed

                if event.key == pygame.K_q:

                    self.l_paddle_v = 5

                    

                elif event.key == pygame.K_a:

                    self.l_paddle_v = -5

                # modifies right paddle velocity when P/L is pressed

                if event.key == pygame.K_p:

                    self.r_paddle_v = 5

                elif event.key == pygame.K_l:

                    self.r_paddle_v = -5

            elif event.type == pygame.KEYUP:

                # modifies both paddles velocity when key released

                if event.key == pygame.K_q or event.key == pygame.K_a:

                    self.l_paddle_v = 0

                if event.key == pygame.K_p or event.key == pygame.K_l:

                    self.r_paddle_v = 0    



    def draw(self): 

        # Draw all game objects.

        # - self is the Game to draw

        

        self.surface.fill(self.bg_color) # clear the display surface first

        self.ball.draw()

        self.left_paddle.draw()

        self.right_paddle.draw()

        self.score('right')

        self.score('left')

        pygame.display.update() # make the updated surface appear on the display

        

        

    def update(self):

        # Update the game objects.

        # - self is the Game to update

        

        # code for how the both paddles would react to input and move

        if self.l_paddle - self.l_paddle_v < 0:

            #when it hits the top left side in the Game

            self.l_paddle = 0 

            #stop the paddle at the top left side once it hits it

        elif self.l_paddle + 40 - self.l_paddle_v > self.surface.get_height(): 

            self.l_paddle = self.surface.get_height() - 40 

        else: 

            #if doesnt touch any of the edges let it be able to move

            self.l_paddle -= self.l_paddle_v 

            #equivalent to self.l_paddle= self.l_paddle - self.l_paddle_v (a -= b a = a-b)

        if self.r_paddle - self.r_paddle_v < 0:

            self.r_paddle = 0

        elif self.r_paddle + 40 - self.r_paddle_v > self.surface.get_height():

            self.r_paddle = self.surface.get_height() - 40

        else:

            self.r_paddle -= self.r_paddle_v

        

        # code for updating for left and right paddles

        self.left_paddle = Paddle('green', pygame.Rect(100, self.l_paddle, 10, 40), 5, self.surface)

        self.right_paddle = Paddle('green', pygame.Rect(self.surface.get_width() - 100, self.r_paddle,10, 40), 5, self.surface)

        

        # score_change = this is when the ball hits the wall of either of their walls, the opponent scores change when it happens.

        score_change = self.ball.move(self.l_paddle, self.r_paddle) #this should b efrom the ball class

        if score_change == 'right':

            self.left_score += 1

        elif score_change == 'left':

            self.right_score += 1

        # I don't know what this does

        self.frame_counter = self.frame_counter + 1  

      

    def decide_continue(self):

        # Check and remember if the game should continue

        # - self is the Game to check

        # Code to stop the game when either of them gets a score of 11

        if self.right_score == 11 or self.left_score == 11:

            self.continue_game = False

    

    

    def score(self, side):

        # sets text score

        # - self is Game

    

        font = pygame.font.SysFont('', 75)

        if side == 'left':

            coordinate = (5, 0)

            text_box = font.render(str(self.left_score), True, self.fg_color,self.bg_color) 

        else:

            text_box = font.render(str(self.right_score), True, self.fg_color,self.bg_color) #dont need the white

            text_rect = text_box.get_rect() # get rect from textbox

            text_rect.right = self.surface.get_width()

            coordinate = text_rect

        # prints to surface

        self.surface.blit(text_box, coordinate)

        



class Ball:

    # An object in this class represents the objects in the game

    def __init__(self, ball_color, ball_radius, ball_center, ball_velocity, surface):

        # Initialize a Ball.

        # - self is the Ball to initialize

        # - color is the pygame.Color of the ball

        # - center is a list containing the x and y int

        # - coordinates of the center of the ball

        # - radius is the int pixel radius of the ball

        # - velocity is a list containing the x and y components

        # - surface is the window's pygame. Surface object

        

        self.color = pygame.Color(ball_color)

        self.radius = ball_radius

        self.center = ball_center

        self.velocity = ball_velocity 

        self.surface = surface

        print(self.surface.get_width())

        print(self.center)

        print(self.velocity)  

        

        

    def move(self, l_paddle, r_paddle):

        # Change the location of the Ball by adding the corresponding

        # speed values to the x and y coordinate of its center

        # - self is the Ball

        # - l_paddle is the top position of left paddle

        # - r_paddle is the top position of right paddle

        

        score_change = 'pass'

        for i in range(0,2):

            if i == 0: 

                if self.surface.get_width() < self.center[i] + 2 + self.velocity[i] or 0 > self.center[i] - 2 + self.velocity[i]:

                    self.velocity[i] = -self.velocity[i]

                    if self.velocity[i] > 0:

                        score_change = 'left'

                    else:

                        score_change = 'right'

                elif (105 <= self.center[i] - 2 + self.velocity[i] <= 111 and self.velocity[i] < 0 and l_paddle - 20 <= self.center[i+1] + self.velocity[i+1] <= l_paddle + 43):

                    self.velocity[i] = -self.velocity[i]

                    print(self.velocity[i])

                elif (self.surface.get_width() - 101 <= self.center[i] - 2 + self.velocity[i] <= self.surface.get_width() - 95 and self.velocity[i] > 0 and r_paddle -3 <= self.center[i+1] + self.velocity[i+1] <= r_paddle + 43):

                    self.velocity[i] = -self.velocity[i]

                    print(self.velocity[i])

            else:

                if self.surface.get_height() < self.center[i] + 2 + self.velocity[i] or 0 > self.center[i] - 2 + self.velocity[i]:

                    self.velocity[i] = -self.velocity[i]

            self.center[i] = (self.center[i] + self.velocity[i])

        return score_change 

    

    def draw(self):

        # Draw the ball on the surface

        # - self is the Ball

        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

        

class Paddle:

    # An object in this class represents the objects in the game

    def __init__(self, paddle_color, paddle_object, paddle_velocity, surface):

        # Initialize a paddle.

        # - self is the paddle to initialize

        # - color is the pygame.Color of the paddle

        # - object of the paddle as a Rect

        # - velocity is a list containing the x and y components

        # - surface is the window's pygame. Surface object

        

        self.color = pygame.Color(paddle_color)

        self.center = paddle_object

        self.velocity = paddle_velocity

        self.surface = surface

    

    def draw(self):

        # Draw the paddle on the surface

        # - self is the Paddle

        pygame.draw.rect(self.surface, self.color, self.center)



main()



''' 

Sources used in this mini Project (Pong Game)

Original Atari PONG (1972) arcade machine gameplay video = https://youtu.be/fiShX2pTz9A?t=2

PongDemo = https://youtu.be/dC72qPyDV9Q?t=58

Pre=poke Framework = https://drive.google.com/file/d/1rbhJWZ91FkD1tuvYr1kjyJIK_SxdrXUv/view (Access to only CMPUT 174 Students)

Pygame Rect Documentation = https://www.pygame.org/docs/ref/rect.html

Python and Pygame Documentation (https://docs.python.org/3/) (https://www.pygame.org/docs/) respectively

https://www.geeksforgeeks.org/create-pong-game-using-python-turtle/

https://www.geeksforgeeks.org/adding-boundary-to-an-object-in-pygame/

https://www.geeksforgeeks.org/create-a-simple-two-player-game-using-turtle-in-python/

https://youtu.be/C6jJg9Zan7w

https://youtu.be/gJnUTX00Z9k

https://www.youtube.com/watch?v=-btAvvPCpUA

'''

