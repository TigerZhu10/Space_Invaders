'''
    @Object(目的):
    储存游戏里所有的设置
'''
class Settings:
    def __init__(self):
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 800

        # check if the game is active or not 
        self.game_active = False

        #Backgroud color
        self.bg_color = (0,0,0)

        #Ship's speed
        self.ship_velocity = 4

        #bullet color(子弹颜色)
        self.bullet_color = (191, 16, 4)

        # setup bullets(设置子弹)
        self.bullet_velocity = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_attributes = 0, 0, self.bullet_width, self.bullet_height
        self.bullet_num_allowed = 10

        self.alien_velocity = 2
        self.alien_direction = 1  
        self.alien_drop_speed = 25

        # setup button
        self.button_attributes = 0, 0, 250, 50
        self.button_color = (123,123,123)

        self.round = 1
        self.score = 0
        self.additional_score = 0
        self.lives = 3
