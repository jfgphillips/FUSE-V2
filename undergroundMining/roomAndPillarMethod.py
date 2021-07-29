from MineIO.underground import *
from calculators import machine_output
import pandas as pd
from calculators import taylorsLaw as tL


class roomAndPillarMethod:
    def __init__(self):
        self.df = pd.read_excel(r"/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx", sheet_name = "r & p method", skiprows=1)
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
        print(self.required_tonnes_per_year)
        self.required_output = machine_output.machine_output_calc(self.required_tonnes_per_year,
                                                                  self.mine.mining_packages,
                                                                  self.mine.conversion_efficiency,
                                                                  self.mine.ore_grade,
                                                                  self.operating_per_week)
        self.tonnes_per_year = self.required_tonnes_per_year
        self.no_of_mining_packages = self.mine.mining_packages

        self.maintenance = self.mine.maintenance_usage
        self.units = 365 # year
        self.shuttle_load = 10  # tonnes
        self.LHD_load = 5  # tonnes
        self.emissions = self.package_emissions() * self.mine.mining_packages
        self.opex = self.opex() * self.mine.mining_packages
        print(self.emissions, " kWhrs/year")
        print(self.emissions/self.required_tonnes_per_year * 365, "kWhrs/tonne")
        print(self.opex, "£/year")
        return



    def package_emissions(self):
        """
        takes the initiate_mining_package dictionary and the qMachines of each machine to calculate emissions
        :return: a value for mining emissions based on the package data in kWhrs per year
        """
        mining_emissions = \
            continuousMiner.qMachine(self.continuous_miner.power, self.required_output, self.continuous_miner.production_output, self.usage_factor, self.units) * self.initiate_mining_package['continuous miner'] + \
            roofBolter.qMachine(self.roof_bolter.power, self.usage_factor, self.units) * self.initiate_mining_package['roof bolter'] + \
            shuttleCar.qMachine(self.shuttle_car.power, self.shuttle_load, self.shuttle_car.nameplate_rating, self.usage_factor, self.units) * self.initiate_mining_package['shuttle car'] + \
            LHD.qMachine(self.LHD.power, self.LHD_load, self.LHD.nameplate_rating, self.usage_factor, self.units) * self.initiate_mining_package['LHD']

        return mining_emissions

    def opex(self):
        labour_costs = self.worker.wage * self.usage_factor * self.initiate_mining_package['worker']
        utility_costs = self.utility.electricity * self.package_emissions()
        package_opex = labour_costs + utility_costs
        return package_opex



if __name__ == '__main__':
    test = roomAndPillarMethod()

