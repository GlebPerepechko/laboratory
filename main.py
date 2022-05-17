'''
laboratory 1
'''
import pandas as pd
import matplotlib.pyplot as plot

ted = pd.read_csv("TED Talks.csv")
ted["like %"] = ted["likes"] * 100 / ted["views"]
sort_tedv = ted.sort_values(by=["views", "like %"], ascending=False).head(10)
sort_tedl = ted.sort_values(by=["like %", "views"], ascending=False).head(10)

sort_tedv.plot(x='author', y='views', kind='bar')
plot.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
print(sort_tedv[["views", "like %"]])

sort_tedl.plot(x='author', y='like %', kind='bar')
print(sort_tedl[["views", "like %"]])
plot.show()
