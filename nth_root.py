def nth_root(a:float,n=2):
    """use Bisection Method to get the nth root of any number"""
    try:
        f =lambda x:x**n-a
        a1,a2=-a,a
        t = (a1 + a2) / 2
        while abs(f(t)-0)>=10**(-10):
            t=(a1+a2)/2
            print(t)
            if f(t) * f(a2) < 0:
                a1 = t
            elif f(t) * f(a2)==0:
                return t
            else:
                a2=t
        return round(t,9)
    except:
        print("Synatax Error:  ")

print(nth_root(1,2))
