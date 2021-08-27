import numpy as np

def fixedBedReactor(reaction_temperature=None,
                    reaction_time=None,
                    surface_area=None,
                    thermal_conductivity=None,
                    wall_thickness=None
                    ):
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

def batchReactor(reaction_temperature=None,
                 reaction_time=None,
                 surface_area=None,
                 thermal_conductivity=None,
                 wall_thickness=None,
                 liq_density=None):
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

    qReactor = (k*A*t*T)/x  #Whr
    qReaction = qReactor/mass_reactants #Whr/gram

    return qReactor, qReaction

def tubeFurnace(reaction_temperature=None,
                reaction_time=None,
                reactor_volume=None,
                weighted_av_density=None):
    """

    :param reaction_temperature: degrees celcius
    :param reaction_time: time in hours
    :param reactor_volume: volume in cm^3
    :param weighted_av_density: weighted_av_density in g cm^(-3)
    :return:
    q reactor = power in Whrs
    q reaction = power in whrs per gram

    """
    critical_point = 1200 # degrees celcius
    capacity = 0.5  # %
    T = reaction_temperature  # degrees celcius
    t = reaction_time  # hours
    V = reactor_volume  # cm^3
    reactant_volume = V * capacity  # cm
    wad = weighted_av_density  # cm^(-3)
    mass_reactants = reactant_volume * wad  # g
    if T < critical_point:
        P = 1.25*T # Watts
    else:
        P = 6.25*T -6000  # Watts
    qReactor = (P * t) # Whr
    qReaction = qReactor/mass_reactants  # Whr/gram

    return qReactor, qReaction


def CSTR():  # TODO: implement this using: https://en.wikipedia.org/wiki/Continuous_stirred-tank_reactor

    return np.nan

def centrifuge(power_kw, time):
    power_consumption = power_kw * time
    return power_consumption



