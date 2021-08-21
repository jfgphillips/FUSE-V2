from molmass import Formula

class HeatVaporization(object):
    def __init__(self):
        # Heat of Vaporization taken form the MatWeb, Material Property data website
        self.Hvap_LiOH = 7850 * 10**3  # J/kg
        self.Hvap_H2O = 2257 * 10**3  # J/kg
        self.Hvap_Li2CO3_kJ_mol = 145.92  # kJ/mol (source: https://www.nuclear-power.com/Lithium-specific-heat-latent-heat-vaporization-fusion/)
        self.Hvap_Li2CO3 = self.Hvap_Li2CO3_kJ_mol * 10**3 / Formula('Li2CO3').mass  #J/kg
        return

def Hvap_LC_purification(total_mass_mixture=None, mass_Li2CO3=None,  mass_H2O=None, Hvap_Li2CO3=None, Hvap_H2O=None):
    """

    :param total_mass_mixture: total mass of the mixture for Li2CO3 purification (Li2CO3, H2O, CO2) in g
    :param mass_Li2CO3: in g
    :param mass_H2O: in g
    :param Hvap_Li2CO3: in J/kg
    :param Hvap_H2O: in J/kg
    :return: heat of vaporization of the Li2CO3 purification mixture in J/kg
    """
    Hvap = ((mass_Li2CO3/total_mass_mixture) * (Hvap_Li2CO3) + ((mass_H2O/total_mass_mixture) * Hvap_H2O))
    return Hvap
