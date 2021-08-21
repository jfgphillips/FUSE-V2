from Geothermal_IO.LDH import Sor_Syn_Chemicals
from molmass import Formula
from calculators import unitConversions as uC

class SorbentSynthesis(object):
    def __init__(self):
        self.chemicals = Sor_Syn_Chemicals.SorbentSynthesisChemicals_att()
        self.RMM_LiOH_H2O = Formula('LiOH').mass + Formula('H2O').mass
        self.RMM_aluminium_hydroxide = Formula('Al(OH)3').mass
        self.RMM_H2O = Formula('H2O').mass
        self.RMM_HCl = Formula('HCl').mass
        self.RMM_LiCl = Formula('LiCl').mass
        self.mass_sorbent_grams = self.chemicals.mass_sorbent_year * 10 ** 6
        self.RMM_sorbent = ((self.chemicals.mol_ratio_LiCl * self.RMM_LiCl) +
                            (self.chemicals.mol_ratio_aluminium_hydroxide * self.RMM_aluminium_hydroxide) +
                            (self.chemicals.mol_ratio_H2O * self.RMM_H2O))
        self.mol_sorbent = self.mass_sorbent_grams / self.RMM_sorbent
        self.mol_LiOH_H2O = (self.chemicals.mol_ratio_LiOH_H2O * self.mol_sorbent) / self.chemicals.Yield
        self.mass_LiOH_H2O = (Formula('LiCl').mass + Formula('H2O').mass) * self.chemicals.mol_ratio_LiOH_H2O
        self.mol_aluminium_hydroxide = (self.chemicals.mol_ratio_aluminium_hydroxide * self.mol_sorbent) / self.chemicals.Yield
        self.mass_aluminium_hydroxide = uC.solidMass('Al(OH)3', self.mol_aluminium_hydroxide)
        self.mol_H2O = (self.chemicals.mol_ratio_H2O * self.mol_sorbent) / self.chemicals.Yield
        self.mass_H2O = uC.solidMass('H2O', self.mol_H2O)
        self.mol_HCl = (self.chemicals.mol_ratio_HCl * self.mol_sorbent) / self.chemicals.Yield
        self.mass_HCl = uC.solidMass('HCl', self.mol_HCl)
        return

    def __repr__(self):
        print_sor_syn = f'For the production of {self.chemicals.mass_sorbent_year} tonnes per year LDH' \
                        f'sorbent the amount of reactants required is:\n' \
                        f'LiOH*H2O: {uC.tonnes(self.mass_LiOH_H2O)} tonnes\n' \
                        f'Al(OH)3: {uC.tonnes(self.mass_aluminium_hydroxide)} tonnes\n' \
                        f'HCl: {uC.tonnes(self.mass_HCl)} tonnes\n' \
                        f'H2O: {self.mass_H2O * 10**(-3)} l'
        output = f"{print_sor_syn}"
        return output

if __name__ == '__main__':
    test = SorbentSynthesis()
    print(test)
