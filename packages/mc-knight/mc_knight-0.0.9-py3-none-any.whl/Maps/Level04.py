from Maps.LevelBase import LevelBase
from Script.assist.Array import Array
class Level04(LevelBase):#关卡名
    def __init__(self,screen,cols,rows):
        LevelBase.__init__(self,screen,cols,rows)
    def LoadLevel(self):
        #1代表存在，0代表不存在
        temp = Array()
        temp.Clear()
        temp.SetSA([[0,0,0,1,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0]])
        self.CreateCastle(temp)#城堡
        temp.Clear()
        temp.SetSA([[2,2,2,0,2,2],
                    [0,0,0,0,1,1],
                    [0,1,1,1,1,1],
                    [0,1,1,1,1,1],
                    [0,0,0,0,0,0]])
        self.CreateWater(temp)#水
        temp.Clear()
        temp.SetSA([[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [1,0,0,0,0,0]])
        self.CreateEquipage(temp)#装备  1宝剑   2头盔   3靴子
        temp.Clear()
        temp.SetSA([[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,1]])
        self.CreatePlayer(temp)#玩家
        self.UpdateCollision()#更新碰撞矩阵
        

