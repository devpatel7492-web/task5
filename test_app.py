import pytest
from dash.testing.application_runners import import_app

# Load your Dash app
app = import_app("index")  # filename without .py


# ✅ 1. Test Header Exists
def test_header_present(dash_duo):
    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Soul Foods Sales Dashboard" in header.text


# ✅ 2. Test Graph Exists
def test_graph_present(dash_duo):
    dash_duo.start_server(app)

    graph = dash_duo.find_element("#sales-graph")
    assert graph is not None


# ✅ 3. Test Radio Button Exists
def test_radio_present(dash_duo):
    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-filter")
    assert radio is not None