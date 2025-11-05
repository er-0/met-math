from matplotlib import pyplot as plt, patches
import numpy as np

#### Yksikköympyrä (tehtävä 1)

# Kuva ja akselit
fig, ax = plt.subplots()

# Piirretään yksikköympyrä
ymp = patches.Circle((0, 0), radius=1, fill=False)
ax.add_patch(ymp)

# Akselit keskellä
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.axis('equal')

plt.xticks([-1, 0, 1])
plt.yticks([-1, 0, 1])

# Kulmat asteina
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270])

# Muunnetaan radiaaneiksi
rads = np.deg2rad(A)

# Pisteiden koordinaatit
x = np.cos(rads)
y = np.sin(rads)

# Piirretään pisteet
ax.scatter(x, y, c=A, cmap='hsv', marker='X', s=100)

# Lisätään tekstit
for i in range(len(A)):
    label = f"{A[i]}°"
    ax.annotate(label,
                xy=(x[i], y[i]),
                xytext=(10, 10),
                textcoords='offset points',
                ha='center',
                fontsize=12,
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))

plt.show()

#### Sini- ja kosinikäyrä (tehtävät 2 & 3)

pii = np.pi

# X-arvot välillä -3π, 3π
X = np.linspace(-3 * pii, 3 * pii)
C, S = np.cos(X), np.sin(X)

# Kolminkertainen leveys
plt.figure(figsize=(19.2, 4.8))

# Piirretään käyrät eri väreillä ja tyyleillä
plt.plot(X, C, color='navy', linestyle='-.', linewidth=2, label='cos(x)')
plt.plot(X, S, color='red', linestyle=':', linewidth=2, label='sin(x)')

# Akselien merkinnät (π, 2π jne.)
plt.xticks(
    [-3 * pii, -2 * pii, -pii, 0, pii, 2 * pii, 3 * pii],
    [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$']
)
plt.yticks(
    [-pii / 2, -pii / 4, 0, pii / 4, pii / 2],
    [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$', r'$\frac{\pi}{2}$', r'$\pi$']
)

# Akselien otsikot ja selite
plt.xlabel('x (radiaaneina)')
plt.ylabel('y')
plt.title('Sini and cosini väliltä -π, π')
plt.legend()

# Ruudukko näkyviin
plt.grid(True, linestyle=':')

plt.show()
