import dash
from dash import dcc, html
from dash.testing.application_runners import import_app
import pytest


def test_header_present(dash_duo):
    # Import the app from app.py
    app = import_app('app', 'app')
    dash_duo.start_server(app)
    
    # Find the H1 element
    header = dash_duo.find_element('h1')
    assert header is not None
    assert header.text == 'Soul Foods Sales Visualiser'


def test_visualisation_present(dash_duo):
    app = import_app('app', 'app')
    dash_duo.start_server(app)
    
    # Find the graph by its id
    graph = dash_duo.find_element('#sales-chart')
    assert graph is not None


def test_region_picker_present(dash_duo):
    app = import_app('app', 'app')
    dash_duo.start_server(app)
    
    # Find the radio items by its id
    radio_items = dash_duo.find_element('#region-filter')
    assert radio_items is not None