import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px
import zeit as z
import util
import datetime
import numpy as np

def get_time_df():
    return z.get_time_df()

def plot_az_bz_fz():
    df = z.get_time_df()

    print(df)

    """fig = px.bar(df, x="Maschine", y="Fahrzeit",
                 barmode='group')
    """

    fig = px.bar(
        data_frame=df,
        x="Maschine",
        y=["Fahrzeit", "Betriebsstd."],
        opacity=0.9,
        orientation="v",
        barmode='group',
        title='Annual In-State Tuition vs Out-of-state Tuition',
    )

    fig.show()


    """fig = go.Figure(data=[
        go.Bar(name='Arbeitszeit', x=df[['Maschine']], y=df[['Arbeitszeit']]),
        go.Bar(name='Betriebszeit', x=df[['Maschine']], y=df[['Betriebsstd.']]),
        go.Bar(name='Fahrzeit', x=df[['Maschine']], y=df[['Fahrzeit']])
    ])
    fig.update_layout(barmode='group')
    fig.show()
    """

def plot_avg_az_bz_fz():
    df = get_time_df()
    az, bz, fz = z.get_az_bz_fz_avg(df)
    dictionary = {'Zeitart': ["Arbeitszeit", "Betriebsstd.", "Fahrzeit"],
                  'Durchschnitt': [float(az), float(bz), float(fz)]}
    fig = px.bar(dictionary, x="Zeitart", y="Durchschnitt")

    fig.update_layout(
        title="Time Distribution of 'Gepäck- und Ausrüstungswagen'",
        xaxis_title="Time Type",
        yaxis_title="Average Time"
    )
    fig.show()


def get_maschinenmodell_avgs():
    return z.get_maschinenmodell_avgs()


def plot_maschinenmodell_avgs():
    df = get_maschinenmodell_avgs()
    print(df)

    df = z.get_time_df()
    maschinenmodell_values = [*set(list(df['Maschinenmodell'].values))]

    modell_s = pd.Series(maschinenmodell_values)
    fig = px.bar(
        data_frame=df,
        x="AZ",
        y=modell_s,
        color="AZ",
        opacity=0.9,
        orientation="h",
        barmode='group',
        title='Maschinenmodelle Zeit Durchschnitt',
    )
    fig.show()


def plot_avg_fz_by_engine():
    avg_fz_dict = z.avg_fz_by_engine()

    fig = go.Figure(go.Bar(
        x=list(avg_fz_dict.keys()),
        y=list(avg_fz_dict.values()),
        orientation='v'))
    fig.update_layout(
        title="Average Fahrzeit by Engine",
        xaxis_title="Average Fahrzeit",
        yaxis_title="Engine"
    )
    fig.show()


def plot_distribution_anfangszeit_stoppzeit():
    df = z.distribution_anfangszeit_stoppzeit()

    for i in range(len(df)):
        if df['Maschinenmodell'].iloc[i] == "Comet 4E":
            df['Maschinenmodell'].iloc[i] = "Elektro"
        elif df['Maschinenmodell'].iloc[i] == "Comet 4H":
            df['Maschinenmodell'].iloc[i] = "Hybrid"
        else:
            df['Maschinenmodell'].iloc[i] = "Diesel"

    for i in range(len(df)):
        df['Startzeit'].iloc[i] = float(z.convert_time_to_float_time(df['Startzeit'].iloc[i]))
        df['Stoppzeit'].iloc[i] = float(z.convert_time_to_float_time(df['Stoppzeit'].iloc[i]))

    fig1 = px.scatter(df, x="Startzeit", color="Maschinenmodell", symbol="Maschinenmodell")
    fig1.update_layout(
        title="Distribution of Startzeit",
    )
    fig1.show()

    fig2 = px.scatter(df, x="Stoppzeit", color="Maschinenmodell", symbol="Maschinenmodell")
    fig2.update_layout(
        title="Distribution of Stoppzeit",
    )
    fig2.show()


def distribution_avg_fz():
    df = z.get_time_df()
    df = df.Fahrzeit.values.tolist()
    length = len(df)
    for i in range(length):
        df[i] = round(time_to_number(df[i]), 2)
        if df[i] == 0.0:
            del df[i]
            i -= 1
    print(df)

    fig = ff.create_distplot(hist_data=[df],
                             group_labels=["Fahrzeit Distribution"],
                             bin_size=[0.1])
    fig.update_layout(
        title="Distribution of Fahrzeit",
    )

    std = np.std(df)
    print(std)
    fig.add_shape(type="line", x0=std, x1=std, y0=0, y1=0.5, xref='x', yref='y',
                  line=dict(color='red', dash='dash'))
    fig.show()


def distribution_avg_fz_per_engine():
    df = z.get_time_df()

    e_list = []
    h_list = []
    d_list = []
    for i in range(len(df)):
        if df['Maschinenmodell'].iloc[i] == "Comet 4E":
            df['Maschinenmodell'].iloc[i] = "Elektro"
            e_list.append(df['Fahrzeit'].iloc[i])
        elif df['Maschinenmodell'].iloc[i] == "Comet 4H":
            df['Maschinenmodell'].iloc[i] = "Hybrid"
            h_list.append(df['Fahrzeit'].iloc[i])
        else:
            df['Maschinenmodell'].iloc[i] = "Diesel"
            d_list.append(df['Fahrzeit'].iloc[i])

    time_to_number_list(e_list)
    time_to_number_list(h_list)
    time_to_number_list(d_list)

    hist_data = [d_list, e_list, h_list]
    group_labels = ["Diesel", "Electro", "Hybrid"]

    fig = ff.create_distplot(hist_data,
                             group_labels,
                             bin_size=[0.01, 0.01, 0.01])
    fig.update_layout(
        title="Distribution of Fahrzeit by Engine",
    )
    fig.show()


def time_to_number_list(number_list):
    for i in range(len(number_list)):
        number_list[i] = round(time_to_number(number_list[i]), 2)


def time_to_number(time):
    res = time.hour + time.minute/60   # + time.second/10000
    return res


if __name__ == '__main__':

    distribution_avg_fz()
    # distribution_avg_fz_per_engine()