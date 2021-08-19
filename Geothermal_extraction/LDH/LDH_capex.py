from Geothermal_IO.LDH import *


class LDH_capex(object):
    def __init__(self):
        self.equipment = Equipment.Equipment_att()
        self.capex = Capex.CapexCostFactors()
        self.equipment_cost = self.Equipment_costs()
        self.FCC, self.TCI = self.Capital_Costs()
        return

    def __repr__(self):
        print_capex = f'The total CAPEX for the addition of a lithium chloride extraction and lithium carbonate ' \
                      f'production plant to a already existing geothermal power plant are:\n' \
                      f'{self.TCI} $'

        output = f"{print_capex}"
        return output

    def Equipment_costs(self):

        cost_dict = {}
        for equipment_item, kwargs in self.equipment.equipment_dict.items():
            if equipment_item == "Pipes":
                temp_kwargs = {key:val for key, val in kwargs.items() if key != 'amount'}
                cost_dict[f'cost_{equipment_item}'] = Equipment.cost_equipment(**temp_kwargs)
            else:
                cost_dict[f'cost_{equipment_item}'] = Equipment.cost_equipment(**kwargs)

        print(cost_dict)


        """
        reactor_1_kwargs = {'FOB': self.equipment.reactor_1_FOB,
                            'CEPCI_base': self.equipment.CEPCI_base,
                            'size_base': self.equipment.reactor_1_size_base,
                            'size_ref': self.equipment.reactor_1_size_ref,
                            'size_factor': self.equipment.reactor_1_size_factor}
        cost_reactor_1 = Equipment.cost_equipment(**reactor_1_kwargs)

        reactor_2_kwargs = {'FOB': self.equipment.reactor_2_FOB,
                            'CEPCI_base': self.equipment.CEPCI_base,
                            'size_base': self.equipment.reactor_2_size_base,
                            'size_ref': self.equipment.reactor_2_size_ref,
                            'size_factor': self.equipment.reactor_2_size_factor}
        cost_reactor_2 = Equipment.cost_equipment(**reactor_2_kwargs)

        reactor_3_kwargs = {'FOB': self.equipment.reactor_3_FOB,
                            'CEPCI_base': self.equipment.CEPCI_base,
                            'size_base': self.equipment.reactor_3_size_base,
                            'size_ref': self.equipment.reactor_3_size_ref,
                            'size_factor': self.equipment.reactor_3_size_factor}
        cost_reactor_3 = Equipment.cost_equipment(**reactor_3_kwargs)

        filter_1_kwargs = {'FOB': self.equipment.filter_1_FOB,
                           'CEPCI_base': self.equipment.CEPCI_base,
                           'size_base': self.equipment.filter_1_size_base,
                           'size_ref': self.equipment.filter_1_size_ref,
                           'size_factor': self.equipment.filter_1_size_factor}
        cost_filter_1 = Equipment.cost_equipment(**filter_1_kwargs)

        filter_2_kwargs = {'FOB': self.equipment.filter_2_FOB,
                           'CEPCI_base': self.equipment.CEPCI_base,
                           'size_base': self.equipment.filter_2_size_base,
                           'size_ref': self.equipment.filter_2_size_ref,
                           'size_factor': self.equipment.filter_2_size_factor}
        cost_filter_2 = Equipment.cost_equipment(**filter_2_kwargs)

        grinder_kwargs = {'FOB': self.equipment.grinder_FOB,
                          'CEPCI_base': self.equipment.CEPCI_base,
                          'size_base': self.equipment.grinder_size_base,
                          'size_ref': self.equipment.grinder_size_ref,
                          'size_factor': self.equipment.grinder_size_factor}
        cost_grinder = Equipment.cost_equipment(**grinder_kwargs)

        EC_kwargs = {'FOB': self.equipment.EC_FOB,
                     'CEPCI_base': self.equipment.CEPCI_base,
                     'size_base': self.equipment.EC_size_base,
                     'size_ref': self.equipment.EC_size_ref,
                     'size_factor': self.equipment.EC_size_factor}
        cost_EC = Equipment.cost_equipment(**EC_kwargs)

        FO_kwargs = {'FOB': self.equipment.FO_FOB,
                     'CEPCI_base': self.equipment.CEPCI_base,
                     'size_base': self.equipment.FO_size_base,
                     'size_ref': self.equipment.FO_size_ref,
                     'size_factor': self.equipment.FO_size_factor}
        cost_FO = Equipment.cost_equipment(**FO_kwargs)

        IEC_kwargs = {'FOB': self.equipment.IEC_FOB,
                      'CEPCI_base': self.equipment.CEPCI_base,
                      'size_base': self.equipment.IEC_size_base,
                      'size_ref': self.equipment.IEC_size_ref,
                      'size_factor': self.equipment.IEC_size_factor}
        cost_IEC = Equipment.cost_equipment(**IEC_kwargs)

        resin_kwargs = {'FOB': self.equipment.resin_FOB,
                        'CEPCI_base': self.equipment.CEPCI_base,
                        'size_base': self.equipment.resin_size_base,
                        'size_ref': self.equipment.resin_size_ref,
                        'size_factor': self.equipment.resin_size_factor}
        cost_resin = Equipment.cost_equipment(**resin_kwargs)

        dryer_kwargs = {'FOB': self.equipment.dryer_FOB,
                        'CEPCI_base': self.equipment.CEPCI_base,
                        'size_base': self.equipment.dryer_size_base,
                        'size_ref': self.equipment.dryer_size_ref,
                        'size_factor': self.equipment.dryer_size_factor}
        cost_dryer = Equipment.cost_equipment(**dryer_kwargs)

        pumps_kwargs = {'FOB': self.equipment.pumps_FOB,
                        'CEPCI_base': self.equipment.CEPCI_base,
                        'size_base': self.equipment.pumps_size_base,
                        'size_ref': self.equipment.pumps_size_ref,
                        'size_factor': self.equipment.pumps_size_factor}
        cost_pumps = Equipment.cost_equipment(**pumps_kwargs)

        valves_kwargs = {'FOB': self.equipment.valves_FOB,
                         'CEPCI_base': self.equipment.CEPCI_base,
                         'size_base': self.equipment.valves_size_base,
                         'size_ref': self.equipment.valves_size_ref,
                         'size_factor': self.equipment.valves_size_factor}
        cost_valves = Equipment.cost_equipment(**valves_kwargs)

        pipes_kwargs = {'FOB': self.equipment.pipes_FOB,
                        'CEPCI_base': self.equipment.CEPCI_base,
                        'size_base': self.equipment.pipes_size_base,
                        'size_ref': self.equipment.pipes_size_ref,
                        'size_factor': self.equipment.pipes_size_factor}
        cost_pipes = Equipment.cost_equipment(**pipes_kwargs)
        """

        equipment_cost = 0# cost_reactor_1 + cost_reactor_2 + cost_reactor_3 + cost_filter_1 + cost_filter_2 + \
                          # cost_grinder + cost_EC + cost_FO + cost_IEC + cost_resin + cost_dryer + cost_pumps + \
                          # cost_valves + cost_pipes

        return equipment_cost

    def Capital_Costs(self):
        cost_installation = self.capex.installation * self.equipment_cost
        cost_IC = self.capex.IC * self.equipment_cost  # Instrumentation and Control
        cost_EEM = self.capex.EEM * self.equipment_cost  # Electric Equipment and Control
        cost_buildings = self.capex.buildings * self.equipment_cost
        cost_service_facilities = self.capex.service_facilities * self.equipment_cost
        depreciable_costs = cost_installation + cost_IC + cost_EEM + cost_buildings + cost_service_facilities

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
