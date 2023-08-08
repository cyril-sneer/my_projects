NUM_SHARES = 2000           # количество акций
PURCHASE_PRICE = 40.0       # цена покупки за 1 акцию
SELLING_PRICE = 42.75       # цена продажи за 1 акцию
COMMISSION_RATE = 0.03      # комиссионные брокеру %

purchase_sum = PURCHASE_PRICE * NUM_SHARES
purchase_comm = purchase_sum * COMMISSION_RATE

selling_sum = SELLING_PRICE * NUM_SHARES
selling_comm = selling_sum * COMMISSION_RATE

profit = selling_sum - selling_comm - purchase_sum - purchase_comm

print(f'При покупке за акции было уплачено: {purchase_sum:.2f} $')
print(f'Комиссионные брокеру при покупке: {purchase_comm:.2f} $')
print(f'При продаже за акции было выручено: {selling_sum:.2f} $')
print(f'Комиссионные брокеру при продаже: {selling_comm:.2f} $')
print(f'Доход составил: {profit:.2f} $')
