import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 178662273 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #print("Дайте пожалуйста еще неделю на решение задачи!")
    alpha = 1 - p
    #loc = x.mean()
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    #return x.mean() + np.sqrt(40*np.var(x)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)), \
    #       x.mean() + np.sqrt(40*np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x))
    return (1-alpha)/np.sqrt(40)
