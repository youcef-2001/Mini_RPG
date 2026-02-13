import random
from Model.Event import Walking


class Environnement:

    def __init__(self):
        self.event= Walking()
        self.eventlist= []
        self.eventcounter=0
        self.title=""


    def lancer(self):
       
       self.event.lancer()
       self.eventcounter+=1



class EnvironnementBuilder:

    def __init__(self) :
        self.env : Environnement


    def reset(self):
        self.env= Environnement()
        return self

    def SetTitle(self,title):
        self.env.title=title
        return self

    def setBoss(self):
        self.env.eventlist.append("boss")
        return self

    def AddEventlist(self,number):
        for i in range(0,number):
            #randomiser apres les event
            self.env.eventlist.append("combat")# combat , marchand,quest, coffre
        return self
    
    def AddQuest(self):
        self.env.eventlist.append("quest")# combat , marchand,quest, coffre
        return self

    def insertKey(self):
        self.env.eventlist.insert(random.randint(0,self.env.eventlist.__len__()),"key")
        return self

    def GetEnv(self):
        return self.env

      
