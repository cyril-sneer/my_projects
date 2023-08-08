import matplotlib.pyplot as plt

DATA_FILE_NAME = r'data\1994_Weekly_Gas_Averages.txt'

data_file = open(DATA_FILE_NAME, 'r')
gas_prices = [float(price.rstrip()) for price in data_file.readlines()]
data_file.close()
weeks = list(range(1, 53))

plt.plot(weeks, gas_prices, color = 'r')        # построить график
plt.bar(weeks, gas_prices)                      # построить гистограмму

plt.title('График цен на бензин')
plt.xlabel('Неделя года')
plt.ylabel("Цена, $/л")
delta = max(gas_prices) - min(gas_prices)
plt.ylim(min(gas_prices)-delta*0.1, max(gas_prices)+delta*0.1)

plt.show()
