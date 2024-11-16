#muestra las graficas de un mismo excel, por columna

import pandas as pd
import matplotlib.pyplot as plt
import time

df = pd.read_excel('Prueba_1.xlsx')

time_data = df.iloc[:, 0]  

unmarked_data = df.iloc[:, 1]
hand_at_rest = df.iloc[:, 2]
hand_clenched_in_fist = df.iloc[:, 3]
wrist_flexion = df.iloc[:, 4]
wrist_extension = df.iloc[:, 5]
radial_deviations = df.iloc[:, 6]
ulnar_deviations = df.iloc[:, 7]
extended_palm = df.iloc[:, 8]

y_data = [unmarked_data, hand_at_rest, wrist_extension, radial_deviations, ulnar_deviations] 
plot_titles = ['Relaxed Hand', 'Fist', 'Wrist Extension', 'Radial Deviation', 'Ulnar Deviation'] 
plt.figure(figsize=(8, 6))
for i, data in enumerate(y_data[:4], start=1):
    plt.subplot(3, 1, i)
    plt.plot(time_data, data) 
    plt.title(f'Time vs {plot_titles[i-1]}')
    plt.xlabel('Time')
    plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()

time.sleep(2)

plt.figure(figsize=(8, 6))
for i, data in enumerate(y_data[4:], start=1):
    plt.subplot(3, 1, i)
    plt.plot(time_data, data)
    plt.title(f'Time vs {plot_titles[i+2]}')
    plt.xlabel('Time')
    plt.ylabel('Y-axis')

plt.tight_layout()
plt.show()
