from calculators import unitConversions


def Li2CO3_refinement(Li2CO3_tpy=None):
    """"
    :param Li2CO3_tpy: production of lithium carbonate in tons per year
    :return: an estimate of the masses of reactant used for the refinement of LiCl to Li2CO3

    2 LiCl + Na2CO2 --> Li2CO2 + 2 NaCl

    """
    YIELD = 0.7 #https://link.springer.com/content/pdf/10.1007/s11814-017-0172-4.pdf,
    mass_Li2CO3_gramms = unitConversions.grams(Li2CO3_tpy)
    moles_Li2CO3 = unitConversions.solidMol('Li2CO3', mass_Li2CO3_gramms)
    moles_LiCl = (2 * moles_Li2CO3)/YIELD
    mass_LiCl = unitConversions.solidMass('LiCl', moles_LiCl)
    mass_LiCl_tonnes = unitConversions.tonnes(mass_LiCl)
    moles_Na2CO3 = moles_Li2CO3 / YIELD
    mass_Na2CO3 = unitConversions.solidMass('Na2CO3', moles_Na2CO3)
    mass_Na2CO3_tonnes = unitConversions.tonnes(mass_Na2CO3)
    mass_reactants = {'LiCl':mass_LiCl_tonnes, 'Na2CO3':mass_Na2CO3_tonnes}
    return mass_reactants

if __name__ == '__main__':
    test = Li2CO3_refinement(20000)
    print(test)


