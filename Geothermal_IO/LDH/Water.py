import pandas as pd
from Geothermal_IO.LDH import Sor_Syn_Chemicals
from Geothermal_IO.LDH import Column_Washing
from Geothermal_IO.LDH import Column_Stripping
from Geothermal_IO.LDH import LC_processing
from Geothermal_IO.LDH import LC_purification
from Geothermal_extraction import Reactant_flow

class Water_att(object):
    def __init__(self):
        self.chemicals = Sor_Syn_Chemicals.SorbentSynthesisChemicals_att()
        self.washing = Column_Washing.ColumnExtractionWashing()
        self.stripping = Column_Stripping.ColumnExtractionStripping()
        self.LC_processing = LC_processing.LiCarbonateProcessing_att()
        self.LC_purification = LC_purification.LiCarbonatePurification_att()
        self.reactant_flow = Reactant_flow.ReactantFlow()
        self.df = pd.read_excel(r'..\..\data\LDH_attributes.xlsx',
                                sheet_name='water', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.sor_syn_washing = self.df['value'].loc['sor_syn_washing']
        self.LC_purification_washing = self.df['value'].loc['LC_purification_washing']
        self.LC_processing_aq = self.df['value'].loc['LC_processing_aq']
        self.total_water_usage = ((self.chemicals.mass_H2O + self.reactant_flow.LC_purification_reactants['H2O'])
                                  * 10**(-3)) + self.sor_syn_washing * self.chemicals.mass_sorbent_grams + \
                                 self.LC_purification_washing * \
                                 self.reactant_flow.LC_purification_product['pure Li2CO3'] + self.LC_processing_aq * \
                                 self.reactant_flow.LC_processing_reactants['Na2CO3'] + \
                                 self.washing.H2O_washing_total + self.stripping.H2O_stripping_total

        return

if __name__ == '__main__':
    test = Water_att()
    print(test)
