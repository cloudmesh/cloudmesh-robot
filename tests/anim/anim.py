import pandas as pd
import matplotlib.pyplot as plt

start_time = 86930.00
end_time = 86934.00
df = pd.read_csv('data.csv', delimiter=',')


fig, ax = plt.subplots(1,1)
plt.ion()
plt.show()

for timestamp in range(int(start_time), int(end_time), 1):
    act_data = df.loc[df['timestamp'] == float(timestamp)]
    X = act_data.x
    Y = act_data.y
    ax.scatter(X, Y)
    plt.pause(1.0)
