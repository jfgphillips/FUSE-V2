from MineIO.underground import *
from calculators import machine_output
import pandas as pd
from calculators import taylorsLaw as tL
import pprint


class roomAndPillarMethod:
    def __init__(self):
        self.df = pd.read_excel(
            r"/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx",
            sheet_name="r & p method", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.initiate_mining_package = {"continuous miner": self.df['value'].loc['continuous miner'],
                                        "LHD": self.df['value'].loc['LHD'],
                                        "roof bolter": self.df['value'].loc['roof bolter'],
                                        "shuttle car": self.df['value'].loc['shuttle car'],
                                        "worker": self.df['value'].loc['worker']}
        self.continuous_miner = continuousMiner.continuousMiner_att()
        self.roof_bolter = roofBolter.roofBolter_att()
        self.shuttle_car = shuttleCar.shuttleCar_att()
        self.worker = worker.worker_att()
        self.LHD = LHD.LHD_att()
        self.utility = utility.utility_att()
        self.mine = mineAttributes.mine_att()
        self.usage_factor = self.mine.mining_usage

        self.operating_per_week = self.mine.mining_operating / 2.173  # hours per week conversion
        self.required_tonnes_per_year = tL.taylors_law(self.mine.expected_reserves, self.mine.mining_operating)
        #print(self.required_tonnes_per_year)
        self.required_output = machine_output.machine_output_calc(self.required_tonnes_per_year,
                                                                  self.mine.mining_packages,
                                                                  self.mine.conversion_efficiency,
                                                                  self.mine.ore_grade,
                                                                  self.operating_per_week)
        self.maintenance = self.mine.maintenance_usage
        self.units = 365  # year
        self.shuttle_load = 10  # tonnes
        self.LHD_load = 5  # tonnes
        self.emissions_df, self.total_emissions_df = self.package_emissions()
        self.opex_df, self.total_opex_df = self.opex()
        self.p_method()
        # print(self.emissions/self.required_tonnes_per_year * 365, "kWhrs/tonne")
        # print(self.opex, "£/year")
        return

    def p_method(self):
        total_emissions = self.total_emissions_df['sum'].loc['room and pillar method']
        total_opex = self.total_opex_df['sum'].loc['room and pillar method']
        print_emissions = f"the total emissions for a mine producing {self.required_tonnes_per_year} TPY in kWhrs is: {total_emissions}\n" \
                          f"this was performed by {self.mine.mining_packages} mining packages\n" \
                          f"a mining package has an output of: {self.required_output} TPH consisted of: \n" \
                          f"{pprint.pformat(self.initiate_mining_package)} \n" \
                          f"The emissions per tonne of soda ash produced was: {total_emissions / self.required_tonnes_per_year * 365} kWhrs"

        print_opex = f"The total operating expenses for this mine was: £{total_opex} \n" \
                     f"The cost per tonne of soda ash was: £{total_opex / self.required_tonnes_per_year * 365}"
        print(print_emissions)
        print(print_opex)
        return

    def package_emissions(self):
        """
        takes the initiate_mining_package dictionary and the qMachines of each machine to calculate emissions
        :return: a data frame containing the total emissions of the mine catagorised into 3 titles
        """

        continuous_miner_emissions = continuousMiner.qMachine(self.continuous_miner.power,
                                                              self.required_output,
                                                              self.continuous_miner.production_output,
                                                              self.usage_factor,
                                                              self.units) * self.initiate_mining_package[
                                         'continuous miner']
        roof_bolter_emissions = roofBolter.qMachine(self.roof_bolter.power,
                                                    self.usage_factor,
                                                    self.units) * self.initiate_mining_package['roof bolter']
        shuttle_car_emissions = shuttleCar.qMachine(self.shuttle_car.power,
                                                    self.shuttle_load,
                                                    self.shuttle_car.nameplate_rating,
                                                    self.usage_factor,
                                                    self.units) * self.initiate_mining_package['shuttle car']
        LHD_emissions = LHD.qMachine(self.LHD.power,
                                     self.LHD_load,
                                     self.LHD.nameplate_rating,
                                     self.usage_factor,
                                     self.units) * self.initiate_mining_package['LHD']

        emissions_df = pd.DataFrame(data={"miner_emissions": [continuous_miner_emissions],
                                          "support_emissions": [roof_bolter_emissions + LHD_emissions],
                                          'transportation_emissions': [shuttle_car_emissions]},
                                    index=['room and pillar method'])
        emissions_df['sum'] = emissions_df.sum(axis=1)
        total_emissions_df = emissions_df.mul(self.mine.mining_packages)
        # print(total_emissions_df)
        return emissions_df, total_emissions_df

    def opex(self):
        """
        this method works out a labour cost by multiplying wage by the total hours worked
        :return: two data frames one for a single mining package and the other for the whole mine
        """
        labour_costs = self.worker.wage * self.initiate_mining_package['worker'] # TODO: find out the factor for working hours
        utility_costs = self.utility.electricity * self.emissions_df['sum'].loc['room and pillar method']
        opex_df = pd.DataFrame(data={"labour_costs": [labour_costs],
                                     "utility_costs": [utility_costs]},
                               index=['room and pillar method'])
        opex_df['sum'] = opex_df.sum(axis=1)
        total_opex_df = opex_df.mul(self.mine.mining_packages)
        return opex_df, total_opex_df


if __name__ == '__main__':
    test = roomAndPillarMethod()
