'''
    @Object(目的):
    储存游戏里所有的设置
'''
class Settings:
    def __init__(self):
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 800

        #背景颜色
        self.bg_color = (0,0,0)

        #飞船的移动速度
        self.ship_velocity = 0.4

        #bullet color(子弹颜色)
        self.bullet_color = (0,255,0)

        # setup bullet(设置子弹)
        self.bullet_velocity = 0.3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_spot = 0, 0, self.bullet_width, self.bullet_height
