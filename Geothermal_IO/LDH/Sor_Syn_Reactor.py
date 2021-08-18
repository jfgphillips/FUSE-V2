import pandas as pd
from calculators import QReactors

class BatchReactor_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name="sorbent_synthesis_reaction", skiprows=1)
        self.df.set_index('key', inplace=True)
        self.reaction_temp = self.df['value'].loc['reaction_temp']
        self.reaction_time_1 = self.df['value'].loc['reaction_time_1']
        self.reaction_time_2 = self.df['value'].loc['reaction_time_2']
        self.thermal_conductivity = self.df['value'].loc['thermal_conductivity_reactor']
        self.wall_thickness = self.df['value'].loc['wall_thickness']
        self.surface_area = self.df['value'].loc['surface_area']
        return


def QReactor(reaction_temperature=None, reaction_time_1=None, reaction_time_2=None, surface_area=None,
             thermal_conductivity=None, wall_thickness=None, liq_density_1=None, liq_density_2=None):
        """"
        Source: Sharma 2020
        Reaction in two steps:
        q_reactor_1 = first step of reaction process: mixing and heating LiOH*H2O, Al(OH)3 and H2O
        q_reactor_2 = second step of reaction process: slowly adding HCl to the reaction mixture
        """
        req_reactor_1_kwargs = {'reaction_temperature': reaction_temperature,
                                'reaction_time': reaction_time_1,
                                'surface_area': surface_area,
                                'thermal_conductivity': thermal_conductivity,
                                'wall_thickness': wall_thickness,
                                'liq_density': liq_density_1}

        q_reactor_1 = QReactors.batchReactor(**req_reactor_1_kwargs)

        req_reactor_2_kwargs = {'reaction_temperature': reaction_temperature,
                                'reaction_time': reaction_time_2,
                                'surface_area': surface_area,
                                'thermal_conductivity': thermal_conductivity,
                                'wall_thickness': wall_thickness,
                                'liq_density': liq_density_2}

        q_reactor_2 = QReactors.batchReactor(**req_reactor_2_kwargs)

        q_reactor_total = q_reactor_1[0] + q_reactor_2[0]
        q_reactor_total_kWh = q_reactor_total * 10**(-3)

        return q_reactor_total_kWh

if __name__ == '__main__':
    test = BatchReactor_att()
    print(test)