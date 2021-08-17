from Geothermal_IO.LDH import LC_processing
from Geothermal_IO.LDH import LC_purification
from Geothermal_IO.LDH import Column
from Geothermal_IO.LDH import Brine
from Geothermal_IO.LDH import Plant
from Geothermal_IO.LDH import ForwardOsmosis
from calculators import unitConversions as uC

class ReactantFlow(object):
    def __init__(self):
        self.LC_processing = LC_processing.LiCarbonateProcessing_att()
        self.LC_purification = LC_purification.LiCarbonatePurification_att()
        self.column = Column.Column_att()
        self.brine = Brine.Brine_att()
        self.plant = Plant.Plant_att()
        self.FO = ForwardOsmosis.ForwardOsmosis()
        self.LiCl_extracted = uC.tonnes(self.brine.Li_conc_brine * ((self.plant.brine_flow_day * 10**(3))/ 24) *\
                              self.column.Li_recovery * self.FO.efficiency * self.plant.plant_uptime)
        LC_processing_kwargs = {'LiCl': self.LiCl_extracted, 'Yield': self.LC_processing.Yield}
        self.LC_processing_reactants, self.LC_processing_product, self.LC_processing_waste = \
            LC_processing.Li2CO3_reaction(**LC_processing_kwargs)
        LC_purification_kwargs = {'Li2CO3_impure': self.LC_processing_product["Li2CO3"],
                                  'CO2_excess': self.LC_purification.CO2_excess,
                                  'Yield_forward': self.LC_purification.Yield_forward,
                                  'Yield_backward': self.LC_purification.Yield_backward}
        self.LC_purification_reactants, self.LC_purification_intermediate, self.LC_purification_product, \
        self.LC_purification_by_products = LC_purification.Purification_raction(**LC_purification_kwargs)
        self.print_dict_production = self.dict_reactants_processing()
        self.print_dict_purification = self.dict_reactants_purification()


    def __repr__(self):
        newline = "\n"
        brine_flow_day_l = self.plant.brine_flow_day * 10**(3)
        print_statement_1 = f'For a daily brine flow of {brine_flow_day_l} l per day the total amount of pure lithium ' \
                          f'carbonate produced is ' \
                          f'{uC.tonnes(self.LC_purification_product["pure Li2CO3"])} tpy \n' \
                          f'The amount of reactants required are for the production of Li3CO3 from the extracted LiCl are:'
        print_format_1 = f'{newline.join(f"{key}: {uC.tonnes(value)} tonnes" for key, value in self.print_dict_production.items())} '
        print_statement_2 = f'The amount of reactants required for the purification process are:'
        print_format_2 = f'{newline.join(f"{key}: {uC.tonnes(value)} tonnes" for key, value in self.print_dict_purification.items())} '
        output = f"{print_statement_1}\n" \
                 f"{print_format_1}\n" \
                 f"{print_statement_2}\n" \
                 f"{print_format_2}"
        return output


    def dict_reactants_processing(self):
        dict_processing = {**self.LC_processing_reactants}
        return dict_processing

    def dict_reactants_purification(self):
        dict_purification = {**self.LC_purification_reactants}
        return dict_purification


if __name__ == '__main__':
    test = ReactantFlow()
    print(test)

