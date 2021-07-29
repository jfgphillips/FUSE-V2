
def machine_output_calc(soda_ash_tpy, mining_package, conversion_efficiency, mineral_grade, production_hrs_wk):
    """
    :param soda_ash_tpy:
    :param mining_package: how many mining packages involved
           e.g
           bolter continuous miner shuttle
           longwall shearer + 2 borer miners + 1 bleeder + shuttle cars
    :return: an estimate of rock and ore tonnes per hour per mining package
    """

    ore_tpy = soda_ash_tpy/conversion_efficiency
    ore_and_rock_tpy = ore_tpy/mineral_grade
    ore_and_rock_tpy_per_miner = ore_and_rock_tpy / mining_package
    ore_and_rock_tpm_per_miner = ore_and_rock_tpy_per_miner / 52
    #print(production_hrs_wk)
    ore_and_rock_tph_per_miner = ore_and_rock_tpm_per_miner / production_hrs_wk


    # print("The output of each mining package per hour is: ", ore_and_rock_tph_per_miner,'tph \n',"The output of each mining package per week is: ", ore_and_rock_tph_per_miner*production_hrs_wk, 'tpwk')
    return ore_and_rock_tph_per_miner
