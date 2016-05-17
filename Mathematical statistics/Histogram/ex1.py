"""
Ссылка на задачу: https://goo.gl/Ztso49

По предложенной выборке постройте гистограмму, используя интервалы
[15, 15.75], (15.75, 16.5], (16.5, 17.25], (17.25, 18.0], (18.0, 18.75], (18.75, 19.5], (19.5, 20.25], (20.25, 21.0]
Найдите относительные частоты попадания элементов выборки в данные интервалы.
Формат ответа: относительные частоты с точностью до третьего знака после запятой через запятую с пробелом
Sample Input: 18.55, 16.5, 18.09, 19.17, 17.09, 18.16, 16.09, 18.79, 17.44, 17.92
Sample Output: 0.000, 0.200, 0.100, 0.200, 0.300, 0.200, 0.000, 0.000
"""

intervals = [(15, 15.75),
             (15.75, 16.5),
             (16.5, 17.25),
             (17.25, 18.0),
             (18.0, 18.75),
             (18.75, 19.5),
             (19.5, 20.25),
             (20.25, 21.0)]
# sample = [18.55, 16.5, 18.09, 19.17, 17.09, 18.16, 16.09, 18.79, 17.44, 17.92]
sample = [15.7, 18.8, 18.62, 17.68, 18.35, 15.67, 17.74, 17.76, 18.54, 17.56, 17.67, 16.61, 16.19, 17.57, 16.64, 17.35,
          16.68, 18.67, 17.85, 16.76, 16.96, 17.33, 16.36, 20.19, 17.77, 16.53, 17.54, 17.89, 17.41, 20.12, 16.68, 18.4,
          18.74, 17.75, 18.97, 18.92, 18.22, 17.58, 18.81, 18.94]
freq = []
for i in range(0, len(intervals)):
    interval = intervals[i]
    freq.append(0)
    for j in range(0, len(sample)):
        first = i == 0 and interval[0] == sample[j];
        other = interval[0] < sample[j] <= interval[1];
        if first or other:
            freq[i] += 1

lst = list(map(lambda x: "%0.3f" % (x / len(sample)), freq))
for el in lst:
    print(el, end=", ")