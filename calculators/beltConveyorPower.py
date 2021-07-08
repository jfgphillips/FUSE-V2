import pandas as pd

def belt_conveyor_power(belt_speed, belt_length, gradient, conveyor_output, drive_train_efficiency):
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
    belt_df = pd.read_csv('data/equivalent_lift_matrix.csv')
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