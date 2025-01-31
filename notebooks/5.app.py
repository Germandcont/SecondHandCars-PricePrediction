#IMPORTAMOS LAS LIBRERÍAS NECESARIAS PARA EL ANÁLISIS DE DATOS, VISUALIZACIÓN Y APLICACIÓN DE STREAMLIT
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from PIL import Image
import json
import os
import ssl


#CARGAMOS EL DATASET
df = pd.read_csv(r"C:\Users\Germán\Github\ProyectoFinal\data\azure_data.csv")

# Configuración de la página
st.set_page_config(page_title="Opticar - Soluciones Rentables", layout="wide")

# Cargar el banner desde la carpeta del proyecto
banner = Image.open("banner_opticar.jpg")

# Mostrar el banner en la parte superior de la aplicación
st.image(banner, use_column_width=True)


# Aplicar estilos personalizados al menú lateral
st.markdown("""
    <style>
        /* Fondo del menú lateral */
        [data-testid="stSidebar"] {
            background-color: #CD9C5C !important;
        }

        /* Texto del menú lateral */
        [data-testid="stSidebar"] * {
            color: white !important;
        }

        /* Títulos en negrita */
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            font-weight: bold;
        }

        /* Alinear mejor el contenido */
        [data-testid="stSidebarContent"] {
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Configuración del menú lateral
menu_lateral = st.sidebar.radio("Selecciona una opción:", 
    ["Introducción", "Visión General", "Segmentación de Ventas", "Tendencias del Mercado", "Modelo predictivo","Conclusiones"]
)

# SOLO SE MUESTRA LA INTRODUCCIÓN CUANDO SE SELECCIONA "Introducción"
if menu_lateral == "Introducción":
    st.markdown('<h3 style="color: #A1753F; font-family: Cambria;">Nuestro objetivo</h3>', unsafe_allow_html=True)
    st.write(
        "Nuestro objetivo es proporcionar herramientas innovadoras basadas en datos "
        "que permitan a concesionarios y particulares maximizar el potencial económico "
        "de cada vehículo, impulsando decisiones más estratégicas y rentables."
    )

    st.write("""
    El presente informe tiene como finalidad asesorar a AutoMaster Select, un concesionario especializado en la venta 
    de vehículos de segunda mano, en la segmentación estratégica de sus ventas. Para ello, se ha llevado a cabo un 
    análisis exhaustivo de datos obtenidos mediante técnicas de web scraping.

    A través de este estudio, buscamos proporcionar a AutoMaster Select una visión clara y basada en datos que le
    permita optimizar su estrategia comercial, mejorar la rentabilidad y potenciar su posicionamiento competitivo en el 
    sector. Se presentarán hallazgos clave que permitirán definir segmentos de clientes, ajustar estrategias de precios 
    y maximizar el retorno de inversión en el inventario de vehículos.

    Este análisis será una herramienta fundamental para la toma de decisiones informadas, permitiendo a la empresa 
    ajustar su oferta a la demanda real del mercado y garantizar una ventaja competitiva sostenible.
    """)

    # Descripción de las variables
    st.markdown('<h3 style="color: #A1753F; font-family: Cambria;">Descripción de las variables analizadas</h3>', unsafe_allow_html=True)
    st.markdown("""
    El dataset proporcionado por AutoMaster Select contiene información detallada sobre las características de los vehículos, 
    entre las cuales se encuentran:
    - <span style="color: #AF6926; font-family: Cambria;"><b>Marca</b></span>: Marca del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Modelo</b></span>: Modelo del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Año</b></span>: Año de fabricación del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Kilometraje</b></span>: Kilometraje del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Tipo de combustible</b></span>: Tipo de combustible utilizado por el vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Tipo de transmisión</b></span>: Tipo de transmisión del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Potencia</b></span>: Potencia del vehículo en caballos de fuerza.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Precio</b></span>: Precio de venta del vehículo.
    - <span style="color: #AF6926; font-family: Cambria;"><b>Ubicación</b></span>: Ubicación del vehículo.
    """, unsafe_allow_html=True)

    st.write("""
    En el menú lateral se podrán visualizar diferentes secciones que contienen análisis detallados.""")

    st.markdown("""
    <hr>
    <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
        <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
        con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
        documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
        limitado a los términos y condiciones acordados entre ambas partes.</i>
    </p>
""", unsafe_allow_html=True)


# VISIÓN GENERAL DE LOS DATOS
elif menu_lateral == "Visión General":
    st.markdown("## 📊 Visión General")


    #Leer 2 df 
    df1 = pd.read_csv(r"C:\Users\Germán\Github\ProyectoFinal\data\car_price.csv")

    st.write("Para poder entregar una asesoría de calidad hemos analizado coches en venta de segunda mano provenientes de toda España.")

    #Mapa España con lat y long
    st.markdown("### 🗺️ Mapa de Vehículos en Venta")

    Q1_lat = df1['lat'].quantile(0.25)
    Q3_lat = df1['lat'].quantile(0.75)
    IQR_lat = Q3_lat - Q1_lat

    Q1_long = df1['long'].quantile(0.25)
    Q3_long = df1['long'].quantile(0.75)
    IQR_long = Q3_long - Q1_long

    # Definir los límites para detectar outliers
    lower_bound_lat = Q1_lat - 1.5 * IQR_lat
    upper_bound_lat = Q3_lat + 1.5 * IQR_lat

    lower_bound_long = Q1_long - 1.5 * IQR_long
    upper_bound_long = Q3_long + 1.5 * IQR_long

    # Filtrar los datos para eliminar los outliers
    df1_filtered = df1[(df1['lat'] >= lower_bound_lat) & (df1['lat'] <= upper_bound_lat) &
                                (df1['long'] >= lower_bound_long) & (df1['long'] <= upper_bound_long)]


    # Crear un mapa con Plotly Express
    fig = px.scatter_mapbox(
        df1_filtered, 
        lat="lat", 
        lon="long", 
        hover_name="make", 
        hover_data=["model", "price"], 
        color_discrete_sequence=["orange"], 
        zoom=5, 
        height=600
    )

    # Configurar el estilo del mapa
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # Mostrar el mapa en Streamlit
    st.plotly_chart(fig)




    if menu_lateral == 'Visión General':

        #tabs 
        tab1, tab2, tab3 = st.tabs(['Marcas',"Tipo de Combustible", 'Kms y Potencia'])

#TAB 1
        with tab1:
            # Gráfico de barras con las marcas de coches (Top 35)
            marca_counts = df1['make'].value_counts().head(35)
            fig_marcas = px.bar(marca_counts, x=marca_counts.index, y=marca_counts.values, labels={'x': 'Marca', 'y': 'Cantidad'}, title="Top 35 Marcas de Coches por Cantidad", color_discrete_sequence=['orange'])
            st.plotly_chart(fig_marcas)


#TAB 2
        with tab2:
            # Gráfico de tarta con el tipo de combustible
            fuel_counts = df1['fuel'].value_counts()
            fig_fuel = px.pie(fuel_counts, values=fuel_counts.values, names=fuel_counts.index, title="Distribución del Tipo de Combustible", color_discrete_sequence=['#F4A460', '#CD853F'])
            st.plotly_chart(fig_fuel)

#TAB 3  
        with tab3:
            # Crear segmentos de kilometraje
            bins = [0, 50000, 100000, 150000, 200000, np.inf]
            labels = ['Bajo (0-50k)', 'Medio (50k-100k)', 'Medio Alto (100k-150k)', 'Alto (150k-200k)', 'Muy Alto (>200k)']
            df1['kms_segment'] = pd.cut(df1['kms'], bins=bins, labels=labels, right=False)

            # Contar la cantidad de coches en cada segmento
            kms_segment_counts = df1['kms_segment'].value_counts().sort_index()

            # Crear gráfico de barras
            fig_kms_segment = px.bar(kms_segment_counts, x=kms_segment_counts.index, y=kms_segment_counts.values, 
                labels={'x': 'Rangos de Kilometraje', 'y': 'Cantidad'}, 
                title="Distribución de Coches por Segmento de Kilometraje", 
                color_discrete_sequence=['orange'])
            st.plotly_chart(fig_kms_segment)

            # Crear segmentos de potencia
            bins = [0, 100, 200, 300, 400, np.inf]
            labels = ['Baja (0-100 CV)', 'Media (100-200 CV)', 'Alta (200-300 CV)', 'Muy Alta (300-400 CV)', 'Extrema (>400 CV)']
            df1['power_segment'] = pd.cut(df1['power'], bins=bins, labels=labels, right=False)

            # Contar la cantidad de coches en cada segmento
            power_segment_counts = df1['power_segment'].value_counts().sort_index()

            # Crear gráfico de barras
            fig_power_segment = px.bar(power_segment_counts, x=power_segment_counts.index, y=power_segment_counts.values, 
                labels={'x': 'Rangos de Potencia', 'y': 'Cantidad'}, 
                title="Distribución de Coches por Segmento de Potencia", 
                color_discrete_sequence=['orange'])
            st.plotly_chart(fig_power_segment)
        



# SOLO SE MUESTRA SEGMENTACIÓN CUANDO SE SELECCIONA ESA OPCIÓN
elif menu_lateral == "Segmentación de Ventas":
    st.markdown("## 📌 Segmentación de Ventas")
    st.write("Análisis detallado de la segmentación de clientes y ventas.")
    sub_option = st.sidebar.radio(
        "Selecciona una subcategoría:",
        ["Segmentación por comunidad autónoma", "Segmentación por marca", "Segmentación por potencia"]
    )
    if sub_option == "Segmentación por comunidad autónoma":
        st.write("🌍 **Análisis de ventas por comunidad autónoma**")
    elif sub_option == "Segmentación por marca":
        st.write("🚗 **Análisis de ventas por marca**")
    elif sub_option == "Segmentación por potencia":
        st.write("🏎️ **Análisis de ventas por potencia**")

# SOLO SE MUESTRA TENDENCIAS CUANDO SE SELECCIONA ESA OPCIÓN
elif menu_lateral == "Tendencias del Mercado":
    st.markdown("## 📈 Tendencias del Mercado")
    st.write("Exploración de tendencias y patrones en el mercado automotriz.")

# SOLO SE MUESTRA CONCLUSIONES CUANDO SE SELECCIONA ESA OPCIÓN
elif menu_lateral == "Conclusiones":
    st.markdown("## ✅ Conclusiones")
    st.write("Puntos clave y recomendaciones estratégicas.")

elif menu_lateral =="Modelo predictivo":

    #Variables de entrada para el modelo predictivo
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    st.markdown("## 📊 Modelo predictivo"
                )

    '''Para que la marca sea correlativa con el modelo a la hora de introducir el input en la aplicación, crearemos un diccionario en el que para cada marca
    introduzcamos los modelos que tiene. De esta forma, cuando el usuario introduzca una marca, podrá seleccionar el modelo correspondiente.'''
    makes_models_dict = (
    df.groupby("make")["model"]
      .unique()          # Devuelve los modelos únicos por marca
      .apply(list)       # Convierte el array de modelos en lista
      .to_dict() )        # Transforma el resultado en diccionario
    
    # Marcas de coches
    marca_seleccionada = st.selectbox("Selecciona la marca del vehículo", list(makes_models_dict.keys()))

    # Modelos de coches
    modelo_seleccionado = st.selectbox("Selecciona el modelo del vehículo", makes_models_dict[marca_seleccionada])

    #Tipo de combustible
    fuel = st.selectbox("Selecciona el tipo de combustible", df["fuel"].unique().tolist())

    # Año
    year = int(st.number_input("Introduce el año de fabricación", min_value=1967, max_value=2023, value=2000, step=1))

    # Kilometraje
    kms = int(st.number_input("Introduce el kilometraje", min_value=0, max_value=750000, value=20000, step=100))

    # Potencia
    power = int(st.number_input("Introduce la potencia en caballos de fuerza", min_value=5, max_value=999, value=100, step=20))
    
    # Transmisión
    transmission_dict = {"manual": "Manual", "automatic": "Automático"}
    transmission = st.selectbox("Selecciona el tipo de transmisión", [transmission_dict[t] for t in df["transmission"].unique()])
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------
    #Inferencia del modelo
    if st.button("🔍 Predecir Precio del Vehículo"):

        def allowSelfSignedHttps(allowed):
        # bypass the server certificate verification on client side
            if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
                ssl._create_default_https_context = ssl._create_unverified_context


        allowSelfSignedHttps(True)  # Habilita certificados auto-firmados si es necesario

        # Datos en el formato requerido por la API
        data = {
            "Inputs": {
                "data": {
                    "make": [marca_seleccionada],
                    "model": [modelo_seleccionado],
                    "fuel": [fuel],
                    "year": [year],
                    "kms": [kms],
                    "power": [power],
                    "transmission": [transmission]
                }
            },
            "GlobalParameters": 1.0
        }

        body = str.encode(json.dumps(data))

        url = '' 
        api_key = ''  
        if not api_key:
            st.error("⚠️ No se ha proporcionado una clave API válida.")
        else:
            headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

            req = urllib.request.Request(url, body, headers)

            try:
                response = urllib.request.urlopen(req)
                result = response.read()
                result_json = json.loads(result)
                predicted_price = int(result_json["Results"][0])

                st.success(f"💰 Precio Estimado: **{predicted_price}€**")

            except urllib.error.HTTPError as error:
                st.error(f"⚠️ La solicitud falló con código de estado: {error.code}")
                st.text(error.info())
                st.text(error.read().decode("utf8", 'ignore'))

