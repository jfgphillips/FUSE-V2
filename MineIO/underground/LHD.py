from calculators.QMachines import haulageVehicle

class LHD_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'data/mine_attributes.xlsx', sheet_name="LHD", skiprows=1)
        self.df.set_index('key', inplace=True)


