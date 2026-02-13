import random
from Model.Event import Walking


class Environnement:

    def __init__(self):
        self.event= Walking()
        self.eventlist= []
        self.eventcounter=0
        self.title=""


    def lancer(self):
       self.eventcounter+=1


class EnvironnementBuilder:

    def __init__(self) :
        self.env : Environnement
    def reset(self):
        self.env= Environnement()
    def SetTitle(self,title):
        self.env.title=title
    def setBoss(self,env: Environnement):
        env.eventlist.append("boss")
    def AddEventlist(self,number):
        for i in range(0,number):
            #randomiser apres les event
            self.env.eventlist.append("combat")# combat , marchand,quest, coffre
    def insertKey(self):
        self.env.eventlist.insert(random.randint(0,self.env.eventlist.__len__()),"key")


      
