import pandas as pd
from calculators import QProcesses
from calculators import unitConversions


class Impeller_att(object):
    def __init__(self):
        self.df = pd.read_excel(r'../../data/LDH_attributes.xlsx',
                                sheet_name='standard_impeller', skiprows=1)
        self.df.set_index('key', inplace=True)
        self.impeller_power_number = self.df['value'].loc['impeller_power_number']
        self.agitator_rotational_speed = self.df['value'].loc['rotational_speed_agitator']
        self.impeller_diameter = self.df['value'].loc['impeller_diameter']
        self.stirring_time_total = self.df['value'].loc['stirring_time']
        self.efficiency = self.df['value'].loc['efficiency']
        return

def StirringEnergySorSyn(impeller_power_number=None, impeller_diameter=None, agitator_rotational_speed=None,
                   stirring_time_1=None, stirring_time_2=None, efficiency=None, density_1=None, density_2=None):
    req_stirring_energy_1_kwargs = {'impeller_power_number': impeller_power_number,
                                    'impeller_diameter': impeller_diameter,
                                    'agitator_rotational_speed': agitator_rotational_speed,
                                    'stirring_time': stirring_time_1,
                                    'density': density_1,
                                    'efficiency': efficiency}

    stirring_energy_1 = QProcesses.stirring_energy(**req_stirring_energy_1_kwargs)

    req_stirring_energy_2_kwargs = {'impeller_power_number': impeller_power_number,
                                    'impeller_diameter': impeller_diameter,
                                    'agitator_rotational_speed': agitator_rotational_speed,
                                    'stirring_time': stirring_time_2,
                                    'density': density_2,
                                    'efficiency': efficiency}

    stirring_energy_2 = QProcesses.stirring_energy(**req_stirring_energy_2_kwargs)

    sitrring_energy_1_kWh = unitConversions.kiloWattHours(stirring_energy_1)
    stirring_energy_2_kWh = unitConversions.kiloWattHours(stirring_energy_2)
    total_stirring_energy_kWh = sitrring_energy_1_kWh + stirring_energy_2_kWh
    return total_stirring_energy_kWh

if __name__ == '__main__':
    test = Impeller_att()
    print(test)



