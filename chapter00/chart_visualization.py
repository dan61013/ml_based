import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def sampleCase01():
    ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.show()
    
# plt.close("all")

if __name__ == "__main__":
    sampleCase01()