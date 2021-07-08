def drum_hoist(hoisting_dist_m, production_avaliability, production_capacity_tpd):
    """
    :param hoisting_dist_m: shaft distance in meters
    :param production_avaliability: how much of the week the shaft is availiable for haulage ops
    :param production_capacity_tpd: mines total production capacity in a day
    :return: skip capacity required for haulage
    """
    optimum_line_spd = 0.405 * hoisting_dist_m**(1/2)
    cycle_time = hoisting_dist_m/optimum_line_spd + 40  # see formula page 119-120 miners handbook
    trips_hr = 3600/cycle_time
    trips_day = trips_hr*24*production_avaliability
    skip_capacity = production_capacity_tpd/trips_day

    return skip_capacity