# Lab 3 Write a program to represent data required for "Job Sequencing with Deadlines" using dataclass#
from dataclasses import dataclass
#importing dataclass
@dataclass
#declaring class
class item:
    jobs : str
    deadlines : int
    profits : int
    def __init__(self,jobs,deadlines,profits) -> None:
        self.jobs = jobs
        self.deadlines = deadlines
        self.profits = profits
        
    def __repr__(self) -> str:
        return f"({self.jobs},{self.deadlines},{self.profits})" 
        
class jobsequence: 
    def __init__(self) -> None:
        self.data = list() # datamodel
        
    def add(self,items):
        '''a method to add the items'''
        self.data.append(items)
    
    def getData(self):
        '''a method to access the data'''
        return self.data

#code to create individual item
i1 = item("J1",1,150) 
i2 = item('J2',2,100)
i3 = item('J3',1,200)
# datamodel
j = jobsequence()
j.add(i1)  # adding items
j.add(i2)
j.add(i3)
# access these model
print(j.getData()) 