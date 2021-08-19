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


def beltConveyor(belt_speed, belt_length, gradient, conveyor_output, drive_train_efficiency):
    """
    credit for this calculation: hard rock mininers handbook
    might be an idea to standardise units across the process

    :param belt_speed: speed of belt feet per minute
    :param belt_length: length of belt in feet
    :param gradient: slope of the conveyor
    :param conveyor_output: conveyor output tonnes per hour
    :param drive_train_efficiency: efficiency of the drive train

    :return: drive power requirements for belt conveyor
    """
    belt_df = pd.read_csv('../equivalent_lift_matrix.csv')
    belt_df.set_index('belt speed feet per minute', inplace=True)

    column = str(belt_length)

    H_f = belt_df[column].loc[belt_speed]

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

