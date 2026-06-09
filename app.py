import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('formatted_sales.csv')

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout with styling
app.layout = html.Div([
    html.H1('Soul Foods Sales Visualiser', 
            style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}),
    
    html.Div([
        html.Label('Select Region:', 
                   style={'fontWeight': 'bold', 'marginRight': '10px', 'color': '#34495e'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': ' North ', 'value': 'north'},
                {'label': ' East ', 'value': 'east'},
                {'label': ' South ', 'value': 'south'},
                {'label': ' West ', 'value': 'west'},
                {'label': ' All ', 'value': 'all'}
            ],
            value='all',
            style={'display': 'flex', 'flexDirection': 'row', 'gap': '15px'},
            labelStyle={'display': 'inline-block', 'marginRight': '15px', 'padding': '5px 10px', 
                       'borderRadius': '5px', 'backgroundColor': '#ecf0f1', 'cursor': 'pointer'},
            inputStyle={'marginRight': '5px'}
        )
    ], style={'textAlign': 'center', 'marginBottom': '30px', 'padding': '20px', 
              'backgroundColor': '#f8f9fa', 'borderRadius': '10px'}),
    
    dcc.Graph(
        id='sales-chart',
        style={'height': '500px'}
    )
], style={'fontFamily': 'Arial, sans-serif', 'margin': '20px', 'backgroundColor': '#ffffff'})

# Define callback to update chart based on selected region
@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data based on selected region
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]
    
    # Group by date and sum sales
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    
    # Sort by date
    daily_sales = daily_sales.sort_values('date')
    
    # Create the line chart
    fig = px.line(daily_sales, x='date', y='sales', 
                  title=f'Sales Before and After Pink Morsel Price Increase - {selected_region.title()} Region')
    
    # Update axis labels
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Total Sales (USD)')
    
    # Add a vertical line at 2021-01-15
    fig.add_vline(x=pd.to_datetime('2021-01-15'), line_width=2, line_dash="dash", line_color="red")
    
    # Update layout for better appearance
    fig.update_layout(
        title_font_size=16,
        title_font_color='#2c3e50',
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)