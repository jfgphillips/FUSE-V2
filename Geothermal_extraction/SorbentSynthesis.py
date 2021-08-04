import pandas as pd
from calculators import unitConversions
from calculators import QProcesses
from Geothermal_IO.SorbentSynthesis import *


class SorbentSynthesis(object):
    def __init__(self):
        self.chemicals = Chemicals.SorbentSynthesisChemicals_att()
        self.heatCapacities = HeatCapacities.HeatCapacities_att()
        self.reactor = Reactor.BatchReactor_att()
        self.Impeller = Impeller.Impeller_att()
        self.Costs = Costs.UtilityAndChemicals_att()
        self.df = pd.read_excel(r'../data\LDH_attributes.xlsx',
                                sheet_name='water', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.water_usage = (self.df['value'].loc['process'] + self.chemicals.mass_H2O * 10 ** (-3))
        self.total_mass_mix_1 = self.chemicals.mass_LiOH_H2O + self.chemicals.mass_aluminium_hydroxide + self.chemicals.mass_H2O
        self.mass_fraction_LiOH_H2O_1 = self.chemicals.mass_LiOH_H2O / self.total_mass_mix_1
        self.mass_fraction_aluminium_hydroxide_1 = self.chemicals.mass_aluminium_hydroxide / self.total_mass_mix_1
        self.mass_fraction_H2O_1 = self.chemicals.mass_H2O / self.total_mass_mix_1
        self.density_1 = 1 / ((self.mass_fraction_LiOH_H2O_1 / self.chemicals.density_LiOH_H2O)
                         + (self.mass_fraction_aluminium_hydroxide_1 / self.chemicals.density_aluminium_hydroxide)
                         + (self.mass_fraction_H2O_1 / self.chemicals.density_H2O))
        self.total_mass_mix_2 = self.total_mass_mix_1 + self.chemicals.mass_HCl
        self.mass_fraction_LiOH_H2O_2 = self.chemicals.mass_LiOH_H2O / self.total_mass_mix_2
        self.mass_fraction_aluminium_hydroxide_2 = self.chemicals.mass_aluminium_hydroxide / self.total_mass_mix_2
        self.mass_fraction_H2O_2 = self.chemicals.mass_H2O / self.total_mass_mix_2
        self.mass_fraction_HCl = self.chemicals.mass_HCl / self.total_mass_mix_2
        self.density_2 = 1 / ((self.mass_fraction_LiOH_H2O_2 / self.chemicals.density_LiOH_H2O)
                         + (self.mass_fraction_aluminium_hydroxide_2 / self.chemicals.density_aluminium_hydroxide)
                         + (self.mass_fraction_H2O_2 / self.chemicals.density_H2O)
                         + (self.mass_fraction_HCl / self.chemicals.density_HCl))
        self.reactant_masses = {'LiOH*H2O': self.chemicals.mass_LiOH_H2O,
                                'HCl': self.chemicals.mass_HCl,
                                'H2O': self.chemicals.mass_H2O}
        self.energy_df = self.EnergyConsumption()
        self.total_costs_chemicals_and_utility = self.opex()
        return

    def __repr__(self):

        total_energy_consumption = self.energy_df['sum'].loc['Sorbent_Synthesis']

        print_emissions = f'The total emissions to produce {self.chemicals.mass_sorbent_year}' \
                          f'kg for one year operation are: {total_energy_consumption} kWh\n' \
                          f'The emissions per kg of sorbent are: ' \
                          f'{total_energy_consumption / self.chemicals.mass_sorbent_year}kWh/kg'

        print_opex = f'The total costs for chemicals, water and electricity to produce {self.chemicals.mass_sorbent_year}' \
                     f'kg for one year operation are: {self.total_costs_chemicals_and_utility} $\n' \
                     f'The costs for chemicals, water and electricity per kg of sorbent are:' \
                     f'{self.total_costs_chemicals_and_utility/self.chemicals.mass_sorbent_year}$/kg'

        output = f"{print_emissions}\n\n" \
                 f"{print_opex}"

        return output


    def EnergyConsumption(self):
        """"
        Energy consumption of all the processes and machines require for the production of the sorbent in kWh

        """
        req_reactants_kwargs = {'mol_LiOH_H2O': self.chemicals.mol_LiOH_H2O,
                                'hc_LiOH': self.heatCapacities.hc_LiOH,
                                'mol_aluminium_hydroxide': self.chemicals.mol_aluminium_hydroxide,
                                'hc_aluminium_hydroxide': self.heatCapacities.hc_aluminium_hydroxide_mol,
                                'mol_H2O': self.chemicals.mol_H2O,
                                'hc_H2O': self.heatCapacities.hc_H2O,
                                'mol_HCl': self.chemicals.mol_HCl,
                                'hc_HCl': self.heatCapacities.hc_HCl,
                                'reaction_temperature': self.reactor.reaction_temp}

        q_reactants = Chemicals.QReactants(**req_reactants_kwargs)

        req_reactor_kwargs = {'reaction_temperature': self.reactor.reaction_temp,
                              'reaction_time_1': self.reactor.reaction_time_1,
                              'reaction_time_2': self.reactor.reaction_time_2,
                              'surface_area': self.reactor.surface_area,
                              'thermal_conductivity': self.reactor.thermal_conductivity,
                              'wall_thickness': self.reactor.wall_thickness,
                              'liq_density_1': self.density_1,
                              'liq_density_2': self.density_2}

        q_reactor = Reactor.QReactor(**req_reactor_kwargs)

        q_reaction = q_reactants + q_reactor


        req_stirring_energy_kwargs = {'impeller_power_number': self.Impeller.impeller_power_number,
                                      'impeller_diameter': self.Impeller.impeller_diameter,
                                      'agitator_rotational_speed': self.Impeller.agitator_rotational_speed,
                                      'density_1': self.density_1,
                                      'density_2': self.density_2,
                                      'stirring_time_1': self.reactor.reaction_time_1,
                                      'stirring_time_2': self.reactor.reaction_time_2,
                                      'efficiency': self.Impeller.efficiency}

        total_stirring_energy = Impeller.StirringEnergy(**req_stirring_energy_kwargs)


        mass_chemicals_tonnes = self.total_mass_mix_2 * 10 ** (-3)
        grinding_energy = QProcesses.grinding_energy(mass_chemicals_tonnes)


        mass_chemicals_tonnes = self.total_mass_mix_2 * 10 ** (-3)
        filtration_energy = QProcesses.filtration_energy(mass_chemicals_tonnes)


        mass_chemicals_tonnes = self.total_mass_mix_2 * 10 ** (-3)
        pumping_energy_J = QProcesses.pumping_energy(mass_chemicals_tonnes)
        pumping_energy_kWh = unitConversions.kiloWattHours(pumping_energy_J)


        # total_energy_consumption = q_reaction + total_stirring_energy + grinding_energy + filtration_energy \
        #                           + pumping_energy_kWh

        energy_df = pd.DataFrame(data={"Reaction energy": [q_reaction + total_stirring_energy],
                                       "Processing energy": [grinding_energy + filtration_energy],
                                       "Transportation energy": [pumping_energy_kWh]},
                                 index=['Sorbent_Synthesis'])
        energy_df['sum'] = energy_df.sum(axis=1)

        return energy_df


    def opex(self):
        """
        gives the total costs for chemicals, water and electricity used for the sorbent synthesis

        """

        cost_chemicals = self.chemicals.mass_LiOH_H2O * 10**(-3) * self.Costs.cost_LiOH_H2O + \
                         self.chemicals.mass_aluminium_hydroxide * 10**(-3)  * self.Costs.cost_aluminium_hydroxide + \
                         self.chemicals.mass_HCl * self.Costs.cost_HCl

        cost_water = self.water_usage * self.Costs.cost_water

        cost_electricity = self.Costs.cost_electricity * self.energy_df['sum'].loc['Sorbent_Synthesis']

        total_costs_chemicals_and_utility = cost_electricity + cost_water + cost_chemicals

        return total_costs_chemicals_and_utility


if __name__ == '__main__':
    test = SorbentSynthesis()
    print(test)

