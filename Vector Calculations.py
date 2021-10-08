class Vect:
    def __init__(self,*list):
        self.val=list
    def __len__(self):
        return len(self.val)
    def __getitem__(self, item):
        return self.val[item]
    def __str__(self):
        return '<<'+','.join(map(lambda x:str(round(x,5)),self.val) )+'>>'
    def __add__(self, other):
        if len(self)!=len(other):
            print('Dimensions are different')
        else:
            l=[self[i]+other[i]for i in range(len(self))]
            return Vect(*l)
    def __sub__(self, other):
        if len(self)!=len(other):
            print('Dimensions are different')
        else:
            l=[self[i]-other[i]for i in range(len(self))]
            return Vect(*l)
        def dot_product(self, other):
            if len(self)!=len(other):
                print('Dimensions are different')
            else:
              sum=0
            for i in range(len(self)):
                sum+=self[i]*other[i]
            return sum
    def mag(self):
        return sum([i**2 for i in self.val])**0.5

    def scale_it(self,n):
        print('er')
        return Vect(*[i*n for i in self.val])
    def __mul__(self, other):
        try:
            if  isinstance(other,Vect):
                return self.dot_product(other)
            else :
                return self.scale_it(other)
        except TypeError:
           print('err')
           return self.scale_it(other)

    def u_vect(self):
        return self.scale_it(1/self.mag())

    def is_normal(self,other):
        return self*other==0
    def is_parrall(self,other):
        return self.u_vect().val==other.u_vect().val

v1=Vect(1,5,7)
v2=Vect(3,15,21)
s=v1.u_vect()
print(v1.u_vect(),v2.u_vect())
