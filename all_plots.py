import pandas as pd
import matplotlib.pyplot as plt
import time


df = pd.read_excel('Prueba_1.xlsx')

time = df.iloc[:, 0]

relaxed_hand = df.iloc[:, 1]
fist = df.iloc[:, 2]

wrist_extension = df.iloc[:, 4]
radius_deviation = df.iloc[:, 5]


ulnar_deviation = df.iloc[:, 8]

y_data = [relaxed_hand, fist, wrist_extension, radius_deviation, ulnar_deviation]

plot_titles = ['Relaxed Hand', 'Fist', 'Wrist Extension', 'Radius Deviation', 'Ulnar Deviation']
plt.figure(figsize=(8, 6))
for i, data in enumerate(y_data[:3], start=1):
    plt.subplot(3, 1, i)
    plt.plot(time, data)
    plt.title(f'Time vs {plot_titles[i-1]}')
    plt.xlabel('Time')
    plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()

time.sleep(2)

plt.figure(figsize=(8, 6))
for i, data in enumerate(y_data[3:], start=1):
    plt.subplot(3, 1, i)
    plt.plot(time, data)
    plt.title(f'Time vs {plot_titles[i+2]}')
    plt.xlabel('Time')
    plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()
