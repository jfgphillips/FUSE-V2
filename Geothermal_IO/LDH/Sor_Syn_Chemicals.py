import pandas as pd
from calculators import unitConversions
from molmass import Formula


class SorbentSynthesisChemicals_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'\Users\chant\PycharmProjects\FUSE-V2\data\LDH_attributes.xlsx',
                                sheet_name="chemicals_sorbent_synthesis", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.mass_sorbent_year = self.df['value'].loc['mass_sorbent']  # kg/year
        self.Yield = self.df['value'].loc['yield']
        self.mol_ratio_aluminium_hydroxide = self.df['value'].loc['mol_ratio_Al(OH)3']
        self.mol_ratio_LiOH_H2O = self.df['value'].loc['mol_ratio_LiOH_H2O']
        self.mol_ratio_H2O = self.df['value'].loc['mol_ratio_DI']
        self.mol_ratio_HCl = self.df['value'].loc['mol_ratio_HCl']
        self.mol_ratio_LiCl = self.mol_ratio_LiOH_H2O
        self.RMM_LiOH_H2O = Formula('LiOH').mass + Formula('H2O').mass
        self.RMM_aluminium_hydroxide = Formula('Al(OH)3').mass
        self.RMM_H2O = Formula('H2O').mass
        self.RMM_HCl = Formula('HCl').mass
        self.RMM_LiCl = Formula('LiCl').mass
        self.mass_sorbent_grams = self.mass_sorbent_year * 10**3
        self.RMM_sorbent = ((self.mol_ratio_LiCl * self.RMM_LiCl) +
                            (self.mol_ratio_aluminium_hydroxide * self.RMM_aluminium_hydroxide) +
                            (self.mol_ratio_H2O * self.RMM_H2O))
        self.mol_sorbent = self.mass_sorbent_grams / self.RMM_sorbent
        self.mol_LiOH_H2O = (self.mol_ratio_LiOH_H2O * self.mol_sorbent) / self.Yield
        self.mass_LiOH_H2O = (Formula('LiCl').mass + Formula('H2O').mass) * self.mol_ratio_LiOH_H2O
        self.mol_aluminium_hydroxide = (self.mol_ratio_aluminium_hydroxide * self.mol_sorbent) / self.Yield
        self.mass_aluminium_hydroxide = unitConversions.solidMass('Al(OH)3', self.mol_aluminium_hydroxide)
        self.mol_H2O = (self.mol_ratio_H2O * self.mol_sorbent) / self.Yield
        self.mass_H2O = unitConversions.solidMass('H2O', self.mol_H2O)
        self.mol_HCl = (self.mol_ratio_HCl * self.mol_sorbent) / self.Yield
        self.mass_HCl = unitConversions.solidMass('HCl', self.mol_HCl)
        return

def QReactants(mol_LiOH_H2O=None, hc_LiOH=None, mol_aluminium_hydroxide=None, hc_aluminium_hydroxide=None,
               mol_H2O=None, hc_H2O=None, mol_HCl=None, hc_HCl=None, reaction_temperature=None):
    """
    source: Sharma 2020
    """
    room_temperature = 298.15 #K
    q_reactants_joule = (mol_LiOH_H2O * hc_LiOH * (reaction_temperature - room_temperature) +
                       mol_aluminium_hydroxide * hc_aluminium_hydroxide * (reaction_temperature - room_temperature) +
                       mol_H2O * hc_H2O * (reaction_temperature - room_temperature) +
                       mol_HCl * hc_HCl * (reaction_temperature - room_temperature))
    q_reactants_kWh = unitConversions.kiloWattHours(q_reactants_joule)
    return q_reactants_kWh



# if __name__ == '__main__':
#    test = SorbentSynthesisChemicals_att()

