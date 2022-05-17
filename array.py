class Array:
    def __init__(self,*args, size=10):
        self.arr = [None]*size
        self.size = size
        self.length = 0
        self.pushArgs(args)

    def getLen(self):
        return self.length

    def pushArgs(self,args):
        args = args[0:self.size]
        for item in args:
            self.arr[self.length]=item
            self.length+=1

    def display(self):
        for item in self.arr[self.length]:
            print(item, end=' ')
        print('')

    def set(self,index,item):
        if(index>-1 and index<self.length):
            self.arr[index]=item

    def get(self,index):
        if(index>-1 and index<self.length):
            return self.arr[index]
        return -1
    
    def avg(self):
        sum=0
        for item in self.arr[self.length]:
            sum+=item
        return sum/self.length

    def min(self):
        m=self.arr[0]
        for item in self.arr[1:self.length]:
            if item<m:
                m=item
        return m

    def max(self):
        m=self.arr[0]
        for item in self.arr[1:self.length]:
            if item>m:
                m=item
        return item

    def push(self,item):
        if self.length < self.size:
            self.arr[self.length]=item
            self.length+=1

    def insert(self,index,item):
        if self.length==self.size:
            return

        if index>-1 and index<self.length:
            for i in range(self.length,index,-1):
                self.arr[i] = self.arr[i-1]
            self.arr[index]=item
            self.length+=1
        
        if(index>=self.length):
            self.push(item)

    def pop(self):
        self.length-=1
        x = self.arr[self.length]
        self.arr[self.length]=None
        return x

    def delete(self, index):
        if(index>-1 and index<self.length):
            x=self.arr[index]
            for i in range(index,self.length,1):
                self.arr[i]=self.arr[i+1]
            self.length-=1
            return x

    def isSorted(self):
        for i in range(self.length-1):
            if(self.arr[i] > self.arr[i+1]):
                return False
        return True
            
    def binarySearch(self, key):
        l=0
        h=self.length-1
        while(l<=h):
            m=(h+l)//2
            if(key==self.arr[m]):
                return m
            elif(key<self.arr[m]):
                h=m-1
            else:
                l=m+1
        return -1   
        
    def reverse(self):
        i=0
        j=self.length-1
        while(i<j):
            self.arr[i],self.arr[j]=self.arr[j],self.arr[i]
            i+=1
            j-=1
    
    def convertToSet(self):
        hash={}
        temp=Array(size=self.length)
        for item in self.arr:
            if item not in hash.keys():
                temp.push(item)
            hash[item] = True
        return temp


    def merge(self,obj):
        i=0
        j=0
        k=0
        z=Array(size=self.length+obj.length)
        while(i<self.length and j<obj.length):
            if(self.arr[i]<obj.arr[j]):
                z.arr[k]=self.arr[i]
                i+=1
                k+=1
            else:
                z.arr[k]=obj.arr[j]
                j+=1
                k+=1
        for a in range(i,self.length):
            z.arr[k]=self.arr[a]
            k+=1
        for a in range(j,obj.length):
            z.arr[k]=obj.arr[a]
            k+=1
        z.length=k
        return z

    #Union for sorted sets
    def union(self,obj):
        i,j,k=0,0,0
        z=Array(size=self.length+obj.length)
        while(i<self.length and j<obj.length):
            if(self.arr[i]<obj.arr[j]):
                z.arr[k]=self.arr[i]
                k+=1
                i+=1
            elif(self.arr[i]>obj.arr[j]):
                z.arr[k]=obj.arr[j]
                k+=1
                j+=1
            else:
                z.arr[k]=self.arr[i]
                k+=1
                i+=1
                j+=1
        for item in self.arr[i:self.length]:
            z.arr[k]=item
            k+=1
        for item in obj.arr[j:obj.length]:
            z.arr[k]=item
            k+=1
        z.length=k
        return z

    #Intersection for sorted sets
    def intersection(self,obj):
        i,j,k=0,0,0
        z=Array(size=self.length+obj.length)
        while(i<self.length and j<obj.length):
            if(self.arr[i]<obj.arr[j]):
                i+=1
            elif(self.arr[i]>obj.arr[j]):
                j+=1
            else:
                z.arr[k]=self.arr[i]
                k+=1
                i+=1
                j+=1
        z.length=k
        return z

    #Union of sorted sets
    def difference(self,obj):
        i,j,k=0,0,0
        z=Array(size=self.size)
        while(i<self.length and j<obj.length):
            if(self.arr[i]<obj.arr[j]):
                z.arr[k]=self.arr[i]
                i+=1
                k+=1
            elif(self.arr[i]>obj.arr[j]):
                z.arr[k]=self.arr[i]
                i+=1
                k+=1
            else:
                i+=1
                j+=1
        z.length=k
        return z

    #Finding missing element in set like(6,7,8,9,10,12......)
    ##step is the common difference between a sequence
    def findMissingElements(self,step=1):
        missing=[]
        diff=self.arr[0]
        for i in range(1,self.length):
            if diff!=self.arr[i]-i*step:
                while(diff!=self.arr[i]-i*step):
                    missing.append(diff+i*step)
                    diff+=step

        return missing
    
    def findMissingElementsByHashing(self,step=1):
        dict={i:0 for i in range(0,self.max(),step)}
        for item in self.arr[0:self.length]:
            dict[item]=1
        return [key for key in dict.keys() if dict[key]==0]

    ##Find pair with sum=k
    #Unsorted Version
    def sumIsK(self,k):
            for (i,item1) in enumerate(self.arr[0:self.length]):
                for(j,item2) in enumerate(self.arr[i+1:self.length]):
                    if item1+item2==k:
                        return (i,j+i+1)

    def sumIsKByHashing(self,k):
        hash={i:0 for i in range(0,self.max())}
        for item in self.arr[0:self.length]:
            hash[item]=1
            if hash.get(k-item,0)==1:
                print(f'{item} + {k-item} = {k}')

    def sumIsKSorted(self,k):
        i=0
        j=self.length-1
        while(i<j):
            if(self.arr[i]+self.arr[j]==k):
                print(f'{self.arr[i]} + {self.arr[j]} = {k}')
                i+=1
                j-=1
            elif(self.arr[i]+self.arr[j]<k):
                i+=1
            else:
                j-=1

    def min_max(self):
        min=self.arr[0]
        max=self.arr[0]
        for item in self.arr[1:self.length]:
            if item<min:
                min=item
            else:
                if item>max:
                    max=item

        return (min,max)