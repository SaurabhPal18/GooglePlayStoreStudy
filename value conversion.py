import math

millnames = ['','k','M','B']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    print(millidx)
    print('{:.1f}{}'.format(n / 10**(3 * millidx), millnames[millidx]))
    
    a=""+str(n/10**(3*millidx))+""+str(millnames[millidx])
    print(a)
millify(23456878)