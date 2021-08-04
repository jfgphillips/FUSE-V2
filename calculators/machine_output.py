
def machine_output_calc(required_tpy=None,
                        mining_package=None,
                        conversion_efficiency=None,
                        ore_grade=None,
                        production_hrs_wk=None):
    """

    :param required_tpy: required tonnes of refined product a year
    :param mining_package: number of mining packages operating on the mine
    :param conversion_efficiency: from ore + rock to product conversion
    :param ore_grade: the percentage of ore in the mineral itself e.g. trona = 90%
    :param production_hrs_wk: how many hours the mine operates a week
    :return:amount of ore plus rock mined by each package per hour
            to achieve the required tonnes per year
    """

    ore_tpy = required_tpy / conversion_efficiency
    ore_and_rock_tpy = ore_tpy / ore_grade
    ore_and_rock_tpy_per_miner = ore_and_rock_tpy / mining_package
    ore_and_rock_tpm_per_miner = ore_and_rock_tpy_per_miner / 52
    #print(production_hrs_wk)
    ore_and_rock_tph_per_miner = ore_and_rock_tpm_per_miner / production_hrs_wk


    # print("The output of each mining package per hour is: ", ore_and_rock_tph_per_miner,'tph \n',"The output of each mining package per week is: ", ore_and_rock_tph_per_miner*production_hrs_wk, 'tpwk')
    return ore_and_rock_tph_per_miner
