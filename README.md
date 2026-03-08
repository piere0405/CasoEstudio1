📊 Análisis Exploratorio de Datos – Bank Marketing Dataset

Aplicación interactiva desarrollada con Python y Streamlit para realizar un Análisis Exploratorio de Datos (EDA) sobre el dataset BankMarketing.csv.

La aplicación permite cargar el dataset, explorar las variables, visualizar distribuciones, analizar relaciones entre variables y obtener insights clave a partir de estadísticas descriptivas.

🔗 Aplicación desplegada:
https://casoestudio1.streamlit.app/

🎯 Objetivo del proyecto

El objetivo de este proyecto es construir una herramienta interactiva de análisis de datos que permita explorar el dataset Bank Marketing utilizando técnicas de estadística descriptiva y visualización de datos.

Este proyecto fue desarrollado como parte de la especialización Python for Analytics, aplicando conceptos fundamentales de programación y análisis de datos.

El enfoque del proyecto es exploratorio, por lo tanto no se desarrollan modelos predictivos, sino que se busca comprender el comportamiento de los datos y generar hallazgos relevantes.

🗂 Dataset

El dataset utilizado corresponde al Bank Marketing Dataset, que contiene información sobre campañas de marketing realizadas por una institución bancaria.

Las variables incluyen características demográficas del cliente, información financiera y datos sobre campañas de contacto realizadas por el banco.

El objetivo del dataset es analizar los factores asociados a que un cliente acepte o no un depósito a plazo.

🧠 Análisis Exploratorio de Datos (EDA)

La aplicación permite realizar diferentes tipos de análisis:

1️⃣ Información general del dataset

Tipos de variables

Conteo de valores nulos

Dimensiones del dataset

2️⃣ Clasificación de variables

Variables numéricas

Variables categóricas

3️⃣ Estadísticas descriptivas

Se analizan métricas como:

Media

Mediana

Moda

Medidas de dispersión

4️⃣ Análisis de valores faltantes

Identificación de datos faltantes

Evaluación de su impacto

5️⃣ Distribución de variables numéricas

Visualización mediante:

Histogramas

Gráficos de distribución

6️⃣ Análisis de variables categóricas

Conteos

Proporciones

Gráficos de barras

7️⃣ Análisis bivariado (numérico vs categórico)

Ejemplos:

age vs y

duration vs y

8️⃣ Análisis bivariado (categórico vs categórico)

Ejemplos:

education vs y

contact vs y

9️⃣ Análisis interactivo

El usuario puede seleccionar variables utilizando widgets como:

Selectbox

Multiselect

Slider

para generar análisis dinámicos.

🔟 Hallazgos clave

Se presentan insights derivados del análisis exploratorio.

🛠 Tecnologías utilizadas

Este proyecto fue desarrollado utilizando las siguientes herramientas:

Python

Pandas

NumPy

Matplotlib

Seaborn

Streamlit (para la interfaz interactiva) Streamlit

Estas herramientas permiten construir aplicaciones de análisis de datos de forma rápida e interactiva directamente en Python.
<img width="1353" height="565" alt="image" src="https://github.com/user-attachments/assets/b79c8be3-58c0-4cc8-a9c1-a9a70758eaf2" />
<img width="1243" height="606" alt="image" src="https://github.com/user-attachments/assets/c6854dce-daa6-4e75-b1a7-829ed7dd35ea" />


🧩 Funcionalidades de la aplicación

La aplicación implementa diferentes componentes de Streamlit:

st.sidebar

st.tabs

st.columns

st.selectbox

st.multiselect

st.slider

st.checkbox

st.file_uploader

Esto permite construir una interfaz ordenada, interactiva y fácil de utilizar.

🧱 Estructura del proyecto

<img width="159" height="105" alt="image" src="https://github.com/user-attachments/assets/a75d025f-a465-4d8a-beee-ec69a163709e" />

▶️ Cómo ejecutar el proyecto

1️⃣ Clonar el repositorio

git clone https://github.com/piere0405/CasoEstudio1

2️⃣ Instalar dependencias

pip install -r requirements.txt

3️⃣ Ejecutar la aplicación

streamlit run app.py

La aplicación se abrirá automáticamente en el navegador.

📌 Conclusiones del análisis

1️⃣ La variable duration muestra una fuerte relación con la respuesta del cliente (y).

2️⃣ Algunas variables categóricas como education y contact presentan diferencias claras en la proporción de aceptación.

3️⃣ La mayoría de los clientes en el dataset no aceptan el depósito, mostrando un fuerte desbalance de clases.

4️⃣ La distribución de variables como age presenta una concentración en ciertos rangos etarios.

5️⃣ El análisis exploratorio permite identificar patrones relevantes que podrían utilizarse en futuros modelos predictivos.

👨‍💻 Autor

Jeampiere Pocomucha Toribio

Especialización: Python for Analytics
Año: 2026
