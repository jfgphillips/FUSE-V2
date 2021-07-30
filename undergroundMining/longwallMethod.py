from MineIO.underground import *
from calculators import machine_output
import pandas as pd

class longwallMethod:
    def __init__(self, req_tonnes_per_year, no_of_mining_packages):
        self.df = pd.read_excel(r"/Users/john/Documents/University Work/summer internship/FUSE/data/mine_attributes.xlsx", sheet_name = "longwall method", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.initiate_mining_package = {"longwall shearer": self.df['value'].loc['longwall shearer'],
                                        "t shield": self.df['value'].loc['t shield'],
                                        "afc": self.df['value'].loc['afc'],
                                        "flat link chain": self.df['value'].loc['flat link chain'],
                                        "low profile chain": self.df['value'].loc['low profile chain'],
                                        "afc drive": self.df['value'].loc['afc drive'],
                                        "stage loader": self.df['value'].loc['stage loader'],
                                        "borer miner": self.df['value'].loc['borer miner'],
                                        "shuttle car": self.df['value'].loc['shuttle car']}
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
        self.units = 365
        self.shuttle_load = 10  # tonnes
        self.LHD_load = 5  # tonnes
        self.emissions = self.package_emissions() * no_of_mining_packages
        print(self.emissions, " kWhrs/year")
        print(self.emissions/req_tonnes_per_year, "kWhrs/tonne/year")
        return


