import matplotlib.pyplot as plt
import pandas as pd
from math import floor, ceil

# TODO: wszystkie rzeczy na wykresach mają być automatyczne, nic nie ma być ustawiane ręcznie
# TODO: linie siatki (wartość max i min odpowiednio przeskalowane), punkty, oś x (np pierwszy ostatni dzień miesiąca)
# TODO: co się da to ma być zautomatyzowane

dane = pd.read_csv('dane.csv', sep = ';', decimal = ',', index_col=0)
dane['Sprzedaz całkowita'] = dane['prodA'] + dane['prodB']
sprzedaz = dane.drop(['prodA', 'prodB'], axis = 1)

sprzedaz['mies_cat'] = pd.Categorical(sprzedaz.Miesiac,
                      categories=["styczen","luty","marzec"],
                      ordered=True)

sprzedaz.sort_values(['mies_cat', 'dzien'], inplace = True, ignore_index = True)

s_min = floor(sprzedaz['Sprzedaz całkowita'].min())
s_max = ceil(sprzedaz['Sprzedaz całkowita'].max())
s_half = s_min + (s_max + s_min) // 2
s_scale = [s_min, s_min + 2, s_half, s_max - 2, s_max]
s_description = [f'{t}k' for t in s_scale]

fig, ax = plt.subplots(figsize = (15, 5))
# plt.plot(sprzedaz['Sprzedaz całkowita'])
sprzedaz['Sprzedaz całkowita'].plot(xlabel='Dzień',
                                    ylabel='Sprzedaż w tyś',
                                    title='Sprzedaż całkowita w kolejnych dniach kwartału 1',
                                    ylim=(s_scale[0], s_scale[-1]))

plt.xticks([0, 30, 31,58,59,89], [1, 31, 1, 28, 1, 31])
plt.yticks(s_scale, s_description)
# ax.axhline(s_scale[1], linestyle = '--')
plt.axhline(s_scale[1], linestyle = '--')
# plt.grid(axis='y', linestyle='--', alpha=1)
plt.show()