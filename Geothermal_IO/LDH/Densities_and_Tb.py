

class DensitiesSorbentSynthesis(object):
    def __init__(self):
        # densities from PubChem database
        self.density_LiOH = 2.54   # g/cm^3
        self.density_LiOH_H2O = 1.51  # g/cm^3
        self.density_aluminium_hydroxide = 2.42  # g/cm^3
        self.density_H2O = 1  # g/cm^3
        self.density_HCl = 1.639 * 10**(-3)  # g/cm^3
        self.density_LiCl = 2.07  # g/cm^3
        self.density_NaCl = 2.165  #g/cm^3
        self.density_Na2CO3 = 2.54  #g/cm^3
        self.density_Li2CO3 = 2.11  #g/cm^3
        self.density_CO2 = 1.773  #g/cm^3 source: https://www.engineeringtoolbox.com/carbon-dioxide-density-specific-weight-temperature-pressure-d_2018.html#Table
        self.Tb_H2O = 373.124  #K
        self.Tb_Li2CO3 = 1573.15  #K
        return


def Densities_sorbent_synthesis(total_mass_mixture_1=None, total_mass_mixture_2=None, mass_LiOH_H2O=None,
                                mass_aluminium_hydroxide=None, mass_H2O=None, mass_HCl=None, density_LiOH_H2O=None,
                                density_aluminium_hydroxide=None, density_H2O=None, density_HCl=None):
    """

    :param total_mass_mixture_1: mass of mixture 1 (LiOH*H2O, Al(OH)3 and water) for sorbent synthesis reaction step 1 in g
    :param total_mass_mixture_2: mass of mixture 2 (mixture 1 + HCl) for sorbent synthesis reaction step 2 in g
    :param mass_LiOH_H2O: in g
    :param mass_aluminium_hydroxide: in g
    :param mass_H2O: in g
    :param mass_HCl: in g
    :param density_LiOH_H2O: in g/cm^3
    :param density_aluminium_hydroxide: in g/cm^3
    :param density_H2O: in in g/cm^3
    :param density_HCl: in g/cm^3
    :return: density of mixture 1 and 2 in g/cm^3
    """
    density_mix_1 = 1/(((mass_LiOH_H2O/total_mass_mixture_1) * density_LiOH_H2O) +
                      ((mass_aluminium_hydroxide/total_mass_mixture_1) * density_aluminium_hydroxide) +
                      ((mass_H2O/total_mass_mixture_1) * density_H2O))
    density_mix_2= 1/(((mass_LiOH_H2O/total_mass_mixture_2) * density_LiOH_H2O) +
                      ((mass_aluminium_hydroxide/total_mass_mixture_2) * density_aluminium_hydroxide) +
                      ((mass_H2O/total_mass_mixture_2) * density_H2O) +
                      ((mass_HCl/total_mass_mixture_2) * density_HCl))
    return density_mix_1, density_mix_2

def Density_NaCl_sol(total_mass_mixture=None, mass_H2O=None, mass_NaCl=None, density_H2O=None,
                               density_NaCl=None):
    """

    :param total_mass_mixture: total mass of the 5wt% NaCl solution used for the column washing in g
    :param mass_H2O: i g
    :param mass_NaCl: in g
    :param density_H2O: in g/cm^3
    :param density_NaCl: in g/cm^3
    :return: density of the 5wt% NaCl solution
    """
    density = 1/(((mass_H2O/total_mass_mixture) * density_H2O) + (mass_NaCl/total_mass_mixture) * density_NaCl)
    return density


def Density_LiCl_sol(total_mass_mixture=None, mass_H2O=None, mass_LiCl=None, density_H2O=None,
                               density_LiCl=None):
    """

    :param total_mass_mixture: total mass of the density of the LiCl sol obtained after the column extraction (40 g/L) in g
    :param mass_H2O: in g
    :param mass_LiCl: in g
    :param density_H2O: in g/cm^3
    :param density_LiCl: in g/cm^3
    :return: density of the LiCl solution (40g/L) in g/cm^3
    """
    density = 1/(((mass_H2O/total_mass_mixture) * density_H2O) + (mass_LiCl/total_mass_mixture) * density_LiCl)
    return density


def Densitiy_LC_processing(total_mass_mixture=None, mass_LiCl=None, mass_Na2CO3=None, density_LiCl=None,
                                  density_Na2CO3=None):
    """

    :param total_mass_mixture: total mass of the reaction mixture for Li2CO3 production (LiCl + Na2CO3) in g
    :param mass_LiCl: in g
    :param mass_Na2CO3: in g
    :param density_LiCl: in g/cm^3
    :param density_Na2CO3: in g/cm^3
    :return: density of the Li2CO2 production mixture in g/cm^3
    """
    density = 1/(((mass_LiCl/total_mass_mixture) * density_LiCl) + ((mass_Na2CO3/total_mass_mixture) * density_Na2CO3))
    return density


def Density_LC_purification(total_mass_mixture=None, mass_Li2CO3=None, mass_CO2=None,  mass_H2O=None,
                            density_Li2CO3=None, density_CO2=None, density_H2O=None):
    """

    :param total_mass_mixture: total mass of the mixture for Li2CO3 purification (Li2CO3, H2O, CO2) in g
    :param mass_Li2CO3: in g
    :param mass_CO2: in g
    :param mass_H2O: in g
    :param density_Li2CO3: in g/cm^3
    :param density_CO2: in g/cm^3
    :param density_H2O: in g/cm^3
    :return: density of the Li2CO3 purification mixture in g/cm^3
    """
    density = 1/(((mass_Li2CO3/total_mass_mixture) * density_Li2CO3) + ((mass_CO2/total_mass_mixture) * density_CO2) +
                 ((mass_H2O/total_mass_mixture) * density_H2O))
    return density


def Tb_LC_purification(total_mass_mixture=None, mass_Li2CO3=None,  mass_H2O=None, Tb_Li2CO3=None, Tb_H2O=None):
    """

    :param total_mass_mixture: total amss of the mixture for Li2CO3 purification (Li2CO3, H2O, CO2) in g
    :param mass_Li2CO3: in g
    :param mass_H2O: in g
    :param Tb_Li2CO3: in K
    :param Tb_H2O: in K
    :return: boiling point of the Li2CO3 purification mixture in K
    """
    Tb = ((mass_Li2CO3/total_mass_mixture) * (Tb_Li2CO3) + ((mass_H2O/total_mass_mixture) * Tb_H2O))
    return Tb
