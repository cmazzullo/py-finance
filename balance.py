import pandas as pd
import matplotlib.pyplot as plt

save = pd.read_csv('CapitalOne_Transactions_8679.csv')
check = pd.read_csv('CapitalOne_Transactions_9218.csv')

def get_series(d):
    d['Date'] = pd.to_datetime(d['Date'])
    d = d.set_index('Date')
    d['Balance'] = d['Balance'].str.replace('$', '').astype(float)
    return d


s1 = get_series(save)
s2 = get_series(check)

# d.plot()
# plt.grid()
# plt.ylim(0, 35000)
# plt.show()
