import random
class Snake():

    def __init__(self,screen_width,screen_height):
        self.sw = screen_width
        self.sh = screen_height
        self._bodyx=[]
        self._bodyy=[]
        self._bodyx.append(random.randint(0,screen_width))
        self._bodyy.append(random.randint(0,screen_height))

    def add(self):
        length=len(self.bodyx)-1
        self._bodyx.append(self.bodyx[length]+40)
        self._bodyy.append(self.bodyy[length] )
    
    
    
    def move(self,x,y):
        length=len(self._bodyx)
        for i in range(length-1,1,-1):
            self._bodyx[i]=self._bodyx[i-1]
            self._bodyy[i]=self._bodyy[i-1]
        
        if length>1:
            self._bodyx[1]=x
            self._bodyy[1]=y


    def food(self):
        food_location=[random.randint(0,self.sw),random.randint(0,self.sh)]
        return food_location
    
    @property
    def bodyx(self):
        return self._bodyx
    
    @property
    def bodyy(self):
        return self._bodyy
    
    @bodyx.setter
    def bodyx(self,new):
        self._bodyx=new

    @bodyy.setter
    def bodyy(self,new):
        self._bodyy=new
        
    
    

