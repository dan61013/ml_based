import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def sampleCase01():
    """
    使用Series資料，產生基本的curve chart
    """
    ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()

def sampleCase02():
    """
    使用DataFrame資料，產生帶有labels的curve chart
    """
    df = pd.DataFrame(np.random.randn(1000, 4),
                      index=pd.date_range('1/1/2000', periods=1000),
                      columns=list('ABCD'))
    df = df.cumsum()
    # plt.figure()
    # df.plot()
    plt.figure()
    df.iloc[5].plot(kind='bar')

def sampleCase03():
    """
    使用plot(x, y)繪製對比圖
    """
    df = pd.DataFrame(np.random.randn(1000, 2), columns=['B', 'C']).cumsum()
    df['A'] = pd.Series(list(range(len(df))))
    df.plot(x='A', y='B')

def sampleCase04():
    """
    Bar plots
    """
    df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    df.plot.bar()

# plt.close("all")

if __name__ == "__main__":
    # sampleCase01()
    # sampleCase02()
    # sampleCase03()
    sampleCase04()
    
    plt.show()