import streamlit as st
import datetime

st.set_page_config(page_title="Mi Agenda Espiritual", page_icon="🌟")

st.title("🌟 Agenda Espiritual Diaria")
st.markdown("Organiza tus prácticas espirituales con intención y amor.")

# Datos de entrada
nombre = st.text_input("Tu nombre")
fecha = st.date_input("Selecciona la fecha", datetime.date.today())
intencion = st.text_area("✨ Intención del día")
gratitud = st.text_area("🙏 Agradecimientos")
afirmacion = st.text_input("💬 Afirmación poderosa del día")
actividad = st.selectbox("🧘 Práctica espiritual", [
    "Meditación", "Oración", "Visualización", "Conexión con el doble cuántico", "Lectura espiritual", "Escritura consciente"
])
notas = st.text_area("📝 Notas adicionales")

if st.button("Guardar mi entrada"):
    st.success("🌈 Entrada guardada con amor. Sigue brillando.")
    st.balloons()
    st.markdown("---")
    st.subheader(f"🌼 Resumen de tu día - {fecha}")
    st.write(f"**Nombre:** {nombre}")
    st.write(f"**Intención:** {intencion}")
    st.write(f"**Gratitud:** {gratitud}")
    st.write(f"**Afirmación:** {afirmacion}")
    st.write(f"**Actividad espiritual:** {actividad}")
    st.write(f"**Notas:** {notas}")
    st.markdown("💖 Gracias por nutrir tu alma hoy.")
