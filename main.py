
import streamlit as st
from lineage_generator import canvas
st.title("Integrator for Data Governance")


def lineage_integrator_interface(st):
    file_upload_type=["PPT","IMAGE"]
    type_of_input=["PPT","CANVAS","IMAGE"]
    type_of_data_input=["",""]
    type_of_lineage=["SYSTEM LINEAGE","DATA LINEAGE"]
    modes_of_output=["JSON","CSV","API"]

    lineage=st.selectbox("Type mode of Lineage",type_of_lineage,key=2)
    if lineage=="SYSTEM LINEAGE":
        mode_of_input=st.selectbox("Type mode of Input",type_of_input,key=1)
    else:
        mode_of_input=st.selectbox("Type mode of Input",type_of_data_input,key=1)
    
    if mode_of_input=="CANVAS":
        canvas(st)
    elif mode_of_input in file_upload_type:
        pass


    output=st.selectbox("Output Option",modes_of_output,key=3)

    action=st.button("Generate Lineage")

def data_curator(st):
    pass