import pandas as pd
from calculators import unitConversions as uC
from calculators import QProcesses
from calculators import QReactors
from calculators import QMachines
from Geothermal_IO.LDH import *
from Geothermal_extraction.LDH import Reactant_flow
from Geothermal_extraction.LDH import SorbentSynthesis


class LDH_energy(object):
    def __init__(self):
        self.chemicals = Sor_Syn_Chemicals.SorbentSynthesisChemicals_att()
        self.sor_syn = SorbentSynthesis.SorbentSynthesis()
        self.hC = HeatCapacities.HeatCapacities_att()
        self.reactor = Sor_Syn_Reactor.BatchReactor_att()
        self.impeller = Impeller.Impeller_att()
        self.densities = Densities_and_Tb.DensitiesSorbentSynthesis()
        self.HV = HeatVaporization.HeatVaporization()
        self.FO = ForwardOsmosis.ForwardOsmosis()
        self.LC_processing = LC_processing.LiCarbonateProcessing_att()
        self.LC_purification = LC_purification.LiCarbonatePurification_att()
        self.reactant_flow = Reactant_flow.ReactantFlow()
        self.water = Water.Water_att()
        self.plant = Plant.Plant_att()
        self.brine = Brine.Brine_att()
        self.washing = Column_Washing.ColumnExtractionWashing()
        self.stripping = Column_Stripping.ColumnExtractionStripping()
        self.BC = Belt_conveyor.BeltConveyor_att()
        self.total_mass_mix_1_sor_syn = self.sor_syn.mass_LiOH_H2O + self.sor_syn.mass_aluminium_hydroxide \
                                        + self.sor_syn.mass_H2O
        self.total_mass_mix_2_sor_syn = self.total_mass_mix_1_sor_syn + self.sor_syn.mass_HCl
        density_sor_syn_kwargs = {'total_mass_mixture_1': self.total_mass_mix_1_sor_syn,
                                  'total_mass_mixture_2': self.total_mass_mix_2_sor_syn,
                                  'mass_LiOH_H2O': self.sor_syn.mass_LiOH_H2O,
                                  'mass_aluminium_hydroxide': self.sor_syn.mass_aluminium_hydroxide,
                                  'mass_H2O': self.sor_syn.mass_H2O,
                                  'mass_HCl': self.sor_syn.mass_HCl,
                                  'density_LiOH_H2O': self.densities.density_LiOH_H2O,
                                  'density_aluminium_hydroxide': self.densities.density_aluminium_hydroxide,
                                  'density_H2O': self.densities.density_H2O,
                                  'density_HCl': self.densities.density_HCl}
        self.density_1, self.density_2 = Densities_and_Tb.Densities_sorbent_synthesis(**density_sor_syn_kwargs)
        self.total_mass_NaCl_washing = self.washing.total_mass_NaCl + self.washing.H2O_washing_total * 10**3
        density_NaCl_washing_kwargs = {'total_mass_mixture': self.total_mass_NaCl_washing,
                                       'mass_H2O': self.washing.H2O_washing_total * 10 ** 3,
                                       'mass_NaCl': self.washing.total_mass_NaCl,
                                       'density_H2O': self.densities.density_H2O,
                                       'density_NaCl': self.densities.density_NaCl}
        self.density_NaCl_washing = Densities_and_Tb.Density_NaCl_sol(**density_NaCl_washing_kwargs)
        self.total_mass_LiCl_sol_stripping = self.stripping.LiCl_sol_output * 10**3 + \
                                             (self.stripping.LiCl_conc_stripping * self.stripping.LiCl_sol_output)
        density_LiCl_sol_stripping_kwargs = {'total_mass_mixture': self.total_mass_LiCl_sol_stripping,
                                             'mass_H2O': self.stripping.LiCl_sol_output * 10**3,
                                             'mass_LiCl': self.stripping.LiCl_conc_stripping *
                                                          self.stripping.LiCl_sol_output,
                                             'density_H2O': self.densities.density_H2O,
                                             'density_LiCl': self.densities.density_LiCl}
        self.density_LiCl_sol_stripping = Densities_and_Tb.Density_LiCl_sol(**density_LiCl_sol_stripping_kwargs)
        self.total_mass_LiCl_sol_FO = self.FO.LiCl_sol_output * 10 ** 3 + \
                                      (self.FO.LiCl_conc_FO * self.FO.LiCl_sol_output)
        density_LiCl_sol_FO_kwargs = {'total_mass_mixture': self.total_mass_LiCl_sol_stripping,
                                      'mass_H2O': self.FO.LiCl_sol_output * 10 ** 3,
                                      'mass_LiCl': self.FO.LiCl_conc_FO * self.FO.LiCl_sol_output,
                                      'density_H2O': self.densities.density_H2O,
                                      'density_LiCl': self.densities.density_LiCl}
        self.density_LiCl_sol_FO = Densities_and_Tb.Density_LiCl_sol(**density_LiCl_sol_FO_kwargs)
        self.total_mass_LC_processing = self.reactant_flow.LC_processing_reactants['LiCl'] + \
                                        self.reactant_flow.LC_processing_reactants['Na2CO3']
        density_LC_processing_kwargs = {'total_mass_mixture': self.total_mass_LC_processing,
                                        'mass_LiCl': self.reactant_flow.LC_processing_reactants['LiCl'],
                                        'mass_Na2CO3':self.reactant_flow.LC_processing_reactants['Na2CO3'],
                                        'density_LiCl': self.densities.density_LiCl,
                                        'density_Na2CO3': self.densities.density_Na2CO3}
        self.density_LC_processing = Densities_and_Tb.Densitiy_LC_processing(**density_LC_processing_kwargs)
        self.total_mass_LC_purification = self.reactant_flow.LC_purification_reactants['H2O'] + \
                                          self.reactant_flow.LC_purification_reactants['CO2'] + \
                                          self.reactant_flow.LC_purification_reactants['impure Li2CO3']
        density_LC_purification_kwargs = {'total_mass_mixture': self.total_mass_LC_purification,
                                          'mass_Li2CO3': self.reactant_flow.LC_purification_reactants['impure Li2CO3'],
                                          'mass_CO2': self.reactant_flow.LC_purification_reactants['CO2'],
                                          'mass_H2O': self.reactant_flow.LC_purification_reactants['H2O'],
                                          'density_Li2CO3': self.densities.density_Li2CO3,
                                          'density_CO2': self.densities.density_CO2,
                                          'density_H2O': self.densities.density_H2O}
        self.density_LC_purification = Densities_and_Tb.Density_LC_purification(**density_LC_purification_kwargs)
        self.total_mass_drying_LC_purification = self.reactant_flow.LC_purification_by_products['H2O'] + \
                                                 self.reactant_flow.LC_purification_product['pure Li2CO3']
        Tb_LC_purification_kwargs = {'total_mass_mixture': self.total_mass_drying_LC_purification,
                                     'mass_Li2CO3': self.reactant_flow.LC_purification_reactants['impure Li2CO3'],
                                     'mass_H2O': self.reactant_flow.LC_purification_reactants['H2O'],
                                     'Tb_Li2CO3': self.densities.Tb_Li2CO3,
                                     'Tb_H2O': self.densities.Tb_H2O}
        self.Tb_LC_purification = Densities_and_Tb.Tb_LC_purification(**Tb_LC_purification_kwargs)
        hC_LC_purification_kwargs = {'total_mass_mixture': self.total_mass_drying_LC_purification,
                                     'mass_Li2CO3': self.reactant_flow.LC_purification_reactants['impure Li2CO3'],
                                     'mass_H2O': self.reactant_flow.LC_purification_reactants['H2O'],
                                     'Hc_Li2CO3': self.hC.hc_Li2CO3_precipitation,
                                     'Hc_H2O': self.hC.hc_H2O}
        self.hC_LC_purification = HeatCapacities.hC_LC_purification(**hC_LC_purification_kwargs)
        Hvap_LC_purification_kwargs = {'total_mass_mixture': self.total_mass_drying_LC_purification,
                                       'mass_Li2CO3': self.reactant_flow.LC_purification_reactants['impure Li2CO3'],
                                       'mass_H2O': self.reactant_flow.LC_purification_reactants['H2O'],
                                       'Hvap_Li2CO3': self.HV.Hvap_Li2CO3,
                                       'Hvap_H2O': self.HV.Hvap_H2O}
        self.Hvap_LC_purification = HeatVaporization.Hvap_LC_purification(**Hvap_LC_purification_kwargs)
        self.energy_df = self.EnergyConsumption()
        return

    def __repr__(self):

        total_energy_consumption = self.energy_df['sum'].loc['Geothermal_LDH']

        print_emissions = f'The total energy required to produce {uC.tonnes(self.reactant_flow.LC_purification_product["pure Li2CO3"])} '\
                          f'tonnes battery grade lithium carbonate per year from a brine flow of ' \
                          f'{self.plant.brine_flow_day} m^3 per day \nwith a LiCL concentration of ' \
                          f'{self.brine.Li_conc_brine} g/L are: {total_energy_consumption} kWh\n' \
                          f'The energy required per kg of lithium carbonate are: ' \
                          f'{total_energy_consumption / (self.reactant_flow.LC_purification_product["pure Li2CO3"]*10**(-3))} ' \
                          f'kWh/kg'

        output = f"{print_emissions}"

        return output


    def EnergyConsumption(self):
        """"
        Energy consumption of all processes and machines require for the geothermal DLE plant, including the sorbent
        synthesis, lithium carbonate processing and lithium carbonate purification

        """
        req_reactants_sor_syn_kwargs = {'mol_LiOH_H2O': self.sor_syn.mol_LiOH_H2O,
                                        'hc_LiOH': self.hC.hc_LiOH,
                                        'mol_aluminium_hydroxide': self.sor_syn.mol_aluminium_hydroxide,
                                        'hc_aluminium_hydroxide': self.hC.hc_aluminium_hydroxide_mol,
                                        'mol_H2O': self.sor_syn.mol_H2O,
                                        'hc_H2O': self.hC.hc_H2O,
                                        'mol_HCl': self.sor_syn.mol_HCl,
                                        'hc_HCl': self.hC.hc_HCl,
                                        'reaction_temperature': self.reactor.reaction_temp}

        q_reactants_sor_syn = Sor_Syn_Chemicals.QReactants(**req_reactants_sor_syn_kwargs)

        req_reactor_sor_syn_kwargs = {'reaction_temperature': self.reactor.reaction_temp,
                                      'reaction_time_1': self.reactor.reaction_time_1,
                                      'reaction_time_2': self.reactor.reaction_time_2,
                                      'surface_area': self.reactor.surface_area,
                                      'thermal_conductivity': self.reactor.thermal_conductivity,
                                      'wall_thickness': self.reactor.wall_thickness,
                                      'liq_density_1': self.density_1,
                                      'liq_density_2': self.density_2}

        q_reactor_sor_syn = Sor_Syn_Reactor.QReactor(**req_reactor_sor_syn_kwargs)

        q_reaction_sor_syn = q_reactants_sor_syn + (q_reactor_sor_syn * 10**(-3))


        req_stir_energy_sor_syn_kwargs = {'impeller_power_number': self.impeller.impeller_power_number,
                                          'impeller_diameter': self.impeller.impeller_diameter,
                                          'agitator_rotational_speed': self.impeller.agitator_rotational_speed,
                                          'density_1': self.density_1 * 10**(-3),
                                          'density_2': self.density_2 * 10**(-3),
                                          'stirring_time_1': self.reactor.reaction_time_1 * 3600,
                                          'stirring_time_2': self.reactor.reaction_time_2 * 3600,
                                          'efficiency': self.impeller.efficiency}

        stirring_energy_sor_syn = uC.kiloWattHours(Impeller.StirringEnergySorSyn(**req_stir_energy_sor_syn_kwargs))

        grinding_energy_sor_syn = QProcesses.grinding_energy(uC.tonnes(self.total_mass_mix_2_sor_syn))

        filtration_energy_sor_syn = QProcesses.filtration_energy(uC.tonnes(self.total_mass_mix_2_sor_syn))

        pumping_energy_sor_syn = uC.kiloWattHours(QProcesses.pumping_energy(uC.tonnes(self.total_mass_mix_2_sor_syn) +
                                                                            self.water.sor_syn_washing))

        req_stir_energy_column_washing_kwargs = {'impeller_power_number': self.impeller.impeller_power_number,
                                                 'impeller_diameter': self.impeller.impeller_diameter,
                                                 'agitator_rotational_speed': self.impeller.agitator_rotational_speed,
                                                 'density': self.density_NaCl_washing * 10 ** (-3),
                                                 'stirring_time': self.washing.stirring_time * 3600,
                                                 'efficiency': self.impeller.efficiency}
        stirring_energy_column_washing = uC.kiloWattHours\
            (QProcesses.stirring_energy(**req_stir_energy_column_washing_kwargs))

        # assuming the brine has the density of water

        pumping_energy_column_extraction = uC.kiloWattHours(QProcesses.pumping_energy
                                                            (((self.plant.brine_flow_day / 24) *
                                                             self.plant.plant_uptime) +
                                                             ((self.washing.H2O_washing_total +
                                                               self.stripping.H2O_stripping_total) * 10**3) +
                                                             self.washing.total_mass_NaCl))

        pumping_energy_effluent = uC.kiloWattHours(QProcesses.pumping_energy(((self.plant.brine_flow_day / 24) *
                                                   self.plant.plant_uptime) +
                                                   (uC.tonnes((self.washing.H2O_washing_total +
                                                               self.stripping.H2O_stripping_total) * 10**3 +
                                                              self.washing.total_mass_NaCl -
                                                              self.stripping.LiCl_sol_output * 10**3 *
                                                              self.density_LiCl_sol_stripping))))

        filtration_energy_FO = QProcesses.filtration_energy(self.FO.LiCl_sol_output * 10**(-3))

        pumping_energy_FO = uC.kiloWattHours(QProcesses.pumping_energy(uC.tonnes(self.stripping.LiCl_sol_output *
                                             10**3 * self.density_LiCl_sol_stripping)))

        req_reactants_LC_processing_kwargs = {'mol_LiCl': uC.solidMol
                                              ('LiCl', self.reactant_flow.LC_processing_reactants['LiCl']),
                                              'hc_LiCl': self.hC.hc_LiCl,
                                              'mol_Na2CO3': uC.solidMol
                                              ('Na2CO3', self.reactant_flow.LC_processing_reactants['Na2CO3']),
                                              'hc_Na2CO3': self.hC.hc_Na2CO3,
                                              'reaction_temperature': self.LC_processing.reaction_temp}
        q_reactants_LC_processing = LC_processing.QReactants(**req_reactants_LC_processing_kwargs)

        q_reactor_LC_processing_kwargs = {'reaction_temperature': self.LC_processing.reaction_temp,
                                          'reaction_time': self.LC_processing.reaction_time,
                                          'surface_area': self.LC_processing.surface_area,
                                          'thermal_conductivity': self.LC_processing.thermal_conductivity,
                                          'wall_thickness': self.LC_processing.wall_thickness,
                                          'liq_density': self.density_LC_processing}

        q_reactor_LC_processing = QReactors.batchReactor(**q_reactor_LC_processing_kwargs)

        q_reaction_LC_processing = q_reactants_LC_processing + (q_reactor_LC_processing[0] * 10**(-3))

        req_stir_energy_LC_processing_kwargs = {'impeller_power_number': self.impeller.impeller_power_number,
                                                'impeller_diameter': self.impeller.impeller_diameter,
                                                'agitator_rotational_speed': self.impeller.agitator_rotational_speed,
                                                'density': self.density_LC_processing * 10**(-3),
                                                'stirring_time': self.LC_processing.reaction_time * 3600,
                                                'efficiency': self.impeller.efficiency}

        stirring_energy_LC_processing = uC.kiloWattHours(QProcesses.stirring_energy
                                                         (**req_stir_energy_LC_processing_kwargs))

        filtration_energy_LC_processing = QProcesses.filtration_energy\
            (uC.tonnes(self.reactant_flow.LC_processing_reactants['LiCl'] +
                       self.reactant_flow.LC_processing_reactants['Na2CO3']))

        pumping_energy_LC_processing = uC.kiloWattHours(QProcesses.pumping_energy
                                                        (uC.tonnes(self.FO.LiCl_sol_output * 10**3 +
                                                         self.density_LiCl_sol_FO +
                                                         self.reactant_flow.LC_processing_reactants['Na2CO3'])))

        req_reactants_LC_carbonation_kwargs = {'mol_Li2CO3': uC.solidMol
                                               ('Li2CO3', self.reactant_flow.LC_purification_reactants['impure Li2CO3']),
                                               'hc_Li2CO3': self.hC.hc_Li2CO3_carbonation,
                                               'mol_CO2': uC.solidMol
                                               ('CO2', self.reactant_flow.LC_purification_reactants['CO2']),
                                               'hc_CO2': self.hC.hc_CO2_carbonation,
                                               'mol_H2O': uC.solidMol
                                               ('H2O', self.reactant_flow.LC_purification_reactants['H2O']),
                                               'hc_H2O': self.hC.hc_H2O,
                                               'reaction_temperature': self.LC_purification.carbonation_temp}

        q_reactants_LC_carbonation = LC_purification.QReactants(**req_reactants_LC_carbonation_kwargs)

        req_reactor_LC_carbonation_kwargs = {'reaction_temperature': self.LC_purification.carbonation_temp,
                                             'reaction_time': self.LC_purification.carbonation_time,
                                             'surface_area': self.LC_purification.surface_area,
                                             'thermal_conductivity': self.LC_purification.thermal_conductivity,
                                             'wall_thickness': self.LC_purification.wall_thickness,
                                             'liq_density': self.density_LC_purification}

        q_reactor_LC_carbonation = QReactors.batchReactor(**req_reactor_LC_carbonation_kwargs)

        q_reaction_LC_carbonation = q_reactants_LC_carbonation + (q_reactor_LC_carbonation[0] * 10**(-3))

        req_stir_energy_carbonation_kwargs = {'impeller_power_number': self.impeller.impeller_power_number,
                                              'impeller_diameter': self.impeller.impeller_diameter,
                                              'agitator_rotational_speed': self.impeller.agitator_rotational_speed,
                                              'density': self.density_LC_purification * 10**(-3),
                                              'stirring_time': self.LC_purification.carbonation_time * 3600,
                                              'efficiency': self.impeller.efficiency}

        stirring_energy_carbonation = uC.kiloWattHours(QProcesses.stirring_energy(**req_stir_energy_carbonation_kwargs))

        filtration_energy_carbonation = QProcesses.filtration_energy\
            (uC.tonnes(self.reactant_flow.LC_purification_intermediate['LiHCO3']))

        pumping_energy_carbonation = uC.kiloWattHours(QProcesses.pumping_energy
                                                      (uC.tonnes(self.reactant_flow.LC_purification_reactants
                                                                 ['impure Li2CO3']) +
                                                       self.reactant_flow.LC_purification_reactants['H2O'] +
                                                       self.reactant_flow.LC_purification_reactants['CO2']))

        pumping_energy_carbonation_processing = uC.kiloWattHours(QProcesses.pumping_energy(uC.tonnes
                                                                 (self.reactant_flow.LC_purification_intermediate
                                                                  ['LiHCO3'])))

        req_reactants_LC_precipitation_kwargs = {'mol_Li2CO3': uC.solidMol
                                                 ('Li2CO3', self.reactant_flow.LC_purification_intermediate['LiHCO3']),
                                                 'hc_Li2CO3': self.hC.hc_Li2CO3_carbonation,
                                                 'mol_CO2': uC.solidMol
                                                 ('CO2', self.reactant_flow.LC_purification_reactants['CO2']),
                                                 'hc_CO2': self.hC.hc_CO2_carbonation,
                                                 'mol_H2O': uC.solidMol
                                                 ('H2O', self.reactant_flow.LC_purification_reactants['H2O']),
                                                 'hc_H2O': self.hC.hc_H2O,
                                                 'reaction_temperature': self.LC_purification.precipitation_temp}

        q_reactants_LC_precipitation = LC_purification.QReactants(**req_reactants_LC_precipitation_kwargs)

        req_reactor_LC_precipitation_kwargs = {'reaction_temperature': self.LC_purification.precipitation_temp,
                                               'reaction_time': self.LC_purification.precipitation_time,
                                               'surface_area': self.LC_purification.surface_area,
                                               'thermal_conductivity': self.LC_purification.thermal_conductivity,
                                               'wall_thickness': self.LC_purification.wall_thickness,
                                               'liq_density': self.density_LC_purification}

        q_reactor_LC_precipitation = QReactors.batchReactor(**req_reactor_LC_precipitation_kwargs)

        q_reaction_LC_precipitation = q_reactants_LC_precipitation + (q_reactor_LC_precipitation[0] * 10**(-3))

        req_stir_energy_precipitation_kwargs = {'impeller_power_number': self.impeller.impeller_power_number,
                                                'impeller_diameter': self.impeller.impeller_diameter,
                                                'agitator_rotational_speed': self.impeller.agitator_rotational_speed,
                                                'density': self.density_LC_purification * 10**(-3),
                                                'stirring_time': self.LC_purification.precipitation_time * 3600,
                                                'efficiency': self.impeller.efficiency}

        stirring_energy_precipitation = uC.kiloWattHours(QProcesses.stirring_energy
                                                         (**req_stir_energy_precipitation_kwargs))

        filtration_energy_precipitation = QProcesses.filtration_energy\
            (uC.tonnes(self.reactant_flow.LC_purification_intermediate['LiHCO3']))

        req_drying_energy_LC_processing_kwargs = {'heat_capacity_solution': self.hC_LC_purification,
                                                  'mass_solution': self.total_mass_drying_LC_purification,
                                                  'boiling_temperature': self.Tb_LC_purification,
                                                  'starting_temperature': self.LC_purification.washing_temperature,
                                                  'evaporation_enthalpy': self.Hvap_LC_purification,
                                                  'mass_vapour': self.LC_purification.mass_difference_evaporation}

        drying_energy_LC_purification = uC.kiloWattHours(QProcesses.drying_energy
                                                         (**req_drying_energy_LC_processing_kwargs))

        pumping_energy_precipitation_filtration = uC.kiloWattHours(QProcesses.pumping_energy
                                                                   (uC.tonnes(self.reactant_flow.LC_purification_product
                                                                              ['pure Li2CO3']) +
                                                                    self.reactant_flow.LC_purification_by_products
                                                                    ['H2O']))

        pumping_energy_LC_purification_wash = uC.kiloWattHours(QProcesses.pumping_energy
                                                               (uC.tonnes(self.water.LC_purification_washing)))

        belt_conveyor_energy_average = QMachines.beltConveyor(self.BC.belt_speed, self.BC.belt_length, self.BC.gradient,
                                                              self.BC.output, self.BC.efficiency)

        energy_df = pd.DataFrame(data={"Reaction energy": [q_reaction_sor_syn + q_reaction_LC_processing +
                                                           q_reaction_LC_carbonation + q_reaction_LC_precipitation +
                                                           stirring_energy_sor_syn + stirring_energy_column_washing +
                                                           stirring_energy_LC_processing + stirring_energy_carbonation +
                                                           stirring_energy_precipitation],
                                       "Processing energy": [filtration_energy_sor_syn + filtration_energy_FO +
                                                             filtration_energy_LC_processing +
                                                             filtration_energy_carbonation +
                                                             filtration_energy_precipitation+ grinding_energy_sor_syn +
                                                             drying_energy_LC_purification],
                                       "Transportation energy": [pumping_energy_sor_syn +
                                                                 pumping_energy_column_extraction +
                                                                 pumping_energy_effluent + pumping_energy_FO +
                                                                 pumping_energy_LC_processing +
                                                                 pumping_energy_carbonation_processing +
                                                                 pumping_energy_carbonation +
                                                                 pumping_energy_carbonation_processing +
                                                                 pumping_energy_precipitation_filtration +
                                                                 pumping_energy_LC_purification_wash +
                                                                 belt_conveyor_energy_average]},
                                 index=['Geothermal_LDH'])
        energy_df['sum'] = energy_df.sum(axis=1)

        return energy_df


if __name__ == '__main__':
    test = LDH_energy()
    print(test)

