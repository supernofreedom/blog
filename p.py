import matplotlib.pyplot as plt
import numpy as np

def demo(N):
    #t=np.arange(0,5,0.2)
    x=np.linspace(0, 8*np.pi, N)
    y=np.sin(x)
    z = np.fft.fft(y)
    w = np.fft.ifft(z)
    plt.plot( x, z, 'b--', x, w, 'g--' )
    plt.show()

if __name__=='__main__':
    demo(2048)
