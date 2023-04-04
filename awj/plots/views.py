from django.shortcuts import render
from django_pandas.io import read_frame
from cutting.models import Cut
from abrasive.models import AbrasiveProperties, Abrasives
from atik.models import NaturalStones, PhysicalProperties, MechanicalProperties
import plotly.express as px
from plotly.offline import plot as plt
import numpy as np
import pandas as pd


def plotting(request, plot):
    # breakpoint()
    y = plot
    x = "abrasive"
    color = "stone"
    labels = {
        "stone": "Doğal Taşlar",
        "kesme_derinligi": "Kesme Derinliği (mm)",
        "abrasive": "Aşındırıcılar",
        "kerf_acisi": "Kerf Açısı (Derece)",
        "yuzey_puruzlulugu": "Yüzey Pürüzlülüğü (Ra, µm)",
        "kd_max": "Maksimum Kesme Derinliği (mm)",
        "kd_min": "Minimum Kesme Derinliği (mm)",
        "ka_max": "Maksimum Kesme Aşınma Derinliği (mm)",
        "ka_min": "Minimum Kesme Aşınma Derinliği (mm)",
        "kesme_asinma": "Kesme Aşınma Derinliği (mm)",
        "kesme_genisligi": "Kesme Genişliği (mm)",
        "plaka_agirlik_kaybi": "Ağırlık Kaybı (gr)",
    }
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
        labels=labels,
    )
    fig2 = px.bar(
        df2,
        x=x,
        y=y,
        color=color,
        barmode="group",
        title="Kesme Hızı 550 mm/dk",
        labels=labels,
    )
    fig3 = px.bar(
        df3,
        x=x,
        y=y,
        color=color,
        barmode="group",
        title="Kesme Hızı 600 mm/dk",
        labels=labels,
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


def corr_plotter(request):
    qs1 = Cut.objects.all()
    df1 = read_frame(qs1)
    df_500 = df1[df1["kesme_hizi"] == 500]
    df_550 = df1[df1["kesme_hizi"] == 550]
    df_600 = df1[df1["kesme_hizi"] == 600]
    print(df_500, df_550, df_600)
    print("df_cut----------------------------------------------")
    df_500_kr = df_500[df_500["abrasive"] == "Garnet"]
    df_500_vt = df_500[df_500["stone"] == "Vitrik Litik Tüf"].drop(
        ["stone", "id"], axis=1
    )
    df_500_lm = df_500[df_500["stone"] == "Lamprofir"].drop(["stone", "id"], axis=1)

    print(df_500_kr)
    print("df_500_kr @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(df_500_vt)
    print("df_500_vt @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(df_500_lm)
    print("df_500_lm @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # df_500 = df1[df1['kesme_hizi']== 500].drop(['stone', 'id'], axis=1)
    # df_550 = df1[df1['kesme_hizi']== 550].drop(['stone', 'id'], axis=1)
    # df_600 = df1[df1['kesme_hizi']== 600].drop(['stone', 'id'], axis=1)

    qs2 = PhysicalProperties.objects.all()
    df2 = read_frame(qs2)
    print(df2)
    print("df2----------------------------------------------")

    corr = df2.corrwith(df_500_kr["kesme_derinligi"], numeric_only=True)

    print("_______________________________________-")

    print(df_500_kr["kesme_derinligi"])
    print("_______________________________________-")
    print(corr)

    fig = px.bar(corr)

    gantt_plot = plt(fig, output_type="div")
    context = {"plot_div": gantt_plot}
    return render(request, "plots/corr.html", context)


	


def max_min_cutting_depth_corr(request):
    # Load the data into a DataFrame
    df = pd.read_csv("static/csv/table6.csv", sep=";")

    # Calculate the correlation matrix
    corr_matrix = df[["ortalama", "max", "min"]].corr()

    # Print the correlation coefficients
    print(corr_matrix["min"])
    print(corr_matrix["max"])

    fig = px.bar(corr_matrix)
    gantt_plot = plt(fig, output_type="div")
    context = {"plot_div":gantt_plot}

    return render(request, "plots/cut-max-min-corr.html", context)
