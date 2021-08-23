import matplotlib.pyplot as plt
from undergroundMining.roomAndPillarMethod import roomAndPillarMethod as rpm
import pandas as pd


class plot:
    def __init__(self):
        self.all_data = rpm()
        self.emissions_data = self.all_data.total_emissions_df.div(self.all_data.required_tonnes_per_year).mul(365)
        self.longwall_df = pd.DataFrame(data={"miner_emissions": [149],
                                                 "support_emissions": [8],
                                                 'transportation_emissions': [21]},
                                           index=['longwall method'])
        self.emissions_data_2 = pd.concat([self.emissions_data, self.longwall_df])
        self.emissions_boxplot()
        return

    def emissions_boxplot(self):
        fields = ['miner_emissions', 'support_emissions', 'transportation_emissions']
        colours = ['#88CCEE', '#CC6677', '#DDCC77']
        labels = ['miner', 'support', 'transportation']

        myplot = self.emissions_data_2.plot(use_index=True,
                                          kind="bar",
                                          stacked=True,
                                          color=colours, y=fields)
        myplot.set_ylabel("Emissions (kWhr/tonne)")
        plt.title("Mining technique")
        plt.xticks(rotation=0)
        plt.legend().remove()
        #plt.legend(loc=0)
        plt.show()
        return

        # print(plt.bar(self.emissions_data.index))

        # for idx, name in enumerate(fields):


if __name__ == '__main__':
    test = plot()

