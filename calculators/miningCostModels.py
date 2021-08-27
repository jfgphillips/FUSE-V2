import pandas as pd

def room_and_pillar_shaft_entry(production_capacity_tpd, mining_method):
    """
    Montana university simplified cost modesl for underground mine evalulation
    :param production_capacity_tpd: integer ore production capacity
    :param mining_method: string: label for the dataframe index
    :return:
    """
    def get_opex():
        eqpmnt_op = 5.84 * production_capacity_tpd ** (-0.0766)
        supplies = 94.2 * production_capacity_tpd ** (-0.326)
        hourly_labour = 606 * production_capacity_tpd ** (-0.475)
        admin = 469 * production_capacity_tpd ** (-0.524)

        op_subtot = eqpmnt_op + supplies + hourly_labour + admin
        provision = op_subtot * 0.10
        opex = op_subtot + provision

        opex_df = pd.DataFrame(data={"equipment operation": [eqpmnt_op],
                                     "supplies": [supplies],
                                     "hourly labour": [hourly_labour],
                                     "administration": [admin],
                                     "sundries": [provision],
                                     "total opex": [opex]},
                               index=[mining_method])
        return opex, opex_df

    def get_capex(op_ex):
        eqpmnt_purch = 1432700 * production_capacity_tpd ** 0.417
        preprod_und_excav = 135000 * production_capacity_tpd ** 0.584
        surf_facilities = 271800 * production_capacity_tpd ** 0.423
        cap_subtot = eqpmnt_purch + preprod_und_excav + surf_facilities
        engineering_and_management = cap_subtot * 0.13
        contingency = cap_subtot * 0.2
        working_capital = op_ex * production_capacity_tpd * 58
        capex = cap_subtot + engineering_and_management + contingency + working_capital
        capex_df = pd.DataFrame(data={"equipment purchase": [eqpmnt_purch],
                                      "preproduction underground excavation": [preprod_und_excav],
                                      "surface facilities": [surf_facilities],
                                      "engineering and management": [engineering_and_management],
                                      "contingency": [contingency],
                                      "working capital": [working_capital],
                                      "total capex": [capex]},
                                index=[mining_method])
        return capex_df

    operational_expenses, operational_expenses_df = get_opex()
    capital_expenses_df = get_capex(operational_expenses)
    return operational_expenses_df, capital_expenses_df


def block_caving_shaft_entry(production_capacity_tpd, mining_method):
    def get_opex():
        eqpmnt_op = 0.442 * production_capacity_tpd ** (0.180)
        supplies = 111 * production_capacity_tpd ** (-0.475)
        hourly_labour = 150 * production_capacity_tpd ** (-0.368)
        admin = 79.9 * production_capacity_tpd ** (-0.355)

        op_subtot = eqpmnt_op + supplies + hourly_labour + admin
        provision = op_subtot * 0.10
        opex = op_subtot + provision

        opex_df = pd.DataFrame(data={"equipment operation": [eqpmnt_op],
                                     "supplies": [supplies],
                                     "hourly labour": [hourly_labour],
                                     "administration": [admin],
                                     "sundries": [provision],
                                     "total opex": [opex]},
                               index=[mining_method])
        return opex, opex_df

    def get_capex(op_ex):
        eqpmnt_purch = 31600 * production_capacity_tpd ** 0.700
        preprod_und_excav = 135000 * production_capacity_tpd ** 0.584 # deviation from the equation as the preprod is same
        surf_facilities = 114900 * production_capacity_tpd ** 0.488
        cap_subtot = eqpmnt_purch + preprod_und_excav + surf_facilities
        engineering_and_management = cap_subtot * 0.17
        contingency = cap_subtot * 0.2
        working_capital = op_ex * production_capacity_tpd * 61
        capex = cap_subtot + engineering_and_management + contingency + working_capital
        capex_df = pd.DataFrame(data={"equipment purchase": [eqpmnt_purch],
                                      "preproduction underground excavation": [preprod_und_excav],
                                      "surface facilities": [surf_facilities],
                                      "engineering and management": [engineering_and_management],
                                      "contingency": [contingency],
                                      "working capital": [working_capital],
                                      "total capex": [capex]},
                                index=[mining_method])
        return capex_df

    operational_expenses, operational_expenses_df = get_opex()
    capital_expenses_df = get_capex(operational_expenses)
    return operational_expenses_df, capital_expenses_df