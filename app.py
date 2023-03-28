import pandas as pd
import folium
import streamlit.components.v1 as components
from geopy.geocoders import Nominatim
import streamlit as st
import branca

st.set_page_config(page_title="Cartographie des produits alimentaires, leurs pays de vente et informations végétariennes",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Cartographie des produits alimentaires, leurs pays de vente et informations végétariennes")

st.markdown(
    """
    <style>
    .theme-primary {
    background-color: #00b894 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def afficher_carte_pays_de_ventes(produits_filtrés):
    geolocator = Nominatim(user_agent="myGeocoder")
    carte = folium.Map(location=[20, 0], zoom_start=2)
    cache_geocode = {}

    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
    
    for index, produit in produits_filtrés.iterrows():
        pays_de_ventes = produit['Pays_de_ventes'].split(', ')
        color = colors[index % len(colors)]
        
        for pays in pays_de_ventes:
            if pays not in cache_geocode:
                try:
                    location = geolocator.geocode(pays,timeout=5)
                    cache_geocode[pays] = (location.latitude, location.longitude)
                except AttributeError:
                    print(f"Impossible de trouver les coordonnées géographiques pour '{pays}'")
            if pays in cache_geocode:
                latitude, longitude = cache_geocode[pays]
                folium.Marker(location=[latitude, longitude], popup=f"{produit['Produit']} - {pays}", icon=folium.Icon(color=color)).add_to(carte)
    return carte


def folium_static(map):
    map_html = map._repr_html_()
    components.html(map_html, width=600, height=400, scrolling=False)

def main():
    data = pd.read_csv('./OpenFoodFacts.csv', sep=',')
    nom_produit = st.text_input("Veuillez saisir un mot clé pour le produit : ")

    if nom_produit:
        produits_filtrés = data[data['Produit'].str.contains(nom_produit, case=False)]

        if not produits_filtrés.empty:
            col1, col2 = st.columns(2)

            with col1:
                carte = afficher_carte_pays_de_ventes(produits_filtrés)
                folium_static(carte)

            with col2:
                st.subheader("Informations végétariennes")  # Ajout d'un titre pour les informations végétariennes
                for index, produit in produits_filtrés.iterrows():
                    nom_complet = produit['Produit']
                    vegetarian_info = produit['vegetarian_info']
                    st.write(f"Le produit '{nom_complet}' est:", vegetarian_info)

        else:
            st.write("Aucun produit correspondant trouvé. Veuillez réessayer.")

if __name__ == "__main__":
    main()
