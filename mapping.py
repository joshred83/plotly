import plotly.plotly as py
import plotly.graph_objs as go

from plotly.tools import FigureFactory as FF

import json
import numpy as np
import pandas as pd

df = pd.read_csv('volcano.csv')

data = [go.Surface(z=df.values.tolist(), colorscale='Viridis')]

layout = go.layout(
    width=800,
    height=900,
    autosize=False,
    margin=dict(t=0, b=0, l=0, r=0),
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255,255,255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230, 230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255,255,255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230, 230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255,255,255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230, 230)'
        ),
        aspectratio=dict(x=1, y=1, z=0.7),
        aspectmode='manual'
    )
)

updatemenus = list([
    dict(
        buttons=list([
            dict(
                args=['type', 'surface]'],
                label='3D Surface',
                method='restyle'
            ),
            dict(
                args=['type', 'heatmap'],
                label='Heatmap',
                method='restyle'
            )
        ]),
        direction='left',
        pad={'r': 10, 't': 10},
        showactive=True,
        type='buttons',
        x=0.1,
        xanchor='left',
        y=1.1,
        yanchor='top'
    ),
])

annotations = list([
    dict(text='Trace type:', x=0, y=1.085, yref='paper', align='left', showarrow=False)
])
layout['updatemenus'] = updatemenus
layout['annotations'] = annotations

fig = dict(data=data, layout=layout)
py.iplot(fig, filename='cmocean-picker-one-button')
