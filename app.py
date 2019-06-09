#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:52:34 2019

@author: Matthew Dunlop

this file describes the application used to take user inputs,
send them to the pricing function and return the outputs.

~ Specially formatted for Heroku App

"""

# -*- coding: utf-8 -*-
import dash # to provide intuitive User Interface
import dash_core_components as dcc # for dash sliders and buttons
import dash_html_components as html # dash page structure
from dash.dependencies import Input, Output, State # interactive dash features
from textwrap import dedent as d # properly fit pages and text
import numpy as np # array operations
import time # to record the run time


# import the Monte-Carlo Pricer
import master_pricing_function # custom script taking user inouts and returning
# the pricing outputs

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# CSS code makes the site look better

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
# Creating the application object

#####
# Application layout
#
# this chunk of code determines how the app will look

app.layout =html.Div([
                html.Div([
                        # this first part takes the user input variables
                        # also defines the range available for sliders etc
                    html.Div([
                            html.H3('Share Price (Now)'),
                            html.Div([
                                    html.Div(id = 'S-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: i for i in range(0, 200, 25)},
                                    min=0,
                                    max=200,
                                    step = 0.5,
                                    value=60,
                                    id='S-state'
                                    )
                                    
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                                            
                            html.Div([
                                    
                                    ]),
                                            
                            html.Div([
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """)),
                                    
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                                    
                            
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                    
                    html.Div([
                            html.H3('Strike Price'),
                            html.Div([
                                    html.Div(id = 'K-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: i for i in range(0, 200, 25)},
                                    min=0,
                                    max=200,
                                    step = 0.5,
                                    value=50,
                                    id='K-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            
                            
                            
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                    
                    html.Div([
                            html.H3('First Barrier Level'),
                            html.Div([
                                    html.Div(id = 'H1-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: i for i in range(0, 200, 25)},
                                    min=0,
                                    max=200,
                                    step = 0.5,
                                    value=65,
                                    id='H1-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            
                            
                            
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                    
                    html.Div([
                            html.H3('Second Barrier Level'),
                            html.Div([
                                    html.Div(id = 'H2-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: i for i in range(0, 200, 25)},
                                    min=0,
                                    max=200,
                                    step = 0.5,
                                    value=85,
                                    id='H2-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            
                            
                            
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                    
                    html.Div([
                            html.H3('Risk-Free Rate'),
                            html.Div([
                                    html.Div(id = 'r-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: i for i in np.linspace(-0.5, 0.5, 5, endpoint = True)},
                                    min=-0.5,
                                    max=0.5,
                                    step = 0.001,
                                    value=0.05,
                                    id='r-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            
                            
                            
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),    
                ], className = 'row'),
                html.Div([
                    html.Div([
                            html.H3('Time to Maturity'),
                            html.Div([
                                    html.Div(id = 'T-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: i for i in range(0, 20, 5)},
                                    min=0,
                                    max=10,
                                    step = 0.1,
                                    value=1,
                                    id='T-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                    
                    html.Div([
                            html.H3('Volatilty'),
                            html.Div([
                                     html.Div(id = 'sigma-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: i for i in np.linspace(0, 1, 5, endpoint = True)},
                                    min=0,
                                    max=1,
                                    step = 0.01,
                                    value=0.3,
                                    id='sigma-state'
                                    )
                                           
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            
                            
                            
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                    
                    html.Div([
                            html.H4('Number of Working Days'),
                            html.Div([
                                    html.Div(id = 'n-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: int(round(i)) for i in np.linspace(0, 366, 5, endpoint = True)},
                                    min=0,
                                    max=366,
                                    step = 1,
                                    value=260,
                                    id='n-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            
                            
                            
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                    
                    html.Div([
                            html.H4('Number of Paths to Simulate'),
                            html.Div([
                                    html.Div(id = 'nr-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: '{}'.format(10**i) for i in range(2,4)},
                                    min=2,
                                    max=4,
                                    step = 0.05,
                                    value=3.69897,
                                    id='nr-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            
                            
                            
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                    
                    html.Div([
                            html.H3('Pricing Method'),
                            # decides which pricing method to use
                             html.Div([
                                    html.Div(id = 'method-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Dropdown(
                                        options=[
                                            {'label': 'Crude Monte Carlo', 'value': 0},
                                            {'label': 'AVT Monte Carlo', 'value': 1},
                                            {'label': 'NPO Crude Monte Carlo', 'value': 2},
                                            {'label': 'NPO AVT Monte Carlo', 'value': 3},
                                        ],
                                        value=0, id = 'method-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            
                            
                            html.Div([
                                    
                                    dcc.Markdown(d("""
                                        ***
                                        
                                    """))
                                    
                                    ],style = {'width': '60%', 'vertical-align': 'top'}),
                            
                            # dcc.Input(id='input-1-state', type='text', value='Montréal'),
                            
                    ], style = {'width': '19%', 'display': 'inline-block', 'vertical-align': 'top'}),
                                
                ], className='row'),
                # this next part of the app returns the outputs as figures
                html.Div([
                        html.Div(id = 'price-state', children='Choose values and press submit'),
                        html.Div(id = 'price_std-state', children='Choose values and press submit'),
                        html.Div(id = 'counter1-state', children='Choose values and press submit'),
                        html.Div(id = 'counter1_std-state', children='Choose values and press submit'),
                        html.Div(id = 'counter2-state', children='Choose values and press submit'),
                        html.Div(id = 'counter2_std-state', children='Choose values and press submit'),
                        html.Div(id = 'runtime-state', children='Choose values and press submit')
                        
                        ],style = {'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'}),
                html.Div([
                        html.Button(id='submit-button', n_clicks=0, children='Run Simulation!'),
                        
                        html.Img(src=app.get_asset_url('full_bench.png'), width = "80%"),
                        html.Img(src=app.get_asset_url('part_bench.png'), width = "80%"),
                        html.Div([
                            html.H6('Counter 1 Level'),
                            html.Div([
                                    html.Div(id = 'rq1-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: int(round(i)) for i in np.linspace(0, 366, 5, endpoint = True)},
                                    min=0,
                                    max=366,
                                    step = 1,
                                    value=100,
                                    id='rq1-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'})
                        ]),
                        html.Div([
                            html.H6('Counter 2 Level'),
                            html.Div([
                                    html.Div(id = 'rq2-o-state')
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                            html.Div([
                                    dcc.Slider(
                                    marks={i: int(round(i)) for i in np.linspace(0, 366, 5, endpoint = True)},
                                    min=0,
                                    max=366,
                                    step = 1,
                                    value=150,
                                    id='rq2-state'
                                    ),
                                            
                                    ],style = {'width': '90%', 'vertical-align': 'top'}),
                        ])
                        
                        ],style = {'width': '20%', 'display': 'inline-block', 'vertical-align': 'top'}),
                html.Div([
                        dcc.Markdown(d("""
                                       ##### Pricing Method Descriptions:
                                        * **Crude Monte Carlo** uses a Python _for_ loop to iterate over each share price, using a matrix of normal variates for daily share return.
                                        * **AVT Monte Carlo** is the same as Crude Monte Carlo but implements Antithetic Variates Technique (AVT) to reduce variance and compute time.
                                        * **NPO Crude Monte Carlo** replaces the Python _for_ loop with Numpy optimized code, resulting in faster compute time.
                                        * **NPO AVT Monte Carlo** implements AVT with Numpy optimized code.
                                        #### Heroku Version Notes:
                                        * PyTorch has been removed as the project size was too large to be deployed on Heroku!
                                        * As RAM on Heroku is limited to 512MB and this is simply a proof-of-concept app, maximum number of paths to simulate is capped at 10,000.
                                        >
                                        > *Created by Matthew Dunlop, penultimate-year BSc. Financial Mathematics student at University College Dublin.*
                                        >
                                    """))
                        
                        ],style = {'width': '55%', 'display': 'inline-block', 'vertical-align': 'top'})
                
                

            ], className='column')

# Heads up for slider inputs
# this function is called each time an input variable is called
# it updates and output area beside the slider, showing what the
# current value for that variable is.
@app.callback([Output('S-o-state', 'children'),
              Output('K-o-state', 'children'),
              Output('H1-o-state', 'children'),
              Output('H2-o-state', 'children'),
              Output('r-o-state', 'children'),
              Output('T-o-state', 'children'),
              Output('sigma-o-state', 'children'),
              Output('n-o-state', 'children'),
              Output('nr-o-state', 'children'),
              Output('method-o-state', 'children'),
              Output('rq1-o-state', 'children'),
              Output('rq2-o-state', 'children')],
              [Input('S-state', 'value'),
              Input('K-state', 'value'),
              Input('H1-state', 'value'),
              Input('H2-state', 'value'),
              Input('r-state', 'value'),
              Input('T-state', 'value'),
              Input('sigma-state', 'value'),
              Input('n-state', 'value'),
              Input('nr-state', 'value'),
              Input('method-state', 'value'),
              Input('rq1-state', 'value'),
              Input('rq2-state', 'value')])
def heads_up(S, K, H1, H2, r, T, sigma, n, nr, method, rq1, rq2):
    # dash has new multiple output capability
    # we return the current value of each of the varaibles
    ret = [i for i in [S, K, H1, H2, r, T, sigma, n,int(round( 10 **nr)), method, rq1, rq2]]
    return ret

#####
# Option Pricing
#
# This function actually prices the option, using the
# user specified inputs, and returns the output
# to the results field.
@app.callback([Output('price-state', 'children'),
               Output('price_std-state', 'children'),
               Output('counter1-state', 'children'),
               Output('counter1_std-state', 'children'),
               Output('counter2-state', 'children'),
               Output('counter2_std-state', 'children'),
               Output('runtime-state', 'children')],
              [Input('submit-button', 'n_clicks')],
              [State('S-state', 'value'),
              State('K-state', 'value'),
              State('H1-state', 'value'),
              State('H2-state', 'value'),
              State('r-state', 'value'),
              State('T-state', 'value'),
              State('sigma-state', 'value'),
              State('n-state', 'value'),
              State('nr-state', 'value'),
              State('method-state', 'value'),
              State('rq1-state', 'value'),
              State('rq2-state', 'value')])
def update_output(n_clicks, S, K, H1, H2, r, T, sigma, n, nr, method, rq1, rq2):
    # convert number of simulations from log-scale
    nr = int(round((10 **nr)/2))*2
    # send the inputs to the pricing function
    t_start = time.time() # to time the pricing process
    # now to do the actual pricing! See master_pricing_function.py
    ave1, std1, ave2, std2, price, p_std = master_pricing_function.Barrier_Option_Pricer(ret = 1, Var_red = method,
                                                                                         nr = nr, S = S, K = K,
                                                                                         H1 = H1, H2 = H2, r = r,
                                                                                         T = T, sigma = sigma, n = n)
    t_price = time.time()-t_start # find time taken
    # Return the outputs to the user
    ret = [i for i in ["Price Mean: {}".format(round(price,5)),
                       "Price Standard Deviation: {}".format(round(p_std,5)),
                       "Counter 1 Mean: {}".format(round(ave1,5)),
                       "Counter 1 Standard Deviation: {}".format(round(std1,5)),
                       "Counter 2 Mean: {}".format(round(ave2,5)),
                       "Counter 2 Standard Deviation: {}".format(round(std2,5)),
                       "Program Run Time: {}".format(round(t_price, 5))]]
    return ret





if __name__ == '__main__':
    app.run_server() # upon execution, run the app
    # default server is 0.0.0.0:8050