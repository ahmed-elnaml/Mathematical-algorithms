import math as m
def polar2cart(mag,ang):
    return Compx(mag*m.cos(ang),mag*m.sin(ang))

class Compx:
    def __init__(self,re,im=0):
        self.re=re
        self.im=im
        self.mag=(re**2+im**2)**0.5
        if self.re==0 :
            self.ang=m.pi/2
        else:
            self.ang=m.atan(im/re)

    def __str__(self):
        return str(round(self.re,20))+' + '+str(round(self.im,20))+' i'

    def __add__(self,other):
        if isinstance(other,Compx):
            return Compx(self.re+other.re,self.im+other.im)
        elif isinstance(other,int) or isinstance(other,float):
           return Compx(self.re+other,self.im)

    def __radd__(self,other):
           return  self+other

    def __sub__(self,other):
        if isinstance(other, Compx):
            return Compx(self.re-other.re,self.im-other.im)
        elif isinstance(other, int) or isinstance(other, float):
           return Compx(self.re-other,self.im)

    def __rsub__(self, other):
        return (self-other)*(-1)

    def __mul__(self,other):
        if isinstance(other,Compx):
            return Compx(self.re*other.re-self.im*other.im,self.re*other.im+self.im*other.re)
        if isinstance(other,int) or isinstance(other,float):
            return Compx(self.re*other,self.im*other)

    def __rmul__(self, other):
        return self*other

    def cong(self):
        return Compx(self.re,(-1)*self.im)

    def __truediv__(self, other):
        if isinstance(other,Compx):
            return self*other.cong()*(1/other.mag)
        if isinstance(other,int) or isinstance(other,float):
            return Compx(self.re/other,self.im/other)
    def __rtruediv__(self, other):
        return (self/other)**(-1)

    def __pow__(self, power, modulo=None):
        ln_self=Compx(m.log(self.mag),self.ang)
        ln_self_w = ln_self * power
        return polar2cart(m.e ** (ln_self_w.re), ln_self_w.im)


    def __rpow__(self, other):
        if isinstance(other,Compx):
            ln_self = Compx(m.log(other.mag), other.ang)
        if isinstance(other,int) or isinstance(Compx,float):
            ln_self = Compx(m.log(other))
        ln_self_w = ln_self * self
        return polar2cart(m.e ** (ln_self_w.re), ln_self_w.im)

    def cos(self):
        return (m.e**(Compx(0,1)*self)+m.e**(Compx(0,-1)*self))/2

a=Compx(0,2)*6
print(a.cos())
