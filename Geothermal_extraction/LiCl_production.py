from Geothermal_IO.LDH import *

class LiClExtraction(object):
    def __init__(self):
        self.brine = Brine.Brine_att()
        self.column_washing = Column_Washing.ColumnExtractionWashing()
        self.column_stripping = Column_Stripping.ColumnExtractionStripping()
        self.FO = ForwardOsmosis.ForwardOsmosis()
        self.column = Column.Column_att()
        self.plant = Plant.Plant_att()
        self.LiCl_extracted_day = self.brine.Li_conc_brine * self.plant.brine_flow_day * 10**(3) * \
                                  self.column.Li_recovery * self.FO.efficiency
        self.LiCl_extracted_year = (self.LiCl_extracted_day / 24) * self.plant.plant_uptime
        self.time_washing = self.column.washing_flow_rate * self.column_washing.H2O_washing_total

if __name__ == '__main__':
    test = LiClExtraction()
    print(test)
