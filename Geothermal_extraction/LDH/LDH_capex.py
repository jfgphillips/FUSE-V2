from Geothermal_IO.LDH import *
import outputs.plot_master as pM
import pandas as pd


class LDH_capex(object):
    def __init__(self):
        self.equipment = Equipment.Equipment_att()
        self.capex = Capex.CapexCostFactors()
        self.equipment_cost_df = self.Equipment_costs()
        self.equipment_cost = self.equipment_cost_df.sum()
        self.FCC, self.TCI = self.Capital_Costs()
        self.plot = pM.plot(self.equipment_cost_df, "cost eqpmnt")
        return

    def __repr__(self):
        print_capex = f'The total CAPEX for the addition of a lithium chloride extraction and lithium carbonate ' \
                      f'production plant to a already existing geothermal power plant are:\n' \
                      f'{self.TCI} $'

        output = f"{print_capex}\n" \
                 f"{self.FCC}"
        return output

    def Equipment_costs(self):
        """
        Source Huang 2021
        :return: total cost of equipment for the geothermal lithium extraction plant in $
        """

        cost_dict = {}
        for equipment_item, kwargs in self.equipment.equipment_dict.items():
            if equipment_item == "Pipes":
                temp_kwargs = {key:val for key, val in kwargs.items() if key != 'amount'}
                cost_dict[f'cost_{equipment_item}'] = Equipment.cost_equipment(**temp_kwargs)
            else:
                cost_dict[f'cost_{equipment_item}'] = Equipment.cost_equipment(**kwargs)

        cost_df = pd.DataFrame.from_dict(cost_dict, orient='index')
        cost_df.rename({0:"$ cost"}, axis=1, inplace=True)

        return cost_df

    def Capital_Costs(self):
        """
        Source Huang 2021
        :return: Total Capital Cost (TCC) and Total Capital Investment (TCI) for the geothermal lithium extraction plant
        in $
        """
        cost_installation = self.capex.installation * self.equipment_cost
        cost_IC = self.capex.IC * self.equipment_cost  # Instrumentation and Control
        cost_EEM = self.capex.EEM * self.equipment_cost  # Electric Equipment and Control
        cost_buildings = self.capex.buildings * self.equipment_cost
        cost_service_facilities = self.capex.service_facilities * self.equipment_cost
        depreciable_costs = self.equipment_cost + cost_installation + cost_IC + cost_EEM + cost_buildings + \
                            cost_service_facilities

        cost_land = self.capex.land * self.equipment_cost
        cost_FSI = self.capex.FSI * self.equipment_cost  # Facility Site Improvement
        non_depreciable_costs = cost_land + cost_FSI

        FCC_contingency = self.capex.FCC_contingency * (depreciable_costs + non_depreciable_costs)
        FCC = depreciable_costs + non_depreciable_costs + FCC_contingency  # Fixed Capital Cost

        working_capital = self.capex.working_capital * FCC
        TCI = FCC + working_capital  # Total Capital Investment

        return FCC, TCI


if __name__ == '__main__':
    test = LDH_capex()
    print(test)
