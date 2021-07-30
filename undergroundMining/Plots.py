import matplotlib.pyplot as plt
from undergroundMining.roomAndPillarMethod import roomAndPillarMethod as rpm


class plot:
    def __init__(self):
        self.all_data = rpm()
        self.emissions_data = self.all_data.total_emissions_df
        #print(self.emissions_data)
        #print(self.emissions_data.index)
        #print(self.emissions_data.columns)
        self.emissions_boxplot()

    def emissions_boxplot(self):
        fields = ['miner_emissions', 'support_emissions', 'transportation_emissions']
        colours = ['#88CCEE', '#CC6677', '#DDCC77']
        labels = ['miner', 'support', 'transportation']

        myplot = self.emissions_data.plot(use_index=True,
                                          kind="bar",
                                          stacked=True,
                                          color=colours, y=fields)
        myplot.set_ylabel("Emissions (kWhr/year)")
        plt.title("Mining technique")
        plt.xticks(rotation=0)
        plt.legend(loc=0)
        plt.show()

        # print(plt.bar(self.emissions_data.index))

        # for idx, name in enumerate(fields):


if __name__ == '__main__':
    test = plot()
