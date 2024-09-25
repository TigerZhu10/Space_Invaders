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

        #飞船移动速度
        self.ship_velocity = 0.4
