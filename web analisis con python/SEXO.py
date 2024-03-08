import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# DATOS AFILIACION HOMBRE  Y MUJER AL 2023
data = {
    "Año": [202312, 202312],
    "Total Afiliado": [2241509.00, 1042214.00],
    "Sexo": ["Hombre", "Mujer"],
    "Rango Edad": ["15-85", "15-89"]
}

df = pd.DataFrame(data)


app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Dashboard de Afiliados'),

    dcc.Graph(
        id='afiliados-chart',
        figure=px.bar(df, x='Sexo', y='Total Afiliado', color='Sexo', title='Afiliados por Sexo')
    )
])

# Ejecutar
if __name__ == '__main__':
    app.run_server(debug=True)
