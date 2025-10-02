import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/dataset/traffici.csv')
x = np.arange(len(df["Months"]))
width = 0.25
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, df["Searches"], width, label="Searches", color="dodgerblue")
rects2 = ax.bar(x, df["Direct"], width, label="Direct", color="palevioletred")
rects3 = ax.bar(x + width, df["Social Media"], width, label="Social Media", color="gold")
ax.set_ylabel("visitors\nin thousands", fontsize=12)
ax.set_xlabel("Months", fontsize=12)
ax.set_title("Visitors by web traffic sources", fontsize=14, weight="bold")
ax.set_xticks(x)
ax.set_xticklabels(df["Months"])
ax.legend()
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

ax.yaxis.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
