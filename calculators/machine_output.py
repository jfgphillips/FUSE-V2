
def machine_output_calc(required_tpy=None, mining_package=None, conversion_efficiency=None, ore_grade=None, production_hrs_wk=None):
    """

    :param required_tpy:
    :param mining_package:
    :param conversion_efficiency:
    :param ore_grade:
    :param production_hrs_wk:
    :return:
    """

    ore_tpy = required_tpy / conversion_efficiency
    ore_and_rock_tpy = ore_tpy / ore_grade
    ore_and_rock_tpy_per_miner = ore_and_rock_tpy / mining_package
    ore_and_rock_tpm_per_miner = ore_and_rock_tpy_per_miner / 52
    #print(production_hrs_wk)
    ore_and_rock_tph_per_miner = ore_and_rock_tpm_per_miner / production_hrs_wk


    # print("The output of each mining package per hour is: ", ore_and_rock_tph_per_miner,'tph \n',"The output of each mining package per week is: ", ore_and_rock_tph_per_miner*production_hrs_wk, 'tpwk')
    return ore_and_rock_tph_per_miner
