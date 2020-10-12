class McCulloch:    
    w1 = 1
    w2 = 1
    bias = 1
    
    def check_v(self,V):
        if V >= 0:
            return 1
        elif V < 0:
            return 0

    def mcCu(self, i):
        while 1:
            V = i[0]*self.w1 + i[1]*self.w2 + self.bias
            
            if self.check_v(V) > i[2]:
               self.bias -= 1 
            elif self.check_v(V) < i[2]:
                self.bias +=1
            elif self.check_v(V) == i[2]:
                break
        
and_gate = [[0,0,0],
            [0,1,0],
            [1,0,0],
            [1,1,1]]

mc_obj = McCulloch()

for i in and_gate:
    mc_obj.mcCu(i)

print(mc_obj.w1, mc_obj.w2, mc_obj.bias)
