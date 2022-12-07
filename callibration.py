import matplotlib.pyplot as plt
import  matplotlib.ticker as ticker
import lightFunctions as j
import numpy as np
mc, l = j.readIntensity("white-mercury_.png", "plot-white-mercury", "Ртутная лампа", "Белый лист")
x = np.array(j.callibration(mc))
y = np.array([578, 546, 435, 491])
N = len(x)
mx = x.sum() / N
my = y.sum() / N
a2 = np.dot(x.T, x) / N
a11 = np.dot(x.T, y) / N
kk = (a11 - mx * my) / (a2 - mx ** 2)
bb = my - kk * mx
plt.clf()
fig, ax = plt.subplots(figsize=(9, 7), dpi=500)

# x = x[1:3]
# y = np.array([546, 435])
# print(y)
# print(x)
# k = (y[0]-y[1])/(x[0] - x[1])
# b=y[0] - k * x[0]

#Включаем видимость сетки и делений (вводим их параметры ниже(сверху нельзя)
ax.minorticks_on()

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(25))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(25))

#Устанавливаем параметры подписей делений: https://pyprog.pro/mpl/mpl_axis_ticks.html
ax.tick_params(axis = 'both', which = 'major', labelsize = 15, pad = 2, length = 10)
ax.tick_params(axis = 'both', which = 'minor', labelsize = 15, pad = 2, length = 5)

#название графика с условием для переноса строки и центрированием
ax.set_title('Калибровочный график зависимости длины волны от номера пикселя', fontsize = 16, loc = 'center')

#сетка основная и второстепенная
ax.grid(which='major', color = 'gray')
ax.grid(which='minor', color = 'gray', linestyle = '--')


#подпись осей
ax.set_ylabel("Длина волны [нм]", fontsize = 16)
ax.set_xlabel("Пиксель", fontsize = 16)

#Добавление самого графика и (в конце присваивает наличие леге label =...)
print(kk, bb)
x1 = [0, 100, 300]
y1 = [634.2494413120518, 568.88061, 438.1429]
ax.plot(x1, y1, c ='blue')
#маркеры
ax.scatter(x, y, marker ='.', c ='red', s=350, label='Измерения')
#Добавил маркеры в легенду с надписью измерения

#Добавление легенды: https://pyprog.pro/mpl/mpl_adding_a_legend.html
ax.legend(shadow = False, loc = 'upper right', fontsize = 17)

#Добавление текста  https://pyprog.pro/mpl/mpl_text.html

ax.text(0.95, 0.01, "Уравнение перевода: y = " + str(kk)[:4] + "*x + " + str(bb)[:5],
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='black', fontsize=10)

fig.savefig("Callibration.png")
