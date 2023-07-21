#___________________МОДУЛЬ_7__УРОВЕНЬ1_НАЧАЛО____________________
# from bs4 import BeautifulSoup
# import requests

# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept-Language': 'en-US,en;q=0.9',
# }

# page = requests.get('https://mfd.ru/currency/?currency=USD', headers=header)

# soup = BeautifulSoup(page.text, 'html.parser')

# exchangeTable = soup.find('table', {'class': 'mfd-table mfd-currency-table'})

# exchanges = exchangeTable.find_all('td')

# print(*[exchange.text for exchange in exchanges])

# # # ____________Удобочитаемый_вывод_данных_о_курсе_доллара________________
# ex1 = [exchange.text for exchange in exchanges]
# print('      Дата           Курс    Изменение')
# print(*(ex1[i:i + 3] for i in range(0, len(ex1), 3)), sep = "\n")
#___________________МОДУЛЬ_7__УРОВЕНЬ1_КОНЕЦ____________________

#___________________МОДУЛЬ_7__УРОВЕНЬ2_НАЧАЛО(доп модуль PyQt5)____________________
# import matplotlib
# import matplotlib.pyplot as plt

# matplotlib.use('Qt5Agg')

# print(matplotlib.get_backend())

# plt.plot([2, 1, -4, 7, 12, 13, 25])
# plt.show()
#___________________МОДУЛЬ_7__УРОВЕНЬ2_КОНЕЦ____________________