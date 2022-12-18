import dash as ds
#import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash import html

happiness = pd.read_csv("world_happiness.csv")
region_options=[{'label':i, 'value':i} for i in happiness['region'].unique()]
country_options=[{'label':i, 'value':i} for i in happiness['country'].unique()]
line_fig=px.line(happiness[happiness['country']=='United States'], x='year',y='happiness_score', title='Happiness Score in the USA')


#Themes : "https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes"
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])






app = ds.Dash(__name__, external_stylesheets=[dbc.themes.YETI])
server = app.server


@app.callback(
    Output(component_id='output-text',component_property='children'), 
    Input(component_id='input-text',component_property='value')
)
def update_output_div(input_text):
    return f'Text: {input_text}'

    
app.layout = dbc.Tabs([
    dbc.Tab([
        html.Div([
                html.H1('OM Shri Ganeshay Namah',
                style={'color': 'blue',
                        'fontSize': '40px'}
                
                ),
                dcc.Input(id='input-text',value='Change this text',type='text' ),
                html.Div(id='output-text')
        ])


    ],label='Dhiren'),



    dbc.Tab([
        dbc.Tabs([
        dbc.Tab([
        html.Div([
        html.H1('Poverty And Equity Database',
                style={'color': 'blue',
                'fontSize': '40px'}),
                html.H2('The World Bank'),
                html.P('Key Facts:'),
                #html.Ul([
                html.Ol([
                    html.Li('Number of Economies: 170'),
                    html.Li('Temporal Coverage: 1974 - 2019'),
                    html.Li('Update Frequency: Quarterly'),
                    html.Li('Last Updated: March 18, 2020'),
                    html.Li([
                        'Source: ',
                    html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database', 
                    href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                            ])
                    ])
                    ])
        ]   , label='Key Facts'),

        dbc.Tab([
            html.Ul([
                html.Br(),
                html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
                html.Li(['GitHub repo: ',
                        html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                                href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')])
            ])
        ], label='Project Info'),
        

        dbc.Tab([
            html.Div([
                html.H1('World Happiness Dashboard',
                style={'color': 'blue',
                'fontSize': '40px'}),

                html.P(['This dashboard shows the happiness score.',
                    html.Br(), 
                    html.A('World Happiness Report Data Source', 
                    href='https://worldhappiness.report/',
                    target = '_blank')
                ]),
                dcc.RadioItems(options=region_options,
                value='North America'),       
                dcc.Checklist(options=region_options,
                value=['North America']) ,           
                dcc.Dropdown(options=country_options,
                value=['United States'])  ,
                dcc.Graph(figure=line_fig)         
            ])
        ], label='World Happiness')
        ])
        ],label='Plotly')

                ] )



if __name__ == '__main__':
    app.run_server(debug=True)
