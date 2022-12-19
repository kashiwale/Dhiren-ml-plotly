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



#Themes : "https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes"
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])






app = ds.Dash(__name__, external_stylesheets=[dbc.themes.YETI])
server = app.server

data_options = [{'label':'Happiness Score','value':'happiness_score'},
                {'label':'Happiness Rank','value':'happiness_rank'}]
@app.callback(
    Output('happiness-graph','figure'), 
    Output('average-div','children'),
    Input('country-dropdown','value'), 
    Input('data-radio','value')
)
def update_output_div(selected_country, selected_data):
    filtered_happiness = happiness[happiness['country']==selected_country]
    line_fig=px.line(filtered_happiness, 
                        x='year',y=selected_data, 
                        title=f'{selected_data} in {selected_country}')
    selected_avg = filtered_happiness[selected_data].mean()
    return line_fig, f'The average {selected_avg} for {selected_country} is ' \
                    f'{selected_avg}'



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
                dcc.Dropdown(id='country-dropdown',options=country_options,
                value='United States')  ,
                dcc.RadioItems(id='data-radio', 
                options=data_options,
                value='happiness_score'),
                #dcc.Graph(id='happiness-graph',figure=line_fig) 
                dcc.Graph(id='happiness-graph') ,
                html.Div(id='average-div')
            ])
        ], label='World Happiness')
        ])
        ],label='Plotly')

                ] )



if __name__ == '__main__':
    app.run_server(debug=True)
