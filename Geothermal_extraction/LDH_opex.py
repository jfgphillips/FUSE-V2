import pandas as pd
from Geothermal_IO.LDH import *
from Geothermal_extraction import LDH_energy
from Geothermal_extraction import Reactant_flow


class LDH_opex(object):
    def __int__(self):
        self.Costs = Costs.UtilityAndChemicals_att()
        self.chemicals = Sor_Syn_Chemicals.SorbentSynthesisChemicals_att()
        self.washing = Column_Washing.ColumnExtractionWashing()
        self.stripping = Column_Stripping.ColumnExtractionStripping()
        self.carbonate_processing = LC_processing.LiCarbonateProcessing_att()
        self.carbonate_purification = LC_purification.LiCarbonatePurification_att()
        self.energy = LDH_energy.LDH_energy()
        self.water = Water.Water_att()
        self.reactant_flow = Reactant_flow.ReactantFlow()
        self.worker = Worker.worker_att()
        self.plant = Plant.Plant_att()
        self.brine = Brine.Brine_att()
        self.opex_df = self.CostsOpex()
        return

    def __repr__(self):

        total_opex = self.opex_df['sum'].loc['Geothermal_LDH']
        print_opex = f'The total opex to product {self.reactant_flow.LC_purification_product["pure Li2CO3"]} ' \
                     f'kg battery grade lithium carbonate per year from a brine flow of ' \
                     f'{self.plant.brine_flow_day} m^3 per day \nwith a LiCl concentration of ' \
                     f'{self.brine.Li_conc_brine} g/L are: {total_opex} $ \n' \
                     f'The costs per kg of lithium carbonate are: ' \
                     f'{total_opex / self.reactant_flow.LC_purification_product["pure Li2CO3"]} $/kg'

        output = f"{print_opex}"
        return output

    def CostsOpex(self):
        cost_chemicals = self.chemicals.mass_LiOH_H2O * 10 ** (-3) * self.Costs.cost_LiOH_H2O + \
                         self.chemicals.mass_aluminium_hydroxide * 10**(-3) * self.Costs.cost_aluminium_hydroxide +\
                         self.chemicals.mass_HCl * 10 ** (-3) * self.Costs.cost_HCl + \
                         self.reactant_flow.LC_processing_reactants['Na2CO3'] * self.Costs.cost_Na2CO3 + \
                         self.reactant_flow.LC_purification_reactants['CO2'] * self.Costs.cost_CO2_high

        cost_water = self.water.total_water_usage * self.Costs.cost_water

        cost_electricity = self.Costs.cost_electricity * self.energy.energy_df['sum'].loc['Geothermal_LDH']

        cost_operating_labour = self.worker.no_operators * self.worker.annual_wage

        # source: Huang 2021

        cost_operating_supervision = self.worker.supervision * cost_operating_labour

        cost_quality_control = self.worker.quality_control * cost_operating_labour

        opex_df = pd.DataFrame(data={"chemical_costs": [cost_chemicals],
                                     "utility_costs": [cost_electricity + cost_water],
                                     "labour_costs": [cost_operating_labour + cost_operating_supervision +
                                                      cost_quality_control]},
                               index=['Geothermal_LDH'])
        opex_df['sum'] = opex_df.sum(axis=1)
        return opex_df


if __name__ == '__main__':
    test = LDH_opex()
    print(test)
