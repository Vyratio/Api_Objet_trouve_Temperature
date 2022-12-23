import streamlit as st
import streamlit_folium as sf
from data_visualisation_api import *

st.set_page_config(page_title="Objet Perdus SNCF", page_icon=":bullettrain_side:",layout="wide")


# header

with st.container():

    st.header("Analyse des objets perdus dans la SNCF :steam_locomotive:")
   
    
   
# section 1

with st.container():

    left_col,right_col = st.columns(2)

    with left_col:
        
        st.header("Le nombre des objets trouvés")
        st.write("Dans le graph à côté on affiche la somme du nombre d’objets perdus par les voyageurs de la SNCF par semaine pendant la période entre 2016 et 2021.")

    with right_col:

        st.plotly_chart(fig)
        
# section 2

with st.container():

    left_col,right_col = st.columns(2)

    with left_col:
        
        st.header("L'évolution des objets perdus.'")
        st.write("Dans le graph à côté on affiche l'évolution du nombre des objets perdus par les voyageurs de la SNCF par semaine pendant la période entre 2016 et 2021.")

    with right_col:

        st.plotly_chart(ax1)
            
# section 3

with st.container():

    left_col,right_col = st.columns(2)

    with left_col:
        
        st.header("La carte des objets perdus")
        st.write("Ici on affiche une carte de France avec le nombre des objets perdus en fonction de la fréquentation de voyageur de chaque région.")

    with right_col:

       
        sf.folium_static(m)