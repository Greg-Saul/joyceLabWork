# %pylab

from mesa_reader import MesaData
import matplotlib.pyplot as plt

md = MesaData('history.data')

# lum = (10 ** np.array(md.data('log_L')))
lum = md.data('log_L')
# tmp = (10 ** np.array(md.data('log_Teff')))
tmp = md.data('log_Teff')
newTmp = tmp[::-1]

# plt.figure(figsize=(10, 6))
plt.plot(tmp, lum, color='blue')
plt.gca().invert_xaxis()
plt.ylabel('Log Luminosity')
plt.xlabel('Log Effective Temperature')
plt.title('Luminosity x Temperature')

# plt.show()
plt.savefig('Lum vs Tmp.png', dpi=300)


