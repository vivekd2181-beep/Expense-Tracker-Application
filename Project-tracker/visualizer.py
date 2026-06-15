# visualizer.py
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from database import get_price_history

def plot_price_history(product_name):
    rows = get_price_history(product_name)
    if len(rows) < 2:
        print(f"[GRAPH] Not enough data for {product_name}")
        return

    prices = [row[0] for row in rows]
    timestamps = [datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S") for row in rows]

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, prices, marker="o", color="#e67e22", linewidth=2, markersize=5)
    plt.fill_between(timestamps, prices, alpha=0.1, color="#e67e22")

    plt.title(f"Price History: {product_name}", fontsize=14, fontweight="bold")
    plt.xlabel("Date & Time")
    plt.ylabel("Price (₹)")
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%d-%b %H:%M"))
    plt.gcf().autofmt_xdate()
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()

    filename = f"{product_name.replace(' ', '_')}_price_history.png"
    plt.savefig(filename)
    plt.show()
    print(f"[GRAPH] Saved as {filename}")

def plot_all_products(product_names):
    for name in product_names:
        plot_price_history(name)