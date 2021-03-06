from Geothermal_IO.LDH import LC_processing # TODO: ask also why the * is not used here
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
        self.Li_extracted = ((self.brine.Li_conc_brine * ((self.plant.brine_flow_day * 10**3) / 24) *
                               self.plant.plant_uptime) * self.column.Li_recovery)   # in g/year
        self.Li_extracted_mol = uC.solidMol('Li', self.Li_extracted)
        self.LiCl_extracted_mol = self.Li_extracted_mol
        self.LiCl_extracted = uC.solidMass('LiCl', self.LiCl_extracted_mol)
        LC_processing_kwargs = {'LiCl': self.LiCl_extracted, 'Yield': self.LC_processing.Yield}
        self.LC_processing_reactants, self.LC_processing_product, self.LC_processing_waste = \
            LC_processing.Li2CO3_reaction(**LC_processing_kwargs)
        LC_purification_kwargs = {'Li2CO3_impure': self.LC_processing_product["Li2CO3"],
                                  'CO2_excess': self.LC_purification.CO2_excess,
                                  'Yield_forward': self.LC_purification.Yield_forward,
                                  'Yield_backward': self.LC_purification.Yield_backward}
        self.LC_purification_reactants, self.LC_purification_intermediate, self.LC_purification_product, \
        self.LC_purification_by_products = LC_purification.Purification_raction(**LC_purification_kwargs)
        return


    def __repr__(self):

        brine_flow_day_l = self.plant.brine_flow_day * 10 ** 3
        print_rf = f'For a daily brine flow of {brine_flow_day_l} l per day the total amount of pure lithium ' \
                   f'carbonate produced is: ' \
                   f'{uC.tonnes(self.LC_purification_product["pure Li2CO3"])} tpy \n' \
                   f'The amount of reactants required are for the production of Li3CO3 from the extracted LiCl are: \n'\
                   f'LiCl: {uC.tonnes(self.LC_processing_reactants["LiCl"])} tonnes \n' \
                   f'Na2CO3: {uC.tonnes(self.LC_processing_reactants["Na2CO3"])} tonnes \n' \
                   f'The amount of reactants required for the purification process are: \n' \
                   f'CO2: {uC.tonnes(self.LC_purification_reactants["CO2"])} tonnes \n' \
                   f'H2O: {self.LC_purification_reactants["H2O"] * 10**(-3)} l'

        output = f"{print_rf}"
        return output



if __name__ == '__main__':
    test = ReactantFlow()
    print(test)

