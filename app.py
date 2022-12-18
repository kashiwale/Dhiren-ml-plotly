import dash as ds
#import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import html

#Themes : "https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes"
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app = ds.Dash(__name__, external_stylesheets=[dbc.themes.YETI])
server = app.server
app.layout = dbc.Tabs([
    dbc.Tab([
        html.Div([
                html.H1('OM Shri Ganeshay Namah',
                style={'color': 'blue',
                        'fontSize': '40px'}
                
                )
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
                ])
            ])
        ], label='World Happiness')
        ])
        ],label='Plotly')

                ] )



if __name__ == '__main__':
    app.run_server(debug=True)
