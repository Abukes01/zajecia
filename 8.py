import numpy as np
from numpy import pi
# import sounddevice as sd
import matplotlib.pyplot as plt
import scipy.signal as sig

#definiujemy "sampling frequency"
fs = 1000 # Hz
dt=1/fs

#definiujemy czas trwania dźwięku - cała nuta, półnuta itd.
t=np.arange(0, 1, dt)
t2=np.arange(0,1/2.,dt)
t4=np.arange(0,1/4.,dt)
t8=np.arange(0,1/8.,dt)

#definiujemy częstotliwości
fc=261.63
fd=293.66
fe=329.631
ff=349.23
fg=392.00

# x=sin(2 pi f t) - oscylacje o częstotliwości f w czasie t
xg=np.sin(2*pi*fg*t4)
xe=np.sin(2*pi*fe*t4)
xf=np.sin(2*pi*ff*t4)
xd=np.sin(2*pi*fd*t4)
xc8=np.sin(2*pi*fc*t8)
xe8=np.sin(2*pi*fe*t8)
xg2=np.sin(2*pi*fg*t2)
xc2=np.sin(2*pi*fc*t2)

#łączymy ze sobą dźwięki o różnej częstotliwości
x=np.concatenate((xg,xe, xe, xf, xd, xd, xc8, xe8, xg2 ,xg ,xe, xe ,xf, xd, xd ,xc8 ,xe8 ,xc2))
#czas trwania dźwieków w tablicy x
tx=np.linspace(0,len(x))


#tak można dźwięk odtworzyć: (przy pomocy sounddevice)
#sd.play(x,fs)


# # #transformata Fouriera:
# Fw=np.fft.fft(x)
# Ffreq = np.fft.fftfreq(len(x))*fs
# plt.plot(Ffreq, abs(Fw))
# plt.show()

freq, time, fig = sig.spectrogram(x, fs)
print(freq, time, fig, sep='\n\n')
plt.pcolormesh(time, freq, fig, shading='gouraud')
plt.show()