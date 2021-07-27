from MineIO.underground import *
from calculators import machine_output
import pandas as pd

class roomAndPillarMethod:
    def __init__(self, req_tonnes_per_year, no_of_mining_packages):
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
        self.mine = mineAttributes.mine_att()
        self.required_output = machine_output.machine_output_calc(req_tonnes_per_year, no_of_mining_packages)
        self.tonnes_per_year = req_tonnes_per_year
        self.no_of_mining_packages = no_of_mining_packages
        self.usage = self.mine.mining_usage
        self.maintenance = self.mine.maintenance_usage
        self.units = 365 # year
        self.shuttle_load = 10  # tonnes
        self.LHD_load = 5  # tonnes
        self.emissions = self.package_emissions() * no_of_mining_packages
        print(self.emissions, " kWhrs/year")
        print(self.emissions/req_tonnes_per_year, "kWhrs/tonne/year")
        return



    def package_emissions(self):
        """
        takes the initiate_mining_package dictionary and the qMachines of each machine to calculate emissions
        :return: a value for mining emissions based on the package data
        """
        mining_emissions = continuousMiner.qMachine(self.continuous_miner.power, self.required_output, self.continuous_miner.production_output, self.usage, self.units) * self.initiate_mining_package['continuous miner'] + \
            roofBolter.qMachine(self.roof_bolter.power, self.usage, self.units) * self.initiate_mining_package['roof bolter'] + \
            shuttleCar.qMachine(self.shuttle_car.power, self.shuttle_load, self.shuttle_car.nameplate_rating, self.usage, self.units) * self.initiate_mining_package['shuttle car'] + \
            LHD.qMachine(self.LHD.power, self.LHD_load, self.LHD.nameplate_rating, self.usage, self.units) * self.initiate_mining_package['LHD']

        return mining_emissions


if __name__ == '__main__':
    test = roomAndPillarMethod(10000000, 10)

