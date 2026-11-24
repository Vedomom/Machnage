import random
import sqlite3

class MakrovModel():
    def __init__(self, db_name : str, order : int) -> None:
        self.db_name  = db_name
        self.order = order
        self.model = dict()
        self.buildModel()
    
    
    def buildModel(self):
        db = sqlite3.connect(f"src/DB/{self.db_name}")
        
        cursor = db.cursor()
        cursor.execute("""
        SELECT name FROM names
        ;
        """)
        
        db.commit()
        nameList = cursor.fetchall()
        
        for name in nameList:
            prefix = "_" * self.order
            name = name[0]
            name = prefix + str(name).lower() + "*"
            for i in range(len(name) - self.order):
                pre = name[i : i+self.order]
                nextChar = name[i+self.order]
                if pre not in self.model.keys():
                    self.model[pre] = list()
                
                self.model[pre].append(nextChar)
                
        db.close()
 
    def getNameList(self ,length:int, limit =0):
        namelist = []
        for i in range(length):
            name = self.generateName(limit)
            name = name[0].upper() + name[1:]  
            namelist.append(name)
        
        print(namelist)
        return namelist   
        

    def generateName(self, limit :int = 0):
        name = ""
        prefix = "_" * self.order
        nextChar = ""
        
        #initializing
        nextChar = random.choice(self.model[prefix])
        if nextChar != "*":
            name += nextChar
        
        prefix = prefix[1:] + nextChar
        
        #name loop
        
        if limit > 0:
            while(nextChar != "*" and len(name) < limit):
                    if prefix in self.model.keys():
                        nextChar = random.choice(self.model[prefix])
                        if nextChar != "*":
                            name += nextChar
                        prefix = prefix[1:] + nextChar
                
        else:
            while(nextChar != "*"):
                if prefix in self.model.keys():
                    nextChar = random.choice(self.model[prefix])
                    if nextChar != "*":
                        name += nextChar
                    prefix = prefix[1:] + nextChar
        return name