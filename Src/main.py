import streamlit as st
import pandas as pd
import plotly.express as px


import SpeckleConnection as SC


st.set_page_config (
    page_title="Minecraft building visualizer",
    page_icon="🎲"
)

# page structure
header  = st.container ()
input   = st.container ()
viewer  = st.container ()
report  = st.container ()
graphs  = st.container ()

with header:
    st.title ("🎲Minecraft building visualizer🎲")

with header.expander ("About🔽", expanded=True):
    st.markdown (
        """This is a beginner web app developed using Streamlit. My goal was to understand how to interact with Speckle API using SpecklePy, 
        analyze what is received and its structure. This was easy and fun experiment.
        """
    )

with input:
    st.subheader ("Inputs")
    serverCol, tokenCol = st.columns ( [1, 3])


    branches = SC.client.branch.list (SC.stream.id)
    commits = SC.client.commit.list (SC.stream.id, limit=100)
def commit2viewer(stream, commit, height=400) -> str:
    embed_src = "https://speckle.xyz/embed?stream="+stream.id+"&commit="+commit.id
    print (embed_src)
    return st.components.v1.iframe(src=embed_src, height=height)

with viewer:
    st.subheader ("Latest commit")
    commit2viewer (SC.stream, commits[0])