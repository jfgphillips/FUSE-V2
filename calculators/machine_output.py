
def machine_output_calc(soda_ash_tpy, mining_package):
    """
    :param soda_ash_tpy:
    :param mining_package: how many mining packages involved
           e.g
           bolter continuous miner shuttle
           longwall shearer + 2 borer miners + 1 bleeder + shuttle cars
    :return: an estimate of rock and ore tonnes per hour per mining package
    """
    SODA_ASH_CONVERSION_EFFICIENCY = 0.588
    DEPOSIT_MINERAL_GRADE = 0.9
    PRODUCTION_HRS_wk = 110

    ore_tpy = soda_ash_tpy/SODA_ASH_CONVERSION_EFFICIENCY
    ore_and_rock_tpy = ore_tpy/DEPOSIT_MINERAL_GRADE
    ore_and_rock_tpy_per_miner = ore_and_rock_tpy / mining_package
    ore_and_rock_tpm_per_miner = ore_and_rock_tpy_per_miner/52
    ore_and_rock_tph_per_miner = ore_and_rock_tpm_per_miner/PRODUCTION_HRS_wk
    print("The output of each mining package per hour is: ", ore_and_rock_tph_per_miner,'tph \n',"The output of each mining package per week is: ", ore_and_rock_tph_per_miner*PRODUCTION_HRS_wk, 'tpwk')
    return ore_and_rock_tph_per_miner

