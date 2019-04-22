import numpy as np
import cmath as c
import matplotlib.pyplot as plt
#j=c.sqrt(-1)
def dft(x1,N):
	k=np.arange(0,N)
	n1=np.arange(0,N)
	z=len(x1)
	if z<N:
		q=N-z
		x1=np.append(x1,np.zeros(q))
	y=[]
	M=[]
	P=[]
	for i in k:
		sum=0;
		for j in n1:
			sum+=x1[j]*np.exp(-1*2*np.pi*1j*i*j/np.float(N))
		y.append(sum)
		
	return y
N=input("number of dft ponts")
x1=input("take x values") #ex:[1,2,3]
z1=len(x1)
if z1<N:
	q1=N-z1
	x1=np.append(x1,np.zeros(q1))
print x1
u=[]
u1=[]
#time reversal
for k in range(N):
		q =x1[-k%N]
		u.append(q)	
if z1<N:
	q1=N-z1
	u=np.append(u,np.zeros(q1))
print u
a=0
for k in range(N):
	 sum = (x1[k]*u[k])
	 a=a+sum
print a
M=dft(x1,N)
M1=dft(u,N)
M3=[]
a1=0
for k in range(N):
	sum1 = (1/N)*(M[k]*M1[k])
	a1=a1+sum1
print a1
'''
R1=(np.abs(M))
R2=(np.angle(M))
R3=(np.abs(M3))
R4=(np.angle(M3))
'''

plt.subplot(411)
plt.stem(x1)
plt.subplot(412)
plt.stem(u)
plt.subplot(413)
plt.stem(M)
plt.subplot(414)
plt.stem(M1)
plt.show()

