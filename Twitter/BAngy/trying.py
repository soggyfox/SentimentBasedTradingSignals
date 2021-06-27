# From https://medium.com/free-code-camp/how-machines-make-predictions-finding-correlations-in-complex-data-dfd9f0d87889
import math


def mean(x):
    return sum(x) / len(x)


def pepe(x, y):
    cov = covariance(x, y)
    return cov / (stDev(x) * stDev(y))


def covariance(dwd, dwddw):
    calc = []
    for i in range(len(dwd)):
        xi = dwd[i] - mean(dwd)
        yi = dwddw[i] - mean(dwddw)
        calc.append(xi * yi)
    return sum(calc) / (len(dwd) - 1)

x = list(df["Bitcoin Price"])
y = list(df["Market Sentiment Twiter"])


# print(covariance(a,b))

def stDev(x):
    variance = 0
    for i in x:
        variance += (i - mean(x) ** 2) / len(x)
    return math.sqrt(variance)


def P2(x, y):
    cov = covariance(x, y)
    return cov / (stDev(x) * stDev(y))


P2(x, y)
