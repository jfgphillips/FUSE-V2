import matplotlib.pyplot as plt
from undergroundMining.roomAndPillarMethod import roomAndPillarMethod as rpm
from undergroundMining.longwallMethod import longwallMethod as lwm
import pandas as pd


class plot:
    def __init__(self):
        self.rpm_data = rpm()
        self.lwm_data = lwm()

        self.emissions_data = pd.concat([self.rpm_data.total_emissions_df, self.lwm_data.total_emissions_df], axis=0)
        self.standardised_emissions_data = self.emissions_data.div(self.rpm_data.required_tonnes_per_year).mul(365)

        self.opex_data = pd.concat([self.rpm_data.opex_df, self.lwm_data.opex_df], axis=0)
        self.standardised_opex_data = self.opex_data

        self.capex_data = pd.concat([self.rpm_data.capex_df, self.lwm_data.capex_df], axis=0)
        self.standardised_capex_data = self.capex_data

        self.emissions_boxplot()
        self.opex_boxplot()
        self.capex_boxplot()
        return

    def capex_boxplot(self):
        fields = [c for c in self.standardised_capex_data.columns if c not in 'total capex']
        # colours = ['#88CCEE', '#CC6677']
        # labels = ['labour', 'utility']

        myplot = self.standardised_capex_data.plot(use_index=True,
                                                  kind="bar",
                                                  stacked=True,
                                                  y=fields)
        myplot.set_ylabel("capex ($)")
        plt.title("Mining technique")
        plt.xticks(rotation=0)
        # plt.legend().remove()
        # plt.legend(labels)
        plt.show()
        return


    def emissions_boxplot(self):
        fields = [c for c in self.standardised_emissions_data.columns if c not in 'sum']
        colours = ['#88CCEE', '#CC6677', '#DDCC77']
        labels = ['miner', 'support', 'transportation']

        myplot = self.standardised_emissions_data.plot(use_index=True,
                                                       kind="bar",
                                                       stacked=True,
                                                       color=colours, y=fields)
        myplot.set_ylabel("Emissions (kWhr/tonne)")
        plt.title("Mining technique")
        plt.xticks(rotation=0)
        #plt.legend().remove()
        plt.legend(labels)
        plt.show()
        return

    def opex_boxplot(self):
        fields = [c for c in self.standardised_opex_data.columns if c not in 'total opex']
        # colours = ['#88CCEE', '#CC6677']
        # labels = ['labour', 'utility']

        myplot = self.standardised_opex_data.plot(use_index=True,
                                                  kind="bar",
                                                  stacked=True,
                                                  y=fields)
        myplot.set_ylabel("opex ($/tonne)")
        plt.title("Mining technique")
        plt.xticks(rotation=0)
        #plt.legend().remove()
        #plt.legend(labels)
        plt.show()
        return

        # print(plt.bar(self.emissions_data.index))

        # for idx, name in enumerate(fields):


if __name__ == '__main__':
    test = plot()
    print(test.emissions_data)
