import matplotlib.pyplot as plt
import numpy as np
def dft(a):
	n=4
	o=complex(0,-1)
	X=[]
	k=np.linspace(0,len(a),n)
	for i in range(0,n):
		sum=0
		for n in range(0,len(a)):
			sum=sum+(a[n]*np.exp((o*2*np.pi*k[i]*n)/len(a)))
		X.append(sum)
	return X
def sum(x,y):
    r=[]
    for i in range(0,len(x),1):
        z=x[i]+y[i]
        r.append(z)
    return r

x1=[1,2,3,4]
x2=[2,3,4,5]
x1k=dft(x1)
x2k=dft(x2)
x3=sum(x1,x2)
x3k=dft(x3)
x3ks=sum(x1k,x2k)
print(x1k)
print(x2k)
print(x3k)
print(x3ks)





