import pandas as pd
from Geothermal_IO.LDH import *
from Geothermal_extraction.LDH import LDH_energy
from Geothermal_extraction.LDH import Reactant_flow
from Geothermal_extraction.LDH import LDH_capex
from Geothermal_extraction.LDH import SorbentSynthesis
from calculators import unitConversions as uC


class LDH_opex(object):
    def __init__(self):
        self.chemicals = Sor_Syn_Chemicals.SorbentSynthesisChemicals_att()
        self.sor_syn = SorbentSynthesis.SorbentSynthesis()
        self.reactant_flow = Reactant_flow.ReactantFlow()
        self.plant = Plant.Plant_att()
        self.opex = Opex.Costs_att()
        self.brine = Brine.Brine_att()
        self.water = Water.Water_att()
        self.worker = Worker.worker_att()
        self.energy = LDH_energy.LDH_energy()
        self.capex = LDH_capex.LDH_capex()
        self.opex_df = self.CostsOpex()
        return


    def __repr__(self):

        total_opex = self.opex_df['sum'].loc['Geothermal_LDH']
        print_opex = f'The total opex to product {uC.tonnes(self.reactant_flow.LC_purification_product["pure Li2CO3"])} ' \
                     f'tonnes battery grade lithium carbonate per year from a brine flow of ' \
                     f'{self.plant.brine_flow_day} m^3 per day \nwith a LiCl concentration of ' \
                     f'{self.brine.Li_conc_brine} g/L are: {total_opex} $ \n' \
                     f'The costs per kg of lithium carbonate are: ' \
                     f'{total_opex / (self.reactant_flow.LC_purification_product["pure Li2CO3"] * 10**(-3))} $/kg'

        output = f"{print_opex}"
        return output

    def CostsOpex(self):
        """
        source: Huang 2021
        :return: total costs of direct costs (chemicals, water, electricity, labour) indirect costs and
         general costs per year operation in $
        """
        cost_chemicals = self.sor_syn.mass_LiOH_H2O * 10 ** (-3) * self.opex.cost_LiOH_H2O + \
                         self.sor_syn.mass_aluminium_hydroxide * 10**(-3) * self.opex.cost_aluminium_hydroxide +\
                         self.sor_syn.mass_HCl * 10 ** (-3) * self.opex.cost_HCl + \
                         self.reactant_flow.LC_processing_reactants['Na2CO3'] * 10**(-3) * self.opex.cost_Na2CO3 + \
                         self.reactant_flow.LC_purification_reactants['CO2'] * 10**(-3) * self.opex.cost_CO2_low

        cost_water = self.water.total_water_usage * self.opex.cost_water

        cost_electricity = self.opex.cost_electricity * self.energy.energy_df['sum'].loc['Geothermal_LDH']

        materials_cost = cost_chemicals + cost_water + cost_electricity

        # source: Huang 2021
        cost_FCC = float(self.capex.FCC)
        cost_TCI = float(self.capex.TCI)
        cost_operating_labour = self.worker.no_operators * self.worker.annual_wage
        cost_operating_supervision = self.worker.supervision * cost_operating_labour
        cost_quality_control = self.worker.quality_control * cost_operating_labour
        cost_maintenance_labour = self.worker.maintenance_labour * cost_FCC
        cost_maintenance_material = self.opex.maintenance_material * cost_FCC
        cost_operating_supplies = self.opex.operating_supplies * cost_FCC
        cost_contingency = self.opex.contingency_1 * materials_cost + \
                           self.opex.contingency_2 * (cost_operating_labour + cost_operating_supervision +
                                                      cost_quality_control + cost_maintenance_labour +
                                                      cost_maintenance_material + cost_operating_supplies)

        direct_costs = materials_cost + cost_operating_labour + cost_operating_supervision + cost_quality_control + \
                       cost_maintenance_labour + cost_maintenance_material + cost_operating_supplies + cost_contingency

        cost_property_taxes = self.opex.property_taxes * cost_FCC
        cost_insurance = self.opex.insurance * cost_FCC
        cost_fringe_benefits = self.opex.fringe_benefits * (cost_operating_labour + cost_operating_supervision)
        cost_overhead = self.opex.overhead * (cost_operating_labour + cost_operating_supervision)
        indirect_costs = cost_property_taxes + cost_insurance + cost_fringe_benefits + cost_overhead

        cost_admin = self.opex.admin * (direct_costs + indirect_costs)
        cost_marketing = self.opex.marketing * (direct_costs + indirect_costs)
        cost_financing = self.opex.financing * cost_TCI
        cost_R_D = self.opex.R_D * (direct_costs + indirect_costs)
        general_costs = cost_admin + cost_marketing + cost_financing + cost_R_D

        opex_df = pd.DataFrame(data={"chemical_costs": [cost_chemicals],
                                     "utility_costs": [cost_electricity + cost_water],
                                     "labour_costs": [cost_operating_labour + cost_operating_supervision +
                                                      cost_quality_control + cost_maintenance_labour],
                                     "other": [cost_maintenance_material + cost_operating_supplies + cost_contingency +
                                               indirect_costs + general_costs]},
                               index=['Geothermal_LDH'])
        opex_df['sum'] = opex_df.sum(axis=1)

        return opex_df


if __name__ == '__main__':
    test = LDH_opex()
    print(test)
