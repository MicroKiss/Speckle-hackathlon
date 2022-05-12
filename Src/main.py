import streamlit as st
import pandas as pd
import plotly.express as px
import SpeckleConnection as SC
import os
from pathlib import Path
from BlockData import BlockData
import AmuletHelper
from  BlockDataParser import ParseBlockDatas
from specklepy.objects import Base

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

    # World selection
    saveDir : Path = Path(os.getenv('APPDATA'), '.minecraft', 'saves')
    saveName : str = None

    def processBlocks (blocks : 'list[BlockData]'):
        parsedDatas = ParseBlockDatas (blocks)
        obj = Base()
        obj.add_chunkable_attrs (entities = 5000)
        obj.entities = parsedDatas
        SC.Send (obj)

    if not saveDir.exists():
        st.text('Minecraft saves path not found.')
    else:
        saveNames = [save for save in saveDir.iterdir() if save.is_dir()]
        saveName = st.selectbox(label="Select your savefile", options=saveNames, help="Select your savefile from the dropdown", format_func=(lambda x : x.name))

    if not saveName == None:
    # Input method selection 0 -> player, 1 -> bbox
        selection = st.radio(label="Block area selection method", options=[0, 1],
                            format_func=(lambda x : "Around player" if x == 0 else "Bounding Box by Coordinates"))
        # player
        if selection == 0:
            r : int = st.number_input(label="Set the radius around the player", min_value=1, step=1)
            st.button(label="Get", on_click=(lambda: processBlocks (AmuletHelper.GetBlockAroundPlayer(r, saveName))))
        # bbox
        else:
            colX1, colY1, colZ1 = st.columns([1, 1, 1])
            x1 = colX1.number_input(label="x1", step=1, value=0)
            y1 = colY1.number_input(label="y1", step=1, value=0)
            z1 = colZ1.number_input(label="z1", step=1, value=0)
            colX2, colY2, colZ2 = st.columns([1, 1, 1])
            x2 = colX2.number_input(label="x2", step=1, value=0)
            y2 = colY2.number_input(label="y2", step=1, value=0)
            z2 = colZ2.number_input(label="z2", step=1, value=0)
            (minX, maxX) = (x1, x2) if x1 < x2 else (x2, x1)
            (minY, maxY) = (y1, y2) if y1 < y2 else (y2, y1)
            (minZ, maxZ) = (z1, z2) if z1 < z2 else (z2, z1)
            st.button(label="Get", on_click=(lambda: processBlocks(AmuletHelper.GetBlockFromBBox(minX, minY, minZ, maxX, maxY, maxZ, saveName))))

    branches = SC.client.branch.list (SC.stream.id)
    commits = SC.client.commit.list (SC.stream.id, limit=100)
def commit2viewer(stream, commit, height=400) -> str:
    embed_src = "https://speckle.xyz/embed?stream="+stream.id+"&commit="+commit.id
    print (embed_src)
    return st.components.v1.iframe(src=embed_src, height=height)

with viewer:
    st.subheader ("Latest commit")
    commit2viewer (SC.stream, commits[0])