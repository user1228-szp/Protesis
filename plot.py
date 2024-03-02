import pandas as pd
import matplotlib.pyplot as plt
import time

df = pd.read_excel('Prueba_1.xlsx')

time = df.iloc[:, 0]

relaxed_hand = df.iloc[:, 1]

print(time)

plt.plot(time, relaxed_hand)

plt.xlabel('time')
plt.ylabel('relaxed_hand')
plt.title('time VS relaxed_hand')

plt.show()
