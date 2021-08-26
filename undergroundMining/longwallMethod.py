from MineIO.longwallEquipment import *
from MineIO import *
from calculators import machine_output
from calculators import taylorsLaw as tL
import pandas as pd
import pprint


class longwallMethod:
    def __init__(self):
        self.df = pd.read_excel(r"../data/mine_attributes.xlsx", sheet_name="longwall method", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.initiate_mining_package = {"longwall shearer": self.df['value'].loc['longwall shearer'],
                                        "t shield": self.df['value'].loc['t shield'],
                                        "afc": self.df['value'].loc['afc'],
                                        "flat link chain": self.df['value'].loc['flat link chain'],
                                        "low profile chain": self.df['value'].loc['low profile chain'],
                                        "afc drive": self.df['value'].loc['afc drive'],
                                        "stage loader": self.df['value'].loc['stage loader'],
                                        "borer miner": self.df['value'].loc['borer miner'],
                                        "shuttle car": self.df['value'].loc['shuttle car'],
                                        "worker": self.df['value'].loc['worker']}
        self.mining_packages = self.df['value'].loc['mining packages']
        self.longwallShearer = longwallSheerer.longwallShearer_att()
        self.borerMiner = borerMiner.borerMiner_att()
        self.shuttle_car = shuttleCar.shuttleCar_att()
        self.worker = worker.worker_att()
        self.stageLoader = stageLoader.stageLoader_att()
        self.afc_drive = miscSupportEqmt.afc_att()
        self.mine = mineAttributes.mine_att()
        self.utility = utility.utility_att()

        self.usage_factor = self.mine.mining_usage
        self.operating_per_week = self.mine.mining_operating / 2.173  # hours per week conversion
        self.required_tonnes_per_year = tL.taylors_law(self.mine.expected_reserves, self.mine.mining_operating)
        # print(self.required_tonnes_per_year)
        req_out_kwargs = {"required_tpy": self.required_tonnes_per_year,
                          "mining_package": self.mining_packages,
                          "conversion_efficiency": self.mine.conversion_efficiency,
                          "ore_grade": self.mine.ore_grade,
                          "production_hrs_wk": self.operating_per_week}
        self.required_output = machine_output.machine_output_calc(**req_out_kwargs)
        self.maintenance = self.mine.maintenance_usage
        self.units = 365  # year
        self.shuttle_load = 10  # tonnes
        # self.LHD_load = 5  # tonnes
        self.emissions_df, self.total_emissions_df = self.package_emissions()
        self.opex_df, self.total_opex_df = self.opex()
        return

    def __repr__(self):
        total_emissions = self.total_emissions_df['sum'].loc['longwall method']
        total_opex = self.total_opex_df['sum'].loc['longwall method']
        print_emissions = f"the total emissions for a mine producing {self.required_tonnes_per_year} TPY in kWhrs is: {total_emissions}\n" \
                          f"this was performed by {self.mining_packages} mining packages\n" \
                          f"a mining package has an output of: {self.required_output} TPH consisted of: \n" \
                          f"{pprint.pformat(self.initiate_mining_package)} \n" \
                          f"The emissions per tonne of soda ash produced was: {total_emissions / self.required_tonnes_per_year * 365} kWhrs"

        print_opex = f"The total operating expenses for this mine was: £{total_opex} \n" \
                     f"The cost per tonne of soda ash was: £{total_opex / self.required_tonnes_per_year * 365}"

        output = f"{print_emissions}\n\n" \
                 f"{print_opex}"
        return output

    def package_emissions(self):
        """
        takes the initiate_mining_package dictionary and the qMachines of each machine to calculate emissions
        :return: a data frame containing the total emissions of the mine catagorised into 3 titles
        """

        longwallShearer_emissions = longwallSheerer.qMachine(self.longwallShearer.power,
                                                             self.required_output,
                                                             self.longwallShearer.production_output,
                                                             self.usage_factor,
                                                             self.units) * self.initiate_mining_package[
                                        'longwall shearer']
        # face_emissions = longwallShearer_emissions + stageLoader
        borerMiner_emissions = borerMiner.qMachine(self.borerMiner.power,
                                                   self.usage_factor,
                                                   self.units) * self.initiate_mining_package['borer miner']
        shuttle_car_emissions = shuttleCar.qMachine(self.shuttle_car.power,
                                                    self.shuttle_load,
                                                    self.shuttle_car.nameplate_rating,
                                                    self.usage_factor,
                                                    self.units) * self.initiate_mining_package['shuttle car']
        # TODO: check the validity of this
        afc_emissions = miscSupportEqmt.afc_att.qMachine(0, self.afc_drive.drive_power,
                                                         self.usage_factor,
                                                         self.units) * self.initiate_mining_package['afc drive']

        stageLoader_emissions = stageLoader.qMachine(self.stageLoader.power,
                                                     self.required_output,
                                                     self.stageLoader.max_output,
                                                     self.usage_factor,
                                                     self.units) * self.initiate_mining_package["stage loader"]

        emissions_df = pd.DataFrame(data={"miner_emissions": [longwallShearer_emissions],
                                          "support_emissions": [borerMiner_emissions],
                                          'transportation_emissions': [stageLoader_emissions +
                                                                       afc_emissions +
                                                                       shuttle_car_emissions]},
                                    index=['longwall method'])
        emissions_df['sum'] = emissions_df.sum(axis=1)
        total_emissions_df = emissions_df.mul(self.mining_packages)
        # print(total_emissions_df)
        return emissions_df, total_emissions_df

    def opex(self):
        """
        this method works out a labour cost by multiplying wage by the total hours worked
        also works out utility cost by multiplying electricity
        :return: two data frames one for a single mining package and the other for the whole mine
        """
        labour_costs = self.worker.wage * self.initiate_mining_package[
            'worker']  # TODO: find out the factor for working hours
        utility_costs = self.utility.electricity * self.emissions_df['sum'].loc['longwall method']
        opex_df = pd.DataFrame(data={"labour_costs": [labour_costs],
                                     "utility_costs": [utility_costs]},
                               index=['longwall method'])
        opex_df['sum'] = opex_df.sum(axis=1)
        total_opex_df = opex_df.mul(self.mining_packages)
        return opex_df, total_opex_df


if __name__ == '__main__':
    test = longwallMethod()
    print(test)