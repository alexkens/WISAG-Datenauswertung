import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import speed as s

import util


def plot_total_speed_avg():
    total_speed_avg, x, y = s.get_models_speed_avg_dict()

    # total_speed_avg
    print("Total Speed Average of all 'Gepäck- und Ausrüstungswagen': ", round(total_speed_avg, 2), " Km/h")


def plot_speed_avg_by_model():
    x, model_speed_avg, y = s.get_models_speed_avg_dict()

    fig = go.Figure(go.Bar(
        x=list(model_speed_avg.values()),
        y=list(model_speed_avg.keys()),
        orientation='h'))
    fig.update_layout(
        title="Speed Average by Model",
        xaxis_title="Km/h",
        yaxis_title="Model"
    )
    fig.show()


def plot_speed_avg_by_engine():
    total_speed_avg, model_speed_avg, speed_avg_by_engine = s.get_models_speed_avg_dict()
    # speed_avg_by_engine

    fig = go.Figure(go.Bar(
        x=list(speed_avg_by_engine.values()),
        y=list(speed_avg_by_engine.keys()),
        orientation='h'))
    fig.update_layout(
        title="Speed Average by Engine",
        xaxis_title="Km/h",
        yaxis_title="Engine"
    )
    fig.show()


if __name__ == '__main__':
    plot_speed_avg_by_engine()

