import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from analyzer import DataAnalyzer
import streamlit as st


st.sidebar.title("MENU")

opcion = st.sidebar.radio("Ir a :", ["Home","EDA"])

if opcion == "Home" :
      st.title("Análisis de Campaña de Marketing Bancario")

      st.write("""
        Este proyecto analiza los factores que influyen en la aceptación
        de campañas de marketing de una institución financiera.
        """)

      st.subheader("Autor")

      st.write("""
        Nombre: Jeampiere Pocomucha Toribio  
        Curso: Python for Analytics  
        Año: 2026
        """)

      st.subheader("Dataset")

      st.write("""
        El dataset contiene información sobre clientes bancarios,
        incluyendo edad, empleo, créditos y variables económicas,
        junto con el resultado de la campaña de marketing.
        """)

      st.subheader("Tecnologías")

      st.write("""
        - Python
        - Pandas
        - Streamlit
        - Matplotlib
        - Seaborn
        """)
if opcion == "EDA":

    st.title("Carga del Dataset")

    archivo = st.file_uploader("Sube el archivo CSV", type=["csv"])

    if archivo is not None:

        df = pd.read_csv(archivo,sep=";")

        st.success("Archivo cargado correctamente")

        st.subheader("Vista previa")

        st.dataframe(df.head())

        st.subheader("Dimensiones ")

        st.write("Filas:", df.shape[0])
        st.write("Columnas:", df.shape[1]) 

    st.title("EDA")
    
    if archivo is None :
        st.warning("Primero debes cargar el dataset")
    else:
        anlyzer = DataAnalyzer(df)
        tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs([
        "1️⃣ Info Dataset",
        "2️⃣ Clasificación Variables",
        "3️⃣ Estadísticas",
        "4️⃣ Valores Faltantes",
        "5️⃣ Distribución Numéricas",
        "6️⃣ Variables Categóricas",
        "7️⃣ Numérico vs Categórico",
        "8️⃣ Categórico vs Categórico",
        "9️⃣ Análisis Dinámico",
        "🔟 Hallazgos"])
        with tab1 :
          st.subheader("Ítem 1: Información general del dataset")
          col1,col2 = st.columns(2)
          with col1 :
            st.write("Tipos de datos")
            st.dataframe(df.dtypes)
          with col2 :
            st.write("Valores nulos")
            nulos = DataAnalyzer(df).valoresNulos()
            st.dataframe(nulos)

          st.write("Dimensiones del dataset")
          st.write(df.shape)
        with tab2:
          st.subheader("Ítem 2: Clasificación de variables")

          num,cat = DataAnalyzer(df).tipos_variables()

          st.write("Variables numéricas:", list(num))
          st.write("Cantidad:", len(num))

          st.write("Variables categóricas:", list(cat))
          st.write("Cantidad:", len(cat))

        with tab3:
            st.subheader("Ítem 3: Estadísticas descriptivas")
            estadistica = DataAnalyzer(df).estadisticas()
            st.dataframe(estadistica)
        with tab4:
            st.subheader("Ítem 4: Valores faltantes")
            nulos = DataAnalyzer(df).valoresNulos()
            st.dataframe(nulos)
            st.bar_chart(nulos)  
        with tab5:
            st.subheader("Ítem 5: Distribución de variables numéricas")
            mostrar_kde = st.checkbox("Mostrar curva kde")
            columna = st.selectbox("Selecciona variable numérica", num)

            fig,ax = plt.subplots()

            sns.histplot(df[columna], kde=mostrar_kde,ax=ax)

            st.pyplot(fig) 
        with tab6 :
            st.subheader("Ítem 6: Variables categóricas")

            col = st.selectbox("Selecciona variable categórica", cat)

            conteo = df[col].value_counts()

            st.bar_chart(conteo)

            st.write("Proporciones")

            st.write(df[col].value_counts(normalize=True))
        with tab7 :
            st.subheader("Ítem 7: Numérico vs Categórico")

            col = st.selectbox("Variable numérica", num)

            fig,ax = plt.subplots()

            sns.boxplot(x="y", y=col, data=df)

            st.pyplot(fig)      
        with tab8 :
            st.subheader("Ítem 8: Categórico vs Categórico")

            col = st.selectbox("Variable categórica", cat)

            tabla = pd.crosstab(df[col], df["y"])

            st.dataframe(tabla)

            st.bar_chart(tabla)
        with tab9 :
            st.subheader("Ítem 9: Análisis dinámico")

            edad = st.slider("Edad mínima",18,90,30)

            trabajo = st.multiselect("Tipo de trabajo", df["job"].unique())

            df_filtrado = df[df["age"] >= edad]

            if trabajo:
                df_filtrado = df_filtrado[df_filtrado["job"].isin(trabajo)]

            st.write("Datos filtrados")

            st.dataframe(df_filtrado.head())

            st.write("Aceptación de campaña")

            st.bar_chart(df_filtrado["y"].value_counts())
        with tab10 :                
            st.subheader("Ítem 10: Hallazgos clave")
            st.write("Moda")
            st.dataframe(df.mode().head(1))
            st.write("""
            1. Las llamadas con mayor duración presentan mayor probabilidad de aceptación.

            2. Los clientes con educación universitaria muestran mayor respuesta positiva.

            3. El canal telefónico presenta mayor conversión que otros métodos.

            4. Clientes con múltiples contactos previos presentan menor probabilidad de aceptación.

            5. Factores económicos como euribor3m influyen en el comportamiento del cliente.
            """)