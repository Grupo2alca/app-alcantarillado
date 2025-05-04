
import streamlit as st
import pandas as pd
from fpdf import FPDF

# Cargar las preguntas y respuestas de cada archivo
# Datos de ejemplo extraídos de los archivos (puedes completar con todos los datos)
preguntas_respuestas_norma_alcantarillado = [
    {
        'Pregunta': '¿Cuál es el objetivo principal de la Norma Técnica de Alcantarillado y Drenaje del DMQ?',
        'Respuesta': 'Establecer criterios técnicos obligatorios para estudios, diseño, construcción y operación de redes de alcantarillado y drenaje pluvial en Quito.'
    },
    {
        'Pregunta': '¿Qué institución es responsable de su aplicación?',
        'Respuesta': 'La Empresa Pública Metropolitana de Agua Potable y Saneamiento (EPMAPS).'
    },
    # Agregar más preguntas y respuestas...
]

preguntas_respuestas_normas_diseno = [
    {
        'Pregunta': '¿Qué tipo de sistemas están prohibidos para nuevos desarrollos?',
        'Respuesta': 'Los sistemas combinados están prohibidos para nuevas construcciones.'
    },
    {
        'Pregunta': '¿Cuál es el diámetro mínimo de tubería en redes sanitarias?',
        'Respuesta': '200 mm de diámetro interno, salvo justificación técnica.'
    },
    # Agregar más preguntas y respuestas...
]

preguntas_respuestas_comparacion_normas = [
    {
        'Pregunta': '¿Qué diferencia existe entre la Norma EMAAP-Q 2009 y la Norma DMQ 2023?',
        'Respuesta': 'La DMQ 2023 prohíbe los sistemas combinados para nuevos desarrollos, mientras que la EMAAP-Q 2009 permitía su uso en ciertas zonas.'
    },
    # Agregar más preguntas y respuestas...
]

preguntas_respuestas_50_preguntas = [
    {
        'Pregunta': '¿Qué importancia tienen los Sistemas de Drenaje Urbano (SDU)?',
        'Respuesta': 'Son esenciales para la salud pública, transporte seguro de aguas residuales y protección ambiental.'
    },
    # Agregar más preguntas y respuestas...
]

# Convertir los datos en DataFrames
df_norma_alcantarillado = pd.DataFrame(preguntas_respuestas_norma_alcantarillado)
df_normas_diseno = pd.DataFrame(preguntas_respuestas_normas_diseno)
df_comparacion_normas = pd.DataFrame(preguntas_respuestas_comparacion_normas)
df_50_preguntas = pd.DataFrame(preguntas_respuestas_50_preguntas)

# Función para generar un PDF con las respuestas usando fpdf
def generate_pdf_fpdf(df, title):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=True, align="C")

    for index, row in df.iterrows():
        pdf.cell(200, 10, txt=f"Pregunta {index + 1}: {row['Pregunta']}", ln=True)
        pdf.multi_cell(0, 10, txt=f"Respuesta: {row['Respuesta']}
")

    return pdf.output(dest='S')

# Función para generar el archivo Excel con las respuestas
def generate_excel(df):
    excel_file = df.to_excel(index=False)
    return excel_file

# Aplicación Streamlit
def app():
    st.title("Aplicación de Preguntas y Respuestas sobre Normas de Alcantarillado")

    # Crear un selector para elegir el cuestionario
    opcion = st.selectbox(
        "Selecciona un cuestionario",
        ("Norma Técnica de Alcantarillado DMQ", "Normas de Diseño de Alcantarillado DMQ", "Comparación de Normas EMAAP-Q 2009 vs DMQ 2023", "50 Preguntas sobre Alcantarillado")
    )

    # Mostrar las preguntas y respuestas según la selección
    if opcion == "Norma Técnica de Alcantarillado DMQ":
        df = df_norma_alcantarillado
    elif opcion == "Normas de Diseño de Alcantarillado DMQ":
        df = df_normas_diseno
    elif opcion == "Comparación de Normas EMAAP-Q 2009 vs DMQ 2023":
        df = df_comparacion_normas
    elif opcion == "50 Preguntas sobre Alcantarillado":
        df = df_50_preguntas

    # Mostrar las preguntas
    st.header(f"Preguntas y Respuestas: {opcion}")
    for index, row in df.iterrows():
        st.subheader(f"Pregunta {index + 1}:")
        st.write(row['Pregunta'])
        st.write("**Respuesta**:")
        st.write(row['Respuesta'])
        st.markdown("---")

    # Opción para exportar como PDF
    if st.button("Generar PDF"):
        pdf = generate_pdf_fpdf(df, f"Respuestas {opcion}")
        st.download_button(label="Descargar PDF", data=pdf, file_name=f"Respuestas_{opcion.replace(' ', '_')}.pdf", mime="application/pdf")

    # Opción para exportar como Excel
    if st.button("Generar Excel"):
        excel_file = generate_excel(df)
        st.download_button(label="Descargar Excel", data=excel_file, file_name=f"Respuestas_{opcion.replace(' ', '_')}.xlsx", mime="application/vnd.ms-excel")

if __name__ == '__main__':
    app()
