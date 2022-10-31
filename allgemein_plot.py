import plotly.graph_objects as go
import plotly.express as px
import allgemein as a
import util

def trip_quantity_info():
    df = util.get_df()

    TOTAL_TRIPS, SCHLEPP_TRIPS = a.get_total_schlepper_trips(df)
    TOTAL_Q, SCHLEPP_Q = a.get_total_schlepper_q(df)

    total_trips_p = 1
    schlepp_trips_p = SCHLEPP_TRIPS / TOTAL_TRIPS

    total_q_p = 1
    schlepp_q_p = SCHLEPP_Q / TOTAL_Q

    x1 = [f"Total Number of Shifts: {TOTAL_TRIPS}"]
    x2 = [f"Total Vehicle Quantity: {TOTAL_Q}"]
    fig = go.Figure(data=[
        go.Bar(name='Schlepper', x=x1, y=[schlepp_trips_p]),                # width, height, text_auto=True
        go.Bar(name='Rest', x=x1, y=[total_trips_p-schlepp_trips_p]),       # fig.update_traces(textposition='outside')

        go.Bar(name='Schlepper', x=x2, y=[schlepp_q_p]),
        go.Bar(name='Rest', x=x2, y=[total_q_p - schlepp_q_p]),
    ])
    fig.update_layout(
        title="Total Number of Shifts and Vehicle",
    )
    # Change the bar mode
    fig.update_layout(barmode='stack')
    fig.show()


def get_schlepper_maschine_trips_dict():
    df = util.get_df()
    return a.get_schlepper_maschine_trips_dict(df)

def plot_schlepper_maschine_trips():
    dictionary = get_schlepper_maschine_trips_dict()

    fig = go.Figure(go.Bar(
        x=list(dictionary.values()),
        y=list(dictionary.keys()),
        orientation='h'))
    fig.update_layout(
        title="Shifts by Vehicle",
        xaxis_title="Shift",
        yaxis_title="Vehicle"
    )
    fig.show()


def get_schlepper_modell_trips_dict():
    df = util.get_df()
    return a.get_schlepper_modell_trips_dict(df)

def plot_schlepper_modell_trips():
    dictionary = get_schlepper_modell_trips_dict()

    fig = go.Figure(go.Bar(
        x=list(dictionary.values()),
        y=list(dictionary.keys()),
        orientation='h'))
    fig.update_layout(
        title="Shifts by Model",
        xaxis_title="Shift",
        yaxis_title="Model"
    )

    fig.show()


def get_schlepper_modell_maschine():
    df = util.get_df()
    return a.get_schlepper_modell_maschine(df)

def plot_schlepper_modell_maschine_count():
    dictionary = get_schlepper_modell_maschine()

    fig = go.Figure(go.Bar(
        x=list(dictionary.values()),
        y=list(dictionary.keys()),
        orientation='h'))
    fig.update_layout(
        title="Number of Vehicles by Model",
        xaxis_title="Number of Vehicles",
        yaxis_title="Model"
    )

    fig.show()



if __name__ == '__main__':

    plot_schlepper_modell_trips()


# graph = go.Figure(data=go.Bar(y=[ELEKTRO_SCHLEPP_ROUTES, HYBRID_SCHLEPP_ROUTES, 44]))
# graph.show()
# graph.write_html('first_html_plot', auto_open=True)





