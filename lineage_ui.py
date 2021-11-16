import streamlit as st
from streamlit_cytoscapejs import st_cytoscapejs

st.sidebar.title("Import Options")
st.sidebar.file_uploader("Upload File")
st.sidebar.button("Click to View Lineage")
st.sidebar.button("Export Lineage")


elements = [
    {"data": {"id": "one", "label": "Node 1"}, "position": {"x": 20, "y": 20}},
    {"data": {"id": "two", "label": "Node 2"}, "position": {"x": 100, "y": 20}},
    {"data": {"source": "one", "target": "two", "label": "Edge from Node1 to Node2"}},
]
stylesheet = [
    {"selector": "node", "style": {"width": 40, "height": 40, "shape": "circle"}},
    {"selector": "edge", "style": {"width": 5}},
]

st.title("Visualization Area")
st_cytoscapejs(elements, stylesheet)