from molmass import Formula


def solidMol(formula, mass):
    """
    solid conversion from mass to mol
    :param formula: string formula
    :param mass: units grams
    :return: moles units mol
    """
    mr = Formula(formula).mass
    mol = mass/mr
    return mol


def solidMass(formula, mol):
    """
    solid conversion from mol to mass
    :param formula: string formula
    :param mol: moles units mol
    :return: mass units grams
    """
    mr = Formula(formula).mass
    mass = mr*mol
    return mass


def liqMol(concentration, volume):
    """
    liquid conversion from concentration to mol
    :param concentration: mol dm^(-3)
    :param volume: cm^3
    :return: moles units moles
    """
    mol = (concentration * volume)/1000
    return mol


def liqConcentration(mol, volume):
    """
    liquid conversion from mol to concentration
    :param mol: units mol
    :param volume: units cm^3
    :return: concentration units mol dm^(-3)
    """
    concentration = (mol * 1000)/volume
    return concentration


def liqVolume(mol, concentration):
    """
    liquid conversion from mol to volume
    :param mol: units mol
    :param concentration: units mol dm^(-3)
    :return: volume units cm^3
    """
    volume = (mol * 1000)/concentration
    return volume

