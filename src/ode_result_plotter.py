import os
from typing import Final

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from src.lotka_volterra import SimulatedPopulations


class ODEResultPlotter:
    def __init__(self, count: int):
        self.output_folder = "output/"
        self.count: Final[str] = str(count)

    def plot_time_series(self, time, simulated_populations: SimulatedPopulations):
        fig = make_subplots(rows=2, cols=1)

        fig.add_trace(go.Scatter(x=time, y=simulated_populations.prey), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=time, y=simulated_populations.predator), row=2, col=1
        )
        fig["data"][0]["name"] = "prey"
        fig["data"][1]["name"] = "predator"

        fig.update_xaxes(
            title_text="Time [arb. units]",
            row=1,
            col=1,
            rangemode="tozero",
            showgrid=True,
            gridwidth=1,
            gridcolor="lightgray",
            showline=True,
            linecolor="black",
        )
        fig.update_xaxes(
            title_text="Time [arb. units]",
            row=2,
            col=1,
            rangemode="tozero",
            showgrid=True,
            gridwidth=1,
            gridcolor="lightgray",
            showline=True,
            linecolor="black",
        )
        fig.update_yaxes(
            title_text="Prey count [arb. units]", row=1, col=1, rangemode="tozero",
            showgrid=True,
            gridwidth=1,
            gridcolor="lightgray",
            zerolinecolor="lightgray",
            showline=True,
            linecolor="black",
        )
        fig.update_yaxes(
            title_text="Predator count [arb. units]", row=2, col=1, rangemode="tozero",
            showgrid=True,
            gridwidth=1,
            gridcolor="lightgray",
            zerolinecolor="lightgray",
            showline=True,
            linecolor="black",
        )

        fig.update_layout(
            height=600,
            width=800,
            title_text="Plots of predator and prey count versus time",
            title={"x": 0.5, "xanchor": "center", "yanchor": "top"},
            showlegend=False,
            plot_bgcolor="#FFF",
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="black"
            )
        )

        #fig.show()
        output_path = os.path.join(self.output_folder, "time_series")
        os.makedirs(output_path, exist_ok=True)
        fig.write_image(os.path.join(output_path, f"{self.count}.pdf"))

    def plot_phase(self, simulated_populations: SimulatedPopulations):
        fig = px.scatter(
            x=simulated_populations.prey,
            y=simulated_populations.predator,
            title="Plot of predator count versus prey count",
        )

        fig.update_layout(
            showlegend=False,
            xaxis_title="Prey count [arb. units]",
            yaxis_title="Predator count [arb. units]",
            title={"x": 0.5, "xanchor": "center", "yanchor": "top"},
            plot_bgcolor="#FFF",
            font=dict(
                family="Courier New, monospace",
                size=16,
                color="black"
            )
        )
        fig.update_xaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor="lightgray",
            showline=True,
            linecolor="black",
            rangemode="tozero",
        )
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor="lightgray",
            zerolinecolor="lightgray",
            showline=True,
            linecolor="black",
            rangemode="tozero",
        )

        #fig.show()
        output_path = os.path.join(self.output_folder, "phase")
        os.makedirs(output_path, exist_ok=True)
        fig.write_image(os.path.join(output_path, f"{self.count}.pdf"))
