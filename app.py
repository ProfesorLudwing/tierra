import streamlit as st
import plotly.express as px
import pandas as pd

# 1. Configuración de la interfaz de la Web App
st.set_page_config(page_title="Clase de Ciencias Naturales", page_icon="🌍", layout="wide")

st.title("🌍 Animación Interactiva: Las Capas de la Tierra")
st.markdown("### CBTIS 303 | Ciencias Naturales")
st.write("Haz clic en las diferentes capas del gráfico circular para abrir su estructura y explorar el contenido.")

# 2. Base de datos para la estructura concéntrica animada
# Definimos jerarquías: Planeta -> Capas Principales -> Subcapas
datos_capas = dict(
    capa=[
        "La Tierra", 
        "Geosfera", "Hidrosfera", "Atmósfera", 
        "Corteza", "Manto", "Núcleo", 
        "Océanos y Mares", "Agua Dulce (Ríos/Lagos)", 
        "Troposfera", "Estratosfera", "Capas Superiores"
    ],
    padre=[
        "", 
        "La Tierra", "La Tierra", "La Tierra", 
        "Geosfera", "Geosfera", "Geosfera", 
        "Hidrosfera", "Hidrosfera", 
        "Atmósfera", "Atmósfera", "Atmósfera"
    ],
    valor=[100, 35, 35, 30, 10, 15, 10, 25, 10, 10, 10, 10] # Tamaños visuales proporcionados
)

df = pd.DataFrame(datos_capas)

# 3. Diccionario con el contenido pedagógico de la clase
CONTENIDO_EDUCATIVO = {
    "Geosfera": {
        "color": "brown", 
        "titulo": "⛰️ La Geosfera",
        "intro": "Es la parte sólida, rocosa y mineral de nuestro planeta. ¡Llega hasta el mismísimo centro de la Tierra!",
        "detalles": ["Corteza: La capa más externa y delgada donde caminamos.", "Manto: Capa intermedia hecha de roca fundida (magma caliente).", "Núcleo: El centro de metal líquido y sólido. ¡Es tan caliente como la superficie del Sol!"]
    },
    "Corteza": {"color": "brown", "titulo": "🪨 La Corteza Terrestre", "intro": "Es la piel del planeta. Aquí se encuentran los continentes y el fondo del océano.", "detalles": ["Varía entre 5 y 70 km de espesor.", "Es la única capa que podemos explorar directamente."]},
    "Manto": {"color": "brown", "titulo": "🔥 El Manto", "intro": "Una capa gigantesca de roca semisólida y extremadamente caliente.", "detalles": ["Representa la mayor parte del volumen de la Tierra.", "Sus corrientes de calor mueven los continentes y causan terremotos."]},
    "Núcleo": {"color": "brown", "titulo": "🔩 El Núcleo", "intro": "El corazón de metal de la Tierra.", "detalles": ["Compuesto principalmente de hierro y níquel.", "Su movimiento genera el escudo magnético que nos protege del espacio."]},
    
    "Hidrosfera": {
        "color": "blue", 
        "titulo": "💧 La Hidrosfera",
        "intro": "Es el sistema que agrupa toda el agua de la Tierra en sus tres estados: líquido, sólido y gaseoso.",
        "detalles": ["Cubre aproximadamente el 71% de la superficie del planeta.", "Es vital para regular la temperatura global de la Tierra."]
    },
    "Océanos y Mares": {"color": "blue", "titulo": "🌊 Océanos y Mares", "intro": "La inmensa masa de agua salada de nuestro planeta.", "detalles": ["Representa más del 97% de toda el agua de la Tierra.", "Produce más de la mitad del oxígeno que respiramos gracias al plancton."]},
    "Agua Dulce (Ríos/Lagos)": {"color": "blue", "titulo": "🥤 Agua Dulce", "intro": "El agua que sostiene la vida en los continentes.", "detalles": ["Solo es cerca del 3% del agua total del planeta.", "Se encuentra en ríos, lagos, lagunas y atrapada en los glaciares polares."]},
    
    "Atmósfera": {
        "color": "orange", 
        "titulo": "🌤️ La Atmósfera",
        "intro": "La capa invisible de gases que envuelve y protege a la Tierra.",
        "detalles": ["Nos proporciona el aire para respirar.", "Actúa como un escudo contra meteoritos y radiación solar dañina."]
    },
    "Troposfera": {"color": "orange", "titulo": "☁️ La Troposfera", "intro": "La capa más baja de la atmósfera, la que tocamos directamente.", "detalles": ["Va desde el suelo hasta unos 12 km de altura.", "Aquí ocurren todos los fenómenos climáticos: lluvia, viento, nieve y nubes."]},
    "Estratosfera": {"color": "orange", "titulo": "🛡️ La Estratosfera", "intro": "La capa superior donde el aire es muy delgado.", "detalles": ["Aquí vuelan los aviones comerciales porque casi no hay tormentas.", "¡Contiene la famosa Capa de Ozono que filtra los rayos UV!"]}
}

# 4. Diseño del espacio de trabajo (2 columnas)
col_grafico, col_informacion = st.columns([1.2, 1])

with col_grafico:
    # Creamos el gráfico Sunburst interactivo con Plotly
    fig = px.sunburst(
        df,
        names='capa',
        parents='padre',
        values='valor',
        branchvalues="total",
        color='capa',
        color_discrete_sequence=px.colors.qualitative.Pastel,
        height=550
    )
    
    # Ajustar márgenes para aprovechar el espacio de proyección de la clase
    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
    
    # Renderizar el gráfico capturando los clics del usuario
    evento_click = st.plotly_chart(fig, use_container_width=True, on_select="rerun")

with col_informacion:
    st.markdown("### 📋 Pizarrón Informativo")
    
    # Detectar dinámicamente qué capa tocó el profesor/alumno
    try:
        capa_seleccionada = evento_click["selection"]["points"][0]["label"]
    except (KeyError, IndexError, TypeError):
        capa_seleccionada = "La Tierra"

    # Mostrar la información correspondiente con estilos visuales limpios
    if capa_seleccionada in CONTENIDO_EDUCATIVO:
        info = CONTENIDO_EDUCATIVO[capa_seleccionada]
        
        # Cambiar el contenedor visual dependiendo de la capa para ayudar a la memoria visual
        if info["color"] == "brown":
            st.success(f"### {info['titulo']}")
        elif info["color"] == "blue":
            st.info(f"### {info['titulo']}")
        else:
            st.warning(f"### {info['titulo']}")
            
        st.write(f"*{info['intro']}*")
        st.write("---")
        st.write("**Datos clave para la clase:**")
        for punto in info["detalles"]:
            st.markdown(f"🔹 {punto}")
    else:
        # Mensaje por defecto cuando el gráfico está cerrado en el centro
        st.info("### 🌍 El Planeta Tierra")
        st.write("Nuestro planeta es un sistema perfecto dividido en subsistemas interactivos.")
        st.markdown("👉 **Haz clic en cualquiera de los anillos externos** del gráfico para desplegar la información científica en este panel en tiempo real.")
