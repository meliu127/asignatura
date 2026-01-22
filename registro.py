import streamlit as st
import pandas as pd

def registrar_asignatura(nombre, codigo, fecha, inicio, final, aula, maestro):
    nueva_fila = {
        "Nombre": nombre,
        "Código": codigo,
        "Fecha Registro": str(fecha),
        "Hora Inicio": str(inicio),
        "Hora Final": str(final),
        "Aula": aula,
        "Maestro": maestro
    }

    st.session_state.asignaturas_data = pd.concat(
        [st.session_state.asignaturas_data, 
         pd.DataFrame([nueva_fila])],
        ignore_index=True
    )

if "asignaturas_data" not in st.session_state:
    st.session_state.asignaturas_data = pd.DataFrame(
        columns=["Nombre", "Código", "Fecha Registro", "Hora Inicio", "Hora Final", "Aula", "Maestro"]
    )

st.title("Registro de Asignaturas Matriculadas")

with st.form("asignatura_form", clear_on_submit=True):
    nombre_asig = st.text_input("Ingrese el nombre de la asignatura")
    codigo_asig = st.number_input("Ingrese el código", min_value=0)
    fecha_reg = st.date_input("Seleccione la fecha de registro")
    hora_i = st.time_input("Hora de Inicio")
    hora_f = st.time_input("Hora Final")
    aula_asig = st.text_input("Ingrese el aula")
    maestro_asig = st.text_input("Ingrese el nombre del maestro")
    
    col1, col2 = st.columns(2)
    with col1:
        registrar_button = st.form_submit_button("Registrador De Asignatura")
    with col2:
        limpiar_button = st.form_submit_button("Limpiar")

if registrar_button:
    registrar_asignatura(nombre_asig, codigo_asig, fecha_reg, hora_i, hora_f, aula_asig, maestro_asig)

st.dataframe(st.session_state.asignaturas_data)