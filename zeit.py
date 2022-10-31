import pandas as pd

import util

AVG_AZ = 0
AVG_BZ = 0
AVG_FZ = 0

DICT_SCHLEPP_MMODELL_AZ = dict()
DICT_SCHLEPP_MMODELL_BZ = dict()
DICT_SCHLEPP_MMODELL_FZ = dict()


def convert_time_to_int(time):
    time_list = list(str(time).split(':'))
    hour = int(time_list[0]) * 3600
    min = int(time_list[1]) * 60
    sec = int(time_list[2])

    return hour + min + sec


def convert_int_to_time(integer):
    int1 = int(integer / 3600)
    value1 = integer % 3600
    int2 = int(value1 / 60)
    value2 = value1 % 60

    return str(int1) + ":" + str(int2) + ":" + str(int(value2))


def time_calc(start, stop):
    res = convert_time_to_int(stop) - convert_time_to_int(start)
    return convert_int_to_time(res)

def get_time_df():
    df = util.get_df()
    df = df[df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP]
    df = df[['Maschine', 'Maschinenmodell', 'Startzeit', 'Stoppzeit', 'Betriebsstd.', 'Fahrzeit']]
    df['Arbeitszeit'] = df.apply(lambda df: time_calc(df['Startzeit'], df['Stoppzeit']), axis=1)
    df = df.drop(columns=['Startzeit', 'Stoppzeit'])
    return df

def avg(column_title, df):
    column = df[column_title]
    avg = 0
    for i in range(column.size):
        avg += convert_time_to_int(column.iloc[i])
    avg = avg / column.size
    avg = convert_int_to_time(avg)
    return avg

def convert_time_to_float_time(time):
    x = time.split(':', 1)[0]
    y = time.split(':', 2)[1]
    time = x + "." + y
    return time

def get_az_bz_fz_avg(df):
    avg_az = convert_time_to_float_time(avg('Arbeitszeit', df))
    avg_bz = convert_time_to_float_time(avg('Betriebsstd.', df))
    avg_fz = convert_time_to_float_time(avg('Fahrzeit', df))
    return avg_az, avg_bz, avg_fz


def get_maschinenmodell_avgs():
    df = get_time_df()
    maschinenmodell_values = [*set(list(df['Maschinenmodell'].values))]
    az_dict = dict()
    bz_dict = dict()
    fz_dict = dict()

    for modell in maschinenmodell_values:
        df_tmp = df[df['Maschinenmodell'] == modell]
        x, y, z = get_az_bz_fz_avg(df_tmp)
        az_dict[modell] = x
        bz_dict[modell] = y
        fz_dict[modell] = z

    az_s = pd.Series(az_dict)
    bz_s = pd.Series(bz_dict)
    fz_s = pd.Series(fz_dict)
    frame = {'AZ': az_s, 'BZ': bz_s, 'FZ': fz_s}
    return pd.DataFrame(frame)


def avg_fz_by_engine():
    df = get_time_df()
    # maschinenmodell_values = [*set(list(df['Maschinenmodell'].values))]
    for i in range(len(df)):
        if df['Maschinenmodell'].iloc[i] == "Comet 4E":
            df['Maschinenmodell'].iloc[i] = "Elektro"
        elif df['Maschinenmodell'].iloc[i] == "Comet 4H":
            df['Maschinenmodell'].iloc[i] = "Hybrid"
        else:
            df['Maschinenmodell'].iloc[i] = "Diesel"

    avg_e = 0
    avg_e_count = 0
    avg_h = 0
    avg_h_count = 0
    avg_d = 0
    avg_d_count = 0
    for i in range(len(df)):
        time = convert_time_to_int(df['Fahrzeit'].iloc[i])
        if df['Maschinenmodell'].iloc[i] == "Elektro":
            avg_e += time
            avg_e_count += 1
        elif df['Maschinenmodell'].iloc[i] == "Hybrid":
            avg_h += time
            avg_h_count += 1
        else:
            avg_d += time
            avg_d_count += 1

    avg_fz_dict = {"Diesel": float(convert_time_to_float_time(convert_int_to_time(avg_d/avg_d_count))),
                   "Elektro": float(convert_time_to_float_time(convert_int_to_time(avg_e/avg_e_count))),
                   "Hybrid": float(convert_time_to_float_time(convert_int_to_time(avg_h/avg_h_count)))}
    return avg_fz_dict

def distribution_anfangszeit_stoppzeit():
    df = util.get_df()
    df = df[df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP]
    df = df[['Maschine', 'Maschinenmodell', 'Startzeit', 'Stoppzeit']]

    return df


if __name__ == '__main__':

    distribution_anfangszeit_stoppzeit()
