def fun(n, m={}):
    if n == 0: return 0
    if n == 1: reutrn 1
    if n in m: return m[n]
    m[n] = fun(n-1) + fun(n-2)
    return m[n]


def calc(m, n, me = {}):
    if m == 2 and n == 2: return 2
    if m == 1 or n == 1: return 1
    if (m, n) in me: return me[(m, n)]
    me[(m, n)] = calc(m - 1, n, me) + calc(m, n - 1, me)
    return me[(m, n)]


def calc(n):

    if n % 4 == 0:
        ret = (n//2) * 10
        return (ret, -ret)
    elif n % 4 == 1:
        ret = (n//4) * 20
        return (ret, ret+10)
    elif n % 4 == 2:
        ret = (n//2) * 10
        return (-(ret+10), ret)
    elif n % 4 == 3:
        ret = -(10 * (n + 1))
        return (ret, ret)
    
    
    

class x:
    def __init__(self, gyro, gps):

        self.gyro = gyro
        self.gps = gps
        
    def __add__(self, other):
        return ((self.gyro + other.gyro), str(self.gps + other.gps))
                
a = x(3, 7)
b = x(4, 6)

print(a + b)

def biological(screentime, tv):
    return (1 / (2 * math.pi * screentime * tv))