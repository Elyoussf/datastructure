

class Array:

    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.core = [None]*self.capacity
    
    
    def add(self,e):
        if self.capacity<=self.size:
            l = [None]*self.capacity*2
            for i in range(len(self.core)):
                l[i] = self.core[i]
            self.core = l
            self.capacity = self.capacity*2
        self.core.append(e)
        self.size+=1
    def delete_ByIndex(self,index):

        if index >= self.size or index < -self.size:
            print('Cannot delete , The index is out of range!')
        else:
            self.core.remove(index)
            self.size = self.size - 1

            if self.size < self.capacity/4:
                self.core = self.core[:max(4*self.size+1,self.capacity)]
                self.capacity = max(4*self.size+1,self.capacity)

    
    def get(self,index):
        if index >= self.size or index < -self.size:
            print('Cannot get the element , The index is out of range!')
        else:
            return self.core[index]
        
    def set(self,index,val):
        if self.capacity<=self.size:
            l = [None]*self.capacity*2
            for i in range(len(self.core)):
                l[i] = self.core[i]
            self.core = l
            self.capacity = self.capacity*2
        if index > self.size or index < -self.size:
            print('The index is not valid ')
        else:
            self.core.insert(index,val)
            self.size+=1


arr = Array(4)

arr.set(0,1)
arr.set(0,1)

print(arr.get(1))
        


        

