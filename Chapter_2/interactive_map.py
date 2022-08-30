import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame(data={'university':['Harvard University','Yale University',
'Princeton University','Columbia University','Brown University',
'Dartmouth University','University of Pennsylvania','Cornell University'],
'latitude':[42.3770,41.3163,40.3573,40.8075,41.8268,43.7044,39.9522,42.4534],
'longitude':[-71.1167,-72.9223,-74.6672,-73.9626,-71.4025,-72.2887,
-75.1932,-76.4735]}
                )

fig = go.Figure(data=go.Scattergeo(
        lon = df['longitude'],
        lat = df['latitude'],
        text = df['university'],
        ))

fig.update_layout(
        geo_scope='usa',
    )

st.plotly_chart(fig)
