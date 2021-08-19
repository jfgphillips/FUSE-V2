import pandas as pd


class Equipment_att(object):  # TODO: Chantal ask if there is a more efficient way of doing this
    """
    e.g.
    for i in machine_names:
        for j in dict_titles:
            self.i = {j:self.df[j].loc[i]}
    self.reactor_1_att = {'FOB':self.df['FOB'].loc['Reactor_1']
    """

    def __init__(self):
        self.df_full = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                     sheet_name="equipment", skiprows=1)
        self.df_full.set_index('key', inplace=True)
        self.df = self.df_full[self.df_full.index.notnull()]
        idx_names = list(self.df.index)
        print(idx_names)
        bad_idx = ['CEPCI_base', 'Belt_Conveyor']
        machine_names = list(set(idx_names) - set(bad_idx))
        dict_titles = ["FOB", 'size_base', 'size_ref', 'n']
        self.equipment_dict = {}
        for i in machine_names:
            default_values = {**{j: self.df[j].loc[i] for j in dict_titles},
                              **{'CEPCI_base': self.df['FOB'].loc['CEPCI_base']}}
            if i == "Pipes":
                add_on = {'amount': self.df['amount'].loc['Pipes']}
                self.equipment_dict[i] = {**default_values, **add_on}
            else:
                self.equipment_dict[i] = default_values

        print(self.equipment_dict['Pipes'])


        """
        self.reactor_1_FOB = self.df['FOB'].loc['Reactor_1']
        self.reactor_1_size_base = self.df['size base'].loc['Reactor_1']
        self.reactor_1_size_ref = self.df['size ref'].loc['Reactor_1']
        self.reactor_1_size_factor = self.df['n'].loc['Reactor_1']
        self.filter_1_FOB = self.df['FOB'].loc['Filter_1']
        self.filter_1_size_base = self.df['size base'].loc['Filter_1']
        self.filter_1_size_ref = self.df['size ref'].loc['Filter_1']
        self.filter_1_size_factor = self.df['n'].loc['Filter_1']
        self.grinder_FOB = self.df['FOB'].loc['Grinder']
        self.grinder_size_base = self.df['size base'].loc['Grinder']
        self.grinder_size_ref = self.df['size ref'].loc['Grinder']
        self.grinder_size_factor = self.df['n'].loc['Grinder']
        self.grinder_FOB = self.df['FOB'].loc['Grinder']
        self.grinder_size_base = self.df['size base'].loc['Grinder']
        self.grinder_size_ref = self.df['size ref'].loc['Grinder']
        self.grinder_size_factor = self.df['n'].loc['Grinder']
        self.EC_FOB = self.df['FOB'].loc['Extraction_column']
        self.EC_size_base = self.df['size base'].loc['Extraction_column']
        self.EC_size_ref = self.df['size ref'].loc['Extraction_column']
        self.EC_size_factor = self.df['n'].loc['Extraction_column']
        self.FO_FOB = self.df['FOB'].loc['FO_unit']
        self.FO_size_base = self.df['size base'].loc['FO_unit']
        self.FO_size_ref = self.df['size ref'].loc['FO_unit']
        self.FO_size_factor = self.df['n'].loc['FO_unit']
        self.reactor_2_FOB = self.df['FOB'].loc['Reactor_2']
        self.reactor_2_size_base = self.df['size base'].loc['Reactor_2']
        self.reactor_2_size_ref = self.df['size ref'].loc['Reactor_2']
        self.reactor_2_size_factor = self.df['n'].loc['Reactor_2']
        self.filter_2_FOB = self.df['FOB'].loc['Filter_2']
        self.filter_2_size_base = self.df['size base'].loc['Filter_2']
        self.filter_2_size_ref = self.df['size ref'].loc['Filter_2']
        self.filter_2_size_factor = self.df['n'].loc['Filter_2']
        self.reactor_3_FOB = self.df['FOB'].loc['Reactor_3']
        self.reactor_3_size_base = self.df['size base'].loc['Reactor_3']
        self.reactor_3_size_ref = self.df['size ref'].loc['Reactor_3']
        self.reactor_3_size_factor = self.df['n'].loc['Reactor_3']
        self.IEC_FOB = self.df['FOB'].loc['Ion_exchange_column']
        self.IEC_size_base = self.df['size base'].loc['Ion_exchange_column']
        self.IEC_size_ref = self.df['size ref'].loc['Ion_exchange_column']
        self.IEC_size_factor = self.df['n'].loc['Ion_exchange_column']
        self.resin_FOB = self.df['FOB'].loc['Ion_exchange_resin']
        self.resin_size_base = self.df['size base'].loc['Ion_exchange_resin']
        self.resin_size_ref = self.df['size ref'].loc['Ion_exchange_resin']
        self.resin_size_factor = self.df['n'].loc['Ion_exchange_resin']
        self.dryer_FOB = self.df['FOB'].loc['Dryer']
        self.dryer_size_base = self.df['size base'].loc['Dryer']
        self.dryer_size_ref = self.df['size ref'].loc['Dryer']
        self.dryer_size_factor = self.df['n'].loc['Dryer']
        self.pumps_FOB = self.df['FOB'].loc['Pumps']
        self.pumps_size_base = self.df['size base'].loc['Pumps']
        self.pumps_size_ref = self.df['size ref'].loc['Pumps']
        self.pumps_size_factor = self.df['n'].loc['Pumps']
        self.valves_FOB = self.df['FOB'].loc['Valves']
        self.valves_size_base = self.df['size base'].loc['Valves']
        self.valves_size_ref = self.df['size ref'].loc['Valves']
        self.valves_size_factor = self.df['n'].loc['Valves']
        

        self.pipes_FOB = self.df['FOB'].loc['Pipes']
        self.pipes_size_base = self.df['size_base'].loc['Pipes']
        self.pipes_size_ref = self.df['size_ref'].loc['Pipes']
        self.pipes_size_factor = self.df['n'].loc['Pipes']
        self.pipes_amount = self.df['amount'].loc['Pipes']
        self.CEPCI_base = self.df['FOB'].loc['CEPCI_base']
        """
        return


def cost_equipment(FOB=None, CEPCI_base=None, size_base=None, size_ref=None, n=None):
    """
    Source: Huang 2021, Life Cycle Assessment and Techno-Economic Assessment of Lithium Recovery from Geothermal
    Brines, Supporting Information
    Including 10% increase for delivery cost
    :return:
    """
    CEPCI_ref = 1000
    cost_base = 1.1 * FOB * (CEPCI_base / CEPCI_ref) * (size_base / size_ref) ** n
    return cost_base


if __name__ == '__main__':
    test = Equipment_att()
    print(test)
