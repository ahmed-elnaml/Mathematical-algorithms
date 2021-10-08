def remov_(l:list):
    l2=l
    flag=True
    while flag:
        try:
            if l2[0]==0:
                l2.remove(0)
            else:
                flag=False
        except:
            return l2
    return l2

class Pol:
    def __init__(self,co:list):
        self.co=co
        # for element in self.co:
        #     if not (isinstance(element,int) or isinstance(element,float)):
        #          raise "error"


    def __len__(self):
        return len(self.co)


    def __getitem__(self, item):
        return self.co[item]
    def __setitem__(self, key, value):
        self.co[key]=value
    def __str__(self):
        return ",".join([str(x) for x in self.co])

    def str(self,x:str="x"):
        re=''
        for i in range(len(self)-1):
            if self[i]!=0:
                if self[i]>0:
                    re+='+'
                re+=str(self[i]) + x + '^' + str(len(self) - i - 1)
        if self[-1]>0:
            re+="+"+str(self[-1])
        elif self[-1]<0:
            re += str(self[-1])
        return re


    def adjust_co(self, other):
        self.co=[0]*(len(other)-len(self))+self.co
        other.co=[0]*(len(self)-len(other))+other.co
        return self,other


    def __add__(self, other):
        l1,l2=self.adjust_co(other)
        result = Pol([0] * len(l1))
        for i in range(len(l1)):
            result[i]=l1[i]+l2[i]
        return result


    def __sub__(self,other):
        l1, l2 = self.adjust_co(other)
        result = Pol([0] * len(l1))
        for i in range(len(l1)):
            result[i] = l1[i] - l2[i]
        return result

    def __mul__(self, other):
        if not isinstance(other,Pol):
            other2=Pol([other])
        else:
            other2=other
        if not isinstance(self,Pol):
            other2=Pol([self])
        result=Pol([0]*(len(self)+len(other2)))
        for i in range(len(self)):
            for i2 in range(len(other2)):
                result[-(i+i2+1)]+=self[-(i+1)]*other2[-(i2+1)]
        return result



    def div(self, other,result=[],remainder=[]):
        self_=Pol(self.co)
        if result==[]:
            global z
            z=len(self_)
        if len(self_)>=len(other):
            r=self_[0]/other[0]
            subtracted=Pol(remov_((other*Pol([r])).co))
            if len(self_)-len(other)>0:
                subtracted.co = subtracted.co + [0] * (len(self_) - len(other))
                result+=[0]*(len(self_) - len(other))
            if len(subtracted)<len(self_):
                subtracted.co=subtracted.co+[0]*(len(self_)-len(subtracted))
            self_=Pol(remov_((self-subtracted).co))
            result.append(r)

        else:
            remainder=self_
            result = remov_(result)
            if len(result) <= (z - len(other)):
                z2 = z+1 - (len(other) + len(result))
                result+=[0]*z2
            if remainder==[]:
                return Pol(result)
            return (Pol(result), remainder)
        return self_.div(other,result)

    def __truediv__(self, other):
        return self.div(other)


    def evaluate(self,x=1):
        result=0
        for (k,v) in enumerate(reversed(self.co)):
            result+=v*x**(k)
        return result
    def diff(self,value=None):
        result = []
        for (k, v) in enumerate(reversed(self.co)):
            result.append(v * k)
        if value==None:
            return Pol(list(reversed(result))[:-1])
        else:
            return Pol(list(reversed(result))[:-1]).evaluate(value)

    def integral(self,to=None,from_=0):
        result = [0]
        for (k, v) in enumerate(reversed(self.co)):
            result.append(v / (k+1))
        if to == None:
            return Pol(list(reversed(result)))
        else:
            return Pol(list(reversed(result))).evaluate(to)-Pol(list(reversed(result))).evaluate(from_)

a=Pol([1,0,-5])
b=(a*a).diff()
print(a)

