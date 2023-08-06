from Maps.LevelBase import LevelBase
from Script.assist.Array import Array
class Level02(LevelBase):#关卡名
    def __init__(self,screen,cols,rows):
        LevelBase.__init__(self,screen,cols,rows)
    def LoadLevel(self):
        #1代表存在，0代表不存在
        temp = Array()
        temp.Clear()
        temp.SetSA([[0,0,0,0,1],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0]])
        self.CreateCastle(temp)#城堡
        temp.Clear()
        temp.SetSA([[2,2,2,2,0],
                    [1,1,1,1,0],
                    [0,0,0,0,0],
                    [0,1,1,1,1],
                    [0,1,1,1,1]])
        self.CreateWater(temp)#水
        temp.Clear()
        temp.SetSA([[0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,0,0,0],
                    [1,0,0,0,0]])
        self.CreatePlayer(temp)#玩家
        self.UpdateCollision()#更新碰撞矩阵
        

