from django.shortcuts import render
from django_pandas.io import read_frame
from cutting.models import Cut
import pandas as pd
import numpy as np
import matplotlib
import plotly.express as px
from plotly.offline import plot as plt
from django.views.generic import TemplateView
import plotly.graph_objs as go


def plotting(request, plot):
    # breakpoint()
    y = plot
    x = "abrasive"
    color = "stone"

    qs = Cut.objects.all()
    df = read_frame(qs)
    df1 = df[df["kesme_hizi"] == 500]
    df2 = df[df["kesme_hizi"] == 550]
    df3 = df[df["kesme_hizi"] == 600]

    fig1 = px.bar(
        df1,
        x=x,
        y=y,
        color=color,
        barmode="group",
        title="Kesme Hızı 500 mm/dk",
        labels={
            "stone": "Doğal Taşlar",
            "kesme_derinligi": "Kesme Derinliği (mm)",
            "abrasive": "Aşındırıcılar",
        },
    )
    fig2 = px.bar(
        df2,
        x=x,
        y=y,
        color=color,
        barmode="group",
        title="Kesme Hızı 550 mm/dk",
        labels={
            "stone": "Doğal Taşlar",
            "kesme_derinligi": "Kesme Derinliği (mm)",
            "abrasive": "Aşındırıcılar",
        },
    )
    fig3 = px.bar(
        df3,
        x=x,
        y=y,
        color=color,
        barmode="group",
        title="Kesme Hızı 600 mm/dk",
        labels={
            "stone": "Doğal Taşlar",
            "kesme_derinligi": "Kesme Derinliği (mm)",
            "abrasive": "Aşındırıcılar",
        },
    )
    fig1.update_layout(
        title_x=0.5,
        title_y=0.84,
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.30, xanchor="right", x=0.70
        ),
    )
    fig2.update_layout(
        title_x=0.5,
        title_y=0.84,
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.30, xanchor="right", x=0.70
        ),
    )
    fig3.update_layout(
        title_x=0.5,
        title_y=0.84,
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.30, xanchor="right", x=0.70
        ),
    )
    gantt_plot1 = plt(fig1, output_type="div")
    gantt_plot2 = plt(fig2, output_type="div")
    gantt_plot3 = plt(fig3, output_type="div")
    context = {
        "plot_div1": gantt_plot1,
        "plot_div2": gantt_plot2,
        "plot_div3": gantt_plot3,
    }
    return render(request, "plots/plot.html", context)
