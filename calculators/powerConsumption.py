def power_consumption(motor_kW, running_load, nameplate_rating, per_unit_run_time, per_unit_time, op_hrs):
    """
    :param motor_kW: engine horse power
    :param running_load: how much the unit is carrying
    :param nameplate_rating: max operating rating
    :param per_unit_run_time: how much the unit is being run
    :param per_unit_time: per specified time (standardised hrs)
    :param op_hrs: intervals of a day, week or month

    :return: unit_energy_consumption: Energy/month (kW hours)
    """
    # motor_kW = motor_HP * 0.746  # conversion factor HP -> kW
    load_factor = running_load/nameplate_rating  # what capacity is equipment being used
    utilisation_factor = per_unit_run_time/per_unit_time
    unit_energy_consumption = motor_kW * load_factor * utilisation_factor * op_hrs  # standardised value

    return unit_energy_consumption
