from Maps.LevelBase import LevelBase
from Script.assist.Array import Array
class Level08(LevelBase):#关卡名
    def __init__(self,screen,cols,rows):
        LevelBase.__init__(self,screen,cols,rows)
    def LoadLevel(self):
        #1代表存在，0代表不存在
        temp = Array()
        temp.Clear()
        temp.SetSA([[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,1]])
        self.CreateCastle(temp)#城堡
        temp.Clear()
        temp.SetSA([[1,1,1,1,1,1,1,1],
                    [0,0,0,1,0,0,0,1],
                    [0,1,0,1,0,1,0,1],
                    [0,1,0,1,0,1,0,1],
                    [0,1,0,1,0,1,0,1],
                    [0,1,0,0,0,1,0,0]])
        self.CreatePine(temp)#树
        temp.Clear()
        temp.SetSA([[0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0],
                    [1,0,0,0,0,0,0,0]])
        self.CreatePlayer(temp)#玩家
        self.UpdateCollision()#更新碰撞矩阵
        

