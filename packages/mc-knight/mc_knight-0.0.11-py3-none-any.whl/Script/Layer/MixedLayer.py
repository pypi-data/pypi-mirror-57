from Script.Layer.GrassLayer import GrassLyaer
from Script.Layer.WaterLayer import WaterLayer
from Script.Layer.PineLayer import PineLayer
from Script.Layer.StoneLayer import StoneLayer
from Script.Layer.StumpLayer import StumpLayer
from Script.Layer.CastleLayer import CastleLayer
from Script.Layer.BackGroundLayer import BackGroundLayer
from Script.Layer.PlayerLayer import PlayerLayer
from Script.Layer.BlankLayer import BlankLayer
from Script.Layer.StumpLayer import StumpLayer
from Script.Layer.CollisionLayer import CollisionLayer
from Script.Layer.SoundsLayer import SoundsLayer
from Script.Layer.EquipageLayer import EquipageLayer
from Script.Layer.BridgeLayer import BridgeLayer
from Script.Layer.FloversLayer import FloversLayer
from Script.Layer.SpikesLayer import SpikesLayer
from Script.Layer.MillLayer import MillLayer
from Script.Layer.BoulderLayer import BoulderLayer
from Script.assist.Array import Array
import threading
import pygame
import time
from pygame.locals import *
from Script.MyScreen import MyScreen
from Script.Timer.Time import Time as p

class MixedLayer:
    _instance_lock = threading.Lock()
    def __init__(self,cols,rows):
        self.cols=cols
        self.rows=rows
        MyScreen.SetBox(cols, rows)
        self.myLayer=Array()
        self.millList = []
        self.boulderList = []
        self.collider=CollisionLayer(cols,rows)
        self.grassLayer=GrassLyaer(self.cols,self.rows)
        self.substance=BlankLayer(self.cols,self.rows)
        self.layer=[]
        self.equList=[]
        self.colliderArray=Array(cols,rows)
        self.layer.append(self.grassLayer)
        self.layer.append(self.substance)
        self.sound=SoundsLayer()
        self.sound.CreateLayer()
        self.sound.PlaySound()
        self.CreateBackGround()
        self.pt = p()
    def CreateBackGround(self):
        self.backGroundLayer=BackGroundLayer() 
    def CreateWater(self,array):
        self.waterLayer=WaterLayer(self.cols,self.rows,array,self.grassLayer,self.colliderArray)  
    def CreateSpikes(self,array):
        self.spikesLayer=SpikesLayer(self.cols,self.rows,array,self.substance,self.colliderArray)
    def CreateBoulder(self,array):
        self.boulderLayer=BoulderLayer(self.cols,self.rows,array,self,self.colliderArray)
    def CreateMill(self,array):
        self.millLayer=MillLayer(self.cols,self.rows,array,self,self.colliderArray)
    def CreateBridge(self,array):
        self.bridgeLayer=BridgeLayer(self.cols,self.rows,array,self.substance,self.colliderArray)
    def CreateFlovers(self,array):
        self.floversLayer=FloversLayer(self.cols,self.rows,array,self.substance,self.colliderArray)  
    def CreatePine(self,array):
        self.pineLayer=PineLayer(self.cols,self.rows,array,self.substance,self.colliderArray) 
    def CreateStone(self,array):
        self.stoneLayer=StoneLayer(self.cols,self.rows,array,self.substance,self.colliderArray) 
    def CreateStump(self,array):
        self.stumpLayer=StumpLayer(self.cols,self.rows,array,self.substance,self.colliderArray) 
    def CreateCastle(self,array):
        self.castleLayer=CastleLayer(self.cols,self.rows,array,self.substance,self.colliderArray) 
    def CreatePlayer(self,array):
        self.playerLayer=PlayerLayer(self.cols,self.rows,array)
    def CreateEquipage(self,array):
        self.EquipageLayer=EquipageLayer(self.cols,self.rows,array,self,self.colliderArray)
    def UpdateCollision(self):
        self.collider.UpdateCollision(self.colliderArray)
    def GetPlayer(self):
        return self.playerLayer.element
    def GetCollision(self):
        return self.collider.myLayer
    def GetCollider():
        return MixedLayer._instance.colliderArray
    def StartMixed(self,screen):   
        while True:
            screen.blit(self.backGroundLayer.GetBackGround(),(0,0))
            for x in self:
                if x!=None:
                    self.myLayer.Set(x)
                    for i in range(0,x.cols):  
                        for j in range(x.rows):
                            a=int((MyScreen.Width-x.rows*65)/2+j*65)
                            b=int((MyScreen.Height-x.cols*65)/2+i*65)
                            if x.myLayer[i,j]:  
                                screen.blit(x.myLayer[i,j], (a,b))
                else:
                    break
            for b in self.boulderList:
                screen.blit(b.GetImage(),b.GetBPos())
                pass
            for m in self.millList:
                screen.blit(m.a,(m.x+5,m.y-40))
                b = m.Rotate(m.x+25,m.y-20)
                screen.blit(b[0],b[1])
                
            for e in self.equList:
                screen.blit(e.GetAnim(),(e.x,e.y))
            screen.blit(self.playerLayer.GetPlayer(),self.playerLayer.GetPlayerPos())
            self.pt.CalculationDeltaTime()
            pygame.display.update()
    @staticmethod
    def GetInstance():
        return MixedLayer._instance
    def __iter__(self):
        self.index=0
        return self
    def __next__(self):
        if self.index < len(self.layer):
            self.index+=1
            return self.layer[self.index-1]
        else:
            return None
    def __new__(cls, *args, **kwargs):
        if not hasattr(MixedLayer, "_instance"):
            with MixedLayer._instance_lock:
                if not hasattr(MixedLayer, "_instance"):
                    MixedLayer._instance = object.__new__(cls)  
        return MixedLayer._instance