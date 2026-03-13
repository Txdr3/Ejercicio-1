import streamlit as st

# 1. Configuración inicial de la página
st.set_page_config(page_title="IA en la Educación", page_icon="🧠", layout="centered")

# 2. Inyección de CSS para Diseño Visual y Animaciones
st.markdown("""
<style>
    /* Ocultar el scrollbar principal lo más posible para dar efecto de presentación */
    ::-webkit-scrollbar {
        width: 0px;
        background: transparent;
    }
    
    /* Tipografía: Títulos en sans-serif, texto en serif */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
        color: #1E1E1E;
    }
    p, li, span, div {
        font-family: 'Georgia', serif;
        font-size: 1.15rem;
        line-height: 1.8;
    }
    
    /* Animación de transición (Fade In + ligero deslizamiento) */
    .fade-in-section {
        animation: fadeInSlide 0.6s ease-out forwards;
        /* Espacio en blanco para centrar el contenido verticalmente */
        min-height: 60vh; 
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 2rem 0;
    }
    
    @keyframes fadeInSlide {
        0% { opacity: 0; transform: translateY(15px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    /* Estilo de los botones de navegación */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-family: 'Helvetica Neue', sans-serif !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. Gestión del estado de la página (Navegación)
if 'paso_actual' not in st.session_state:
    st.session_state.paso_actual = 0

def siguiente():
    if st.session_state.paso_actual < 7:
        st.session_state.paso_actual += 1

def anterior():
    if st.session_state.paso_actual > 0:
        st.session_state.paso_actual -= 1

# 4. Definición del Cuadro de Texto (Modal/Pop-up) para las referencias
@st.dialog("Resumen del Artículo")
def mostrar_resumen(titulo, resumen):
    st.markdown(f"**{titulo}**")
    st.write(resumen)

# 5. Contenedor principal con animación
st.markdown('<div class="fade-in-section">', unsafe_allow_html=True)

# Lógica de renderizado según el paso actual
paso = st.session_state.paso_actual

if paso == 0:
    st.title("La Inteligencia Artificial como herramienta para educar")
    st.info("💡 *La IA nos puede ser de gran ayuda para reforzar la manera de enseñar y de aprender*")

elif paso == 1:
    st.header("¿Cómo la IA está transformando el aprendizaje?")
    st.subheader("Una mirada desde la psicología educativa")
    st.markdown("**Por: Victor Hugo Zúñiga Sandoval**")
    st.markdown("""
    En los últimos años, hemos escuchado mucho sobre la Inteligencia Artificial (IA), pero ¿sabemos realmente cómo está ayudando a nuestros estudiantes? Más allá de los robots y la ciencia ficción, la IA se ha convertido en una herramienta aliada de la psicología educacional. 
    
    Su objetivo no es reemplazar a los maestros, sino ayudarlos a entender mejor cómo aprende cada niño y adolescente. A continuación, exploramos los puntos clave de esta revolución tecnológica en las aulas, basándonos en investigaciones recientes.
    """)

elif paso == 2:
    st.header("1. Un traje a la medida: El aprendizaje personalizado")
    st.markdown("""
    Cada estudiante es un mundo. Algunos aprenden rápido las matemáticas, otros necesitan más tiempo para la lectura. Tradicionalmente, era difícil para un solo profesor atender 30 necesidades distintas al mismo tiempo. Aquí es donde entra la IA.

    A través de lo que los expertos llaman **Sistemas de Tutoría Inteligente (ITS)** y Chatbots, la tecnología puede actuar como un tutor personal que acompaña al alumno las 24 horas. Estos sistemas ajustan el ritmo de las lecciones según lo que el estudiante ya sabe y lo que le falta reforzar, lo que mejora significativamente la eficiencia del aprendizaje (Mejía Chiriboga et al., 2025; Villamar Vásquez et al., 2024).
    """)

elif paso == 3:
    st.header("2. Nadie se queda atrás: Apoyo a la diversidad")
    st.markdown("""
    Uno de los mayores logros de la IA es su capacidad para ayudar a estudiantes con Necesidades Educativas Especiales (NEE). 
    
    La tecnología actual puede detectar "señales invisibles" en la forma en que un alumno interactúa con el contenido, permitiendo que el material se adapte a sus capacidades cognitivas o emocionales (Duarte Gahona, 2025). Esto significa que la educación se vuelve más inclusiva y humana gracias a los algoritmos.
    """)

elif paso == 4:
    st.header("3. Detectar problemas antes de que aparezcan")
    st.markdown("""
    En psicología educativa, el tiempo es oro. Identificar una dificultad de aprendizaje (como la dislexia o problemas de atención) de forma temprana puede cambiar el futuro de un niño. 
    
    Gracias al análisis predictivo, la IA analiza grandes cantidades de datos para avisar a los docentes cuando un alumno está en riesgo de quedarse atrás, permitiendo intervenir mucho antes de que el problema se vuelva crítico (Salazar Vega et al., 2025).
    """)

elif paso == 5:
    st.header("4. Una nueva forma de evaluar")
    st.markdown("""
    ¿Te imaginas una evaluación que no sea un examen estresante de una hora? La IA permite una evaluación continua. 
    
    Mediante redes neuronales y robots educativos, los profesores pueden ver cómo evoluciona el alumno día a día, de forma más objetiva y sin los sesgos que a veces tenemos los humanos (Martínez-Comesaña et al., 2023).
    """)

elif paso == 6:
    st.header("5. ¿Es todo perfecto? Los desafíos éticos")
    st.markdown("""
    Como toda gran herramienta, la IA tiene sus retos. Los investigadores advierten que debemos ser cuidadosos con la ética y la privacidad de los datos de los menores. 
    
    El objetivo debe ser siempre cerrar brechas, no crear nuevas desigualdades. La clave está en usar la IA para potenciar el talento humano, no para automatizar la educación sin alma (Peñafiel Arteaga et al., 2025).
    """)

elif paso == 7:
    st.header("📚 Referencias Bibliográficas")
    st.write("Selecciona una referencia para leer su resumen:")
    
    referencias = {
        "Duarte Gahona, Y. K. (2025)": {
            "titulo": "Aplicación de la Inteligencia Artificial en la Personalización del Aprendizaje...",
            "resumen": "Este artículo analiza cómo la inteligencia artificial puede adaptarse a las necesidades de estudiantes con discapacidades o dificultades de aprendizaje. Explica que los sistemas de IA pueden ajustar el ritmo, tipo de contenido y métodos de enseñanza..."
        },
        "Guishca Ayala, L. A., et al. (2024)": {
            "titulo": "Integración de la Inteligencia Artificial en la Enseñanza de Matemáticas.",
            "resumen": "El estudio examina cómo la inteligencia artificial puede mejorar la enseñanza de las matemáticas mediante plataformas digitales, tutores inteligentes y sistemas que analizan el desempeño del estudiante..."
        },
        "Martínez-Comesaña, M., et al. (2023)": {
            "titulo": "Impacto de la inteligencia artificial en los métodos de evaluación...",
            "resumen": "Este artículo estudia cómo la inteligencia artificial está transformando la forma en que se evalúa a los estudiantes. Describe herramientas que permiten evaluaciones automáticas, análisis del progreso académico y retroalimentación inmediata..."
        },
        "Mejía Chiriboga, C. A., et al. (2025)": {
            "titulo": "Aplicación de la inteligencia artificial en la personalización del aprendizaje.",
            "resumen": "El artículo explica cómo la IA permite adaptar el proceso educativo a cada estudiante. Describe plataformas educativas que analizan el comportamiento, progreso y estilo de aprendizaje del alumno para recomendar contenidos específicos..."
        },
        "Peñafiel Arteaga, E. E., et al. (2025)": {
            "titulo": "La inteligencia artificial en la educación: desafíos y oportunidades.",
            "resumen": "Este trabajo ofrece una visión general sobre el uso de la inteligencia artificial en la educación. Analiza tanto sus beneficios como los desafíos que presenta, como la brecha digital, la capacitación docente y los riesgos éticos..."
        },
        "Salazar Vega, L. R., et al. (2025)": {
            "titulo": "Análisis del uso de la IA para la detección temprana de dificultades...",
            "resumen": "El artículo estudia cómo los sistemas de inteligencia artificial pueden identificar de forma temprana problemas de aprendizaje en los estudiantes. Mediante el análisis de datos académicos y comportamiento en plataformas..."
        },
        "Villamar Vásquez, G. I., et al. (2024)": {
            "titulo": "Aplicación de la inteligencia artificial en la educación.",
            "resumen": "Este artículo presenta una revisión general del uso de la inteligencia artificial en el ámbito educativo. Describe diversas aplicaciones como tutores virtuales, plataformas de aprendizaje adaptativo, análisis de datos..."
        }
    }
    
    with st.expander("Ver lista completa de artículos"):
        for autor, datos in referencias.items():
            if st.button(f"📄 {autor} - {datos['titulo']}", key=autor):
                mostrar_resumen(datos['titulo'], datos['resumen'])

st.markdown('</div>', unsafe_allow_html=True) # Cierra el div de la animación
st.divider()

# 6. Botones de Control (Navegación Siguiente / Anterior)
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.paso_actual > 0:
        st.button("⬅️ Anterior", on_click=anterior)

# Columna central vacía para empujar los botones a los extremos
with col2:
    # Indicador de progreso opcional en el centro
    st.markdown(f"<p style='text-align: center; color: gray; font-size: 0.9rem;'>Página {paso + 1} de 8</p>", unsafe_allow_html=True)

with col3:
    if st.session_state.paso_actual < 7:
        st.button("Siguiente ➡️", on_click=siguiente)
