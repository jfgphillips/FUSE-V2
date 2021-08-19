from Geothermal_extraction.LDH import Plot as LHD_plt
from undergroundMining import Plots as Na_mining_plt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot(df, title):
    df_sorted = df.sort_values('$ cost')
    plt.figure(figsize=(24, 14))
    my_plot = df_sorted.plot.bar(use_index=True,
                          stacked=True)
    my_plot.set_ylabel("cost")
    plt.title(title)
    plt.xticks(rotation=0,
               fontsize=5)
    plt.legend(loc=0)
    plt.show()

