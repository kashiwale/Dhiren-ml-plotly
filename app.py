from pydoc import classname
import dash as ds
#import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from dash import html


happiness = pd.read_csv("world_happiness.csv")
soccer=pd.read_csv('fifa_soccer_players.csv')
region_options=[{'label':i, 'value':i} for i in happiness['region'].unique()]
#country_options=[{'label':i, 'value':i} for i in happiness['country'].unique()]
player_name_options=[{'label': i, 'value': i} for i in soccer['long_name'].unique()]


#Themes : "https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/#available-themes"
#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])






# app = ds.Dash(__name__, external_stylesheets=[dbc.themes.YETI,'/assets/stylesheet.css'])
app = ds.Dash(__name__, external_stylesheets=[dbc.themes.YETI])
server = app.server

data_options = [{'label':'Happiness Score','value':'happiness_score'},
                {'label':'Happiness Rank','value':'happiness_rank'}]


@app.callback(
    Output('country-dropdown','options'),
    Output('country-dropdown','value'),
    Input('region-radio','value')
)
def update_dropdown(selected_region):
    filtered_happiness = happiness[happiness['region']==selected_region]
    country_options=[{'label':i, 'value':i} for i in filtered_happiness['country'].unique()]
    return country_options, country_options[0]['value']
@app.callback(
    Output('happiness-graph','figure'), 
    Output('average-div','children'),
    Input('submit-button-state','n_clicks'),
    State('country-dropdown','value'), 
    State('data-radio','value')
)
def update_graph(button_click,selected_country, selected_data):
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
                html.H1('OM Shri Ganeshay Namah', className="om"
                # ,
                
                # style={'color': 'blue',
                #         'fontSize': '40px'}
                
                ),
                html.Img(src='/assets/DhirenCloseup.png'),
                html.Br(),
                dcc.Input(id='input-text',value='Change this text',type='text' ),
                html.Div(id='output-text')
        ], className="banner")


    ],label='Dhiren'),

    dbc.Tab([
        html.Div([
                html.H1('Soccer Players Dashboard' , 
                
                style={'textAlign':'center',
                        'fontFamily':'fantacy',
                        'fontSize':50,
                        'color':'blue'                
                }),
                html.P(['Source: ',
                    html.A('Sofifa',
                        href='https://sofifa.com',
                        target='_blank'                   
                    )               
                ],
                style={'border':'solid'}
                 ),
        html.Label('Player name: '),
        dcc.Dropdown(options=player_name_options,
        value=player_name_options[0]['value'],
        style={'backgroundColor':'lightblue'}
        )],
        style={'padding': 100, 'border':'solid'})


    ],label='Soccer'),





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
                html.Div([dcc.RadioItems(id='region-radio',options=region_options,
                value='North America')])
                ,       
                #dcc.Checklist(options=region_options,
                #value=['North America']) ,           
                dcc.Dropdown(id='country-dropdown'), # options=country_options and value will be over written by region-radio
                dcc.RadioItems(id='data-radio', 
                options=data_options,
                value='happiness_score'),
                html.Br(),
                html.Button(id='submit-button-state',
                n_clicks=0,
                children='Update the Output'
                ) ,
                #dcc.Graph(id='happiness-graph',figure=line_fig) 
                dcc.Graph(id='happiness-graph') ,
                html.Div(id='average-div')
            ])
        ], label='World Happiness')
        ])
        ],label='Plotly')

                ] )

# app.css.append_css({
#     "external_url":"https://codepen.io/chriddyp/pen/bWLwgP.css"
# })

if __name__ == '__main__':
    app.run_server(debug=True)
