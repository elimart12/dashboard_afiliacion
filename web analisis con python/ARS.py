import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd


data = {
    'ARS': ['SENASA', 'PRIMERA ARS', 'ARS MAPHRE SALUD', 'OTRAS ARS'],
    'Afiliados': [1688290, 1350000, 850000, 1516798,],
}

df = pd.DataFrame(data)


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Distribucion de ARS en RD'),

    dcc.Graph(
        id='grafico-afiliados',
        figure=px.bar(df, x='ARS', y='Afiliados', title='Afiliados por ARS'),
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)
