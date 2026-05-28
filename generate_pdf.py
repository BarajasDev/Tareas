import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as RLImage, PageBreak
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER

# Datos del alumno y actividad
student_name = "Jahaziel Barajas Avila"
institution = "Centro de Estudios Superiores del Noroeste"
career = "Ingeniería en Desarrollo de Software"
group = "07IDESVA"
activity_name = "U1 Inv. Fundamentos FastAPI"
teacher_name = "Carlos Leonel Espinosa Martinez"
current_date = datetime.now().strftime("%d de %B de %Y")

output_folder = r"c:\Users\LAP-ANALISIS\OneDrive\ESCRITORIO LAPTOP\tareas\outputs"
os.makedirs(output_folder, exist_ok=True)
output_path = os.path.join(output_folder, f"{activity_name}.pdf")

logo_path = r"c:\Users\LAP-ANALISIS\OneDrive\ESCRITORIO LAPTOP\tareas\uploads\logo.png"

# Configuracion de estilos
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name='Justify',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=12,
    leading=18, # 1.5 spacing
    alignment=TA_JUSTIFY,
    spaceAfter=12
))

styles.add(ParagraphStyle(
    name='CustomTitle',
    parent=styles['Heading1'],
    fontName='Helvetica-Bold',
    fontSize=14,
    spaceAfter=12,
    textColor=colors.black
))

styles.add(ParagraphStyle(
    name='CustomSubtitle',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=12,
    spaceAfter=6,
    textColor=colors.black
))

styles.add(ParagraphStyle(
    name='CoverInstitution',
    fontName='Helvetica-Bold',
    fontSize=18,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#FFFFFF'),
    spaceAfter=20
))

styles.add(ParagraphStyle(
    name='CoverText',
    fontName='Helvetica',
    fontSize=14,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#E0E0E0'),
    spaceAfter=15
))

styles.add(ParagraphStyle(
    name='CoverAccent',
    fontName='Helvetica-Bold',
    fontSize=16,
    alignment=TA_CENTER,
    textColor=colors.HexColor('#E0AA3E'),
    spaceAfter=20
))


# Funcion para dibujar la portada
def draw_cover(canvas, doc):
    canvas.saveState()
    # Fondo oscuro
    canvas.setFillColor(colors.HexColor('#171717'))
    canvas.rect(0, 0, letter[0], letter[1], fill=1)
    canvas.restoreState()

# Documento
doc = SimpleDocTemplate(
    output_path,
    pagesize=letter,
    rightMargin=2.5*cm,
    leftMargin=2.5*cm,
    topMargin=2.5*cm,
    bottomMargin=2.5*cm
)

story = []

# PORTADA
if os.path.exists(logo_path):
    img = RLImage(logo_path, width=4*cm, height=4*cm)
    story.append(img)
else:
    story.append(Paragraph("[LOGO UNIVERSIDAD]", styles['CoverInstitution']))

story.append(Spacer(1, 2*cm))
story.append(Paragraph(institution, styles['CoverInstitution']))
story.append(Spacer(1, 1*cm))
story.append(Paragraph(f"<b>Carrera:</b> {career}", styles['CoverText']))
story.append(Paragraph(f"<b>Grupo:</b> {group}", styles['CoverText']))
story.append(Spacer(1, 2*cm))
story.append(Paragraph(activity_name, styles['CoverAccent']))
story.append(Spacer(1, 2*cm))
story.append(Paragraph(f"<b>Maestro:</b> {teacher_name}", styles['CoverText']))
story.append(Paragraph(f"<b>Alumno:</b> {student_name}", styles['CoverText']))
story.append(Spacer(1, 2*cm))
story.append(Paragraph(current_date, styles['CoverText']))

story.append(PageBreak())

# CONTENIDO

# Introduccion
story.append(Paragraph("Introducción", styles['CustomTitle']))
intro_text = "En la presente investigación se abordarán los conceptos fundamentales del framework FastAPI, así como las herramientas y librerías que lo complementan para el desarrollo moderno de APIs web. Analizaremos su arquitectura, el manejo de asincronía, validación de datos y la integración con ORMs para la persistencia."
story.append(Paragraph(intro_text, styles['Justify']))

# Desarrollo
story.append(Paragraph("Desarrollo del Tema", styles['CustomTitle']))

story.append(Paragraph("¿Qué es FastAPI?", styles['CustomSubtitle']))
story.append(Paragraph("FastAPI es un framework web moderno y de alto rendimiento para construir APIs con Python 3.8+ basado en las anotaciones de tipos estándar (type hints). Sus características principales son su altísimo rendimiento, velocidad de desarrollo, reducción de errores y un diseño intuitivo.", styles['Justify']))

story.append(Paragraph("Usos", styles['CustomSubtitle']))
story.append(Paragraph("FastAPI es utilizado principalmente para crear APIs RESTful, microservicios, backends para aplicaciones web, y servicios de Machine Learning e Inteligencia Artificial, donde el alto rendimiento y la capacidad de procesar múltiples peticiones de manera eficiente son clave.", styles['Justify']))

story.append(Paragraph("Arquitectura", styles['CustomSubtitle']))
story.append(Paragraph("FastAPI se apoya fuertemente en una arquitectura asíncrona mediante Starlette (para el manejo web) y Pydantic (para la validación de datos). Sigue el estándar OpenAPI y JSON Schema para la documentación automática. Es agnóstico respecto a la base de datos, permitiendo el uso de cualquier ORM o base de datos.", styles['Justify']))

story.append(Paragraph("Librerías", styles['CustomSubtitle']))
story.append(Paragraph("FastAPI utiliza las siguientes librerías de manera nativa o como dependencias principales: Starlette (partes web), Pydantic (validación de datos) y Uvicorn (servidor web ASGI). Además, suele integrarse con SQLAlchemy, SQLModel o Alembic.", styles['Justify']))

story.append(Paragraph("¿Qué es ORM?", styles['CustomSubtitle']))
story.append(Paragraph("Un ORM (Object-Relational Mapping) es una técnica que permite convertir los datos de una base de datos relacional en objetos orientados a objetos en código. En lugar de escribir SQL, los desarrolladores interactúan con la base de datos a través de clases y métodos.", styles['Justify']))

story.append(Paragraph("1. Comunicación y Validaciones", styles['CustomTitle']))

story.append(Paragraph("FastAPI y Asincronía", styles['CustomSubtitle']))
story.append(Paragraph("¿Qué significa que el framework sea asíncrono y qué ventajas da? Que sea asíncrono significa que el framework puede manejar múltiples operaciones de entrada/salida (I/O) sin bloquear el hilo de ejecución de la aplicación. Aumenta la capacidad de concurrencia y rendimiento del servidor.", styles['Justify']))

story.append(Paragraph("Uvicorn", styles['CustomSubtitle']))
story.append(Paragraph("¿Qué es un servidor ASGI y por qué FastAPI lo requiere obligatoriamente? Un servidor ASGI es un estándar para interfaces web en Python que soporta manejo asíncrono. FastAPI lo requiere porque construye la lógica, pero necesita un servidor web subyacente compatible con asincronía (ASGI) para recibir peticiones HTTP.", styles['Justify']))

story.append(Paragraph("Pydantic", styles['CustomSubtitle']))
story.append(Paragraph("¿Cómo ayuda a validar y limpiar datos (JSON) que envía un cliente? Pydantic transforma y valida el JSON recibido usando anotaciones de tipos de Python. Si los datos son compatibles, los convierte al tipo adecuado automáticamente (limpieza) o devuelve un mensaje de error claro y estructurado.", styles['Justify']))

story.append(Paragraph("2. Persistencia de Datos", styles['CustomTitle']))

story.append(Paragraph("ORM (SQLAlchemy/SQLModel)", styles['CustomSubtitle']))
story.append(Paragraph("¿Qué problema resuelven los ORM y por qué es mejor usarlos? Previenen los ataques de inyección SQL de forma predeterminada, mantienen el código limpio, evitan el acoplamiento a un motor de base de datos específico y aumentan considerablemente la velocidad de desarrollo al usar objetos en vez de cadenas SQL.", styles['Justify']))

story.append(Paragraph("Alembic (Migraciones)", styles['CustomSubtitle']))
story.append(Paragraph("Si necesitas agregar una columna en producción, ¿cómo ayuda Alembic? Alembic permite crear migraciones, que aplican alteraciones estructurales (como agregar una columna) en la base de datos de manera controlada y versionada. Permite actualizar la base sin tener que destruir y recrear tablas, manteniendo la información a salvo.", styles['Justify']))

story.append(Paragraph("3. Arquitectura y Calidad", styles['CustomTitle']))

story.append(Paragraph("Arquitectura en Capas", styles['CustomSubtitle']))
story.append(Paragraph("¿Por qué es un error poner las conexiones a BD dentro de los Routers? Es un error porque viola el principio de Responsabilidad Única. Mezclar capas hace el código difícil de leer y probar. Cada capa (rutas, lógica y persistencia) debe ser independiente.", styles['Justify']))

story.append(Paragraph("Pytest", styles['CustomSubtitle']))
story.append(Paragraph("¿Por qué es fundamental automatizar las pruebas? Es fundamental para garantizar la calidad del software y evitar regresiones. Al automatizar las pruebas de los endpoints, validamos que la API responda como se espera, incluyendo seguridad y persistencia, sin tener que probar manualmente.", styles['Justify']))

# Conclusion
story.append(Paragraph("Conclusión Personal", styles['CustomTitle']))
story.append(Paragraph("En esta investigación he logrado comprender los cimientos principales del desarrollo de aplicaciones web asíncronas con FastAPI. El uso de validaciones automáticas con Pydantic y la facilidad que proporciona ASGI con Uvicorn para la concurrencia me ha permitido ver una gran evolución en comparación con frameworks más clásicos. Por otro lado, la interacción con la base de datos apoyándome en un ORM como SQLAlchemy y aplicando control de versiones a través de Alembic me demuestra lo importante que es tener una buena arquitectura en capas para que el sistema sea escalable y fácil de probar mediante herramientas como Pytest. Entender estas tecnologías me brindará una excelente ventaja técnica y profesional para la creación de APIs y microservicios robustos.", styles['Justify']))

# Referencias
story.append(Paragraph("Referencias", styles['CustomTitle']))
story.append(Paragraph("- Alembic. (s.f.). Alembic Documentation. Recuperado de https://alembic.sqlalchemy.org/", styles['Justify']))
story.append(Paragraph("- FastAPI. (s.f.). FastAPI. Recuperado de https://fastapi.tiangolo.com/es/", styles['Justify']))
story.append(Paragraph("- Pydantic. (s.f.). Pydantic Documentation. Recuperado de https://docs.pydantic.dev/", styles['Justify']))
story.append(Paragraph("- SQLAlchemy. (s.f.). SQLAlchemy Documentation. Recuperado de https://docs.sqlalchemy.org/", styles['Justify']))
story.append(Paragraph("- SQLModel. (s.f.). SQLModel. Recuperado de https://sqlmodel.tiangolo.com/", styles['Justify']))

# Generar PDF con fondo oscuro en la portada
def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor('#171717'))
    canvas.rect(0, 0, letter[0], letter[1], fill=1)
    canvas.restoreState()

def myLaterPages(canvas, doc):
    pass

doc.build(story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
print(f"PDF generado exitosamente en: {output_path}")
