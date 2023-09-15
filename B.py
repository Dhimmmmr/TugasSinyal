import numpy as np
import matplotlib.pyplot as plt

print ("Mukhammad Amirul Adhim Ramadhani")
print ("5009211145")

t = np.linspace(0, 2 * np.pi, 1000) 
amplitude = 5.0  
frequency = 2.0  
sinyal = amplitude * np.sin(frequency * t)


plt.figure(figsize=(10, 4))  
plt.plot(t, sinyal, label='Sinyal Sinusoidal')
plt.title('Contoh Sinyal Sinusoidal')
plt.xlabel('Waktu (s)')
plt.ylabel('Amplitudo')
plt.legend()
plt.grid(True)
plt.show()
