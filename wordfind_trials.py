import random
import time
import matplotlib.pyplot as plt

class Find():
    def __init__(self):
        self.alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.word= 'SORRY'
        self.splitted= [char for char in self.word]
        self.predicted=[]
        self.predicted_new=[]
        self.reward_t= 0
        self.l=0
        self.state_n=0
        self.state=[]
        self.reward_graph_n=0
        self.reward_graph=[]
        

    def random_generator(self):
        for i in range(len(self.splitted)):
            r= random.randint(1,len(self.alphabet)-1)
            self.predicted.append(self.alphabet[r])

        print(self.predicted)
        return self.predicted
        
    
    def compare(self):
        predicted_r= self.random_generator()
        
        while self.l<=(len(self.splitted)):
            print(self.l)
            if self.splitted[self.l]==predicted_r[self.l]:
                
                return True
            else:
                return False

    def reward(self):
        c= self.compare()
        self.state_n+=1
        self.state.append(self.state_n)
        if c==True:
            self.predicted_new.append(self.predicted[self.l])
            print(self.predicted_new)
        if len(self.predicted)>=len(self.splitted):
            self.predicted=[]
        if c==False:
            self.reward_graph_n+=-1
            self.reward_graph.append(self.reward_graph_n)
            return -1
            
        if c==True:
            self.reward_graph_n+=1
            self.l+=1
            self.reward_graph.append(self.reward_graph_n)
            return 1
            
            
ff= Find()

try:
    while ff.reward!=len(ff.splitted):
        print(ff.reward())
        print('Generation:',ff.state)
        print('Rewards',ff.reward_graph)
except:
     pass

plt.plot(ff.state,ff.reward_graph)
plt.show()

    
    
    
                
            
            
    

    

