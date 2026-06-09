import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('formatted_sales.csv')

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and sum sales
daily_sales = df.groupby('date')['sales'].sum().reset_index()

# Sort by date
daily_sales = daily_sales.sort_values('date')

# Create the line chart
fig = px.line(daily_sales, x='date', y='sales', title='Sales Before and After Pink Morsel Price Increase')

# Update axis labels
fig.update_xaxes(title_text='Date')
fig.update_yaxes(title_text='Total Sales (USD)')

# Add a vertical line at 2021-01-15
fig.add_vline(x=pd.to_datetime('2021-01-15'), line_width=2, line_dash="dash", line_color="red")

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Soul Foods Sales Visualiser'),
    dcc.Graph(
        id='sales-chart',
        figure=fig
    )
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)