import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# zad1
# x2=np.arange(-5,5,2)
# y2=-((x2)**2)-4(x2)
# plt.plot(x2,y2,'g-',label='f(x)=-x^2-4x')
# plt.title('tytul')
# plt.ylabel('f(x)=-x^2-4x')
# plt.xlabel('x')
# plt.show()

# zad2
# plt.subplot(3,1,1)
# x1=np.arange(4,9,1)
# y1=np.sqrt(x1)
# plt.bar(x=x1,height=y1,color='blue')
# plt.ylabel('wykres funkcji')
# plt.xlabel('x')
# plt.title('wykres slupkowy funkcji')
# plt.legend(labels='f(x)=(pierwiastek)z x')
# plt.subplot(3,1,3)
# x=np.arange(0,10,0.02)
# y=np.cos(x)+0.4
# plt.plot(x,y,'go',label='cos(x)+0.4')
# plt.title('wykres cos(x)+0.4')
# plt.ylabel('cos(x)+0.4')
# plt.xlabel('x')
# plt.legend()
# plt.savefig('Michal_Naumowicz_zad2.png')
# plt.show()

# zad3

df =pd.read_csv('cars.csv',header=0,sep=';',decimal='.')
print(df)
