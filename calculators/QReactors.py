import numpy as np

def fixedBedReactor(reaction_temperature, reaction_time, surface_area,thermal_conductivity, wall_thickness):
    """
    Sharma 2020 towards sustainable batteries d0ee02511a1
    :param reaction_temperature:
    :param reaction_time:
    :param surface_area:
    :param thermal_conductivity:
    :param wall_thickness:
    :return:
    """

    T = reaction_temperature  # degrees celcius
    t = reaction_time  # s
    A = surface_area  # m^2
    k = thermal_conductivity  # W/(m*K)
    x = wall_thickness  # m
    Qreactor = (k*A*t(T-25))/x

    return Qreactor

def batchReactor(reaction_temperature, reaction_time, surface_area,thermal_conductivity, wall_thickness, liq_density):
    """
    Sharma 2020 towards sustainable batteries d0ee02511a1
    :param reaction_temperature:
    :param reaction_time:
    :param surface_area:
    :param thermal_conductivity:
    :param wall_thickness:
    :return:
    """
    capacity = 0.5
    P = liq_density  # kg/l
    mass_reactants = capacity * P  # kg

    T = (reaction_temperature - 25) + 273.15  # kelvin
    t = reaction_time  # hr
    A = surface_area  # m^2
    k = thermal_conductivity  # W/(m*K)
    x = wall_thickness  # m

    Qreactor = (k*A*t(T-25))/x  #Whr
    qReaction = Qreactor/mass_reactants #Whr/gram

    return qReaction

def tubeFurnace(reaction_temperature,reaction_time, reactor_diameter, reactor_length, weighted_av_density): #TODO: change reactor diameter and lenghh to volume
    critical_point = 1200 # degrees celcius
    capacity = 0.5  # %
    T = reaction_temperature  # degrees celcius
    t = reaction_time  # hours
    r = reactor_diameter/2  # cm
    l = reactor_length  # cm
    V = np.pi * (r ** 2) * l  # cm
    reactant_volume = V * capacity  # cm
    wad = weighted_av_density  # cm^(-3)
    mass_reactants = reactant_volume * wad  # g
    if T < critical_point:
        P = 1.25*T # Watts
    else:
        P = 6.25*T -6000  # Watts
    qReactor = (P * t) # Whr
    qReaction = qReactor/mass_reactants  # Whr/gram

    return qReaction





