#___________________МОДУЛЬ_7__УРОВЕНЬ1_НАЧАЛО____________________
from bs4 import BeautifulSoup
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
}

page = requests.get('https://mfd.ru/currency/?currency=USD', headers=header)

soup = BeautifulSoup(page.text, 'html.parser')

exchangeTable = soup.find('table', {'class': 'mfd-table mfd-currency-table'})

exchanges = exchangeTable.find_all('td')

print(*[exchange.text for exchange in exchanges])

# # # ____________Удобочитаемый_вывод_данных_о_курсе_доллара________________
# ex1 = [exchange.text for exchange in exchanges]
# print('      Дата           Курс    Изменение')
# print(*(ex1[i:i + 3] for i in range(0, len(ex1), 3)), sep = "\n")
#___________________МОДУЛЬ_7__УРОВЕНЬ1_КОНЕЦ____________________

#___________________МОДУЛЬ_7__УРОВЕНЬ2_НАЧАЛО___________________
import matplotlib.pyplot as plt
import matplotlib.ticker as tckr

graphData = [exchange.text for exchange in exchanges]

graphData.reverse()

dates =  [item.replace('с ', '') for item in graphData[2::3]]
values = [float(item) for item in graphData[1::3]]
changes = graphData[::3]

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(tckr.FormatStrFormatter('%.4f'))
ax.plot(dates, values)
ax.set_yticks(values)
ax.set_xlabel('Дата')
ax.set_ylabel('Курс USD/RUB')
ax.set_title(f'График изменения курса доллара c {dates[0]} по {dates[len(dates)-1]}')
plt.xticks(rotation=60)

# Отображение изменений курса на графике
def annotate_changes(x, y, changes):
    for i in range(len(x)):
        change = changes[i]
        ax.annotate(f'{change}', (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')

annotate_changes(dates, values, changes)

plt.show()
#___________________МОДУЛЬ_7__УРОВЕНЬ2_КОНЕЦ____________________