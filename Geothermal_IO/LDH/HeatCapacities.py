import pandas as pd
from Geothermal_IO.LDH import Sor_Syn_Chemicals
from Geothermal_IO.LDH import Sor_Syn_Reactor
from Geothermal_IO.LDH import LC_processing
from Geothermal_IO.LDH import LC_purification
from calculators import heatCapacities


class HeatCapacities_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name="sorbent_synthesis_reaction", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.temperature = self.df['value'].loc['reaction_temp']
        self.chemicals = Sor_Syn_Chemicals.SorbentSynthesisChemicals_att()
        self.sorbent_synthesis_reaction = Sor_Syn_Reactor.BatchReactor_att()
        self.LC_processing = LC_processing.LiCarbonateProcessing_att()
        self.LC_purification = LC_purification.LiCarbonatePurification_att()
        self.temp_sor_syn = self.sorbent_synthesis_reaction.reaction_temp
        self.temp_LC_processing = self.LC_processing.reaction_temp
        self.temp_carbonation = self.LC_purification.carbonation_temp
        self.temp_precipitation = self.LC_purification.precipitation_temp
        hc_LiOH_kwargs = {'A': 42.14004, 'B': 145.8434, 'C': -110.738, 'D': 32.62106, 'E': -0.48495,
                          'temp': self.temp_sor_syn}
        hc_HCl_kwargs = {'A': 32.12392, 'B': -13.4581, 'C': 19.86852, 'D': -6.85394, 'E': -0.04967,
                         'temp': self.temp_sor_syn}
        hc_H2O_kwargs = {'A': -203.606, 'B': 1523.29, 'C': -3196.41, 'D': 2474.445, 'E': 3.855326,
                         'temp': self.temp_sor_syn}
        hc_LiCl_kwargs = {'A': 43.74372, 'B': 20.37056, 'C': 0.306430, 'D': -0.094178, 'E': -0.160419,
                          'temp': self.temp_LC_processing}
        hc_Na2CO3_kwargs = {'A': 175.2010, 'B': -348.0580, 'C': 734.0720, 'D': -305.5510, 'E': -1.634221,
                            'temp': self.temp_LC_processing}
        hc_Li2CO3_carbonation_kwargs = {'A': 68.3323, 'B': 146.6390, 'C': -162.5730, 'D': 248.0260, 'E': -0.702297,
                                        'temp': self.temp_carbonation}
        hc_Li2CO3_precipitation_kwargs = {'A': 68.3323, 'B': 146.6390, 'C': -162.5730, 'D': 248.0260, 'E': -0.702297,
                                        'temp': self.temp_precipitation}
        hc_CO2_carbonation_kwargs = {'A': 24.99735, 'B': 55.18696, 'C': -33.69137, 'D': 7.948387, 'E': -0.136638,
                                        'temp': self.temp_carbonation}
        hc_CO2_precipitation_kwargs = {'A': 24.99735, 'B': 55.18696, 'C': -33.69137, 'D': 7.948387, 'E': -0.136638,
                                     'temp': self.temp_precipitation}
        self.hc_aluminium_hydroxide_kg = 1193  #J/(kg*K) source: Huang 2021
        self.chemicals = Sor_Syn_Chemicals.SorbentSynthesisChemicals_att()
        self.hc_aluminium_hydroxide_mol = self.hc_aluminium_hydroxide_kg * (self.chemicals.RMM_aluminium_hydroxide / 10**3)
        self.hc_LiOH = heatCapacities.Schomate_equation(**hc_LiOH_kwargs)
        self.hc_H2O = heatCapacities.Schomate_equation(**hc_H2O_kwargs)
        self.hc_HCl = heatCapacities.Schomate_equation(**hc_HCl_kwargs)
        self.hc_LiCl = heatCapacities.Schomate_equation(**hc_LiCl_kwargs)
        self.hc_Na2CO3 = heatCapacities.Schomate_equation(**hc_Na2CO3_kwargs)
        self.hc_Li2CO3_carbonation = heatCapacities.Schomate_equation(**hc_Li2CO3_carbonation_kwargs)
        self.hc_Li2CO3_precipitation = heatCapacities.Schomate_equation(**hc_Li2CO3_precipitation_kwargs)
        self.hc_CO2_carbonation = heatCapacities.Schomate_equation(**hc_CO2_carbonation_kwargs)
        self.hc_CO2_precipitation = heatCapacities.Schomate_equation(**hc_CO2_precipitation_kwargs)
        return

def hC_LC_purification(total_mass_mixture=None, mass_Li2CO3=None,  mass_H2O=None, Hc_Li2CO3=None, Hc_H2O=None):
    hC = ((mass_Li2CO3/total_mass_mixture) * (Hc_Li2CO3) + ((mass_H2O/total_mass_mixture) * Hc_H2O))
    return hC


if __name__ == '__main__':
   test = HeatCapacities_att()
   print(test)





