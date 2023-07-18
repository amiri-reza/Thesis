from django.shortcuts import render, redirect
import plotly.express as px
from plotly.offline import plot as plt
import pandas as pd
from cutting_plots.forms import PlotSelectorForm
from cutting_performance.models import (
    NaturalStone,
    Abrasive,
    CuttingData
)



def plot_selector(request):
    form = PlotSelectorForm(request.POST)
    if form.is_valid():
        print(request.POST)
        return redirect("cutting_plots:plotter", parameter=request.POST.get("cutting_parameter"))
    context = {"form": form}
    return render(request, "cutting_plots/plot_selector.html", context)    



def plotter(request, parameter):
    df = pd.DataFrame(list(CuttingData.objects.all().values()))
    df["natural_stone_id"] = df["natural_stone_id"].replace(
        [1,2,3],[
            NaturalStone.objects.get(id=1).stone,
            NaturalStone.objects.get(id=2).stone,
            NaturalStone.objects.get(id=3).stone
        ]
    )
    df["abrasive_id"] = df["abrasive_id"].replace(
        [1,2,3,4,5],[
            Abrasive.objects.get(id=1).abrasive,
            Abrasive.objects.get(id=2).abrasive,
            Abrasive.objects.get(id=3).abrasive,
            Abrasive.objects.get(id=4).abrasive,
            Abrasive.objects.get(id=5).abrasive
        ]
    )
    speed500 = df[df["cutting_speed"] == 500]
    speed550 = df[df["cutting_speed"] == 550]
    speed600 = df[df["cutting_speed"] == 600]
    color = "abrasive_id"
    labels = {
        "natural_stone_id": "Natural Stones",
        "abrasive_id": "Abrasives",
        "cutting_depth": "Cutting Depth (mm)",
        "cd_stddev": "Cutting Depth Standard Deviation",
        "cd_max": "Maximum Cutting Depth Point (mm)",
        "cd_min": "Minimum Cutting Depth Poin (mm)",
        "wear_zone_depth": "Wear Zone Depth (mm)",
        "wz_stddev": "Wear Zone Standart Deviation",
        "wz_max": "Maximum Depth of Wear Zone Point (mm)",
        "wz_min": "Minimum Depth of Wear Zone Point (mm)",
        "cutting_width": "Cutting Width (mm)",
        "cw_stddev": "Cutting Width Standard Deviation",
        "kerf_angle": "Kerf Angle (°)",
        "material_removal_rate": "Material Removal Rate (cm³/sec)",
        "Ra_surface_roughness": "Surface Roughness (Ra) (μm)",
        "Ra_stddev": "Surface Roughness (Ra) Standard Deviation",
        "Rq_surface_roughness": "Surface Roughness (Rq) (μm)",
        "Rq_stddev": "Surface Roughness (Rq) Standard Deviation",
        "Rz_surface_roughness": "Surface Roughness (Rz) (μm)",
        "Rz_stddev": "Surface Roughness (Rz) Standard Deviation"
    }
# Traverse Speed 500 mm/min
    fig1 = px.bar(
        speed500,
        x="natural_stone_id",
        y=parameter,
        color=color,
        barmode="group",
        title="Traverse Speed: 500 mm/min",
        labels=labels,
    )
    fig1.update_layout(
        title_x=0.5,
        title_y=0.95,
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.15, xanchor="right", x=0.70
        )
    )
# Traverse Speed 550 mm/min
    fig2 = px.bar(
        speed550,
        x="natural_stone_id",
        y=parameter,
        color=color,
        barmode="group",
        title="Traverse Speed: 550 mm/min",
        labels=labels,
    )

    fig2.update_layout(
        title_x=0.5,
        title_y=0.95,
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.15, xanchor="right", x=0.70
        )
    )
# Traverse Speed 600 mm/min
    fig3 = px.bar(
        speed600,
        x="natural_stone_id",
        y=parameter,
        color=color,
        barmode="group",
        title="Traverse Speed: 600 mm/min",
        labels=labels,

    )
    fig3.update_layout(
        title_x=0.5,
        title_y=0.95,
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.15, xanchor="right", x=0.70
        )
    )   
    plot1 = plt(fig1, output_type="div")
    plot2 = plt(fig2, output_type="div")
    plot3 = plt(fig3, output_type="div")

    context = {"plot1": plot1, "plot2": plot2, "plot3": plot3 }
    return render(request, "cutting_plots/plotter.html", context)

