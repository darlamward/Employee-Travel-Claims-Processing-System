
import matplotlib.pyplot as plt
M = 0
Month_arr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
TotalSales_arr = []

while M <= 11:
    TotalSales_arr.append(float(input(f"Enter total sales for {Month_arr[M]}: ")))
    M += 1

plt.plot(Month_arr, TotalSales_arr, color='magenta')

plt.xlabel("Month")
plt.ylabel("Total sales per month($)")

plt.title("Monthly Claim Totals")
plt.grid(True)

plt.show()

