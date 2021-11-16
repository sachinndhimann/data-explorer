import streamlit as st
from streamlit_agraph import agraph, Config,Node,Edge
import pandas as pd
import json
st.sidebar.title("Import Options")
f=st.sidebar.file_uploader("Upload File")
#import streamlit.components.v1 as components
nodes=[]
edges=[]
data_dictionary=[]
if st.sidebar.button("Click to View Lineage"):
    inp_file=json.load(f)
    df=pd.json_normalize(inp_file)
    nodes_list=[]
    nodes_list2=[]
    nodes_list=df["source"].tolist()
    nodes_list2=df["target"].tolist()
    nodes_list.extend(nodes_list2)
    nodes_list=list(set(nodes_list))
    for node in nodes_list:    
        nodes.append(Node(id=node, size=500, label=node))
    tfn=df["transformationRule"].tolist()
    for index,t in enumerate(tfn):
        sequence=index+1
        #rule_id=f"Rule_{sequence}"
        nodes.append(Node(id=t, size=300, label="Rule",symbolType="square",color="#f56642"))
        #data_dictionary.append([rule_id,t])
    for idx,rows in df.iterrows():
        if rows["transformationRule"]:
            edges.append( Edge(source=rows["source"], target=rows["transformationRule"]))
            edges.append( Edge(source=rows["transformationRule"], target=rows["target"]))
        else:
            edges.append( Edge(source=rows["source"], target=rows["target"]))
    config = Config(height=500, width=600, nodeHighlightBehavior=True, highlightColor="#F7A7A6", directed=True,
                  collapsible=True)
    agraph(nodes, edges, config)
    if st.button("Export this Lineage"):
        pass
    #st.plotly_chart([""])
