import pandas as pd

import util


ELEKTRO_SCHLEPP_Q = 0
ELEKTRO_SCHLEPP_TRIPS = 0
HYBRID_SCHLEPP_Q = 0
HYBRID_SCHLEPP_TRIPS = 0

MASCHINENMODELLE_SCHLEPP_Q = dict()
MASCHINENMODELLE_SCHLEPP_TRIPS = dict()


def get_total_schlepper_trips(df):
    TOTAL_TRIPS = len(df)
    SCHLEPP_TRIPS = df[df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP].shape[0]
    return TOTAL_TRIPS, SCHLEPP_TRIPS


def get_total_schlepper_q(df):
    machine_series = df['Maschine']
    filt = (df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP)
    schlepper_series = df.loc[filt, 'Maschine']

    l = []
    for e in machine_series.values:
        if e in l:
            continue
        else:
            l.append(e)
    TOTAL_Q = len(l)

    l = []
    for e in schlepper_series.values:
        if e in l:
            continue
        else:
            l.append(e)
    SCHLEPP_Q = len(l)

    return TOTAL_Q, SCHLEPP_Q


def get_elektro_q_trips(df):
    series = df[df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP]

def get_schlepper_maschine_trips_dict(df):
    filt = (df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP)
    schlepper_maschine_series = df.loc[filt, 'Maschine']
    schlepper_values = [*set(list(schlepper_maschine_series.values))]

    dict_maschine_per_trips = dict()
    for e in schlepper_values:
        dict_maschine_per_trips[e] = schlepper_maschine_series[schlepper_maschine_series == e].size

    return dict_maschine_per_trips


def get_schlepper_modell_trips_dict(df):
    df = df[['Maschine', 'Maschinenmodell', 'Maschinentyp']]
    filt = (df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP)
    df = df.loc[filt]

    modell_values = [*set(list(df['Maschinenmodell'].values))]

    dict_maschine_per_modell = dict()
    for e in modell_values:
        dict_maschine_per_modell[e] = df[df == e].size

    maschinenmodell_df = df[['Maschinenmodell']]
    maschinenmodell_df_len = len(maschinenmodell_df)
    res_dict = dict()
    for e in modell_values:
        res_dict[e] = 0
    for model in modell_values:
        for i in range(maschinenmodell_df_len):
            if maschinenmodell_df['Maschinenmodell'].values[i] == model:
                res_dict[model] += 1

    return res_dict

def get_schlepper_modell_maschine(df):
    df = df[['Maschine', 'Maschinenmodell', 'Maschinentyp']]
    filt = (df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP)
    df = df.loc[filt]

    maschine_values = [*set(list(df['Maschine'].values))]
    modell_values = [*set(list(df['Maschinenmodell'].values))]

    res_dict = dict()
    for e in modell_values:
        res_dict[e] = 0

    for maschine in maschine_values:
        modell_tmp = df[df['Maschine'] == maschine].iloc[0]['Maschinenmodell']
        res_dict[modell_tmp] += 1

    return res_dict


if __name__ == '__main__':

    df = util.get_df()
    get_schlepper_modell_maschine(df)




    #print(dict_maschine_per_modell)
    #print(modell_values)



    """filt = (df['Maschinentyp'] == util.MASCHINENTYP_SCHLEPP)
    schlepper_maschine_series = df.loc[filt, 'Maschinenmodell']
    maschinenmodell_values = [*set(list(schlepper_maschine_series.values))]

    e_values = [maschinenmodell_values[3]]
    h_values = [maschinenmodell_values[0]]
    non_e_values = [maschinenmodell_values[1], maschinenmodell_values[2], maschinenmodell_values[4]]

    ELEKTRO_SCHLEPP_TRIPS = schlepper_maschine_series[schlepper_maschine_series == e_values[0]].size
    HYBRID_SCHLEPP_TRIPS = schlepper_maschine_series[schlepper_maschine_series == h_values[0]].size"""







