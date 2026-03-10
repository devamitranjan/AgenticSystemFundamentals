import pandas as pd
import matplotlib.pyplot as plt

data = {
    "day": [1, 2, 3, 4,5],
    "users": [120, 150, 170, 160, 180],
    "purchases": [30, 35, 40, 38, 45]
}

df = pd.DataFrame(data)


# 0, s, ^, x
plt.plot(df["day"], df["users"], linestyle="--", marker="s", linewidth=3, color="magenta", markerfacecolor="black", label="Users")
plt.plot(df["day"], df["purchases"], linestyle="--", marker="o", linewidth=1, color="green", markerfacecolor="blue", label="Purchases")

plt.grid(True)
plt.legend()

plt.text(3,170, "Peak Day", fontsize=12, fontweight=1, color="red")
plt.show()