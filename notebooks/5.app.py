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
import folium
from streamlit_folium import folium_static


#CARGAMOS EL DATASET
df = pd.read_csv('data/car_price 2.csv')

#Creamos un anueva columna que sea la combinación de marca y modelo
df['brand_model'] = df['make'] + ' ' + df['model']

#Convertir la columna 'year' a formato datetime
df['year_formato_fecha'] = pd.to_datetime(df['year'], format='%Y')

# Configuración de la página
st.set_page_config(page_title="Opticar - Soluciones Rentables", layout="wide")

# Cargar el banner desde la carpeta del proyecto
banner = Image.open("banner_opticar.jpg")

# Mostrar el banner en la parte superior de la aplicación
st.image(banner, use_container_width=True)

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

# Cargar la imagen en la barra lateral
st.sidebar.image("opticar_logo.jpeg", use_container_width=True)
# Configuración del menú lateral
menu_lateral = st.sidebar.radio("Selecciona una opción:", 
    ["Introducción", "Visión General", "Tendencia de mercado","Modelo predictivo","Panel de control | PowerBI","Conclusiones"]
)

# SOLO SE MUESTRA LA INTRODUCCIÓN CUANDO SE SELECCIONA "Introducción"
if menu_lateral == "Introducción":

    st.markdown('<h1 style="color: #A1753F; font-family: Cambria; font-weight: bold; text-align: center;">DATA-DRIVEN CONFIDENCE ON EVERY RIDE</h1>', unsafe_allow_html=True)
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
    st.markdown('<h2 style="color: #A1753F; font-weight: bold; font-family: Cambria;"> Visión General</h2>', unsafe_allow_html=True)


    st.write("Para poder entregar una asesoría de calidad hemos analizado coches en venta de segunda mano provenientes de toda España.")



    # Crear un mapa con Plotly Express
    fig = px.scatter_mapbox(
        df, 
        lat="lat", 
        lon="long", 
        hover_name="make", 
        hover_data=["model", "price"], 
        color_discrete_sequence=["#AF6926"], 
        zoom=5, 
        height=600
    )

    # Configurar el estilo del mapa
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    # Mostrar el mapa en Streamlit
    st.plotly_chart(fig)

    st.markdown("### <b style='color:#AF6926'>Algunos datos</b>", unsafe_allow_html=True)


    if menu_lateral == 'Visión General':

        #tabs 
        tab1, tab2, tab3 = st.tabs(['Marcas',"Tipo de Combustible", 'Kms y Potencia'])

#TAB 1
        with tab1:
            # Gráfico de barras con las marcas de coches (Top 35)
            marca_counts = df['make'].value_counts().head(35)
            fig_marcas = px.bar(marca_counts, x=marca_counts.index, y=marca_counts.values, labels={'make': 'Marca', 'y': 'Cantidad'}, title="<b style='color:#A1753F; font-family: Cambria;'>Top 35 marcas de coches por cantidad</b>", color_discrete_sequence=['#AF6926'])
            st.plotly_chart(fig_marcas)
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
            # Gráfico de tarta con el tipo de combustible
            fuel_counts = df['fuel'].value_counts()
            fig_fuel = px.pie(fuel_counts, values=fuel_counts.values, names=fuel_counts.index, title="<b style='color:#A1753F'>Distribución del tipo de combustible</b>", color_discrete_sequence=['#F4A460', '#CD853F'])
            st.plotly_chart(fig_fuel)
            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True)

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
                labels={'kms_segment': 'Rangos de Kilometraje', 'y': 'Cantidad'}, 
                title="<b style='color:#A1753F'>Distribución de coches por segmento de kilometraje</b>", 
                color_discrete_sequence=['#AF6926'])
            st.plotly_chart(fig_kms_segment)

            # Crear segmentos de potencia
            bins = [0, 100, 200, 300, 400, np.inf]
            labels = ['Baja (0-100 CV)', 'Media (100-200 CV)', 'Alta (200-300 CV)', 'Muy Alta (300-400 CV)', 'Extrema (>400 CV)']
            df['power_segment'] = pd.cut(df['power'], bins=bins, labels=labels, right=False)

            # Contar la cantidad de coches en cada segmento
            power_segment_counts = df['power_segment'].value_counts().sort_index()

            # Crear gráfico de barras
            fig_power_segment = px.bar(power_segment_counts, x=power_segment_counts.index, y=power_segment_counts.values, 
                labels={'power_segment': 'Rangos de Potencia', 'y': 'Cantidad'}, 
                title="<b style='color:#A1753F; font-family: Cambria;'>Distribución de coches por segmento de potencia</b>", 
                color_discrete_sequence=['#AF6926'])
            st.plotly_chart(fig_power_segment)
            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True)
# TENDENCIA DE MERCADO
elif menu_lateral == "Tendencia de mercado":
    st.markdown('<h2 style="color: #A1753F; font-weight: bold; font-family: Cambria;">Tendencia de Mercado</h2>', unsafe_allow_html=True)

    st.write("En esta sección se analizarán los precios del mercado de vehículos de coches de segunda mano en cuanto a diferentes características como la marca, la zona geográfica, potencia, kilometraje, etc.")
    #tabs 
    tab1, tab2, tab3, tab4 = st.tabs(['Análisis de marcas',"Análisis por potencia", 'Análisis por kilometraje', "Análisis geográfico"])
#TAB 1
    with tab1:

        
        analisis_seleccionado = st.radio("Selecciona el análisis:",["Precio medio y rango de precios", "Modelos más populares", "Depreciación de precio"])

        # Selección Múltiple de Marcas
        marcas_disponibles = list(df["make"].unique())
        marcas_seleccionadas = st.multiselect(
            "Filtrar por marca:",
            ["Todas"] + marcas_disponibles,
            default=["Todas"]
        )

        #Filtrar DataFrame según la selección múltiple
        if "Todas" in marcas_seleccionadas:
            df_filtrado = df  # Mostrar todas las marcas
        else:
            df_filtrado = df[df["make"].isin(marcas_seleccionadas)]  # Filtrar solo las seleccionadas

        #PRECIO MEDIO Y RANGO DE PRECIOS
        if analisis_seleccionado == "Precio medio y rango de precios":
            st.markdown("## <b style='color:#A1753F; font-family: Cambria;'>Precio medio y rango de precios por marca</b>", unsafe_allow_html=True)
            st.write("""
            En este análisis se muestra la distribución de precios para cada marca seleccionada.  
            Se puede visualizar la dispersión de los valores y la diferencia entre marcas premium y marcas más accesibles.
            """)

            # 📊 Gráfico de Boxplot (Distribución de Precios por Marca con Selección Múltiple)
            fig = px.box(
                df_filtrado,
                x="make",
                y="price",
                title="<b style='color:#A1753F; font-family: Cambria;'>Distribución de precios por marca</b>",
                labels={"make": "Marca", "price": "Precio (€)"},
                color="make"
            )
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, key="boxplot_precio_marca")

            st.markdown("""
            Como era de esperar, marcas como <span style='color:#A1753F; font-family: Cambria;'>**Tesla, Maserati, Ferrari, Bentley y Lamborghini**</span> son las que tienen por lo general los precios más elevados. 
            Notese que <span style='color:#A1753F; font-family: Cambria;'>**Audi, Mercedes-Benz y BMW**</span> tienen vehículos en un rango de precio muy elevado también como podemos ver en sus outliers, sin embargo también tenemos coches más económicos.

            Entre las marcas más económicas podemos encontrar <span style='color:#A1753F; font-family: Cambria;'>**Galloper, Lancia, Daihatsu, Daewoo, Chrysler, FIAT, Suzuki, Subaru, MG**</span>.

            Si queremos <span style='color:#A1753F; font-family: Cambria;'>**atraer a clientes con alto poder adquisitivo**</span> nos podríamos centrar en adquirir las <span style='color:#A1753F; font-family: Cambria;'>**marcas con los precios más elevados**</span> mientras que si queremos atraer a un <span style='color:#A1753F; font-family: Cambria;'>**poder adquisitivo bajo**</span> nos 
            podríamos <span style='color:#A1753F; font-family: Cambria;'>**centrar más en las segundas**</span>.""", unsafe_allow_html=True)

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
                title="<b style='color:#A1753F; font-family: Cambria;'>Top modelos más populares</b>",
                labels={"Modelo": "Modelo", "Cantidad": "Cantidad de Vehículos"},
                text_auto=True,
                color_discrete_sequence=['#AF6926']
            )
            fig2.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig2, key="modelos_populares")

            st.markdown("""
            Mediante este gráfico el cliente puede tener una idea de los <span style='color:#A1753F; font-family: Cambria; font-weight: bold;'>**modelos más populares en el mercado de segunda mano**</span>. Se podría <span style='color:#A1753F; font-family: Cambria; font-weight: bold;'>**evitar**</span> la adquisición de los modelos
            más populares ya que podrían tener una mayor competencia en el mercado y por ende, una <span style='color:#A1753F; font-family: Cambria; font-weight: bold;'>**mayor dificultad**</span> para venderlos. Por otro lado, si se adquieren los modelos
            menos populares podríamos tener una mayor facilidad para venderlos.""", unsafe_allow_html=True)

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
        elif analisis_seleccionado == "Depreciación de precio":
            st.markdown("## <b style='color:#A1753F; font-family: Cambria;'>Relación entre año de fabricación y precio</b>", unsafe_allow_html=True)
            st.write("Este gráfico analiza cómo varía el precio según el año de fabricación para las marcas seleccionadas.")

            # Definir la columna de color según selección
            if len(marcas_seleccionadas) == 1 and "Todas" not in marcas_seleccionadas:
                color_columna = "model"  # Si es una sola marca, usar el modelo como color
                labels = {"model": "Modelo"}  # Cambiar la etiqueta de la leyenda a "Modelo"
            else:
                color_columna = "make"  # Si son varias marcas, usar la marca como color
                labels = {"make": "Marca"}  # Cambiar la etiqueta de la leyenda a "Marca"

            # 📊 Scatter plot de depreciación con color dinámico
            fig3 = px.scatter(
            df_filtrado,
            x="year_formato_fecha",
            y="price",
            color=color_columna,  # Color por marca o modelo según el caso
            title="<b style='color:#A1753F; font-family: Cambria;'>Depreciación de Precio por Año de Fabricación</b>",
            labels={**labels, "year_formato_fecha": "Año de Fabricación", "price": "Precio (€)"},
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
            
            Entre las marcas que aguantan más se encuentran <span style='color:#A1753F; font-weight: bold;'>Mercedes-Benz, BMW, Audi</span>. Marcas de lujo como <span style='color:#A1753F; font-weight: bold;'>Porsche, Ferrari, Aston-Martin, Bentley</span> también mantienen su valor a lo largo del tiempo.
            """, unsafe_allow_html=True)

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
    with tab2:

        # Filtro de marca
        marcas_disponibles = df['make'].unique()
        marca_seleccionada = st.selectbox("Selecciona una marca:", ["Todas"] + list(marcas_disponibles))

        # Filtrar DataFrame según la selección de marca
        if marca_seleccionada != "Todas":
            df_filtrado = df[df['make'] == marca_seleccionada]
        else:
            df_filtrado = df

        # Crear segmentos de potencia
        bins = [0, 100, 200, 300, 400, np.inf]
        labels = ['Baja (0-100 CV)', 'Media (100-200 CV)', 'Alta (200-300 CV)', 'Muy Alta (300-400 CV)', 'Extrema (>400 CV)']
        df_filtrado['power_segment'] = pd.cut(df_filtrado['power'], bins=bins, labels=labels, right=False)

        # Contar la cantidad de coches en cada segmento
        power_segment_counts = df_filtrado['power_segment'].value_counts().sort_index()

        # Calcular el precio promedio por segmento de potencia
        avg_price_power_segment = df_filtrado.groupby('power_segment')['price'].mean().reset_index()
        # Selección del gráfico a visualizar
        grafico_seleccionado = st.radio(
            "Selecciona el gráfico a visualizar:", 
            ["Segmentación de potencias", "Diagrama de agrupación (hexagonal) de datos"]
        )

        if grafico_seleccionado == "Segmentación de potencias":
            
            st.markdown("""
            Se realiza una segmentación de los coches según su potencia para analizar la distribución de precios y la cantidad de coches en cada segmento,
            debido a que había muchos valores de potencia y se decidió segmentarlos para un mejor análisis.
            """)

            with st.expander("Opciones de visualización"):
                cantidad_o_precio = st.radio("Seleccione la métrica a visualizar:", 
                                            ["Cantidad de coches por segmento", "Precio promedio por segmento"], horizontal=True)

            if cantidad_o_precio == "Cantidad de coches por segmento":
                # Crear gráfico de barras para la cantidad de coches en cada segmento
                fig_power_segment = px.bar(
                    power_segment_counts, 
                    x=power_segment_counts.index, 
                    y=power_segment_counts.values, 
                    labels={'power_segment': 'Rangos de potencia', 'y': 'Cantidad'}, 
                    title="<b style='color:#A1753F; font-family: Cambria;'>Distribución de coches por segmento de potencia</b>", 
                    color_discrete_sequence=['#AF6926']
                )
                st.plotly_chart(fig_power_segment)

                st.markdown("""
                La distribución de vehículos por segmento de potencia <span style='color:#A1753F'>**por lo general**</span> muestra una clara concentración en la categoría de <span style='color:#A1753F'>**100-200 CV**</span>, con una presencia 
                significativamente menor en los rangos de mayor potencia. Dependiendo de la marca la distribución puede variar, por ejemplo <span style='color:#A1753F'>**Tesla**</span> o <span style='color:#A1753F'>**Ferrari**</span>.""", unsafe_allow_html=True)
                st.markdown("""
                <hr>
                <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                    <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                    con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                    documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                    limitado a los términos y condiciones acordados entre ambas partes.</i>
                </p>
            """, unsafe_allow_html=True)

            elif cantidad_o_precio == "Precio promedio por segmento":
                # Crear gráfico de barras para el precio promedio por segmento de potencia
                fig_avg_price_power_segment = px.bar(
                    avg_price_power_segment, 
                    x='power_segment', 
                    y='price', 
                    labels={'power_segment': 'Rangos de potencia', 'price': 'Precio promedio (€)'}, 
                    title="<b style='color:#A1753F; font-family: Cambria;'>Precio promedio por segmento de potencia</b>", 
                    color_discrete_sequence=['#AF6926']
                )
                st.plotly_chart(fig_avg_price_power_segment)
                st.markdown("El **precio** promedio de los vehículos **aumenta progresivamente con la potencia**, alcanzando su máximo en la categoría de más de 400 CV.")
                st.markdown("""
                <hr>
                <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                    <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                    con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                    documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                    limitado a los términos y condiciones acordados entre ambas partes.</i>
                </p>
            """, unsafe_allow_html=True)




                
        elif grafico_seleccionado == "Diagrama de agrupación (hexagonal) de datos":
            fig, ax = plt.subplots(figsize=(6, 4))
            hb = ax.hexbin(df['power'], df['price'], gridsize=50, cmap='Oranges', mincnt=1, edgecolors='#AF6926')
            ax.set_xlabel('Potencia (CV)')
            ax.set_ylabel('Price (€)')
            ax.set_ylim(0, 50000)  # Establecer límite superior para el precio
            ax.set_xlim(0, 200)  # Establecer límite superior para la potencia
            cb = fig.colorbar(hb, ax=ax)
            cb.set_label('Cantidad')
            ax.set_facecolor('white')  # Quitar el fondo

            plt.tight_layout()
            st.pyplot(fig)

            #Interpretacion 
            st.markdown("### <b style='color:#A1753F; font-family: Cambria;'>Interpretación</b>", unsafe_allow_html=True)
            st.markdown("En este tipo de gráfico agrupamos en hexágonos todos los registros y los  rellenamos con un color más oscuro si hay más registros en esa zona. Por lo tanto, en este caso, podemos ver que hay una <span style='color:#A1753F'>**mayor concentración de coches con potencia de 150CV**</span> y precios <span style='color:#A1753F'>**entre 10.000 y 20.000€**</span>. Esto nos puede dar una idea de la distribución de los precios y potencias de los coches en el dataset.", unsafe_allow_html=True)
            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True) 
 

    with tab3:


            analisis_kms = st.radio("Selecciona tipo de análisis:", ["Cantidad de coches por kilometraje", "Relación Kilometraje - Precio","Relación Kilometraje - Tipo de transmisión"])

            if analisis_kms == "Cantidad de coches por kilometraje":

                # Crear segmentos de kilometraje
                bins = [0, 50000, 100000, 150000, 200000, np.inf]
                labels = ['Bajo (0-50k)', 'Medio (50k-100k)', 'Medio Alto (100k-150k)', 'Alto (150k-200k)', 'Muy Alto (>200k)']
                df_filtrado['kms_segment'] = pd.cut(df_filtrado['kms'], bins=bins, labels=labels, right=False)

                # Contar la cantidad de coches en cada segmento
                kms_segment_counts = df_filtrado['kms_segment'].value_counts().sort_index()
                # Crear gráfico de barras
                fig_kms_segment = px.bar(kms_segment_counts, x=kms_segment_counts.index, y=kms_segment_counts.values, 
                labels={'kms_segment': 'Rangos de kilometraje', 'y': 'Cantidad'}, 
                title="<b style='color:#A1753F; font-family: Cambria;'>Distribución de coches por segmento de kilometraje</b>", 
                color_discrete_sequence=['#AF6926'])
                st.plotly_chart(fig_kms_segment)
                st.markdown("""
                <hr>
                <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                    <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                    con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                    documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                    limitado a los términos y condiciones acordados entre ambas partes.</i>
                </p>
            """, unsafe_allow_html=True)

            elif analisis_kms == "Relación Kilometraje - Precio":

                df['kms_classification'] = pd.cut(df['kms'], bins=[0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000, 150000, 160000, 170000, 180000, 190000, 200000, 210000, 220000, 230000, 240000, 250000, 260000, 270000, 280000, 290000, 300000, 310000, 320000, 330000, 340000, 350000, 360000, 370000, 380000, 390000, 400000, np.inf], labels=['0-10k', '10k-20k', '20k-30k', '30k-40k', '40k-50k', '50k-60k', '60k-70k', '70k-80k', '80k-90k', '90k-100k', '100k-110k', '110k-120k', '120k-130k', '130k-140k', '140k-150k', '150k-160k', '160k-170k', '170k-180k', '180k-190k', '190k-200k', '200k-210k', '210k-220k', '220k-230k', '230k-240k', '240k-250k', '250k-260k', '260k-270k', '270k-280k', '280k-290k', '290k-300k', '300k-310k', '310k-320k', '320k-330k', '330k-340k', '340k-350k', '350k-360k', '360k-370k', '370k-380k', '380k-390k', '390k-400k', '400k+'])
                # Crear el gráfico de líneas con la media de precio
                plt.figure(figsize=(20, 10))
                mean_price_by_kms = df.groupby('kms_classification')['price'].mean()
                mean_price_by_kms.plot(kind='line', marker='o', color='#AF6926')
                plt.title('Relación entre el kms y el precio medio de los coches', fontsize=16, color='#A1753F', fontname='Cambria')
                plt.xlabel('Kilometraje (kms)')
                plt.ylabel('Precio medio (€)')
                plt.xticks(rotation=90)
                plt.xticks(ticks=range(len(mean_price_by_kms.index)), labels=mean_price_by_kms.index)

                st.pyplot(plt)

                #Conclusiones

                st.markdown("Existe una relación inversa entre el kilometraje y el precio medio de los coches, donde a mayor cantidad de kilómetros recorridos, menor es el <span style='color:#A1753F; font-weight: bold;'>precio promedio</span>.", unsafe_allow_html=True)
                st.markdown("""
                <hr>
                <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                    <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                    con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                    documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                    limitado a los términos y condiciones acordados entre ambas partes.</i>
                </p>
            """, unsafe_allow_html=True)
                

            elif analisis_kms == "Relación Kilometraje - Tipo de transmisión":
                # Crear segmentos de kilometraje
                bins = [0, 50000, 100000, 150000, 200000, np.inf]
                labels = ['Bajo (0-50k)', 'Medio (50k-100k)', 'Medio Alto (100k-150k)', 'Alto (150k-200k)', 'Muy Alto (>200k)']
                df['kms_segment'] = pd.cut(df['kms'], bins=bins, labels=labels, right=False)

                # Calcular el precio promedio por segmento de kilometraje y tipo de transmisión
                avg_price_kms_transmission = df.groupby(['kms_segment', 'shift'])['price'].mean().reset_index()
                # Crear gráfico de barras
                fig_avg_price_kms_transmission = px.bar(avg_price_kms_transmission, x='kms_segment', y='price', color='shift', 
                    labels={'kms_segment': 'Rangos de kilometraje', 'price': 'Precio promedio (€)', 'shift': 'Transmisión'}, 
                    title="<b style='color:#A1753F; font-family: Cambria;'>Precio promedio por segmento de kilometraje y tipo de transmisión</b>", 
                    barmode='group', color_discrete_sequence=['#AF6926', '#CD853F'])
                st.plotly_chart(fig_avg_price_kms_transmission)

                st.markdown("""
                El <span style='color:#A1753F'>**precio**</span> promedio de los vehículos <span style='color:#A1753F'>**disminuye a medida que aumenta el kilometraje**</span>, y los coches con <span style='color:#A1753F'>**transmisión manual**</span> tienden a ser más <span style='color:#A1753F'>**económicos**</span> en todos los segmentos en 
                comparación con los automáticos, con una diferencia más pronunciada en los vehículos de bajo kilometraje.
                """, unsafe_allow_html=True)
                st.markdown("""
                <hr>
                <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                    <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                    con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                    documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                    limitado a los términos y condiciones acordados entre ambas partes.</i>
                </p>
            """, unsafe_allow_html=True)
 

    #TAB 4
    with tab4:
        # 📌 Introducción
        
        analisis_seleccionado = st.radio("Selecciona el análisis:", [
            "Distribución de las marcas según la comunidad autónoma",
            "Relación de los precios por comunidad autónoma",
            "Mapa geográfico de anuncios por comunidad autónoma"
        ])

        # Filtros interactivos
        comunidades_disponibles = list(df["state"].unique())
        comunidades_seleccionadas = st.multiselect(
            "🔎 Filtrar por comunidad autónoma:",
            ["Todas"] + comunidades_disponibles,
            default=["Todas"]
        )

        # Filtrado de datos según selección múltiple
        df_filtrado = df.copy()
        if "Todas" not in comunidades_seleccionadas:
            df_filtrado = df[df["state"].isin(comunidades_seleccionadas)]

        if analisis_seleccionado == "Distribución de las marcas según la comunidad autónoma":
            st.markdown("## <b style='color:#A1753F; font-family: Cambria;'>Distribución de marcas por comunidad autónoma</b>", unsafe_allow_html=True)
            marcas_por_comunidad = df_filtrado.groupby(['state', 'make']).size().unstack().fillna(0)
            fig_marcas_comunidad = px.bar(
                marcas_por_comunidad,
                title="<b style='color:#A1753F; font-family: Cambria;'>Distribución de marcas por comunidad autónoma</b>",
                labels={'value': 'Cantidad', 'state': 'Comunidad autónoma'},
                height=600
            )
            st.plotly_chart(fig_marcas_comunidad)

            st.markdown("""
            En este gráfico se puede observar la distribución de las marcas de coches por Comunidad Autónoma.
            Se puede ver que marcas son más populares en cada Comunidad Autónoma y así poder adaptar la estrategia de marketing a las preferencias de los clientes de cada región.
            Las comunidades autónomas con mayor cantidad de anuncios son <span style='color:#A1753F'>**Andalucía, Cataluña, Comunidad de Madrid y Comunitat Valenciana.**</span>
            """, unsafe_allow_html=True)
            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True)




        elif analisis_seleccionado == "Relación de los precios por comunidad autónoma":
            st.markdown("### <b style='color:#A1753F; font-family: Cambria;'>Distribución de Precios por comunidad autónoma</b>", unsafe_allow_html=True)
            fig_precios_comunidad = px.scatter(
                df_filtrado,
                x='state',
                y='price',
                title="<b style='color:#A1753F; font-family: Cambria;'>Relación entre precios y comunidad autónoma</b>",
                labels={'state': 'Comunidad Autónoma', 'price': 'Precio'},
                height=600
            )
            st.plotly_chart(fig_precios_comunidad)

            st.markdown("""
            En este gráfico se puede observar la relación entre los precios de los coches y la Comunidad Autónoma.
            Se puede ver que hay comunidades autónomas con precios más elevados que otras, por lo que se podría adaptar la estrategia de precios según la región.
            Las comunidades autónomas con precios más elevados son <span style='color:#A1753F'>**Comunidad de Madrid, Cataluña y País Vasco.**</span>
            """, unsafe_allow_html=True)

            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True)

        elif analisis_seleccionado == "Mapa geográfico de anuncios por comunidad autónoma":
            st.markdown("### <b style='color:#A1753F; font-family: Cambria;'>🌍 Mapa Geográfico de Anuncios por Comunidad Autónoma</b>", unsafe_allow_html=True)
            comunidades_coords = {
                'Andalucía': [37.544270, -4.727753], 'Aragón': [41.597628, -0.905662],
                'Principado de Asturias': [43.361915, -5.849389], 'Cantabria': [43.182839, -4.033444],
                'Castilla y León': [41.835441, -4.397635], 'Castilla-La Mancha': [39.862831, -3.919183],
                'Cataluña': [41.820460, 1.867682], 'Comunitat Valenciana': [39.484010, -0.753280],
                'Extremadura': [39.223597, -6.833239], 'Galicia': [42.755087, -7.618896],
                'Comunidad de Madrid': [40.416775, -3.703790], 'Región de Murcia': [37.992240, -1.130654],
                'Comunidad Foral de Navarra': [42.695391, -1.676069], 'País Vasco': [43.106453, -2.620040],
                'La Rioja': [42.287073, -2.539603], 'Illes Baleares': [39.695263, 3.017571],
                'Canarias': [28.291565, -16.629129]
            }
            coords_df = pd.DataFrame(comunidades_coords).T.reset_index()
            coords_df.columns = ['state', 'lat', 'lon']

            state_counts = df_filtrado['state'].value_counts().reset_index()
            state_counts.columns = ['state', 'counts']
            merged_df = pd.merge(coords_df, state_counts, on='state', how='left').fillna(0)

            if "Todas" in comunidades_seleccionadas:
                comunidades_a_mostrar = comunidades_disponibles
            else:
                comunidades_a_mostrar = comunidades_seleccionadas

            merged_df = merged_df[merged_df['state'].isin(comunidades_a_mostrar)]

            m = folium.Map(location=[40.416775, -3.703790], zoom_start=6)
            for _, row in merged_df.iterrows():
                folium.CircleMarker(
                    location=[row['lat'], row['lon']],
                    radius=row['counts'] / 100,
                    popup=f"{row['state']}: {row['counts']} anuncios",
                    color='#A1753F',
                    fill=True,
                    fill_color='#A1753F'
                ).add_to(m)
            folium_static(m)

            st.markdown("""
            En este mapa interactivo se puede observar la cantidad de anuncios de coches de segunda mano por Comunidad Autónoma.
            Se puede ver que hay comunidades autónomas con mayor cantidad de anuncios que otras, lo que puede ser útil para enfocar la estrategia de marketing en esas regiones.
            Las comunidades autónomas con mayor cantidad de anuncios son <span style='color:#A1753F'>**Andalucía, Cataluña, Comunidad de Madrid y Comunitat Valenciana.**</span>
            """, unsafe_allow_html=True)

            st.markdown("""
            <hr>
            <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
                <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
                con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
                documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
                limitado a los términos y condiciones acordados entre ambas partes.</i>
            </p>
        """, unsafe_allow_html=True)




# PANEL DE CONTROL POWERBI
elif menu_lateral == "Panel de control | PowerBI":
# SOLO SE MUESTRA EL INFORME DE POWER BI CUANDO SE SELECCIONA ESA OPCIÓN
    st.markdown("## <b style='color:#A1753F; font-family: Cambria;'>Panel de control interactivo | PowerBI</b>", unsafe_allow_html=True)
    st.write("""
    En esta sección se presenta un panel de control interactivo creado con Power BI.
    En este panel interactivo el cliente podrá visualizar los vehículos que mejor se adapten a sus necesidades, por ejemplo,
    según el rango de precio, marca y modelo, el tipo de combustible, el kilometraje, etc. 
    """)
    powerbi_url = f"https://app.powerbi.com/view?r=eyJrIjoiZmU3NDYxYmItNWZkMS00Mzk2LTk0ODktMDMzMDQ2ZmQyNjIxIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9&pageName=d338a4e41a65b0c0d13b"
  
    # Mostrar el informe en un iframe
    st.markdown(
    f"""
    <iframe width="100%" height="600"
            src="{powerbi_url}"
            frameborder="0" allowFullScreen="true"></iframe>
    """,
    unsafe_allow_html=True
    )
    st.markdown("""
    <hr>
    <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
        <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
        con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
        documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
        limitado a los términos y condiciones acordados entre ambas partes.</i>
    </p>
""", unsafe_allow_html=True)

    

elif menu_lateral =="Modelo predictivo":

    #Intro 
    st.markdown('<h2 style="color: #A1753F; font-family: Cambria;">Objetivo</h2>', unsafe_allow_html=True)
    st.markdown("Este modelo predictivo tiene como objetivo estimar el precio de un vehículo en función de diversas características como **marca, modelo, tipo de combustible, año de fabricación, kilometraje, potencia del motor y tipo de transmisión**. Para ello, se ha aplicado un pipeline de preprocesamiento que transforma las variables categóricas y numéricas antes de alimentar un modelo de regresión.")    
    

    #Vamos a crear tabs con 3 opciones, Correlación Variables, PowerBI Variables modelo y Herraienta de Predicción
    tab1, tab2 = st.tabs(['Desarrollo del Modelo', 'Herramienta de Predicción'])

    #TAB 1
    with tab1:

        from sklearn.preprocessing import LabelEncoder

    #Hacemos un label encoder de shift y fuel 
        # Crear una copia del dataframe original para no modificarlo directamente
        df_encoded = df.copy()

    # Inicializar el LabelEncoder
        le = LabelEncoder()

        # Aplicar el LabelEncoder a las columnas 'fuel' y 'shift'
        df_encoded['fuel'] = le.fit_transform(df_encoded['fuel'])
        df_encoded['shift'] = le.fit_transform(df_encoded['shift'])

    # Seleccionar variablaes para heatmap price, year, kms, power
        st.markdown("## <b style='color:#A1753F; font-family: Cambria;'>Mapa de Calor </b>", unsafe_allow_html=True)

        # Crear un gráfico de correlación con Plotly Express
        fig_heatmap = px.imshow(df_encoded[['price', 'year', 'kms', 'power', 'fuel', 'shift']].corr(), color_continuous_scale='Oranges')
        fig_heatmap.update_layout()
        st.plotly_chart(fig_heatmap)

        # Conclusiones
        st.markdown("## <b style='color:#A1753F; font-family: Cambria;'>Insights</b>", unsafe_allow_html=True)
        st.write("Con el objetivo de que nuestro modelo de predicción sea lo mejor posible el primer paso fue analizar que variables eran las más importantes y como se correlacionaban entré si y sobre todo con el precio. Para esto hemos realizado una análisis de correlación a través de un Heatmap. Como podemos observar  la variable más correlacionada con el precio es la potencia del vehículo, seguida del año de fabricación y el kilometraje que al mismo tiempo tiene una correlación negativa con el año de fabricación ya que mientras menor sea el número del año de fabricacion (osea mientras más viejo sea), más kilometraje tendrá.")
        st.markdown("---")

        st.markdown("## <b style='color:#A1753F; font-family: Cambria;'>Desarrollo del modelo</b>", unsafe_allow_html=True)
        st.markdown("### Transformación de variables")
        st.write("Los datos originales contienen tanto variables **categóricas** como **numéricas**, por lo que es necesario aplicar diferentes técnicas de preprocesamiento antes de entrenar el modelo. Esta foto sacada de Azure ML Studio resume el pipeline de transformación de variables aplicado:")
        #Insertamos la imagen referente al pipeline de transformación de variables pipeline_transformacion.png
        st.image("pipeline_transformación_modelo.png", use_container_width=True)
        st.markdown("""
        

        ### <b style='color:#A1753F; font-family: Cambria;'>Manejo de Datos Categóricos</b>
        Para las variables categóricas, que incluyen: **Marca**, **Modelo**, **Tipo de combustible**, **Tipo de transmisión**, se han transformado utilizando métodos diferentes según su naturaleza:

        #### **Codificación Hash (HashOneHotEncoder)**
        - Aplicada a variables categóricas con una gran cantidad de categorías únicas, como **marca y modelo**.
        - Convierte los valores en una representación binaria con 512 columnas.
        
        #### **Imputación de Valores Faltantes (ModeCatImputer)**
        - Se reemplazan valores faltantes en variables categóricas con la moda de la columna correspondiente.

        #### **Codificación Ordinal (LabelEncoder)**
        - Se aplica a variables con pocas categorías, como **tipo de combustible y tipo de transmisión**.
        - Se sustituyen los valores de texto por números enteros, asignando un número único entero a cada categoría.

        #### **Vectorización de Caracteres (CharGramCountVectorizer)**
        - Se usa en algunos atributos textuales para capturar patrones internos en los nombres de las marcas y modelos, dividiendo el texto en pequeños fragmentos de caracteres llamados n-gramas.

        ---

        ### <b style='color:#A1753F; font-family: Cambria;'>Manejo de Variables Numéricas</b>
        Para las variables numéricas que incluyen: **Kilometraje**, **Potencia del motor**, se han utilizado las siguientes técnicas:

        #### **Imputación de Media (MeanImputer)**
        - Los valores faltantes en variables numéricas se reemplazan por la media de la columna.

        ---

        ### <b style='color:#A1753F; font-family: Cambria;'>Resultados Modelo</b>
        Tras el preprocesamiento, los datos se introducen en un Voting Ensemble, que combina múltiples modelos para mejorar la precisión. En este caso, incluye un XGBRegressor, un modelo de gradient boosting eficaz en la detección de patrones complejos y el manejo de valores atípicos. Esta combinación reduce la varianza, logrando predicciones más estables y precisas.

        ##### Métricas de Evaluación  
        - <span style="color: #AF6926; font-family: Cambria;"><b>R2 Score</b></span>: 0.95212 ➝ Es la métrica clave, ya que muestra que el modelo explica el **95.21%** de la variabilidad de los precios de los coches. Por lo tanto podemos afirmar que el modelo tiene una alta capacidad predictiva y captura con precisión la relación entre las variables y el precio del coche.
        - <span style="color: #AF6926; font-family: Cambria;"><b>MAE</b></span> (Error Absoluto Medio): 1679.7 ➝ En promedio, el modelo comete un error de aproximadamente 1679€ en sus predicciones.  
        - <span style="color: #AF6926; font-family: Cambria;"><b>RMSE</b></span> (Raíz del Error Cuadrático Medio): 3754.7 ➝ Refleja que los errores en la predicción tienen una magnitud promedio de aproximadamente 3754€. Nuestro dataset incluye tanto coches de gama media como vehículos de lujo con precios muy elevados. Esto genera una gran variabilidad en los datos y puede explicar por qué el RMSE es significativamente mayor que el MAE. En particular, los coches de alto valor pueden tener errores de predicción más grandes, lo que impacta más el RMSE.
        """, unsafe_allow_html=True)
    

    with tab2:

        #Variables de entrada para el modelo predictivo
        # -----------------------------------------------------------------------------------------------------------------------------------------------------------
        st.markdown("## <b style='color:#A1753F; font-family: Cambria;'> Modelo predictivo</b>", unsafe_allow_html=True)

        #Para que la marca sea correlativa con el modelo a la hora de introducir el input en la aplicación, crearemos un diccionario en el que para cada marca
        #introduzcamos los modelos que tiene. De esta forma, cuando el usuario introduzca una marca, podrá seleccionar el modelo correspondiente.
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

        st.markdown("""
        <hr>
        <p style="text-align: center; font-size: 14px; color: #7D6B5B; font-style: italic;">
            <i>El presente informe ha sido elaborado en el margen de la relación contractual entre <b>Opticar</b> y <b>AutoMaster Select</b>,
            con el propósito de proporcionar asesoramiento estratégico basado en el análisis de datos. Toda la información contenida en este
            documento es confidencial y ha sido obtenida de fuentes de datos recopiladas mediante técnicas de web scraping. Su uso está estrictamente
            limitado a los términos y condiciones acordados entre ambas partes.</i>
        </p>
    """, unsafe_allow_html=True)

# SOLO SE MUESTRA CONCLUSIONES CUANDO SE SELECCIONA ESA OPCIÓN
elif menu_lateral == "Conclusiones":
    st.markdown("## <b style='color:#A1753F; font-family: Cambria;'>Conclusiones</b>", unsafe_allow_html=True)
    st.markdown("""
            - Evitar la venta de Citroën, Renault y Opel debido a la saturación del mercado.
            - Priorizar la venta de coches con menos de 100.000 km, ya que se devalúan menos.
            - Enfocarse en la venta de coches con menos de 10 años de antigüedad para minimizar la devaluación.
            - Los concesionarios en Madrid, Andalucía y Cataluña deberían adquirir coches de precio más elevado debido a la mayor demanda en estas regiones.
            - No adquirir coches con más de 180.000 km, ya que la devaluación del precio es mucho más pronunciada.
            - Aconsejamos comprar coches de gasolina posteriores a 2001 y de diésel posteriores a 2006, en línea con la normativa de etiquetas medioambientales. La venta de coches diésel sigue siendo el mercado más extendido.
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