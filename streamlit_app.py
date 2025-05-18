import streamlit as st

# Estados iniciales
if 'page' not in st.session_state:
    st.session_state.page = 'start'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_data' not in st.session_state:
    st.session_state.user_data = {"correo": "", "contrasena": ""}
if 'cv_data' not in st.session_state:
    st.session_state.cv_data = {
        "nombre": "", "estudios": "", "skills": "", "experiencia": "", "pasatiempos": ""
    }
if 'postulacion' not in st.session_state:
    st.session_state.postulacion = {
        "puesto": "", "modalidad": "", "region": "", "descripcion": "", "postular": None,
        "requiere_cv": None, "cv_adjuntado": False, "datos_confirmados": False,
        "oferta_seleccionada": None, "entrevista_pregunta_idx": 0, "entrevista_respuestas": []
    }
if 'confirmacion' not in st.session_state:
    st.session_state.confirmacion = None


def reset_confirmacion():
    st.session_state.confirmacion = None

def reset_postulacion():
    st.session_state.postulacion = {
        "puesto": "", "modalidad": "", "region": "", "descripcion": "", "postular": None,
        "requiere_cv": None, "cv_adjuntado": False, "datos_confirmados": False,
        "oferta_seleccionada": None, "entrevista_pregunta_idx": 0, "entrevista_respuestas": []
    }
    reset_confirmacion()


# --- Páginas previas: registro, login, crear CV (igual que antes) ---

def start_page():
    st.title("¿Tiene cuenta creada?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button('"Sí"'):
            st.session_state.page = 'login_email'
            reset_confirmacion()
            st.rerun()
    with col2:
        if st.button('"No"'):
            st.session_state.page = 'register_email'
            reset_confirmacion()
            st.rerun()


def register_email():
    st.title("Crear cuenta - Ingrese su correo electrónico")
    email = st.text_input("Correo electrónico:", value=st.session_state.user_data["correo"])
    if email != st.session_state.user_data["correo"]:
        st.session_state.user_data["correo"] = email
        reset_confirmacion()
    if email and st.button("Confirmar correo"):
        st.session_state.confirmacion = f"El correo ingresado es **{email}**, ¿es correcto?"
    if st.session_state.confirmacion:
        st.markdown(f"### {st.session_state.confirmacion}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('"Sí"'):
                st.session_state.page = 'register_password'
                reset_confirmacion()
                st.rerun()
        with col2:
            if st.button('"No"'):
                reset_confirmacion()


def register_password():
    st.title("Crear cuenta - Ingrese su contraseña")
    pwd = st.text_input("Contraseña:", type="password", value=st.session_state.user_data["contrasena"])
    if pwd != st.session_state.user_data["contrasena"]:
        st.session_state.user_data["contrasena"] = pwd
        reset_confirmacion()
    if pwd and st.button("Confirmar contraseña"):
        st.session_state.confirmacion = "¿La contraseña es correcta?"
    if st.session_state.confirmacion:
        st.markdown(f"### {st.session_state.confirmacion}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('"Sí"'):
                st.success("Cuenta creada exitosamente!")
                st.session_state.logged_in = True
                st.session_state.page = 'post_login_menu'
                reset_confirmacion()
                st.rerun()
        with col2:
            if st.button('"No"'):
                reset_confirmacion()


def login_email():
    st.title("Iniciar sesión - Ingrese su correo electrónico")
    email = st.text_input("Correo electrónico:", value=st.session_state.user_data["correo"])
    if email != st.session_state.user_data["correo"]:
        st.session_state.user_data["correo"] = email
        reset_confirmacion()
    if email and st.button("Confirmar correo"):
        st.session_state.confirmacion = f"El correo ingresado es **{email}**, ¿es correcto?"
    if st.session_state.confirmacion:
        st.markdown(f"### {st.session_state.confirmacion}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('"Sí"'):
                st.session_state.page = 'login_password'
                reset_confirmacion()
                st.rerun()
        with col2:
            if st.button('"No"'):
                reset_confirmacion()


def login_password():
    st.title("Iniciar sesión - Ingrese su contraseña")
    pwd = st.text_input("Contraseña:", type="password", value=st.session_state.user_data["contrasena"])
    if pwd != st.session_state.user_data["contrasena"]:
        st.session_state.user_data["contrasena"] = pwd
        reset_confirmacion()
    if pwd and st.button("Confirmar contraseña"):
        st.session_state.confirmacion = "¿La contraseña es correcta?"
    if st.session_state.confirmacion:
        st.markdown(f"### {st.session_state.confirmacion}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('"Sí"'):
                st.success("Sesión iniciada correctamente!")
                st.session_state.logged_in = True
                st.session_state.page = 'post_login_menu'
                reset_confirmacion()
                st.rerun()
        with col2:
            if st.button('"No"'):
                reset_confirmacion()


# --- Menú post-login ---

def post_login_menu():
    st.title("¿Qué desea hacer?")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('"Crear CV"'):
            st.session_state.page = 'cv_nombre'
            st.rerun()
    with col2:
        if st.button('"Postular a ofertas laborales"'):
            st.session_state.page = 'postulacion_puesto'
            reset_postulacion()
            st.rerun()
    with col3:
        if st.button('"Cerrar sesión"'):
            st.session_state.logged_in = False
            st.session_state.page = 'start'
            st.rerun()


def back_to_menu_button():
    if st.button("Volver al menú principal"):
        st.session_state.page = 'post_login_menu'
        st.rerun()


# --- Funciones para crear CV (iguales que antes) ---

def cv_input(label, key, input_type=None):
    if input_type == "password":
        value = st.text_input(label, value=st.session_state.cv_data[key], type="password")
    else:
        value = st.text_input(label, value=st.session_state.cv_data[key])
    if value != st.session_state.cv_data[key]:
        st.session_state.cv_data[key] = value
        reset_confirmacion()
    if value and st.button(f"Confirmar {label}"):
        st.session_state.confirmacion = f"El {label.lower()} ingresado es **{value}**, ¿es correcto?"
    if st.session_state.confirmacion and label.lower() in st.session_state.confirmacion:
        st.markdown(f"### {st.session_state.confirmacion}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('"Sí"'):
                reset_confirmacion()
                next_pages = {
                    "nombre completo": "cv_estudios",
                    "estudios": "cv_skills",
                    "skills": "cv_experiencia",
                    "experiencia": "cv_pasatiempos",
                    "pasatiempos": "cv_resumen"
                }
                st.session_state.page = next_pages.get(label.lower(), "post_login_menu")
                st.rerun()
        with col2:
            if st.button('"No"'):
                reset_confirmacion()


def cv_nombre():
    st.title("Crear CV - Nombre completo")
    cv_input("Nombre completo", "nombre")
    back_to_menu_button()


def cv_estudios():
    st.title("Crear CV - Estudios")
    cv_input("Estudios", "estudios")
    back_to_menu_button()


def cv_skills():
    st.title("Crear CV - Skills")
    cv_input("Skills", "skills")
    back_to_menu_button()


def cv_experiencia():
    st.title("Crear CV - Experiencia")
    cv_input("Experiencia", "experiencia")
    back_to_menu_button()


def cv_pasatiempos():
    st.title("Crear CV - Pasatiempos")
    cv_input("Pasatiempos", "pasatiempos")
    back_to_menu_button()


def cv_resumen():
    st.title("Resumen de CV")
    for k, v in st.session_state.cv_data.items():
        st.write(f"**{k.capitalize()}**: {v}")
    if st.button("Finalizar y guardar CV"):
        st.success("CV guardado correctamente!")
    back_to_menu_button()


OFERTAS = [
    {"titulo": "Jefe de Proyecto", "descripcion": "Liderar proyectos, coordinar equipos y entregar resultados en tiempo."},
    {"titulo": "Analista de Datos", "descripcion": "Analizar grandes volúmenes de datos para tomar decisiones estratégicas."},
    {"titulo": "Desarrollador Backend", "descripcion": "Diseñar y mantener la arquitectura del servidor y base de datos."},
    {"titulo": "Diseñador UX/UI", "descripcion": "Crear interfaces amigables y mejorar experiencia de usuario."},
    {"titulo": "Especialista en Marketing Digital", "descripcion": "Planificar y ejecutar campañas digitales efectivas."}
]

# Pregunta puesto deseado
def postulacion_puesto():
    st.title("Postulación - Puesto deseado")
    puesto = st.text_input("Ingrese el puesto deseado:", value=st.session_state.postulacion["puesto"])
    if puesto != st.session_state.postulacion["puesto"]:
        st.session_state.postulacion["puesto"] = puesto
        reset_confirmacion()
    if puesto and st.button("Confirmar puesto"):
        st.session_state.confirmacion = f"El puesto ingresado es **{puesto}**, ¿es correcto?"
    if st.session_state.confirmacion and "puesto" in st.session_state.confirmacion:
        st.markdown(f"### {st.session_state.confirmacion}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('"Sí"'):
                st.session_state.page = 'postulacion_modalidad'
                reset_confirmacion()
                st.rerun()
        with col2:
            if st.button('"No"'):
                reset_confirmacion()
    back_to_menu_button()

# Pregunta modalidad
def postulacion_modalidad():
    st.title("Postulación - Modalidad de trabajo")
    opciones = ["Presencial/hibbrido", "Virtual"]
    seleccion = st.radio("Seleccione modalidad:", opciones,
                         index=0 if st.session_state.postulacion["modalidad"] == "" else opciones.index(st.session_state.postulacion["modalidad"]))
    if seleccion != st.session_state.postulacion["modalidad"]:
        st.session_state.postulacion["modalidad"] = seleccion
        reset_confirmacion()
    if seleccion and st.button("Confirmar modalidad"):
        st.session_state.confirmacion = f"La modalidad seleccionada es **{seleccion}**, ¿es correcta?"
    if st.session_state.confirmacion and "modalidad" in st.session_state.confirmacion:
        st.markdown(f"### {st.session_state.confirmacion}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('"Sí"'):
                if seleccion == "Presencial/hibbrido":
                    st.session_state.page = 'postulacion_region'
                else:
                    st.session_state.page = 'postulacion_resultados'
                reset_confirmacion()
                st.rerun()
        with col2:
            if st.button('"No"'):
                reset_confirmacion()
    back_to_menu_button()

# Pregunta región solo si presencial/hibbrido
def postulacion_region():
    st.title("Postulación - Región")
    region = st.text_input("Ingrese la región deseada:", value=st.session_state.postulacion["region"])
    if region != st.session_state.postulacion["region"]:
        st.session_state.postulacion["region"] = region
        reset_confirmacion()
    if region and st.button("Confirmar región"):
        st.session_state.confirmacion = f"La región ingresada es **{region}**, ¿es correcta?"
    if st.session_state.confirmacion and "región" in st.session_state.confirmacion:
        st.markdown(f"### {st.session_state.confirmacion}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button('"Sí"'):
                st.session_state.page = 'postulacion_resultados'
                reset_confirmacion()
                st.rerun()
        with col2:
            if st.button('"No"'):
                reset_confirmacion()
    back_to_menu_button()

# Mostrar resultados simulados según filtros
def postulacion_resultados():
    st.title("Resultados de búsqueda")
    st.write("Se encontraron las siguientes ofertas:")
    # Para simulación listamos todas las ofertas (podrías filtrar según puesto, modalidad, región)
    for i, oferta in enumerate(OFERTAS):
        if st.button(oferta["titulo"]):
            st.session_state.postulacion["oferta_seleccionada"] = i
            st.session_state.page = 'postulacion_descripcion'
            st.rerun()
    back_to_menu_button()

# Mostrar descripción de oferta seleccionada
def postulacion_descripcion():
    idx = st.session_state.postulacion["oferta_seleccionada"]
    oferta = OFERTAS[idx]
    st.title(f"Descripción de la oferta: {oferta['titulo']}")
    st.write(oferta["descripcion"])
    st.write("¿Desea postular?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button('"Sí"'):
            st.session_state.postulacion["postular"] = True
            st.session_state.page = 'postulacion_entrevista'
            st.session_state.postulacion["entrevista_pregunta_idx"] = 0
            st.session_state.postulacion["entrevista_respuestas"] = []
            st.rerun()
    with col2:
        if st.button('"No"'):
            st.session_state.postulacion["postular"] = False
            st.session_state.page = 'postulacion_ver_mas'
            st.rerun()
    back_to_menu_button()

# Preguntar si desea ver más vacantes o volver al inicio
def postulacion_ver_mas():
    st.title("¿Desea ver más vacantes?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button('"Sí"'):
            reset_postulacion()
            st.session_state.page = 'postulacion_resultados'
            st.rerun()
    with col2:
        if st.button('"No"'):
            st.session_state.page = 'post_login_menu'
            st.rerun()
    back_to_menu_button()

# Entrevista simulada con preguntas predefinidas
ENTREVISTA_PREGUNTAS = [
    {"pregunta": "¿Tiene experiencia previa en el área?", "respuestas": ["Sí", "No"]},
    {"pregunta": "¿Está disponible para trabajar en horario completo?", "respuestas": ["Sí", "No"]},
    {"pregunta": "¿Cuenta con certificaciones relevantes?", "respuestas": ["Sí", "No"]},
    {"pregunta": "¿Prefiere trabajo presencial o remoto?", "respuestas": ["Presencial", "Remoto", "Indiferente"]},
    {"pregunta": "¿Está dispuesto a viajar?", "respuestas": ["Sí", "No"]}
]

def postulacion_entrevista():
    idx = st.session_state.postulacion["entrevista_pregunta_idx"]
    if idx >= len(ENTREVISTA_PREGUNTAS):
        # Entrevista finalizada
        st.title("Entrevista finalizada")
        st.write("Gracias por responder. Su postulación ha sido enviada.")
        # Aquí se simula guardar la postulación con respuestas
        st.session_state.postulacion["datos_confirmados"] = True
        if st.button("Volver al menú principal"):
            st.session_state.page = 'post_login_menu'
            st.rerun()
        return
    
    pregunta = ENTREVISTA_PREGUNTAS[idx]
    st.title(f"Entrevista: {pregunta['pregunta']}")
    col = st.columns(len(pregunta['respuestas']))
    for i, resp in enumerate(pregunta['respuestas']):
        with col[i]:
            if st.button(f'"{resp}"'):
                st.session_state.postulacion["entrevista_respuestas"].append(resp)
                st.session_state.postulacion["entrevista_pregunta_idx"] += 1
                st.rerun()
    back_to_menu_button()


# Función para botón volver menú en cualquier pantalla post-login
def back_to_menu_button():
    if st.button("Volver al menú principal"):
        st.session_state.page = 'post_login_menu'
        st.rerun()


# El menú post-login y pantallas de login/registro y creación CV se mantienen iguales que antes (omitidos aquí para brevedad)


# Mapear páginas para ejecución
pages = {
    'start': start_page,
    'register_email': register_email,
    'register_password': register_password,
    'login_email': login_email,
    'login_password': login_password,
    'post_login_menu': post_login_menu,
    'cv_nombre': cv_nombre,
    'cv_estudios': cv_estudios,
    'cv_skills': cv_skills,
    'cv_experiencia': cv_experiencia,
    'cv_pasatiempos': cv_pasatiempos,
    'cv_resumen': cv_resumen,
    'postulacion_puesto': postulacion_puesto,
    'postulacion_modalidad': postulacion_modalidad,
    'postulacion_region': postulacion_region,
    'postulacion_resultados': postulacion_resultados,
    'postulacion_descripcion': postulacion_descripcion,
    'postulacion_ver_mas': postulacion_ver_mas,
    'postulacion_entrevista': postulacion_entrevista
}

# Ejecutar página actual
pages.get(st.session_state.page, start_page)()
