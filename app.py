import streamlit as st
import os

# Configuración del Pizarrón Escolar
st.set_page_config(page_title="Clase de Ciencias: Capas de la Tierra", page_icon="🌍", layout="wide")

st.title("🌍 Esquema Visual Interactivo: Las Capas de la Tierra")
st.markdown("### CBTIS 303 | Recursos Didácticos de Ciencias Naturales")
st.write("Selecciona una capa en las pestañas para desplegar su estructura real, ilustraciones científicas e información clave.")

# Definimos las rutas a tus archivos locales (incluyendo el carrusel de la atmósfera)
IMAGENES_CAPAS = {
    "Vista General": "general.gif",
    "Geosfera": "geosfera.jpg",
    "Hidrosfera": "hidrosfera.jpg",
    "Atmo_Distancia": "atmosfera_distancia.jpg",
    "Atmo_Temperatura": "atmosfera_temperatura.jpg"
}

# Función auxiliar para mostrar imagen local
def mostrar_imagen(nombre_archivo, texto_alternativo):
    if os.path.exists(nombre_archivo):
        st.image(nombre_archivo, caption=texto_alternativo, use_container_width=True)
    else:
        st.warning(f"⚠️ Guarda una imagen llamada '{nombre_archivo}' en tu carpeta para verla aquí.")

# Creación de pestañas interactivas superiores
tab_general, tab_geo, tab_hidro, tab_atmo = st.tabs(["🌍 Nuestro Planeta", "⛰️ La Geosfera", "💧 La Hidrosfera", "🌤️ La Atmósfera"])

with tab_general:
    col1, col2 = st.columns(2)
    with col1:
        mostrar_imagen(IMAGENES_CAPAS["Vista General"], "La Tierra vista desde el espacio exterior.")
    with col2:
        st.info("### El Sistema Terrestre")
        st.write("La Tierra no es solo una roca flotando; es un conjunto de subsistemas que interactúan de manera constante para albergar la vida.")
        st.markdown("• **Estructura Concéntrica:** Desde la atmósfera exterior hasta el núcleo de metal denso, cada capa tiene un grosor y función específica basados en la física real.")

with tab_geo:
    col1, col2 = st.columns([1.2, 1])
    with col1:
        mostrar_imagen(IMAGENES_CAPAS["Geosfera"], "Esquema a escala de la estructura interna (Corteza, Manto y Núcleo)")
    with col2:
        st.success("### ⛰️ La Geosfera")
        st.markdown("**Grosor y composición real:**")
        st.markdown("- **Corteza (0 - 70 km):** Capa rocosa externa y sólida. Es apenas el 1% del volumen del planeta.")
        st.markdown("- **Manto (70 - 2,890 km):** Roca sólida y semisólida caliente sometida a altas presiones.")
        st.markdown("- **Núcleo (2,890 - 6,371 km):** Esfera de hierro y níquel dividida en un exterior líquido y un centro sólido extremadamente denso.")

with tab_hidro:
    col1, col2 = st.columns(2)
    with col1:
        mostrar_imagen(IMAGENES_CAPAS["Hidrosfera"], "Distribución del agua global")
    with col2:
        st.info("### 💧 La Hidrosfera")
        st.markdown("**Distribución real del agua en la Tierra:**")
        st.markdown("• **97.5% Agua Salada:** Mares y océanos que cubren la mayor parte de la corteza.")
        st.markdown("• **2.5% Agua Dulce:** Concentrada principalmente en los glaciares de los polos, aguas subterráneas y una mínima fracción en ríos y lagos.")

with tab_atmo:
    col1, col2 = st.columns([1.2, 1])
    with col1:
        # 👇 Carrusel dinámico usando sub-pestañas internas
        subtab_distancia, subtab_temperatura = st.tabs(["📏 Escala de Distancias", "🌡️ Gráfico de Temperaturas"])
        
        with subtab_distancia:
            mostrar_imagen(IMAGENES_CAPAS["Atmo_Distancia"], "Infografía de las alturas de cada capa atmosférica.")
        with subtab_temperatura:
            mostrar_imagen(IMAGENES_CAPAS["Atmo_Temperatura"], "Esquema térmico: cómo cambia la temperatura al subir.")
            
    with col2:
        st.warning("### 🌤️ La Atmósfera")
        st.markdown("**Capas físicas del escudo gaseoso:**")
        st.markdown("1. **Troposfera (0 - 12 km):** Alberga el aire respirable y los fenómenos meteorológicos.")
        st.markdown("2. **Estratosfera (12 - 50 km):** Contiene la capa de ozono que filtra la radiación UV.")
        st.markdown("3. **Mesosfera, Termosfera y Exosfera:** Capas externas donde los gases se disipan hacia el espacio exterior.")
