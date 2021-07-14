import numpy as np
import matplotlib.pyplot as plt

class pedacoDeBosta:
    zeRuela = None
    doido = None
    paraQueda = None

pedacoDeBosta.zeRuela = 70
pedacoDeBosta.doido = 90
pedacoDeBosta.paraQueda = 21

g = 9.81
sigma = 1.1

def quedaDoPedacoDeBosta(r, t):
    y = r[0]
    v = r[1]
    f_y = v
    f_v = -(sigma/(pedacoDeBosta.paraQueda + pedacoDeBosta.doido + pedacoDeBosta.zeRuela)*v)-g
    f_r = np.array([f_y, f_v], float)
    return f_r

y_0 = 3657.6
v_0 = 0

a = 0
b = 60
div = 1000
h = (b-a)/div     
tempo = np.arange(a, b, h)

s_r = np.array([y_0, v_0], float)

s_y = []
s_v = []

for i in tempo:
    s_y.append(s_r[0])
    s_v.append(s_r[1])
    k1 = h*quedaDoPedacoDeBosta(s_r, i)
    k2 = h*quedaDoPedacoDeBosta(s_r + k1/2, i + h/2)
    k3 = h*quedaDoPedacoDeBosta(s_r + k2/2, i + h/2)
    k4 = h*quedaDoPedacoDeBosta(s_r + k3, i + h/2)
    s_r += (k1 + 2*k2 + 2*k3 + k4)/6

plt.plot(tempo, s_v, 'k')
plt.title('Velocidade da bosta')
plt.xlabel('t(s)')
plt.ylabel('V(m/s)')
plt.legend(['Velocidade'], loc='upper right')
plt.show()