import math 
import random
import sys
class cfg():
    def __init__(self,rangeX,rangeY,populationLen,speed):
        self.rangeX = rangeX
        self.rangeY = rangeY
        self.populationLen = populationLen
        self.speed = speed
    pass
def getfitness(x,y):
    return 21.5+(x*math.sin(4*math.pi*x))+(y*math.sin(20*math.pi*y))
def Init(cfg):
    x1 = random.uniform(cfg.rangeX[0],cfg.rangeX[1])
    x2 = random.uniform(cfg.rangeY[0],cfg.rangeY[1])
    speed = random.uniform(-2,2)
    ans = getfitness(x1,x2)
    #[current x1,current x2,speed,fitness,best x1,best x2,best fitness ]
    return [x1,x2,speed,ans,x1,x2,ans]
def findMax(d1):
    d2 = d1.copy()
    max = 0
    ans = []
    for item in d2:
        if item[6]>max:
            max = item[6]
            ans = item
    return ans
def move(cfg,population,best):
    c1 = 1.4
    c2 = 1.1
    for item  in population:
        vx = item[2]*0.2+c1*random.uniform(-0.2,1.2)*(item[4]-item[0])+c2*random.random()*(best[0]-item[0])
        vy = item[2]*0.2+c1*random.uniform(-0.2,1.3)*(item[5]-item[1])+c2*random.random()*(best[1]-item[1])
        newx1 = item[0]+vx
        newx2 = item[1]+vy
        newfitnesss = getfitness(newx1,newx2)
        #move
        if cfg.rangeX[0]<=newx1<=cfg.rangeX[1] and cfg.rangeY[0]<=newx2<=cfg.rangeY[1] :
            item[0] = newx1
            item[1] = newx2
            item[3] = newfitnesss
        else :
            #position x1 overflow
            if not cfg.rangeX[0]<=newx1<=cfg.rangeX[1]:
                item[0] = random.uniform(cfg.rangeX[0],cfg.rangeX[1])
            #position x2 overflow
            if not cfg.rangeY[0]<=newx2<=cfg.rangeY[1]:
                item[1] = random.uniform(cfg.rangeY[0],cfg.rangeY[1])
            # caculate new fitness
            newfitnesss = getfitness(newx1,newx2)
            item[3] = newfitnesss
        #update best
        if newfitnesss>item[6] and cfg.rangeX[0]<=newx1<=cfg.rangeX[1] and cfg.rangeY[0]<=newx2<=cfg.rangeY[1]:
            item[4] = newx1
            item[5] = newx2
            item[6] = newfitnesss
    return population

if __name__ == "__main__":
    weight = 0.5
    population = []
    cfg = cfg([-3.0,12.1],[4.1,5.8],32,[0,1])
    for  i in range(100):
        population.append(Init(cfg))
    for i in range(4000):
        best =  findMax(population)
        population = move(cfg,population,best)
        if i%500 == 1:
           print('x1->',best[4],' x2->',best[5],' fitness->',best[6])