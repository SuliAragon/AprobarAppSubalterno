"""Relaciones de estudio redactadas a partir del manual aportado (septiembre 2026).
No consultar noticias ni actualizar datos municipales al regenerar este banco.
"""
GROUPS=[]
def group(topic, section, direct, reverse, rows, ref, note=''):
    entries=[tuple(x.strip() for x in line.split('|',1)) for line in rows.strip().splitlines() if line.strip()]
    assert len(entries)>=4 and all(len(x)==2 for x in entries),(section,entries)
    GROUPS.append(dict(topic=topic,section=section,direct=direct,reverse=reverse,rows=entries,reference=ref,note=note))

group(1,'Constitución: elaboración','¿En qué fecha tuvo lugar {key}?','¿Qué hito constitucional corresponde al {value}?','''
la elección de las Cortes constituyentes|15 de junio de 1977
la aprobación de la Constitución por las Cortes|31 de octubre de 1978
la ratificación de la Constitución en referéndum|6 de diciembre de 1978
la sanción y promulgación de la Constitución|27 de diciembre de 1978
la publicación y entrada en vigor de la Constitución|29 de diciembre de 1978
''','PDF 6–11')
group(1,'Constitución: cifras','¿Qué cifra corresponde a {key}?','¿A qué dato de la Constitución corresponde la cifra {value}?','''
los artículos de la Constitución|169
los títulos numerados, sin contar el preliminar|10
las disposiciones adicionales|4
las disposiciones transitorias|9
los votos favorables del Congreso en 1978|325
los votos contrarios del Congreso en 1978|6
las abstenciones del Congreso en 1978|14
el porcentaje favorable del referéndum de 1978|87,78 %
el número del BOE que publicó la Constitución|311
''','PDF 6–11', 'Además de los diez títulos numerados existe un título preliminar.')
group(1,'Constitución: títulos','¿Qué materia regula {key}?','¿En qué título se regula {value}?','''
el título preliminar|Principios generales, artículos 1–9
el título I|Derechos y deberes fundamentales, artículos 10–55
el título II|Corona, artículos 56–65
el título III|Cortes Generales, artículos 66–96
el título IV|Gobierno y Administración, artículos 97–107
el título V|Relaciones Gobierno-Cortes, artículos 108–116
el título VI|Poder Judicial, artículos 117–127
el título VII|Economía y Hacienda, artículos 128–136
el título VIII|Organización territorial, artículos 137–158
el título IX|Tribunal Constitucional, artículos 159–165
el título X|Reforma constitucional, artículos 166–169
''','PDF 6–8')
group(1,'Constitución: organización del título I','¿Qué artículos comprende {key}?','¿Qué parte del título I corresponde a los artículos {value}?','''
el capítulo I, españoles y extranjeros|11–13
el capítulo II, derechos y libertades|14–38
la sección primera del capítulo II|15–29
la sección segunda del capítulo II|30–38
el capítulo III, principios rectores|39–52
el capítulo IV, garantías|53–54
el capítulo V, suspensión|55
''','PDF 6–8', 'El artículo 10 queda fuera del capítulo I y el 14 fuera de las dos secciones del capítulo II.')
group(1,'Constitución: artículos del preliminar','¿Qué contenido se vincula específicamente a {key}?','¿Qué precepto del título preliminar establece {value}?','''
el artículo 1|Estado social y democrático, soberanía popular y monarquía parlamentaria
el artículo 2|Unidad, autonomía y solidaridad territorial
el artículo 3|Castellano y lenguas cooficiales
el artículo 4|Bandera de España y banderas autonómicas
el artículo 5|Capital del Estado en Madrid
el artículo 6|Partidos políticos como expresión del pluralismo
el artículo 7|Sindicatos y asociaciones empresariales
el artículo 8|Misiones de las Fuerzas Armadas
el artículo 9.3|Legalidad, jerarquía, publicidad, seguridad y prohibición de arbitrariedad
''','PDF 11–14')
group(1,'Constitución: derechos fundamentales','¿Qué regula principalmente {key}?','¿Qué artículo reconoce {value}?','''
el artículo 14|Igualdad ante la ley sin discriminación
el artículo 15|Vida, integridad y prohibición de tortura
el artículo 16|Libertad ideológica, religiosa y de culto
el artículo 17|Libertad y seguridad, con garantías de detención
el artículo 18|Honor, intimidad, imagen, domicilio y comunicaciones
el artículo 19|Residencia, circulación y entrada o salida de España
el artículo 20|Expresión e información veraz
el artículo 21|Reunión pacífica y sin armas
el artículo 22|Asociación
el artículo 23|Participación política y acceso a cargos públicos
el artículo 24|Tutela judicial y garantías procesales
el artículo 25|Legalidad penal y sancionadora
el artículo 26|Prohibición de tribunales de honor civiles y profesionales
el artículo 27|Educación y libertad de enseñanza
el artículo 28|Libertad sindical y huelga
el artículo 29|Petición individual o colectiva por escrito
''','PDF 14–23')
group(1,'Constitución: deberes y derechos de ciudadanía','¿Qué materia corresponde a {key}?','¿Qué precepto de la sección segunda se refiere a {value}?','''
el artículo 30|Defensa de España y objeción de conciencia
el artículo 31|Contribución tributaria y gasto público
el artículo 32|Matrimonio en igualdad jurídica
el artículo 33|Propiedad, herencia y expropiación
el artículo 34|Fundaciones de interés general
el artículo 35|Trabajo y remuneración sin discriminación por sexo
el artículo 36|Colegios profesionales
el artículo 37|Negociación colectiva y conflicto colectivo
el artículo 38|Libertad de empresa en economía de mercado
''','PDF 21–24')
group(1,'Constitución: principios rectores','¿Qué política recoge {key}?','¿Qué artículo de los principios rectores regula {value}?','''
el artículo 39|Protección de familia e hijos
el artículo 40|Empleo, formación, seguridad laboral y descanso
el artículo 41|Régimen público de Seguridad Social
el artículo 42|Protección de trabajadores españoles en el extranjero
el artículo 43|Protección de la salud
el artículo 44|Acceso a cultura e investigación científica
el artículo 45|Medio ambiente y deber de conservación
el artículo 46|Patrimonio histórico, cultural y artístico
el artículo 47|Vivienda digna y regulación del suelo
el artículo 48|Participación de la juventud
el artículo 49|Autonomía, inclusión y accesibilidad de personas con discapacidad
el artículo 50|Pensiones y servicios para mayores
el artículo 51|Defensa de consumidores y usuarios
el artículo 52|Organizaciones profesionales democráticas
''','PDF 24–27')
group(1,'Constitución: garantías y conceptos','¿Qué descripción corresponde a {key}?','¿Qué concepto constitucional se define por {value}?','''
la parte dogmática|Título preliminar y título I
la parte orgánica|Títulos II a X
la tutela del artículo 53.2|Preferencia y sumariedad, y amparo para los derechos protegidos
la protección del artículo 53.3|Alegación de principios rectores según leyes de desarrollo
el Defensor del Pueblo|Alto comisionado de las Cortes Generales, independiente
la suspensión general del artículo 55|Suspensión de derechos enumerados en excepción o sitio
la suspensión individual del artículo 55|Derechos de los arts. 17.2 y 18.2–18.3 en investigaciones de terrorismo, con controles
la reforma ordinaria citada en el manual|Procedimiento del artículo 167, mayoría de tres quintos
''','PDF 6–11 y 27–33')

group(2,'Igualdad: conceptos básicos','¿Qué significa {key}?','¿Qué concepto se describe como {value}?','''
sexo|Características biológicas
 género|Construcción social de roles y expectativas
igualdad formal|Reconocimiento normativo de igualdad
igualdad efectiva|Igualdad real de oportunidades y eliminación de obstáculos
estereotipo de género|Creencia generalizada sobre cómo deben ser mujeres y hombres
rol de género|Función social atribuida según el género
brecha de género|Diferencia observable en acceso, participación o resultados
transversalidad|Integración de igualdad en todas las políticas y fases
''','PDF 33–40')
group(2,'Igualdad: discriminación y protección','¿Qué caracteriza a {key}?','¿Qué concepto corresponde a {value}?','''
la discriminación directa|Trato menos favorable por sexo en situación comparable
la discriminación indirecta|Criterio neutro con desventaja particular sin justificación legítima y proporcionada
el acoso sexual|Conducta de naturaleza sexual que atenta contra dignidad por propósito o efecto
el acoso por razón de sexo|Conducta basada en sexo, sin necesitar contenido sexual
la discriminación por embarazo o maternidad|Discriminación directa por razón de sexo
la indemnidad|Protección frente a represalias por reclamar igualdad
la acción positiva|Medida razonable y proporcionada para corregir desigualdad de hecho mientras subsista
la discriminación interseccional|Interacción de varios motivos que genera desventaja específica
''','PDF 33–46')
group(2,'Igualdad: normas principales','¿Cuál es el objeto de {key}?','¿Qué norma se identifica por {value}?','''
LO 3/2007, de 22 de marzo|Igualdad efectiva de mujeres y hombres
LO 1/2004, de 28 de diciembre|Protección integral frente a violencia de género de pareja o expareja
Ley 12/2007, de 26 de noviembre|Promoción de igualdad de género en Andalucía
Ley 13/2007, de 26 de noviembre|Prevención y protección integral frente a violencia contra mujeres en Andalucía
''','PDF 38–41 y 55–56 y 102–103')
group(2,'LO 3/2007: artículos iniciales','¿Qué regula {key} de la LO 3/2007?','¿A qué artículo de la LO 3/2007 corresponde {value}?','''
el artículo 6|Discriminación directa e indirecta
el artículo 7|Acoso sexual y acoso por razón de sexo
el artículo 8|Discriminación por embarazo o maternidad
el artículo 9|Indemnidad frente a represalias
el artículo 10|Consecuencias jurídicas de conductas discriminatorias
el artículo 11|Acciones positivas
el artículo 12|Tutela judicial efectiva
el artículo 13|Carga de la prueba, con excepción penal
el artículo 14|Criterios generales de actuación de poderes públicos
el artículo 15|Transversalidad del principio de igualdad
el artículo 16|Nombramientos con presencia equilibrada
el artículo 17|Plan Estratégico de Igualdad de Oportunidades
el artículo 19|Informes de impacto de género
el artículo 20|Estadísticas y estudios con perspectiva de género
''','PDF 41–46')
group(2,'LO 3/2007: empleo','¿Qué establece {key}?','¿Qué instrumento laboral de la LO 3/2007 corresponde a {value}?','''
el artículo 43|Promoción de igualdad en negociación colectiva
el artículo 44|Conciliación y corresponsabilidad
el artículo 45|Obligación de planes de igualdad en empresas previstas
el artículo 46|Concepto, diagnóstico y contenidos de planes
el artículo 47|Transparencia en implantación del plan
el artículo 48|Prevención de acoso en trabajo, incluido entorno digital
el artículo 49|Apoyo a planes voluntarios en pequeñas y medianas empresas
el artículo 50|Distintivo empresarial de igualdad
''','PDF 49–52')
group(2,'LO 3/2007: empleo público','¿Qué contenido atribuye el manual a {key}?','¿Qué artículo de empleo público se vincula a {value}?','''
el artículo 51|Criterios de actuación administrativa como empleadora
el artículo 55|Impacto de género en convocatorias de acceso
el artículo 57|Protección de conciliación en valoración de méritos
el artículo 58|Riesgo durante embarazo y lactancia
el artículo 59|Vacaciones coincidentes con situaciones protegidas
el artículo 60|Preferencia formativa tras reincorporación y reserva para mujeres
el artículo 61|Formación y estudio de igualdad en acceso
el artículo 62|Protocolo frente a acoso sexual y por sexo
el artículo 63|Evaluación anual de igualdad en empleo público
el artículo 64|Plan de igualdad de AGE al inicio de legislatura
''','PDF 52–55')
group(2,'Igualdad: cifras y plazos','¿Qué cifra corresponde a {key}?','¿A qué regla corresponde la cifra {value}?','''
el mínimo de presencia equilibrada de cada sexo|40 %
el máximo de presencia equilibrada de cada sexo|60 %
el umbral de plantilla para plan empresarial obligatorio|50 personas trabajadoras
la preferencia formativa estatal tras reincorporación protegida|Un año
la periodicidad del plan integral andaluz contra violencia citada|Cinco años
el plazo sin financiación por prácticas discriminatorias recogido en Ley 12/2007|Cinco años desde condena o sanción firme
la multa máxima de infracción leve en Ley 12/2007|6.000 euros
el límite superior de multa grave en Ley 12/2007|60.000 euros
el límite superior de multa muy grave en Ley 12/2007|120.000 euros
la reducción de multa del artículo 84 en sus condiciones|30 %
''','PDF 35–36, 49–55, 60–61, 101–103', 'Se mantienen las cifras y condiciones de los apuntes; cada plazo se aplica únicamente a su supuesto.')
group(2,'LO 1/2004: derechos y órganos','¿Qué regula {key} de la LO 1/2004?','¿Qué artículo de la LO 1/2004 corresponde a {value}?','''
el artículo 18|Derecho a información accesible
el artículo 19|Asistencia social integral
el artículo 20|Asistencia jurídica
el artículo 21|Derechos laborales y de Seguridad Social
el artículo 22|Programa específico de empleo
el artículo 23|Acreditación de situaciones de violencia
el artículo 27|Ayuda económica en condiciones de renta y empleabilidad
el artículo 28|Acceso prioritario a vivienda y residencias públicas
el artículo 29|Delegación Especial del Gobierno contra violencia sobre mujer
el artículo 30|Observatorio Estatal de Violencia sobre la Mujer
el artículo 31|Fuerzas y Cuerpos de Seguridad
el artículo 32|Planes de colaboración institucional
''','PDF 57–66')
group(2,'Ley 12/2007: órganos y sanciones','¿Qué función se relaciona con {key}?','¿Qué órgano o instrumento corresponde a {value}?','''
el Instituto Andaluz de la Mujer en el art. 85|Imposición de sanciones leves
la consejería competente en igualdad en el art. 85|Imposición de sanciones graves
el Consejo de Gobierno en el art. 85|Imposición de sanciones muy graves
el Consejo Audiovisual de Andalucía en el art. 85|Competencia especial en infracciones de publicidad y medios previstas
la consejería de educación en el art. 85|Competencia especial en materiales educativos discriminatorios
el Observatorio de igualdad de género|Análisis e indicadores de igualdad en Andalucía
el Consejo Andaluz de Participación de las Mujeres|Participación y representación del movimiento de mujeres
las unidades de igualdad|Integración de perspectiva de género en cada ámbito administrativo
''','PDF 95–103')
group(2,'Ley 13/2007: protección y recursos','¿Qué contenido se asocia a {key}?','¿Qué recurso o medida de Ley 13/2007 corresponde a {value}?','''
la violencia física|Daño corporal o riesgo de producirlo
la violencia psicológica|Conductas que causan daño emocional o sometimiento
la violencia sexual|Atentados contra libertad sexual sin consentimiento
la violencia económica|Privación o control de recursos económicos en los términos de la ley
los centros de emergencia|Acogida y protección inmediata
las casas de acogida|Atención y recuperación con estancia más prolongada
los pisos tutelados|Alojamiento y autonomía en proceso de recuperación
la ventanilla única|Acceso coordinado a recursos y atención
''','PDF 103–126')
group(2,'Igualdad municipal: protocolo','¿Qué exige {key} del protocolo de acoso?','¿Qué principio o fase municipal corresponde a {value}?','''
la confidencialidad|Reserva de denuncia, investigación y datos personales
la indemnidad|Ausencia de represalias contra denunciante o testigos
la presunción de inocencia|No anticipar culpabilidad por denuncia o cautelar
la investigación|Recabar documentos y testimonios mediante responsables previstos
la resolución|Decidir medidas y actuaciones por órgano competente
la reparación|Restablecer condiciones y apoyar a persona afectada
la prevención|Formación, detección y compromiso de tolerancia cero
el seguimiento|Comprobar eficacia de medidas y evitar reiteración
''','PDF 129–132')

group(3,'PRL: definiciones del artículo 4','¿Qué definición corresponde a {key}?','¿Qué concepto preventivo significa {value}?','''
prevención|Medidas y actividades en todas las fases para evitar o disminuir riesgos
riesgo laboral|Posibilidad de sufrir daño derivado del trabajo
 daños derivados del trabajo|Enfermedades, patologías o lesiones con motivo u ocasión del trabajo
riesgo grave e inminente|Probabilidad de materialización inmediata con daño grave
proceso o producto potencialmente peligroso|Genera riesgo sin medidas preventivas específicas
 equipo de trabajo|Máquina, aparato, instrumento o instalación utilizada en trabajo
condición de trabajo|Característica del puesto o su organización que influye en riesgos
EPI|Equipo llevado o sujetado por persona para protegerla de riesgos
''','PDF 135–138')
group(3,'PRL: principios del artículo 15','¿Qué actuación ejemplifica {key}?','¿Qué principio preventivo se aplica al {value}?','''
evitar los riesgos|Eliminar un obstáculo antes de iniciar el trabajo
 evaluar los riesgos inevitables|Analizar probabilidad y gravedad de lo que no se puede eliminar
combatir en origen|Corregir la causa del peligro
adaptar trabajo a persona|Ajustar puesto y método para reducir carga repetitiva
considerar evolución técnica|Incorporar mejoras técnicas de seguridad
sustituir lo peligroso|Elegir alternativa de poco o ningún peligro
planificar la prevención|Integrar técnica, organización y condiciones sociales y ambientales
priorizar protección colectiva|Proteger el conjunto antes de recurrir sólo a equipos personales
dar instrucciones|Informar del procedimiento y límites del equipo
''','PDF 139–140')
group(3,'PRL: identificación de riesgos','En prevención, ¿cómo se clasifica {key}?','¿Qué ejemplo corresponde a {value}?','''
un cable atravesando una zona de paso|Condición que origina riesgo de caída
una lesión sufrida al caer trabajando|Daño derivado del trabajo
un guante protector utilizado por trabajador|Equipo de protección individual
una barrera fija de una máquina|Medida de protección colectiva
una destructora utilizada en oficina|Equipo de trabajo
la posibilidad de sufrir una caída en el puesto|Riesgo laboral
las medidas previstas antes y durante reparto|Actividad preventiva
un incendio con daño grave probable e inmediato|Riesgo grave e inminente
''','PDF 132–140')
group(3,'PRL: derechos y obligaciones','¿Qué regla se aplica a {key}?','¿A qué aspecto preventivo corresponde {value}?','''
el coste de las medidas preventivas|No debe recaer en personas trabajadoras
el empresario que contrata un servicio de prevención|Conserva su deber de protección eficaz
el convenio colectivo respecto al mínimo legal|Puede mejorar las garantías preventivas
la exposición inmediata a un agente peligroso|Puede ser grave e inminente aunque daño aparezca después
la gravedad del riesgo|Combina probabilidad y severidad
la entrada en zona de riesgo grave específico|Exige información suficiente del personal autorizado
la planificación frente a despistes|Debe prever distracciones o imprudencias no temerarias
una reparación eléctrica compleja de oficina|Corresponde a personal técnico competente
''','PDF 132–140')
group(3,'PRL: ámbito de aplicación','¿Cómo trata la Ley 31/1995 {key}?','¿A qué ámbito corresponde esta regla: {value}?','''
las relaciones laborales ordinarias|Aplicación de la normativa preventiva general
el personal administrativo o estatutario público|Aplicación con particularidades previstas
los socios trabajadores de cooperativas|Inclusión cuando prestan trabajo personal
actividades policiales cuyas particularidades impiden aplicar la ley|Regulación específica inspirada en principios preventivos
actividades militares de Fuerzas Armadas o Guardia Civil|Exclusión específica en términos del artículo 3
protección civil en grave riesgo o catástrofe incompatible con ley|Excepción por particularidades de actividad
los establecimientos militares|Aplicación con especialidades de normativa específica
los centros penitenciarios|Adaptación en los términos previstos
''','PDF 133–138')

group(4,'Atención: principios','¿Qué actuación aplica {key}?','¿Qué principio de atención se refleja en {value}?','''
la eficacia|Resolver la necesidad evitando demoras y desplazamientos innecesarios
la claridad|Utilizar lenguaje comprensible y sin tecnicismos innecesarios
la igualdad y accesibilidad|Adaptar atención sin discriminar por discapacidad u otra circunstancia
la neutralidad e imparcialidad|Evitar prejuicios y favoritismos
la confidencialidad|Proteger datos personales y expedientes reservados
la escucha activa|Dejar terminar, reformular y comprobar comprensión
la asertividad|Expresar límites con firmeza respetuosa
la eficiencia|Obtener objetivos con buena gestión de recursos
''','PDF 140–144 y 162–164')
group(4,'Atención: tipos y canales','¿Qué caracteriza a {key}?','¿Qué modalidad de atención corresponde a {value}?','''
la información general|Se facilita sin acreditar condición de interesado
la información particular|Estado de expediente concreto para interesado o representante identificado
la atención presencial|Interacción directa en oficina o registro
la atención telefónica|Identificación del centro y modulación clara de voz
la atención electrónica|Acceso por sede y medios telemáticos previstos
la queja de funcionamiento|Expresa insatisfacción, no es recurso ni interrumpe plazo para recurrir
la sugerencia|Propone mejora del servicio
el recurso administrativo|Impugna un acto por cauce legal previsto
''','PDF 142–150')
group(4,'Atención: funciones del RD 208/1996','¿En qué consiste {key}?','¿Qué función de atención corresponde a {value}?','''
recepción y acogida|Facilitar primera orientación e identificar necesidad
orientación e información|Explicar dónde y cómo realizar gestiones
 gestiones sencillas|Actuar dentro de atribuciones de tramitación material
recepción de iniciativas|Recoger propuestas de mejora
recepción de quejas|Canalizar insatisfacción por retrasos o desatenciones
asistencia en petición|Ayudar al ejercicio de petición por cauce correspondiente
tratamiento de información|Mantener y difundir datos administrativos disponibles
coordinación informativa|Interconectar unidades y actualizar datos entre ellas
''','PDF 144–150')
group(4,'Atención: comunicación','¿Qué elemento caracteriza {key}?','¿Qué tipo o técnica de comunicación corresponde a {value}?','''
la comunicación verbal|Palabras habladas o escritas
la comunicación no verbal|Gestos, postura, mirada y distancia
la comunicación paraverbal|Tono, volumen, ritmo y pausas
el disco rayado|Repetir serenamente un límite o mensaje esencial
el banco de niebla|Reconocer parte del sentimiento sin aceptar exigencia improcedente
el aplazamiento|Posponer diálogo cuando no puede mantenerse adecuadamente
la fase de empatía|Reconocer y resumir el malestar tras disminuir hostilidad
la fase de solución|Ofrecer alternativas concretas y viables
''','PDF 162–164')
group(4,'Ley 39/2015: artículos del título II','¿Qué regula {key} de la Ley 39/2015?','¿Qué artículo de la Ley 39/2015 se refiere a {value}?','''
el artículo 13|Derechos de personas en relaciones con Administraciones
el artículo 14|Derecho y obligación de relación electrónica
el artículo 15|Lengua de procedimientos
el artículo 16|Registros
el artículo 17|Archivo de documentos
el artículo 18|Colaboración de personas
el artículo 19|Comparecencia
el artículo 20|Responsabilidad de tramitación
el artículo 21|Obligación de resolver
el artículo 22|Suspensión del plazo máximo
el artículo 23|Ampliación del plazo máximo para resolver y notificar
el artículo 24|Silencio en procedimientos iniciados a solicitud
el artículo 25|Falta de resolución en procedimientos de oficio
el artículo 26|Documentos administrativos
el artículo 27|Copias auténticas
el artículo 28|Documentos aportados por interesados
''','PDF 150–162')
group(4,'Relación electrónica: sujetos','¿Qué regla aplica a {key}?','¿Qué sujeto se relaciona con esta regla electrónica: {value}?','''
una persona física no obligada|Puede elegir canal y cambiarlo en los términos legales
una persona jurídica|Está obligada a relación electrónica del artículo 14.2
una entidad sin personalidad jurídica|Está incluida entre obligadas del artículo 14.2
un profesional de colegiación obligatoria actuando profesionalmente|Debe usar canal electrónico en su actividad profesional
un representante de un obligado electrónico|Debe usar canal electrónico por representación
un empleado público en trámite por su condición|Usa medios electrónicos en forma determinada reglamentariamente
un grupo de personas físicas con acceso acreditado por capacidad técnica o económica|Puede quedar obligado por disposición reglamentaria en trámites previstos
un notario o registrador actuando como tal|Figura expresamente en profesionales del artículo 14.2
''','PDF 150–151')
group(4,'Procedimiento: documentos y constancias','¿Qué dato o efecto corresponde a {key}?','¿Qué elemento administrativo tiene esta función: {value}?','''
el recibo automático de registro|Acredita presentación, número, fecha, hora y anexos
la signatura archivística|Permite localizar unidad documental
la copia auténtica administrativa|Tiene eficacia del original cuando reúne requisitos legales
el código seguro de verificación|Permite contrastar autenticidad de copia por acceso previsto
los metadatos del documento|Aportan identificación y contexto electrónico
el archivo electrónico único|Conserva documentos de procedimientos finalizados
la digitalización de papel en OAMR|Permite registro electrónico y devolución de originales salvo excepción
la declaración responsable|Documento del interesado con manifestaciones y responsabilidad previstas
''','PDF 151–162')
group(4,'Atención: supuestos de mostrador','{key} ¿Qué actuación procede?','¿En qué supuesto resulta adecuada esta actuación: {value}?','''
Una persona pide horario y sede de un servicio.|Informar con carácter general sin exigir legitimación de interesado
Un vecino pide datos del expediente reservado de otra persona sin representación.|No revelar información particular y derivar al cauce autorizado
Una persona desea quejarse por la demora de la cola.|Facilitar formulario y remitir queja a unidad competente
Una persona exige que el subalterno conceda una subvención.|Explicar límites del puesto y derivar al órgano decisor
Una persona empieza a gritar en el pico de hostilidad.|Escuchar sin confrontar y mantener tono sereno
Un usuario no comprende tecnicismos del impreso.|Reformular con palabras sencillas y comprobar comprensión
Una persona con dificultad de acceso solicita ayuda.|Adaptar atención y facilitar acceso al servicio
Una persona pide comparecer obligatoriamente sin norma que lo imponga.|Recordar que comparecencia obligatoria exige previsión legal
''','PDF 140–164')

group(5,'Actos: artículos de Ley 39/2015','¿Qué regula {key}?','¿Qué artículo se corresponde con {value}?','''
el artículo 34|Producción y contenido de actos
el artículo 35|Motivación
el artículo 36|Forma
el artículo 37|Inderogabilidad singular de reglamentos
el artículo 38|Ejecutividad
el artículo 39|Efectos y presunción de validez
el artículo 40|Contenido y plazo de notificación
el artículo 41|Condiciones generales de notificación
el artículo 42|Práctica de notificación en papel
el artículo 43|Práctica electrónica
el artículo 44|Notificación infructuosa
el artículo 45|Publicación
el artículo 46|Protección de derechos en publicación
el artículo 47|Nulidad de pleno derecho
el artículo 48|Anulabilidad
el artículo 49|Límites a extensión de invalidez
el artículo 50|Conversión de actos viciados
el artículo 51|Conservación de actos y trámites
el artículo 52|Convalidación
''','PDF 170–177')
group(5,'Notificaciones: plazos y condiciones','¿Qué condición numérica corresponde a {key}?','¿A qué regla de notificación corresponde {value}?','''
el plazo para cursar notificación desde dictado|Diez días
el tiempo para repetir un intento domiciliario fallido|Dentro de los tres días siguientes
el número de repeticiones ordinarias tras primer intento fallido|Una sola vez
la separación mínima entre horas de intentos|Tres horas
el punto horario que separa los dos intentos|15:00 horas
el rechazo por no acceder cuando medio electrónico es obligatorio o elegido|Diez días naturales desde puesta a disposición
la edad del receptor domiciliario distinto del interesado|Mayor de catorce años, presente e identificado
el dato temporal que prevalece si hay varias notificaciones válidas|Fecha de la primera notificación practicada
''','PDF 166–177')
group(5,'Notificaciones: documentos y canales','¿Qué función corresponde a {key}?','¿Qué medio o documento corresponde a {value}?','''
el aviso por correo o dispositivo|Informa de puesta a disposición sin ser notificación
la sede electrónica|Permite comparecencia identificada y acceso al contenido
la dirección electrónica habilitada única|Medio electrónico previsto junto con sede
el anuncio en BOE del artículo 44|Notifica cuando destinatario, lugar o entrega resultan infructuosos
la publicación en proceso selectivo|Tiene efectos según medio señalado en convocatoria
el texto íntegro del acto|Elemento indispensable del contenido de notificación
la constancia del rechazo expreso|Permite dar trámite por efectuado y continuar
el documento con cheque u otro medio de pago|No se notifica electrónicamente en el supuesto del artículo 41
''','PDF 164–176')
group(5,'Invalidez: conceptos','¿Qué efecto caracteriza a {key}?','¿Qué figura administrativa corresponde a {value}?','''
la nulidad por incompetencia manifiesta|Afecta incompetencia por materia o territorio
la anulabilidad por defecto formal|Requiere requisito indispensable o indefensión
la desviación de poder|Es causa de anulabilidad
la convalidación|Subsana vicio de un acto anulable
la conversión|Un acto inválido produce efectos de otro cuyos elementos contiene
la conservación|Mantiene trámites cuyo contenido habría sido igual
la invalidez parcial|No se extiende a partes independientes salvo relación esencial
la inderogabilidad singular|Un acto particular no puede vulnerar reglamento aunque proceda de órgano superior
''','PDF 168–177')
group(5,'Notificaciones: supuestos','{key} ¿Qué procede?','¿Qué situación se resuelve con esta actuación: {value}?','''
Primer intento en domicilio a las 10:00 sin receptor.|Repetir una vez en tres días siguientes, después de 15:00, con separación horaria mínima
Segundo intento domiciliario también fallido.|Aplicar anuncio en BOE del artículo 44
El destinatario electrónico accede al contenido identificado.|Tener por practicada notificación en el momento de acceso
Obligado electrónico no accede durante diez días naturales.|Entender rechazada la notificación en condiciones del artículo 43
Interesado o representante rechaza expresamente recibir.|Documentar rechazo y continuar procedimiento
Notificación contiene texto íntegro pero omite recursos.|Aplicar efectos desde actuación que revela conocimiento o recurso, según artículo 40.3
Publicación completa puede lesionar derechos legítimos.|Publicar indicación limitada y lugar/plazo para conocer texto íntegro
Sólo se ha enviado un SMS informativo.|No confundir ese aviso con notificación del contenido
''','PDF 164–177')

group(6,'Ayuntamiento: áreas de coordinación','¿Quién coordina {key}, según el decreto del manual?','¿Qué área coordina {value}, según los apuntes?','''
I. Presidencia y Relaciones Institucionales|Pablo Otero Gallardo
II. Desarrollo Urbano Sostenible|José Manuel Cossi González
III. Gestión Económica y Administrativa|María Teresa González García-Negrotto
IV. Ciudadanía|Juan José Ortiz Quevedo
VI. Desarrollo Económico y Empleo|Beatriz Gandullo Sosa
VII. Medio Ambiente|José Carlos Teruel Bienvenido
''','PDF 177–182','El área V, Desarrollo Social, también corresponde a Pablo Otero; se evita inferir que coordina sólo una área.')
group(6,'Ayuntamiento: delegaciones','¿A quién asigna el manual {key}?','¿Qué delegación está asignada a {value} en estos apuntes?','''
Vivienda|Ana María Sanjuán Luna
Participación Ciudadana y Distritos|María Dolores Pavón Aragón
Igualdad, inclusión LGTBI y mayores|Virginia Martín García
Salud, juventud e infancia|Gloria María Bazán Zambrana
Accesibilidad|Nuria María Álvarez López
Movilidad y Hermandades|José Manuel Verdulla Otero
Deporte|Carlos Lucero Román
Carnaval y Fiestas|Beatriz Gandullo Sosa
''','PDF 177–182')
group(6,'Ayuntamiento: tenientes del tema 6','¿Qué rango indica el tema 6 para {key}?','¿A quién corresponde el rango {value} en el tema 6?','''
José Manuel Cossi González|Primer teniente
María Teresa González García-Negrotto|Segunda teniente
Juan José Ortiz Quevedo|Tercer teniente
Pablo Otero Gallardo|Cuarto teniente
Beatriz Gandullo Sosa|Quinta teniente
José Carlos Teruel Bienvenido|Sexto teniente
''','PDF 177–182','Se cita específicamente el tema 6; el tema 10 menciona otra cifra global de tenientes.')
group(6,'Ayuntamiento: áreas y materias','¿En qué área se incluye {key}?','¿Qué materia del listado pertenece a {value}?','''
Presidencia y Comunicación|Área I
Urbanismo y Vivienda|Área II
Economía, Hacienda y Función Pública|Área III
Seguridad, Cultura y Carnaval|Área IV
Asuntos Sociales e Igualdad|Área V
Empleo, Turismo y Comercio|Área VI
Limpieza, Playas y Accesibilidad|Área VII
''','PDF 177–182')
group(6,'Ayuntamiento: sedes municipales','¿Dónde sitúa el manual {key}?','¿Qué servicio se ubica en {value}, según los apuntes?','''
Casa Consistorial|Plaza San Juan de Dios, s/n
Participación, edificio Amaya|Plaza San Juan de Dios, 11
Policía Local y Protección Civil|Plaza San Juan de Puerto Rico, s/n
Urbanismo, Casa de los Lilas|Calle Sopranis, 10
Igualdad y Fundación Municipal de la Mujer|Plaza del Palillero
Juventud y Educación|Calle Cánovas del Castillo, 41
Fiestas, Turismo y Comercio|Cuesta de las Calesas, 39
Consumo|Calle García de Sola, 12–14
Servicios Sociales, La Laguna|Calle Conil de la Frontera, s/n
Servicios Sociales, Barriada de la Paz|Avenida Guadalquivir, s/n, frente al 22
Centro Hermanas Mirabal|Plaza Real Hospital de la Segunda Aguada, s/n
Servicios Sociales, centro|Calle Isabel la Católica, 12
Archivo Municipal, referencia del tema 10|Calle Isabel la Católica, 13
Medio Ambiente e informática municipal|Avenida María Auxiliadora, 4
Fundación Municipal de Cultura, referencia del tema 6|Avenida Juan Carlos I, s/n
''','PDF 182–193 y 302–332','Las direcciones corresponden al manual de septiembre de 2026, sin actualización externa.')
group(6,'Ayuntamiento: otras administraciones','¿Dónde se encuentra {key}, según el tema 6?','¿Qué institución del listado se asocia a {value}?','''
Diputación Provincial|Plaza de España, s/n
Autoridad Portuaria|Plaza de España, 17
Consorcio Zona Franca|Avenida de la Ilustración, s/n, recinto interior
Rectorado de UCA en el tema 6|Calle Ancha, 16
Facultad de Medicina|Plaza Fragela
Facultad de Filosofía y Letras|Avenida Doctor Gómez Ulla
Subdelegación del Gobierno|Avenida de Andalucía, 3
Hospital Puerta del Mar|Avenida Ana de Viya, 21
Delegaciones territoriales de Junta|Plaza de Asdrúbal
Colegio de Médicos|Calle Benjumeda
''','PDF 185–193','Para Rectorado se pregunta expresamente la referencia del tema 6; el tema 10 cita Paseo Carlos III.')
group(6,'Ayuntamiento: funciones y naturaleza','¿Qué función caracteriza a {key}?','¿Qué órgano o unidad del listado corresponde a {value}?','''
Alcaldía|Dirección y representación municipal
Pleno|Control del gobierno y acuerdos de ordenanzas y presupuesto
Junta de Gobierno Local|Asistencia a Alcaldía y competencias delegadas o atribuidas
Tenientes de alcalde|Sustitución del alcalde por orden en supuestos previstos
Secretaría General|Fe pública y asesoramiento legal preceptivo
Intervención|Control económico-financiero
Tesorería|Gestión de cobros y pagos
Registro y OAMR|Presentación y asistencia en registro de documentos
Estadística y Padrón|Gestión padronal y datos poblacionales
Conserjería|Custodia material, accesos y apoyo operativo
''','PDF 177–193 y 302–312')
group(6,'Ayuntamiento: organismos del manual','¿Qué ámbito identifica a {key}?','¿Qué entidad municipal se vincula a {value}?','''
FMM|Políticas de igualdad y mujer
FMC|Cultura municipal
IMD|Deporte municipal
IFEF|Fomento, empleo y formación
Patronato del COAC y Fiestas del Carnaval|Concurso y logística festiva del Carnaval
PROCASA|Vivienda municipal
Aguas de Cádiz, ACASA|Servicio de agua
Eléctrica de Cádiz|Suministro eléctrico
''','PDF 177–193 y 306–312','FMM, FMC, IMD, IFEF y Patronato son los autónomos que enumera el tema 10; no se sustituye su clasificación con noticias.')
group(6,'Ayuntamiento: datos organizativos','¿Qué dato corresponde a {key}?','¿A qué dato municipal de los apuntes corresponde {value}?','''
el decreto organizativo citado|2023/3402
la firma del decreto organizativo|22 de junio de 2023
la eficacia del decreto organizativo|23 de junio de 2023
el número de áreas coordinadas|Siete áreas
el número de integrantes del Pleno en el tema 10|27 miembros
los miembros del equipo de gobierno en el tema 10|14 concejales
la sesión ordinaria del Pleno citada|Último jueves de mes a las 10:30
el máximo de concejales de Junta para corporación de 27|Nueve, además del alcalde
''','PDF 177–182 y 306–312')

group(7,'Archivo: clases documentales','¿Qué función corresponde a {key}?','¿Qué clase documental corresponde a {value}?','''
los documentos de decisión|Expresar una decisión: resolución, decreto o acuerdo
los documentos de transmisión|Comunicar: notificación, publicación, oficio o nota interior
los documentos de constancia|Acreditar hechos: acta, certificado o diligencia
los documentos de juicio|Emitir valoración: informe o dictamen
los documentos del ciudadano|Solicitar, alegar, recurrir o comunicar por cauce previsto
''','PDF 193–197')
group(7,'Archivo: tipos de documento','¿Qué finalidad específica tiene {key}?','¿Qué documento del listado corresponde a {value}?','''
una resolución|Expresar una decisión administrativa
un oficio|Transmitir información entre órganos
una nota interior|Transmitir información dentro de organización
un acta|Dejar constancia de una sesión o hechos
un certificado|Acreditar extremos por persona habilitada
una diligencia|Hacer constar una actuación material o trámite
un informe|Aportar juicio técnico o jurídico
una solicitud|Pedir actuación al órgano competente
un recurso|Impugnar un acto administrativo
una alegación|Exponer argumentos dentro de procedimiento
''','PDF 193–199')
group(7,'Archivo: fases y edades orientativas','¿Qué rango utiliza el manual para {key}?','¿Qué fase documental se asocia a {value}?','''
el archivo de oficina o gestión|0–5 años, documentación activa
el archivo central|5–15/30 años, documentación semiactiva
el archivo intermedio|15/30–50 años, valoración y uso bajo
el archivo histórico|Más de 50 años, conservación permanente
''','PDF 194–196','Las edades son orientativas: no autorizan por sí solas eliminar documentos.')
group(7,'Archivo: organización','¿Qué significa {key}?','¿Qué concepto archivístico corresponde a {value}?','''
el principio de procedencia|No mezclar documentos de distintos productores
el orden original|Respetar organización derivada de actividad productora
la clasificación|Asignar documentos a serie o grupo del cuadro
la ordenación|Determinar secuencia dentro de cada clase
la instalación|Colocar e identificar unidades en carpetas, cajas y estantes
la foliación|Numerar correlativamente hojas, no páginas
la transferencia|Trasladar custodia con relación y control
el expurgo autorizado|Seleccionar y eliminar tras valoración competente
la signatura|Código de localización física o unidad documental
el desglose|Retirada autorizada de documento con diligencia
''','PDF 197–203')
group(7,'Archivo: sistemas de ordenación','¿Qué criterio define {key}?','¿Qué sistema de ordenación corresponde a {value}?','''
el alfabético|Apellidos y nombre, con tratamiento previsto de partículas
el cronológico|Año, mes y día
el numérico|Número de expediente o asiento
el temático|Materia del documento
el alfanumérico|Combinación de letras y números, como URB-2026-0054
''','PDF 197–203')
group(7,'Archivo: préstamo y consulta','¿Qué función cumple {key}?','¿Qué instrumento o medida archivística corresponde a {value}?','''
el vale de préstamo|Constancia firmada de salida y destino
la tarjeta testigo|Sustituye expediente prestado en su ubicación
el registro de devolución|Confirma retorno, fecha e integridad
el inventario de transferencia|Relaciona series, fechas, cajas y signaturas trasladadas
la autorización de consulta|Delimita acceso de interesado, representante o tercero
la reproducción supervisada|Facilita copia permitida sin dañar original
la revisión del vencimiento de préstamo|Permite reclamar o renovar conforme a instrucciones
la copia auténtica|Requiere competencia y requisitos, no sello informal del subalterno
''','PDF 200–207')
group(7,'Archivo: conservación material','¿Qué regla se aplica a {key}?','¿A qué medida de conservación corresponde {value}?','''
la separación de cajas respecto al suelo|Al menos diez centímetros, según manual
los pasillos del depósito|Mantenerlos despejados sin bloquear salidas
la temperatura y humedad|Evitar variaciones y exceso de humedad
los documentos frágiles|Manipulación cuidadosa y medios especializados
los elementos metálicos oxidados|Retirada o sustitución conforme a instrucciones
la eliminación de un expediente antiguo|Necesita valoración y autorización, no sólo antigüedad
la devolución de expediente prestado|Comprobar integridad y recolocar en signatura
los datos personales en consulta|Aplicar límites y protección, no acceso indiscriminado
''','PDF 199–207')

group(8,'Ortografía: reglas de acentuación','¿Qué regla se aplica a {key}?','¿Qué clase o caso ortográfico responde a {value}?','''
las palabras agudas|Tilde cuando terminan en vocal, n o s
las palabras llanas|Tilde cuando no terminan en vocal, n o s
las palabras esdrújulas|Tilde siempre
la palabra Cádiz|Llana acabada en z y con tilde
la palabra examen|Llana acabada en n y sin tilde
la palabra exámenes|Esdrújula y con tilde
la palabra guion según manual|Monosílaba ortográfica y sin tilde
la palabra día|Hiato con vocal débil tónica y tilde
''','PDF 221–224')
group(8,'Ortografía: abreviaturas','¿Cuál es la forma correcta de {key}?','¿Qué expresión se abrevia {value}?','''
artículo|art.
página|pág.
número con letra volada|n.º
departamento|dpto.
administración|admón.
firmado|fdo.
señor|Sr.
señora|Sra.
don|D.
doña|D.ª
excelentísimo|Excmo.
ilustrísimo|Ilmo.
visto bueno|V.º B.º
sin número|s/n
cuenta corriente|c/c
''','PDF 214–220')
group(8,'Ortografía: acortamientos','¿Qué rasgo caracteriza a {key}?','¿Qué recurso ortográfico corresponde a {value}?','''
la abreviatura por truncamiento|Suprime final de palabra, como art.
la abreviatura por contracción|Suprime letras interiores, como dpto.
la sigla|Iniciales sin puntos ni plural escrito con s
el acrónimo lexicalizado|Se lee como palabra y sigue ortografía ordinaria
el símbolo de unidad|Forma convencional sin punto abreviativo ni plural
la letra volada en abreviatura|Va después del punto abreviativo
la duplicación de iniciales abreviadas|Forma plurales como EE. UU. con punto y espacio
la abreviatura con barra|No añade punto abreviativo, como s/n
''','PDF 212–222')
group(8,'Ortografía: usos administrativos','¿Qué escritura prescribe el manual para {key}?','¿A qué caso de redacción administrativa corresponde {value}?','''
los cargos como alcalde o concejal|Minúscula como nombres comunes
los días, meses y estaciones|Minúscula ordinaria
el nombre Ayuntamiento de Cádiz|Mayúsculas en denominación institucional
la acentuación de mayúsculas|Mantener tilde cuando corresponda
el año 2026|Sin punto de separación de millares
el título de un documento|Sin punto final
la separación de sujeto y verbo|Sin coma, salvo inciso correctamente delimitado
la datación en Cádiz|Coma entre ciudad y fecha
el EXPONE o SOLICITA del modelo|Dos puntos y nuevo párrafo con mayúscula
el plural de DNI|Los DNI, sin s ni apóstrofo
''','PDF 222–232')

group(9,'Informática: programas','¿Qué clase de programa es {key}?','¿Qué programa del listado corresponde a {value}?','''
Windows|Sistema operativo de Microsoft
Linux|Sistema operativo del ecosistema GNU/Linux
macOS|Sistema operativo de equipos Mac
Word|Procesador de textos de Microsoft
Writer|Procesador de textos de LibreOffice
Excel|Hoja de cálculo de Microsoft
Calc|Hoja de cálculo de LibreOffice
Access|Gestor de bases de datos de Microsoft
PowerPoint|Presentaciones de Microsoft
Impress|Presentaciones de LibreOffice
''','PDF 232–241')
group(9,'Informática: componentes','¿Qué función corresponde a {key}?','¿Qué componente cumple esta función: {value}?','''
hardware|Elementos físicos del equipo
software|Programas e instrucciones lógicas
firmware|Programación incorporada al dispositivo
unidad de control|Dirigir ejecución de instrucciones de CPU
ALU|Realizar cálculo y comparación lógica
registros de CPU|Guardar datos inmediatos de procesamiento
memoria RAM|Lectura y escritura volátil para trabajo de programas
memoria ROM|Memoria no volátil de lectura en explicación del manual
memoria caché|Acceso muy rápido entre CPU y RAM
HDD|Almacenamiento magnético con platos
SSD|Almacenamiento flash sin piezas móviles
controlador o driver|Comunicación entre sistema operativo y dispositivo
''','PDF 232–238')
group(9,'Informática: unidades','¿Qué mide o representa {key}?','¿Qué unidad o concepto corresponde a {value}?','''
bit|Valor binario 0 o 1
byte|Conjunto de ocho bits
KB en escala del manual|1.024 bytes
MB en escala del manual|1.024 KB
GB en escala del manual|1.024 MB
GHz|Frecuencia de reloj
píxel|Elemento de imagen digital
ppm|Velocidad en páginas por minuto
ppp o dpi|Resolución en puntos por pulgada
pulgada|2,54 centímetros
''','PDF 235–238')
group(9,'Informática: extensiones','¿Con qué tipo de archivo se relaciona {key}?','¿Qué extensión se asocia a {value}?','''
.docx|Documento de Word
.odt|Documento de Writer
.xlsx|Hoja de Excel
.ods|Hoja de Calc
.pptx|Presentación de PowerPoint
.pdf|Documento de distribución estable
.jpg|Imagen fotográfica comprimida
.png|Imagen que admite transparencia
.zip|Archivo comprimido
.exe|Ejecutable, ejemplo bloqueado como adjunto
''','PDF 238–241 y 295–298')
group(9,'Informática: redes y hojas de cálculo','¿Qué significa {key}?','¿Qué concepto informático corresponde a {value}?','''
LAN|Red de un área reducida como oficina o edificio
MAN|Red de alcance de una ciudad o municipio
WAN|Red de gran extensión geográfica
intranet|Red privada interna de organización
Internet|Red pública global
sede electrónica|Dirección oficial para trámites ciudadanos con garantías
celda|Intersección de columna y fila
rango|Conjunto de celdas como A1:A10
fórmula de hoja de cálculo|Expresión que comienza por signo igual
SUMA|Función que agrega valores del rango indicado
''','PDF 239–241')
group(9,'Reprografía: partes de fotocopiadora','¿Qué función cumple {key}?','¿Qué componente de fotocopiadora corresponde a {value}?','''
el cristal de exposición|Superficie de colocación de original
el ADF|Alimentación automática de hojas originales
la bandeja de papel|Depósito de hojas para copias
la lámpara de exposición|Ilumina original para obtener imagen
el tambor fotosensible|Recibe imagen y es delicado al contacto
el tóner|Pigmento para formar imagen impresa
el fusor|Fija tóner con calor y presión
la bandeja de salida|Recoge copias terminadas
el panel de control|Permite elegir funciones y leer incidencias
los rodillos de transporte|Desplazan papel por recorrido de máquina
''','PDF 244–252')
group(9,'Reprografía: funciones y consumibles','¿Qué caracteriza a {key}?','¿Qué concepto de reprografía corresponde a {value}?','''
el alzado|Juegos completos ordenados 1-2-3, 1-2-3
la copia sin alzado|Páginas iguales agrupadas 1-1, 2-2, 3-3
el dúplex|Impresión a dos caras
la impresión láser|Uso de tóner
la inyección|Uso de tinta líquida
la impresión térmica|Uso de calor para producir imagen
el gramaje|Masa por unidad de superficie de papel
el cartucho OEM|Consumible original del fabricante
el cartucho compatible|Fabricado para ser utilizado sin ser original
el cartucho remanufacturado|Consumible recuperado y acondicionado
la cuatricromía CMYK|Cian, magenta, amarillo y negro
la fijación|Etapa de calor y presión del fusor
''','PDF 244–270')
group(9,'Reprografía: tamaños DIN A','¿Cuáles son las medidas de {key} en milímetros?','¿Qué tamaño DIN A tiene medidas {value} milímetros?','''
A0|841 × 1.189
A1|594 × 841
A2|420 × 594
A3|297 × 420
A4|210 × 297
A5|148 × 210
A6|105 × 148
''','PDF 255–270')
group(9,'Digitalización: formatos y herramientas','¿Qué caracteriza a {key}?','¿Qué herramienta o formato corresponde a {value}?','''
OCR|Reconocimiento de caracteres para obtener texto procesable
PDF/A|Formato orientado a conservación de documentos
TIFF|Formato de imagen de calidad según uso
JPEG|Compresión fotográfica con pérdida según ajuste
PNG|Imagen que admite transparencia
BMP|Imagen habitualmente de gran tamaño y sin compresión en manual
escáner cenital|Captura superior apropiada para libros en los apuntes
escáner de mano|Captura al desplazar dispositivo manualmente
escáner plano|Captura sobre cristal de apoyo
fax|Transmisión de imagen de documento por línea telefónica en equipo clásico
''','PDF 270–280')
group(9,'Máquinas auxiliares: componentes','¿Qué función corresponde a {key}?','¿Qué componente de máquina cumple esta función: {value}?','''
el yunque de grapadora|Dobla extremos de grapa
el cargador de grapadora|Aloja las grapas
el punzón de perforadora|Corta orificio al descender
la guía de perforadora|Centra hojas respecto a orificios
el depósito de perforadora|Recoge recortes de papel
la prensa de guillotina|Sujeta hojas durante corte
el protector de guillotina|Impide acceso a cuchilla en movimiento
el termostato de plastificadora|Controla temperatura y protege ante sobrecalentamiento
los rodillos térmicos|Aplican calor y presión a funda
el sensor de destructora|Detecta inserción o condiciones de uso
''','PDF 280–294')
group(9,'Máquinas auxiliares: seguridad','¿Qué precaución corresponde específicamente a {key}?','¿Para qué operación se prescribe {value}?','''
extraer papel atascado|Tirar suavemente en sentido natural de avance
iniciar limpieza permitida|Apagar, desconectar y esperar enfriamiento
introducir funda de plastificar|Borde cerrado o sellado primero
terminar trabajo con guillotina|Bloquear cuchilla mediante pestillo
destruir documentos con datos personales|Corte cruzado o microcorte, referencia P-4 o superior
eliminar expedientes en destructora|Autorización previa de eliminación documental
copiar documento encuadernado o delicado|Evitar forzar y utilizar soporte apropiado
sustituir componente eléctrico complejo|Avisar al servicio técnico competente
''','PDF 250–294')
group(9,'Correo: protocolos y campos','¿Qué función identifica a {key}?','¿Qué protocolo o campo corresponde a {value}?','''
SMTP|Enviar correo electrónico
POP3|Recibir y descargar según configuración
IMAP|Sincronizar buzón y carpetas en servidor
Para|Destinatarios principales
Cc|Copia visible para receptores
Cco|Copia oculta para no divulgar direcciones
Asunto|Identificación breve del motivo del mensaje
Firma corporativa|Identificación institucional del remitente
''','PDF 294–298')
group(9,'Correo: carpetas y riesgos','¿Qué caracteriza a {key}?','¿Qué carpeta o riesgo corresponde a {value}?','''
Bandeja de entrada|Mensajes recibidos
Borradores|Mensajes redactados todavía no enviados
Bandeja de salida|Mensajes pendientes de envío
Enviados|Mensajes que han salido, no prueba por sí sola lectura humana
Papelera|Mensajes eliminados sujetos a configuración y conservación
Spam|Correo no deseado
Phishing|Suplantación para robar claves o datos o inducir acciones
Adjunto ejecutable sospechoso|Contenido que no debe ejecutarse y debe consultarse por canal seguro
''','PDF 298–302')

group(10,'Cádiz: historia y fechas','¿Qué fecha corresponde a {key}, según el manual?','¿Qué hito gaditano se asocia a {value}?','''
la fundación fenicia de Gadir|Hacia 1100 a. C., siglo XII a. C.
la incorporación de Gades al ámbito romano|206 a. C.
la entrada en la etapa musulmana de Qādis|711
la reconquista por Alfonso X|1262
el traslado de Casa de la Contratación a Cádiz|1717
la maqueta de Cádiz del Museo de las Cortes|1777
la designación de Torre Tavira como vigía oficial|1778
el inicio de Casa Consistorial|1799
la Constitución de Cádiz, La Pepa|19 de marzo de 1812
el puente José León de Carranza|1969
el descubrimiento del Teatro Romano|1980
el puente de la Constitución de 1812|2015
''','PDF 302–305 y 313–326')
group(10,'Cádiz: nombres y protagonistas','¿Qué persona o denominación corresponde a {key}?','¿Qué hecho o elemento histórico se vincula a {value}?','''
la ciudad fenicia|Gadir
la ciudad romana|Gades
la ciudad musulmana|Qādis
el rey de la reconquista de 1262|Alfonso X el Sabio
el rey del traslado comercial de 1717|Felipe V
el realizador de la maqueta de 1777|Alfonso Jiménez
el rey que encargó la maqueta|Carlos III
el pintor del Juramento de las Cortes|Salvador Viniegra
el autor del inicio de Catedral Nueva|Vicente Acero
el arquitecto de Puerta de Tierra citado|Torcuato Cayón
el arquitecto de Casa Consistorial escrito en manual|Torcuato Benjumea
el pintor del techo del Falla|Felipe Abarzuza
''','PDF 313–326','Se conserva la grafía Torcuato Benjumea que aparece en los apuntes.')
group(10,'Cádiz: barrios y rasgos','¿Qué rasgo identifica {key}?','¿Qué barrio histórico corresponde a {value}?','''
El Pópulo|Núcleo medieval, tres arcos, Catedral Vieja y Teatro Romano
La Viña|Barrio marinero occidental, Caleta y Carnaval
Santa María|Flamenco, Santo Domingo y Virgen del Rosario
San Carlos|Trazado neoclásico, Plaza de España y Aduana
Mentidero y San Lorenzo|Entorno cultural y universitario de Fragela y Carlos III
''','PDF 302–305 y 316–320')
group(10,'Cádiz: espacios culturales y dirección','¿Dónde se encuentra {key}?','¿Qué equipamiento cultural corresponde a {value}?','''
Museo de las Cortes|Calle Santa Inés, 9
Museo de Cádiz|Plaza de Mina, 5
ECCO|Paseo Carlos III, s/n
Casa de Iberoamérica|Concepción Arenal, s/n
Centro de Arte Flamenco La Merced|Plaza de la Merced
Gran Teatro Falla|Plaza Fragela, s/n
Teatro del Títere La Tía Norica|Calle San Miguel, 15
Biblioteca Celestino Mutis|Calle San Miguel, 16–17
Sala Central Lechera|Plaza de Argüelles, s/n
Torre Tavira|Calle Marqués del Real Tesoro
''','PDF 319–326')
group(10,'Cádiz: patrimonio y contenido','¿Qué elemento identifica {key}?','¿En qué lugar del listado se encuentra o desarrolla {value}?','''
Museo de las Cortes|Maqueta de 1777 y lienzo del Juramento
Museo de Cádiz|Sarcófagos fenicios y pinturas de Zurbarán
ECCO|Colección de Costus, El Valle de los Caídos
Casa de Iberoamérica|Edificio de la Antigua Cárcel Real
Teatro del Títere La Tía Norica|Programación de títeres y marionetas
Sala Central Lechera|Teatro de vanguardia, danza y pequeño formato
Oratorio de San Felipe Neri|Cortes y Constitución de 1812
Catedral Nueva|Cúpula dorada y cripta de Falla y Pemán
Teatro Romano|Restos romanos descubiertos en El Pópulo
Yacimiento Gadir|Calles y viviendas fenicias bajo Tía Norica
''','PDF 319–326')
group(10,'Cádiz: características patrimoniales','¿Qué característica corresponde a {key}?','¿Qué monumento o lugar tiene este rasgo: {value}?','''
Casa Consistorial|Edificio neoclásico con Salón Isabelino en primera planta
Catedral Nueva|Inicio 1722 y terminación 1838, barroco y neoclásico
Catedral Vieja|Iglesia de Santa Cruz en El Pópulo, origen de Alfonso X
Oratorio de San Felipe Neri|Templo barroco de planta elíptica
Castillo de Santa Catalina|Planta estrellada al norte de Caleta
Castillo de San Sebastián|Islote unido por paseo Fernando Quiñones
Puerta de Tierra|Defensa del siglo XVIII y separación casco-extramuros
Torre Tavira|Cámara oscura y altura aproximada de 45 metros
Gran Teatro Falla|Neomudéjar, ladrillo rojo y arcos de herradura
Baluarte de la Candelaria|Fortificación marítima adaptada a actividades culturales
''','PDF 319–326')
group(10,'Cádiz: fiestas y actos','¿Qué lugar o fecha caracteriza a {key}?','¿Qué celebración o acto corresponde a {value}?','''
el pregón de Carnaval|Plaza de San Antonio
la Cabalgata Magna|Avenida de Andalucía y Puerta Tierra
la Cabalgata del Humor|Calles del casco antiguo
los carruseles de coros|Bateas por Mercado, Palillero y Candelaria
las callejeras o ilegales|No concursantes en Viña, Pópulo y Flores
la Noche de San Juan|23 de junio, quema de Juanillos
la Virgen del Carmen|16 de julio, tradición marinera y Caleta
la Virgen del Rosario|7 de octubre, patrona y Santo Domingo
la Cruz de Mayo|Altares florales en barrios históricos
Alcances|Festival de cine documental
FIT|Festival Iberoamericano de Teatro
Nocturnos de Verano|Música, danza y teatro en Baluarte de la Candelaria
''','PDF 327–332')
group(10,'Cádiz: geografía y cultura, cifras','¿Qué dato corresponde a {key}, según el manual?','¿Qué dato de los apuntes se identifica por {value}?','''
la superficie municipal|12,30 km²
la población del cuadro estadístico|118.048 habitantes
las mujeres de ese cuadro|62.123
los hombres de ese cuadro|55.925
el porcentaje aproximado de mayores de 65|23 %
las modalidades tradicionales del COAC|Cuatro: coros, comparsas, chirigotas y cuartetos
las categorías de edad del COAC|Infantil, juvenil y adulta
las fases del COAC|Preliminares, cuartos, semifinales y final
los arcos medievales del Pópulo|Pópulo, Rosa y Blancos
el material de la maqueta de Cádiz|Caoba y marfil
''','PDF 302–305 y 319–332','Son datos del temario de septiembre de 2026, no cifras actuales consultadas en Internet.')

# Relaciones adicionales que completan delegaciones y reglas específicas.
group(6,'Ayuntamiento: delegaciones complementarias','¿Quién tiene asignada {key} en el manual?','¿Qué delegación de este listado corresponde a {value}?','''
Comunicación|Juan José Ortiz Quevedo
Administración Electrónica, Transformación Digital y Transparencia|José Carlos Teruel Bienvenido
Fondos Europeos y Memoria Democrática|José Manuel Cossi González
Emprendimiento, Formación, Economía Azul e Industria|Carlos Lucero Román
Artesanía|Gloria María Bazán Zambrana
Parques y Jardines|María Dolores Pavón Aragón
Estrategia, Transformación y Desarrollo Sostenible|Ana María Sanjuán Luna
Asuntos Sociales y Familia|Pablo Otero Gallardo
''','PDF 177–182')

# Desambiguación de reglas: una opción debe identificar la categoría exacta.
for g in GROUPS:
    if g['section']=='Relación electrónica: sujetos':
        g['rows']=[
          ('una persona física no obligada','Elección de canal y posibilidad de cambio, salvo obligación legal'),
          ('una persona jurídica','Entidad con personalidad obligada por artículo 14.2 a)'),
          ('una entidad sin personalidad jurídica','Entidad sin personalidad obligada por artículo 14.2 b)'),
          ('un profesional con colegiación obligatoria en ejercicio profesional','Obligación profesional del artículo 14.2 c)'),
          ('un representante de obligado electrónico','Representación del sujeto obligado, artículo 14.2 d)'),
          ('un empleado público en trámite por su condición','Relación por condición de empleado, artículo 14.2 e)'),
          ('un grupo con acceso acreditado por capacidad técnica o económica','Posible obligación reglamentaria del artículo 14.3'),
        ]
        g['note']='Notarios y registradores están incluidos en profesionales del artículo 14.2 c).'
    if g['section']=='Ayuntamiento: áreas de coordinación':
        g['rows'].append(('V. Desarrollo Social','Pablo Otero Gallardo'))
    if g['section']=='Procedimiento: documentos y constancias':
        g['rows']=[r for r in g['rows'] if r[0]!='la signatura archivística']
    if g['section']=='Ortografía: reglas de acentuación':
        g['rows']=[
          ('las palabras agudas','Regla general de agudas: tilde si terminan en vocal, n o s'),
          ('las palabras llanas','Regla general de llanas: tilde si no terminan en vocal, n o s'),
          ('las palabras esdrújulas','Regla general de esdrújulas: tilde siempre'),
          ('la palabra Cádiz','Cádiz: llana acabada en z, con tilde'),
          ('la palabra examen','Examen: llana acabada en n, sin tilde'),
          ('la palabra exámenes','Exámenes: esdrújula, con tilde'),
          ('la palabra guion según manual','Guion: monosílaba ortográfica, sin tilde'),
          ('la palabra día','Día: hiato con vocal débil tónica, con tilde'),
        ]

group(8,'Ortografía: tilde diacrítica','¿Qué uso identifica {key}?','¿Qué forma corresponde a {value}?','''
él|Pronombre personal con tilde, frente a artículo el
tú|Pronombre con tilde, frente a posesivo tu
mí|Pronombre con tilde, frente a posesivo mi
sí|Afirmación o pronombre, frente a conjunción si
té|Bebida, frente a pronombre te
dé|Verbo dar, frente a preposición de
sé|Verbo saber o ser, frente a pronombre se
más|Cantidad, frente a conjunción mas con sentido de pero
qué interrogativo|Tilde en interrogación directa o indirecta
''','PDF 221–224')
group(8,'Ortografía: signos de puntuación','¿Qué función tiene {key}?','¿Qué signo corresponde a {value}?','''
el punto y coma|Separar elementos complejos que ya contienen comas
los dos puntos|Introducir enumeración, cita o bloque estructural
los paréntesis|Añadir aclaración o desarrollar sigla
los corchetes|Introducir aclaración en cita o dentro de paréntesis
el guion|Unir elementos o indicar intervalos
la raya|Delimitar incisos o intervenciones
las comillas|Marcar cita literal o denominación señalada
los signos de interrogación|Abrir y cerrar preguntas en español
''','PDF 227–232')
group(8,'Aritmética: conjuntos y propiedades','¿Qué rasgo define {key}?','¿Qué concepto aritmético corresponde a {value}?','''
los números naturales del manual|0, 1, 2, 3 y sucesivos no negativos
los enteros|Naturales, cero y negativos sin fracción
los racionales|Expresables como cociente de enteros con denominador no nulo
los irracionales|Decimales infinitos no periódicos, no cociente de enteros
el sistema decimal|Base diez y valor posicional
la propiedad distributiva|a × (b + c) = a × b + a × c
el elemento neutro de suma|Cero
el elemento neutro de producto|Uno
la división exacta|Resto cero
la división entera correcta|Dividendo = divisor × cociente + resto, con resto menor que divisor positivo
''','PDF 207–212')
