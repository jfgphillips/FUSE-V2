

def stirring_energy(impeller_power_number, impeller_diameter, agitator_rotational_speed, density, stirring_time):
    """
    source: Huang 2021 life cycle assessment and techno-echonomic assessment of lithium recovery from geothermal brine
    :param impeller_power_number: power number of the impeller (axial flow = 0.79)
    :param impeller_diameter: diameter of the impeller
    :param agitator_rotational_speed: rotational speed of the agitator
    :param density: density of the reaction mixture to be stirred
    :param stirring_time: stirring time of the mixture
    :return: stirring energy (E_stirr) in Joules
    """

    efficiency = 0.9 # taken from source
    N_p = impeller_power_number
    d = impeller_diameter # meter
    N = agitator_rotational_speed # 1/seconds
    p = density # kg/m^3
    T = stirring_time # seconds
    n_stirr = efficiency

    E_stirr = (N_p * p * N**(3) * d**(5) * T)/n_stirr

    return(E_stirr)


def drying_energy(heat_capacity_solution, mass_solution, boiling_temperature, starting_temperature,evaporation_enthalpy,mass_vapour):
    """
    source: Huang 2021 life cycle assessment and techno-echonomic assessment of lithium recovery from geothermal brine
    :param heat_capacity_solution: heat capacity of the solution
    :param mass_solution: mass of the solution
    :param boiling_temperature: boiling temperature of the solution
    :param starting_temperature: starting temperature
    :param evaporation_enthalpy: enthalpy of evaporation
    :param mass_vapour: mass of liquid to be vapourised
    :return: drying energy (Q_drying) in Joules
    """

    efficiency = 0.8 # taken from source
    C_p_liq = heat_capacity_solution # J/(kg*K)
    m_liq = mass_solution # kg
    T_boil = boiling_temperature # K
    T_0 = boiling_temperature # K
    H_vap = evaporation_enthalpy # J/kg
    m_vap = mass_vapour # kg
    n_dry = efficiency

    Q_drying = (C_p_liq * m_liq * (T_boil - T_0) + H_vap * m_vap) / n_dry

    return(Q_drying)


def filtration_energy(tonnes):
    """
    source: Huang 2021 life cycle assessment and techno-echonomic assessment of lithium recovery from geothermal brine
    :param tonnes: mass of mixture in tonnes
    :return: filtration energy
    """

    energy = 10 # kWh/ton; upper limit of 5.5 - 10 kWh/ton given in source
    Q_filtration = energy * tonnes
    return(Q_filtration)


def grinding_energy(tonnes):
    """
    source: Huang 2021 life cycle assessment and techno-echonomic assessment of lithium recovery from geothermal brine
    :param tonnes: mass of the mixture in tonnes
    :return: grinding energy
    """

    energy = 16 # kWh/ton, upper limit of 8 - 16 kWh/ton given in source
    Q_grinding = energy * tonnes
    return(Q_grinding)
