import numpy as np

print("\ntehtävä 1.1")
a, b = 2.493, 0.911

print(np.degrees(a))
print(np.degrees(b))

print("\ntehtävä 1.2")
a, b = 137.7, 62.3

print(np.radians(a))
print(np.radians(b))

print("\ntehtävä 1.3")
A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

print("astetta", "radiaania")
for i in A:
  print('{0: <7}'.format(i), np.radians(i))


print("\ntehtävä 2.1")
a, b = 1.6, 2.3
hypot = np.hypot(a, b)
print(f"Kateettien ollessa {a} metriä ja {b} metriä hypotenuusan pituus on {hypot:.1f} metriä.")
