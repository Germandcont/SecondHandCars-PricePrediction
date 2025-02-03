#IMPORTAMOS LAS LIBRERÍAS NECESARIAS PARA EL ANÁLISIS DE DATOS, VISUALIZACIÓN Y APLICACIÓN DE STREAMLIT
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px
from PIL import Image
import urllib.request
import json
import os
import ssl


#CARGAMOS EL DATASET
df = pd.read_csv('car_price.csv')

#Creamos un anueva columna que sea la combinación de marca y modelo
df['brand_model'] = df['make'] + ' ' + df['model']

#Convertir la columna 'year' a formato datetime
df['year_formato_fecha'] = pd.to_datetime(df['year'], format='%Y')

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
    ["Introducción", "Visión General", "Tendencia de mercado","Modelo predictivo","Conclusiones"]
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


    st.write("Para poder entregar una asesoría de calidad hemos analizado coches en venta de segunda mano provenientes de toda España.")



    # Crear un mapa con Plotly Express
    fig = px.scatter_mapbox(
        df, 
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
            marca_counts = df['make'].value_counts().head(35)
            fig_marcas = px.bar(marca_counts, x=marca_counts.index, y=marca_counts.values, labels={'x': 'Marca', 'y': 'Cantidad'}, title="Top 35 Marcas de Coches por Cantidad", color_discrete_sequence=['orange'])
            st.plotly_chart(fig_marcas)


#TAB 2
        with tab2:
            # Gráfico de tarta con el tipo de combustible
            fuel_counts = df['fuel'].value_counts()
            fig_fuel = px.pie(fuel_counts, values=fuel_counts.values, names=fuel_counts.index, title="Distribución del Tipo de Combustible", color_discrete_sequence=['#F4A460', '#CD853F'])
            st.plotly_chart(fig_fuel)

#TAB 3  
        with tab3:
            # Crear segmentos de kilometraje
            bins = [0, 50000, 100000, 150000, 200000, np.inf]
            labels = ['Bajo (0-50k)', 'Medio (50k-100k)', 'Medio Alto (100k-150k)', 'Alto (150k-200k)', 'Muy Alto (>200k)']
            df['kms_segment'] = pd.cut(df['kms'], bins=bins, labels=labels, right=False)

            # Contar la cantidad de coches en cada segmento
            kms_segment_counts = df['kms_segment'].value_counts().sort_index()

            # Crear gráfico de barras
            fig_kms_segment = px.bar(kms_segment_counts, x=kms_segment_counts.index, y=kms_segment_counts.values, 
                labels={'x': 'Rangos de Kilometraje', 'y': 'Cantidad'}, 
                title="Distribución de Coches por Segmento de Kilometraje", 
                color_discrete_sequence=['orange'])
            st.plotly_chart(fig_kms_segment)

            # Crear segmentos de potencia
            bins = [0, 100, 200, 300, 400, np.inf]
            labels = ['Baja (0-100 CV)', 'Media (100-200 CV)', 'Alta (200-300 CV)', 'Muy Alta (300-400 CV)', 'Extrema (>400 CV)']
            df['power_segment'] = pd.cut(df['power'], bins=bins, labels=labels, right=False)

            # Contar la cantidad de coches en cada segmento
            power_segment_counts = df['power_segment'].value_counts().sort_index()

            # Crear gráfico de barras
            fig_power_segment = px.bar(power_segment_counts, x=power_segment_counts.index, y=power_segment_counts.values, 
                labels={'x': 'Rangos de Potencia', 'y': 'Cantidad'}, 
                title="Distribución de Coches por Segmento de Potencia", 
                color_discrete_sequence=['orange'])
            st.plotly_chart(fig_power_segment)
        

# TENDENCIA DE MERCADO
elif menu_lateral == "Tendencia de mercado":
    st.markdown("## 📈 Tendencia de Mercado")

    st.write("En esta sección se analizarán los precios del mercado de vehículos de coches de segunda mano en cuanto a diferentes características como la marca, la zona geográfica, potencia, kilometraje, etc.")
    #tabs 
    tab1, tab2, tab3, tab4 = st.tabs(['Análisis de marcas',"Análisis por potencia", 'Análisis por kilometraje', "Análisis geográfico"])

#TAB 1
    with tab1:

        st.write("En este apartado se realiza un análisis de las marcas de coches más vendidas en el mercado de segunda mano.")
        analisis_seleccionado = st.radio("Selecciona el Análisis:",["Precio Medio y Rango de Precios", "Modelos más populares", "Depreciación de Precio"])

        # Selección Múltiple de Marcas
        marcas_disponibles = list(df["make"].unique())
        marcas_seleccionadas = st.multiselect(
            "🔎 Filtrar por Marca:",
            ["Todas"] + marcas_disponibles,
            default=["Todas"]
        )

        #Filtrar DataFrame según la selección múltiple
        if "Todas" in marcas_seleccionadas:
            df_filtrado = df  # Mostrar todas las marcas
        else:
            df_filtrado = df[df["make"].isin(marcas_seleccionadas)]  # Filtrar solo las seleccionadas

        #PRECIO MEDIO Y RANGO DE PRECIOS
        if analisis_seleccionado == "Precio Medio y Rango de Precios":
            st.markdown("## Precio Medio y Rango de Precios por Marca")
            st.write("""
            En este análisis se muestra la distribución de precios para cada marca seleccionada.  
            Se puede visualizar la dispersión de los valores y la diferencia entre marcas premium y marcas más accesibles.
            """)

            # 📊 Gráfico de Boxplot (Distribución de Precios por Marca con Selección Múltiple)
            fig = px.box(
                df_filtrado,
                x="make",
                y="price",
                title=f"Distribución de Precios por Marca",
                labels={"make": "Marca", "price": "Precio (€)"},
                color="make"
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, key="boxplot_precio_marca")

            st.markdown("""
            Como era de esperar, marcas como **Tesla, Maserati, Ferrari, Bentley y Lamborghini** son las que tienen por lo general los precios más elevados. 
            Notese que **Audi, Mercedes-Benz y BMW** tienen vehículos en un rango de precio muy elevado también como podemos ver en sus outliers, sin embargo también tenemos coches más económicos.

            Entre las marcas más económicas podemos encontrar **Galloper, Lancia, Daihatsu, Daewoo, Chrysler, FIAT, Suzuki, Subaru, MG**.

            Si queremos ***atraer a clientes con alto poder adquisitivo*** nos podríamos centrar en adquirir las ***marcas con los precios más elevados*** mientras que si queremos atraer a un ***poder adquisitivo bajo*** nos 
            podríamos ***centrar más en las segundas***.""")

            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True)



        #MODELOS MÁS POPULARES
        elif analisis_seleccionado == "Modelos más populares":
            st.write("Este análisis muestra los modelos más frecuentes dentro de las marcas seleccionadas.")

            conteo_modelos = df_filtrado["model"].value_counts().reset_index()
            conteo_modelos.columns = ["Modelo", "Cantidad"]

            # 📊 Gráfico de Barras de Modelos más Vendidos con Selección Múltiple
            fig2 = px.bar(
                conteo_modelos,
                x="Modelo",
                y="Cantidad",
                title=f"Top Modelos más Populares",
                labels={"Modelo": "Modelo", "Cantidad": "Cantidad de Vehículos"},
                text_auto=True
            )
            fig2.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig2, key="modelos_populares")

            st.markdown("""
            Mediante este gráfico el cliente puede tener una idea de los modelos más populares en el mercado de segunda mano. Se podría evitar la adquisición de los modelos
            más populares ya que podrían tener una mayor competencia en el mercado y por ende, una mayor dificultad para venderlos. Por otro lado, si se adquieren los modelos
            menos populares podríamos tener una mayor facilidad para venderlos.""")

            st.markdown("""
            También nos puede servir para detectar tendencias de mercado, si un modelo en concreto está siendo muy demandado, podríamos adquirir más unidades de ese modelo para 
            satisfacer la demanda.""")


            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True)


        # DEPRECIACIÓN DE PRECIO
        elif analisis_seleccionado == "Depreciación de Precio":
            st.markdown("## 📉 Relación entre Año de Fabricación y Precio")
            st.write("Este gráfico analiza cómo varía el precio según el año de fabricación para las marcas seleccionadas.")

            # Definir la columna de color según selección
            if len(marcas_seleccionadas) == 1 and "Todas" not in marcas_seleccionadas:
                color_columna = "model"  # Si es una sola marca, usar el modelo como color
            else:
                color_columna = "make"  # Si son varias marcas, usar la marca como color

            # 📊 Scatter plot de depreciación con color dinámico
            fig3 = px.scatter(
                df_filtrado,
                x="year_formato_fecha",
                y="price",
                color=color_columna,  # Color por marca o modelo según el caso
                title="Depreciación de Precio por Año de Fabricación",
                labels={"year_formato_fecha": "Año de Fabricación", "price": "Precio (€)"},
                hover_data=["model", "kms"],
                opacity=0.7
            )
            
            fig3.update_xaxes(
                tickformat="%Y",  # Mostrar solo el año en formato YYYY
                dtick="M60",  # Espaciado de cada 5 años
            )
            
            st.plotly_chart(fig3, key="scatter_precio_anio")

            st.markdown("""
            Gracias a este gráfico observamos que hay marcas que aguantan el precio a lo largo de los años, mientras que otras marcas presentan una mayor depreciación.
            
            Entre las marcas que aguantan más se encuentran ***Mercedes-Benz, BMW, Audi***. Marcas de lujo como ***Porsche, Ferrari, Aston-Martin, Bentley*** también mantienen su valor a lo largo del tiempo.
            """)

            st.markdown("""
            Se podría hacer el análisis de segmentación por modelos de cada marca para ver qué modelos aguantan mejor el precio con los años, dependiendo de la clientela objetivo.
            """)



            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True)




                
#TAB 2
    with tab2:
        # 📌 Introducción
        st.markdown("## 📉 Análisis de Depreciación por Marca")
        st.write("""
        Este análisis permite evaluar cómo varían los precios de los vehículos en función del tiempo, 
        la marca y el kilometraje. Compararemos:
        - **La dispersión de precios por marca** para identificar qué marcas mantienen mejor su valor.
        - **La relación entre el año de fabricación y el precio** para ver tendencias de depreciación.
        - **El impacto del kilometraje en el precio** para evaluar la influencia del uso en la valoración del vehículo.
        """)

        # Filtros interactivos
        marcas_disponibles = df["make"].unique()
        marca_seleccionada = st.selectbox("🔎 Selecciona una Marca:", ["Todas"] + list(marcas_disponibles))

        # Filtrado de datos según selección
        df_filtrado = df.copy()
        if marca_seleccionada != "Todas":
            df_filtrado = df[df["make"] == marca_seleccionada]

        ### 📊 Gráfico 1: Boxplot de Precios por Marca
        st.markdown("### 💰 Distribución de Precios por Marca")
        fig_boxplot = px.box(
            df_filtrado,
            x="make",
            y="price",
            title="Distribución de Precios por Marca",
            labels={"make": "Marca", "price": "Precio (€)"},
            color="make"
        )
        fig_boxplot.update_layout(xaxis_title="Marca", yaxis_title="Precio (€)", xaxis_tickangle=-45)
        st.plotly_chart(fig_boxplot)

        ### 📊 Gráfico 2: Scatter Plot Precio vs. Año
        st.markdown("### 🕒 Relación entre Año de Fabricación y Precio")
        fig_scatter_año = px.scatter(
            df_filtrado,
            x="year",
            y="price",
            color="make",
            title="Precio vs. Año de Fabricación",
            labels={"year": "Año de Fabricación", "price": "Precio (€)"},
            hover_data=["model", "kms"]
        )
        fig_scatter_año.update_layout(xaxis_title="Año de Fabricación", yaxis_title="Precio (€)")
        st.plotly_chart(fig_scatter_año)

        ### 📊 Gráfico 3: Scatter Plot Precio vs. Kilometraje
        st.markdown("### 🚗 Relación entre Kilometraje y Precio")
        fig_scatter_km = px.scatter(
            df_filtrado,
            x="kms",
            y="price",
            color="make",
            title="Precio vs. Kilometraje",
            labels={"kms": "Kilometraje (km)", "price": "Precio (€)"},
            hover_data=["model", "year"]
        )
        fig_scatter_km.update_layout(xaxis_title="Kilometraje (km)", yaxis_title="Precio (€)")
        st.plotly_chart(fig_scatter_km)

        # Conclusiones
        st.markdown("## 📌 Conclusiones")
        st.write("""
        - Algunas marcas conservan mejor su valor a lo largo de los años, mientras que otras presentan una mayor depreciación.
        - El kilometraje influye directamente en el precio de los vehículos, pero en algunas marcas el efecto es menor.
        - Este análisis permite definir estrategias de precio y segmentación según la marca y el estado del vehículo.
        """)

         





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
    transmission = st.selectbox("Selecciona el tipo de transmisión", [transmission_dict[t] for t in df["shift"].unique()])
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

        url = 'http://c46f109b-f399-4a88-a0b5-70030985f904.eastus2.azurecontainer.io/score' 
        api_key = 'uwwIMT6N69MOvr2GatGBtXMbwKPPOG1U'  
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
