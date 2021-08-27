import pandas as pd
import numpy as np


def haulageVehicle(motor_kW=None, running_load=None, nameplate_rating=None, utilisation_factor=None, op_units=None):
    """
    :param motor_kW: engine horse power
    :param running_load: how much the unit is carrying
    :param nameplate_rating: max operating rating
    :param utilisation_factor: utilisation factor
    :param op_units: intervals of a day, week, month, year

    :return: unit_energy_consumption: Energy/month (kW hours)
    """
    # motor_kW = motor_HP * 0.746  # conversion factor HP -> kW
    load_factor = running_load / nameplate_rating  # what capacity is equipment being used
    unit_energy_consumption = motor_kW * load_factor * utilisation_factor * op_units  # standardised value

    return unit_energy_consumption

def beltConveyor(motor_kW=None, utilisation_factor=None, op_units=None):
    """
    Function deals with energy consumption of a belt conveyor
    :param motor_kW: integer for the motor units: kW
    :param utilisation_factor: float 0-1 for utilisation factor: unitless
    :param op_units: integer a unit of time for the unit energy consumption, default = yrs
    :return unit_energy_consumption: float units kWhrs/yr
    """

    unit_energy_consumption = motor_kW * utilisation_factor * op_units
    return unit_energy_consumption


def beltConveyor_requirement(belt_speed=None, belt_length=None, gradient=None, conveyor_output=None, drive_train_efficiency=None):
    """
    credit for this calculation: hard rock miners handbook
    Function to calculate the power requirements of a belt conveyor (output in kW)

    :param belt_speed: float for speed of belt, units: m/min
    :param belt_length: float for length of belt, units: m
    :param gradient: float for slope of the conveyor with + 0-100 for uphill and - 0-100 for downhill , units %
    :param conveyor_output: float for conveyor output, units: t/hrs
    :param drive_train_efficiency: float for efficiency of the drive train 0-1 (representing 0-100%), unitless

    :return: drive power requirements for belt conveyor in kW
    """

    """
        belt_df = pd.read_csv('../../data/equivalent_lift_matrix.csv')
        belt_df.set_index('belt speed feet per minute', inplace=True)
        column = str(belt_length)
        H_f = belt_df[column].loc[belt_speed]
    """

    def speed_convertor(belt_speed):
        """
        Function to convert belt speed input of m/min into feet/min
        :param belt_speed: float for speed of belt, units: m/min
        :return: float for speed of belt, units: f/min
        """
        foot_per_minute = belt_speed * 3.28084
        return foot_per_minute

    def length_converter(belt_length):
        """
        Function to convert belt length input of meters into feet
        :param belt_length: float for length of belt, units: m
        :return: float for length of belt, units: feet
        """
        footage = belt_length * 3.28084
        return footage

    foot_per_min = speed_convertor(belt_speed)
    feet = length_converter(belt_length)

    if foot_per_min <= 100:
        H_f = 7.58813 + 0.04957*feet - 1.46623e-5*(feet**2) + 2.54432e-9*(feet**3)
    elif 200 >= foot_per_min > 100:
        H_f = 8.41089 + 0.05524*feet - 1.63515e-5*(feet**2) + 2.83452e-9*(feet**3)
    elif 300 >= foot_per_min > 200:
        H_f = 10.04759 + 0.06634*feet - 1.96818e-5*(feet**2) + 3.41284e-9*(feet**3)
    elif 400 >= foot_per_min > 300:
        H_f = 11.7842 + 0.07739*feet - 2.28826e-5*(feet**2) + 3.96428e-9*(feet**3)
    else:
        H_f = 13.43053 + 0.08901*feet - 2.64782e-5*(feet*2) + 4.59918e-9*(feet*3)

    Q = conveyor_output * 36.7434  # tonne per hour conv to pounds per min
    H_g = gradient * 10  # gradient given as a percentage * 10 for some reason
    H = H_g + H_f  # total lift, H = gradient + length/speed table (.csv file)
    belt_HP = (Q * H) / 33000  # conversion to horse power
    drive_HP = belt_HP / drive_train_efficiency
    drive_kW = drive_HP * 0.746

    return drive_kW


def poweredVehicle(motor_kW=None, utilisation_factor=None, op_units=None):
    """

    :param motor_kW: the power requirement of the motor in kilowatts
    :param utilisation_factor: how much the vehicle is being used per year
    :param op_units: the unit factor being a year, month, day etc, default = year
    :return:
    """
    unit_energy_consumption = motor_kW * utilisation_factor * op_units

    return unit_energy_consumption


def environment():
    environment_impact = np.nan
    return environment_impact

