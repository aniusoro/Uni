
1  # Pre-Poke Framework
2  # Implements a general game template for games with animation
3  # You must use this template for all your graphical lab assignments
4  # and you are only allowed to inlclude additional modules that are part of
5  # the Python Standard Library; no other modules are allowed
6  
7  import pygame
8  
9  
10 # User-defined functions
11 
12 def main():
13    # initialize all pygame modules (some need initialization)
14    pygame.init()
15    # create a pygame display window
16    pygame.display.set_mode((500, 400))
17    # set the title of the display window
18    pygame.display.set_caption('A template for graphical games with two moving dots')   
19    # get the display surface
20    w_surface = pygame.display.get_surface() 
21    # create a game object
22    game = Game(w_surface)
23    # start the main game loop by calling the play method on the game object
24    game.play() 
25    # quit pygame and clean up the pygame window
26    pygame.quit() 
27 
28 
29 # User-defined classes
30 
31 class Game:
32    # An object in this class represents a complete game.
33 
34    def __init__(self, surface):
35       # Initialize a Game.
36       # - self is the Game to initialize
37       # - surface is the display window surface object
38 
39       # === objects that are part of every game that we will discuss
40       self.surface = surface
41       self.bg_color = pygame.Color('black')
42       
43       self.FPS = 60
44       self.game_Clock = pygame.time.Clock()
45       self.close_clicked = False
46       self.continue_game = True
47       
48       # === game specific objects
49       self.small_dot = Dot('red', 30, [50, 50], [1, 2], self.surface)
50       self.big_dot = Dot('blue', 40, [200, 100], [2, 1], self.surface)
51       self.max_frames = 150
52       self.frame_counter = 0
53 
54    def play(self):
55       # Play the game until the player presses the close box.
56       # - self is the Game that should be continued or not.
57 
58       while not self.close_clicked:  # until player clicks close box
59          # play frame
60          self.handle_events()
61          self.draw()            
62          if self.continue_game:
63             self.update()
64             self.decide_continue()
65          self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 
66 
67    def handle_events(self):
68       # Handle each user event by changing the game state appropriately.
69       # - self is the Game whose events will be handled
70 
71       events = pygame.event.get()
72       for event in events:
73          if event.type == pygame.QUIT:
74             self.close_clicked = True
75 
76    def draw(self):
77       # Draw all game objects.
78       # - self is the Game to draw
79       
80       self.surface.fill(self.bg_color) # clear the display surface first
81       self.small_dot.draw()
82       self.big_dot.draw()
83       pygame.display.update() # make the updated surface appear on the display
84 
85    def update(self):
86       # Update the game objects for the next frame.
87       # - self is the Game to update
88       
89       self.small_dot.move()
90       self.big_dot.move()
91       self.frame_counter = self.frame_counter + 1
92 
93    def decide_continue(self):
94       # Check and remember if the game should continue
95       # - self is the Game to check
96       
97       if self.frame_counter > self.max_frames:
98          self.continue_game = False
99 
100
101class Dot:
102   # An object in this class represents a Dot that moves 
103   
104   def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
105      # Initialize a Dot.
106      # - self is the Dot to initialize
107      # - color is the pygame.Color of the dot
108      # - center is a list containing the x and y int
109      #   coords of the center of the dot
110      # - radius is the int pixel radius of the dot
111      # - velocity is a list containing the x and y components
112      # - surface is the window's pygame.Surface object
113
114      self.color = pygame.Color(dot_color)
115      self.radius = dot_radius
116      self.center = dot_center
117      self.velocity = dot_velocity
118      self.surface = surface
119      
120   def move(self):
121      # Change the location of the Dot by adding the corresponding 
122      # speed values to the x and y coordinate of its center
123      # - self is the Dot
124      
125      for i in range(0,2):
126         self.center[i] = (self.center[i] + self.velocity[i])
127   
128   def draw(self):
129      # Draw the dot on the surface
130      # - self is the Dot
131      
132      pygame.draw.circle(self.surface, self.color, self.center, self.radius)
133
134
135main()
pre_poke_framework_line_numbers.txt
Displaying pre_poke_framework_line_numbers.txt.