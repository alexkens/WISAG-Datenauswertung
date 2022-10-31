import pandas as pd

import util



# avg speed of
# 1. all models
# 2. E, H, D

# schlepp_df
# E_df
# H_df
# D_df


def get_maschinenmodell_df(df):
    pass


def get_models_speed_avg_dict():
    model_speed_avg = dict()

    df = util.get_maschinentyp_schlepp_df()
    df = df[['Maschine', 'Maschinenmodell', 'Km', 'Fahrzeit']]

    # create new column='Geschwindigkeit'
    df['Fahrzeit'] = df['Fahrzeit'].apply(util.convert_time_to_float_time)
    df = df[df['Fahrzeit'] > 0]
    df['Geschwindigkeit'] = df['Km'] / df['Fahrzeit']

    # total_speed_avg
    total_speed_avg = df['Geschwindigkeit'].sum() / len(df)

    # speed_avg_by_model
    maschinenmodell_values = [*set(list(df['Maschinenmodell'].values))]
    for model in maschinenmodell_values:
        sum = 0
        count = 0
        for i in range(len(df)):
            if df['Maschinenmodell'].iloc[i] == model:
                sum += df['Geschwindigkeit'].iloc[i]
                count += 1
        model_speed_avg[model] = sum / count

    # speed_avg_by_engine
    e_speed_avg = model_speed_avg['Comet 4E']
    h_speed_avg = model_speed_avg['Comet 4H']
    d_speed_avg = (model_speed_avg['Comet 3D'] + model_speed_avg['Comet 6D'] + model_speed_avg['Comet 4D-DK']) / 3
    speed_avg_by_engine = {'Elektro': e_speed_avg, 'Hybrid': h_speed_avg, 'Diesel': d_speed_avg}

    return total_speed_avg, model_speed_avg, speed_avg_by_engine


if __name__ == '__main__':

    df = get_models_speed_avg_dict()