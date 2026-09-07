import streamlit as st
import os

# Configuración del Pizarrón Escolar
st.set_page_config(page_title="Clase de Ciencias: Capas de la Tierra", page_icon="🌍", layout="wide")

st.title("🌍 Esquema Visual Interactivo: Las Capas de la Tierra")
st.markdown("### CBTIS 303 | Recursos Didácticos de Ciencias Naturales")
st.write("Selecciona una capa en las pestañas para desplegar su estructura real, ilustraciones científicas e información clave.")

# Definimos las rutas a tus archivos locales
IMAGENES_CAPAS = {
    "Vista General": "general.gif",
    "Capas": "tierra.png",
    "Geosfera": "geosfera.jpg",
    "Geosfera_Temperatura": "geosfera_temperatura.png",
    "Hidrosfera": "hidrosfera.jpg",
    "Atmo_Distancia": "atmosfera_distancia.jpg",
    "Atmo_Temperatura": "atmosfera_temperatura.jpg"
}

# --- BANCO DE PREGUNTAS ---
CUESTIONARIO = {
    "general": [
        {
            "id": "g1",
            "pregunta": "¿Cuáles son las tres grandes capas principales que componen el sistema terrestre?",
            "opciones": ["Corteza, Manto y Núcleo", "Hidrosfera, Geosfera y Atmósfera", "Troposfera, Estratosfera y Mesosfera"],
            "correcta": "Hidrosfera, Geosfera y Atmósfera",
            "pista": "Recuerda revisar el último punto del panel informativo."
        }
    ],
    "geosfera": [
        {
            "id": "geo1",
            "pregunta": "¿Qué capa de la Geosfera representa apenas el 1% del volumen del planeta y es donde habitamos?",
            "opciones": ["El Manto", "El Núcleo externo", "La Corteza"],
            "correcta": "La Corteza",
            "pista": "Es la capa sólida superficial donde se desarrollan los continentes."
        },
        {
            "id": "geo2",
            "pregunta": "¿Cuáles son las 4 partes o subcapas que componen la Geosfera?",
            "opciones": ["Corteza, Manto, Núcleo externo y Núcleo interno", "Hidrosfera, Litosfera, Núcleo y Magma", "Suelo, Rocas, Lava y Metal"],
            "correcta": "Corteza, Manto, Núcleo externo y Núcleo interno",
            "pista": "Revísalo en la pestaña de Grosor y Composición."
        },
        {
            "id": "geo3",
            "pregunta": "¿Cuál es la distancia/espesor correcto desde la base del Manto hasta el inicio del Núcleo Interno (Núcleo Externo)?",
            "opciones": ["De 0 a 70 Km", "De 70 a 2900 Km", "De 2900 a 5100 Km"],
            "correcta": "De 2900 a 5100 Km",
            "pista": "Mira con atención los límites numéricos de las distancias de la geosfera."
        },
        {
            "id": "geo4",
            "pregunta": "¿Cuál es el rango de temperatura estimado para el Manto de la Geosfera?",
            "opciones": ["De 15 °C a 1000 °C", "De 1000 °C a 4000 °C", "De 4000 °C a 5000 °C"],
            "correcta": "De 1000 °C a 4000 °C",
            "pista": "Revisa los datos específicos de temperatura térmica por capa."
        }
    ],
    "hidrosfera": [
        {
            "id": "hid1",
            "pregunta": "De acuerdo con los datos oficiales de nuestra imagen, ¿qué porcentaje de toda el agua del planeta corresponde a agua dulce?",
            "opciones": ["El 97%", "El 50%", "El 3%"],
            "correcta": "El 3%",
            "pista": "Checa los datos actualizados del recuadro informativo azul."
        },
        {
            "id": "hid2",
            "pregunta": "¿Cuáles son las partes o estados en los que se distribuye el agua de la Hidrosfera según nuestro panel de estudio?",
            "opciones": ["Océanos, mares, ríos, lagos, hielo y agua subterránea", "Solo agua salada y lluvia", "Ríos, nubes y vapor exclusivamente"],
            "correcta": "Océanos, mares, ríos, lagos, hielo y agua subterránea",
            "pista": "Incluye tanto el agua superficial como las reservas subterráneas y polares."
        }
    ],
    "atmosfera": [
        {
            "id": "atmo1",
            "pregunta": "¿En qué capa específica de la atmósfera se localiza la Capa de Ozono protectora contra rayos UV?",
            "opciones": ["En la Troposfera", "En la Mesosfera", "En la Estratosfera"],
            "correcta": "En la Estratosfera",
            "pista": "Se encuentra inmediatamente arriba de la Troposfera."
        },
        {
            "id": "atmo2",
            "pregunta": "¿Cuáles son las 5 capas que componen la atmósfera desde la más cercana hasta la más lejana?",
            "opciones": ["Troposfera, Estratosfera, Mesosfera, Termosfera y Exosfera", "Oxígeno, Nitrógeno, Ozono, Helio y Vapor", "Capa baja, Capa media, Capa alta, Capa térmica y Espacio"],
            "correcta": "Troposfera, Estratosfera, Mesosfera, Termosfera y Exosfera",
            "pista": "Están enumeradas del 1 al 5 en el pizarrón de distancias."
        },
        {
            "id": "atmo3",
            "pregunta": "¿Cuál es la altura aproximada que alcanza la Troposfera, la capa donde ocurre el clima?",
            "opciones": ["De 0 a 12 km", "De 12 a 50 km", "De 2900 a 5100 km"],
            "correcta": "De 0 a 12 km",
            "pista": "Es la primera y más baja de las capas gaseosas."
        },
        {
            "id": "atmo4",
            "pregunta": "¿Qué ocurre con la temperatura en la Troposfera a medida que ascendemos (subimos hacia el espacio)?",
            "opciones": ["Aumenta drásticamente hasta los 2500°C", "Disminuye progresivamente con la altura, llegando hasta los -60°C", "Se mantiene fija a 15°C exactos"],
            "correcta": "Disminuye progresivamente con la altura, llegando hasta los -60°C",
            "pista": "Fíjate en las características de temperatura al ascender en la primera capa."
        }
    ]
}

# Función estándar y limpia para el OVA
def mostrar_imagen(nombre_archivo, texto_alternativo):
    if os.path.exists(nombre_archivo):
        st.image(nombre_archivo, caption=texto_alternativo, use_container_width=True)
    else:
        st.warning(f"⚠️ Guarda una imagen llamada '{nombre_archivo}' en tu carpeta para verla aquí.")

# Creación de pestañas interactivas superiores
tab_general, tab_geo, tab_hidro, tab_atmo = st.tabs(["🌍 Nuestro Planeta", "⛰️ La Geosfera", "💧 La Hidrosfera", "🌤️ La Atmósfera"])
# --- PESTAÑA 1: NUESTRO PLANETA ---
with tab_general:
    col1, col2 = st.columns(2)
    with col1:
        subtab_general, subtab_capas = st.tabs(["📏 Vista General", "🌡️ Las tres capas principales"])
        with subtab_general:
            mostrar_imagen(IMAGENES_CAPAS["Vista General"], "La Tierra vista desde el espacio exterior.")
        with subtab_capas:
            mostrar_imagen(IMAGENES_CAPAS["Capas"], "Las tres capas principales de la Tierra.")
    with col2:
        st.info("### El Sistema Terrestre")
        st.write("La Tierra no es solo una roca flotando; es un conjunto de subsistemas que interactúan de manera constante para albergar la vida.")
        st.markdown("• **Estructura Concéntrica:** Desde la atmósfera exterior hasta el núcleo de metal denso, cada capa tiene un grosor y función específica basados en la física real.")
        st.markdown("• **Las tres capas principales de la tierra son Hidrosfera, Geosfera y Atmósfera.**")

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre Nuestro Planeta"):
        for q in CUESTIONARIO["general"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# --- PESTAÑA 2: LA GEOSFERA ---
with tab_geo:
    col1, col2 = st.columns([1.2, 1])
    with col1:
        subtab_general, subtab_capas = st.tabs(["📏 Grosor y composición", "🌡️ Temperatura por capa"])
        with subtab_general:
            mostrar_imagen(IMAGENES_CAPAS["Geosfera"], "Esquema a escala de la estructura interna (Corteza, Manto y Núcleo)")
        with subtab_capas:
            mostrar_imagen(IMAGENES_CAPAS["Geosfera_Temperatura"], "Esquema térmico de la Geosfera.")
    with col2:
        subtab_generalt, subtab_capast = st.tabs(["📏 Grosor y composición", "🌡️ Temperatura por capa"])
        with subtab_generalt:
            st.success("### ⛰️ La Geosfera")
            st.markdown("**Grosor y composición real (Distancias):**")
            st.markdown("- **Corteza:** 0 a 70 Km")
            st.markdown("- **Manto:** 70 a 2900 Km")
            st.markdown("- **Núcleo externo:** 2900 a 5100 Km")
            st.markdown("- **Núcleo interno:** 5100 a 6371 Km")
        with subtab_capast:
            st.success("### 🌡️ Temperatura por capa")
            st.markdown("**Cómo cambia la temperatura al profundizar:**")
            st.markdown("- **Corteza:** De 15 °C a 1000 °C")
            st.markdown("- **Manto:** De 1000 °C a 4000 °C")
            st.markdown("- **Núcleo externo:** De 4000 °C a 5000 °C")
            st.markdown("- **Núcleo interno:** De 5000 °C a 6000 °C")

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Geosfera"):
        for q in CUESTIONARIO["geosfera"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# --- PESTAÑA 3: LA HIDROSFERA ---
with tab_hidro:
    col1, col2 = st.columns(2)
    with col1:
        mostrar_imagen(IMAGENES_CAPAS["Hidrosfera"], "Distribución del agua global")
    with col2:
        st.info("### 💧 La Hidrosfera")
        st.markdown("**Distribución real del agua en la Tierra:**")
        st.markdown("• **97% Agua Salada:** Mares y océanos que cubren la mayor parte de la corteza.")
        st.markdown("• **3% Agua Dulce:** Concentrada principalmente en los glaciares de los polos, aguas subterráneas y una mínima fracción en ríos y lagos.")

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Hidrosfera"):
        for q in CUESTIONARIO["hidrosfera"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")

# --- PESTAÑA 4: LA ATMÓSFERA ---
with tab_atmo:
    col1, col2 = st.columns([1.2, 1])
    with col1:
        subtab_distancia, subtab_temperatura = st.tabs(["📏 Escala de Distancias", "🌡️ Gráfico de Temperaturas"])
        with subtab_distancia:
            mostrar_imagen(IMAGENES_CAPAS["Atmo_Distancia"], "Infografía de las alturas de cada capa atmosférica.")
        with subtab_temperatura:
            mostrar_imagen(IMAGENES_CAPAS["Atmo_Temperatura"], "Esquema térmico: cómo cambia la temperatura al subir.")
    with col2:
        subtab_distanciat, subtab_temperaturat = st.tabs(["📏 Escala de Distancias", "🌡️ Gráfico de Temperaturas"])
        with subtab_distanciat:
            st.warning("### 🌤️ La Atmósfera")
            st.markdown("**Capas físicas del escudo gaseoso:**")
            st.markdown("1. **Troposfera (0 - 12 km):** Alberga el aire respirable y los fenómenos meteorológicos.")
            st.markdown("2. **Estratosfera (12 - 50 km):** Contiene la capa de ozono que filtra la radiación UV.")
            st.markdown("3. **Mesosfera, Termosfera y Exosfera:** Capas externas donde los gases se disipan hacia el espacio exterior.")
        with subtab_temperaturat:
            st.warning("### 🌡️ Temperatura por capa")
            st.markdown("**Cómo cambia la temperatura al ascender:**")
            st.markdown("- **Troposfera:** Disminuye con la altura, llegando a -60°C.")
            st.markdown("- **Estratosfera:** Aumenta debido a la absorción de radiación UV por el ozono.")
            st.markdown("- **Mesosfera:** Disminuye nuevamente hasta -90°C.")
            st.markdown("- **Termosfera y Exosfera:** Aumenta drásticamente, alcanzando hasta 2500°C o más.")

    st.write("---")
    with st.expander("📝 Pon a prueba tus conocimientos sobre la Atmósfera"):
        for q in CUESTIONARIO["atmosfera"]:
            ans = st.radio(q["pregunta"], q["opciones"], key=q["id"])
            if st.button("Validar Respuesta", key=f"btn_{q['id']}"):
                if ans == q["correcta"]:
                    st.success("🎉 ¡Excelente! Respuesta correcta.")
                else:
                    st.error(f"❌ Incorrecto. Pista: {q['pista']}")
