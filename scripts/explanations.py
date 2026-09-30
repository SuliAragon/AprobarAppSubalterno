"""Contrastes pedagógicos del manual: una razón diferente para cada elección.
Las razones se construyen desde la relación concreta y los distractores de cada pregunta.
No hay un texto de reserva para preguntas no revisadas: un caso sin reglas detiene el banco.
"""
import re, math
from fractions import Fraction
from decimal import Decimal
from question_safety import SCOPE,SCOPE_DISTRACTORS
from legal_distractors import DISTRACTOR_MEANINGS

CONTEXT = {
'Constitución: elaboración':'Aprobación parlamentaria, referéndum, sanción y publicación son hitos distintos del proceso constitucional.',
'Constitución: cifras':'El número de artículos, títulos, disposiciones y votos corresponde a magnitudes diferentes; una cifra no puede trasladarse de una a otra.',
'Constitución: títulos':'El título preliminar se cuenta aparte de los diez títulos numerados; cada título tiene su materia y su intervalo de artículos.',
'Constitución: organización del título I':'El artículo 10 está fuera del capítulo I; el artículo 14 pertenece al capítulo II, pero no a sus dos secciones.',
'Constitución: artículos del preliminar':'Estos preceptos se encuentran en los artículos 1–9 del título preliminar, que fija los principios básicos del Estado.',
'Constitución: derechos fundamentales':'La materia del derecho permite distinguir su artículo de otros próximos; participación política y tutela judicial, por ejemplo, son derechos distintos.',
'Constitución: deberes y derechos de ciudadanía':'La sección segunda del capítulo II reúne los artículos 30–38: no debe confundirse con la sección primera, artículos 15–29.',
'Constitución: principios rectores':'Los artículos 39–52 son principios rectores; su protección se rige por el artículo 53.3, según las leyes que los desarrollen.',
'Constitución: garantías y conceptos':'La protección de los derechos depende de su ubicación constitucional; las garantías de los artículos 53.2 y 53.3 tienen alcances diferentes.',
'Igualdad: conceptos básicos':'Sexo describe características biológicas; género, roles sociales. La igualdad formal reconoce derechos y la efectiva busca realizarlos eliminando obstáculos.',
'Igualdad: discriminación y protección':'El trato desfavorable por sexo identifica discriminación directa; el criterio aparentemente neutro con desventaja injustificada identifica la indirecta.',
'Igualdad: normas principales':'La ley estatal de igualdad, la protección estatal frente a violencia de pareja y las dos leyes andaluzas tienen objetos y ámbitos diferentes.',
'LO 3/2007: artículos iniciales':'Son los preceptos de la LO 3/2007 sobre igualdad de trato, protección y actuación pública, con el contenido diferenciado de cada artículo.',
'LO 3/2007: empleo':'En estos artículos se distinguen los planes de igualdad, su diagnóstico, su transparencia, la prevención del acoso y el distintivo empresarial.',
'LO 3/2007: empleo público':'Estos artículos regulan medidas de igualdad en el empleo público; su número identifica la medida concreta, no un derecho laboral genérico.',
'Igualdad: cifras y plazos':'La presencia equilibrada de cada sexo se mueve entre 40 % y 60 %; los plazos y cuantías restantes se aplican al supuesto que indica cada regla.',
'LO 1/2004: derechos y órganos':'Información, asistencia social, asistencia jurídica, empleo y vivienda son medidas distintas; los órganos de coordinación se regulan en otros artículos.',
'Ley 12/2007: órganos y sanciones':'La competencia general diferencia leves, graves y muy graves; el propio artículo 85 prevé competencias especiales por razón de la materia.',
'Ley 13/2007: protección y recursos':'Las formas de violencia se distinguen por la conducta o el daño; los recursos de acogida se distinguen por su finalidad dentro de la recuperación.',
'Igualdad municipal: protocolo':'Confidencialidad protege la reserva; indemnidad evita represalias; presunción de inocencia impide anticipar culpabilidad. Son garantías diferentes.',
'PRL: definiciones del artículo 4':'Riesgo es la posibilidad del daño; daño es la lesión o enfermedad. Equipo de trabajo y equipo de protección individual tampoco son equivalentes.',
'PRL: principios del artículo 15':'Los principios distinguen eliminar el riesgo, evaluar el inevitable y combatir su causa; la protección colectiva se antepone a la individual.',
'PRL: identificación de riesgos':'La clasificación depende de si se describe un peligro del puesto, una posibilidad de lesión, un daño producido o una medida de protección.',
'PRL: derechos y obligaciones':'El empleador conserva el deber de protección y los costes preventivos no recaen en el personal; el trabajo debe ajustarse a formación y capacidad.',
'PRL: ámbito de aplicación':'La excepción depende de las particularidades de la actividad, no de excluir a cualquier empleado de una institución. Los establecimientos militares tienen regulación con especialidades.',
'Atención: principios':'Eficacia busca resolver la necesidad; eficiencia atiende al uso de recursos. Claridad, escucha activa e imparcialidad describen aspectos diferentes de la atención.',
'Atención: tipos y canales':'La información general no exige acreditar interés; la particular se refiere a un expediente y requiere interesado o representación acreditada.',
'Atención: funciones del RD 208/1996':'Acoger e identificar la necesidad no es lo mismo que explicar trámites; recoger una queja tampoco convierte al empleado en órgano que resuelve recursos.',
'Atención: comunicación':'Lo verbal son las palabras; lo no verbal, gestos y postura; lo paraverbal, cómo suena la voz: tono, ritmo, volumen y pausas.',
'Ley 39/2015: artículos del título II':'La suspensión del plazo, su ampliación y el silencio administrativo son reglas distintas; el artículo aplicable depende de la actuación descrita.',
'Relación electrónica: sujetos':'El artículo 14.2 enumera sujetos obligados; el 14.3 permite obligaciones reglamentarias para determinados colectivos. La persona física no obligada conserva elección de canal.',
'Procedimiento: documentos y constancias':'El recibo acredita presentación; la copia auténtica tiene la eficacia legal del original; la digitalización material no atribuye por sí sola competencia certificadora.',
'Atención: supuestos de mostrador':'La actuación se ajusta a la necesidad planteada, a los límites del puesto y a la protección de datos; el subalterno orienta y canaliza, no concede por sí solo una ayuda.',
'Actos: artículos de Ley 39/2015':'La Ley separa producción, eficacia y comunicación del acto de sus posibles vicios. Nulidad, anulabilidad, conservación y convalidación tienen reglas propias.',
'Notificaciones: plazos y condiciones':'Cursar una notificación es enviarla, no asegurar su recepción. El rechazo electrónico por falta de acceso se cuenta en días naturales y tiene otro punto de partida.',
'Notificaciones: documentos y canales':'El aviso sólo informa de la puesta a disposición; la notificación comunica el acto con garantías. El anuncio en BOE responde al supuesto del artículo 44.',
'Invalidez: conceptos':'La convalidación subsana un acto anulable; la conversión aprovecha sus elementos para otro acto; la conservación mantiene trámites que no cambiarían.',
'Notificaciones: supuestos':'El segundo intento, el rechazo expreso, la falta de acceso electrónico y la publicación limitada son situaciones con efectos y requisitos distintos.',
'Ayuntamiento: áreas de coordinación':'Se pregunta por el coordinador del área, que puede ser distinto del titular de una delegación integrada en ella. Pablo Otero coordina tanto I como V.',
'Ayuntamiento: delegaciones':'Se pregunta por la delegación concreta del decreto de los apuntes; la coordinación general de un área no atribuye todas sus delegaciones al coordinador.',
'Ayuntamiento: tenientes del tema 6':'Los rangos corresponden al listado concreto del tema 6. El tema 10 menciona una cifra global distinta, por lo que no se mezclan las dos referencias.',
'Ayuntamiento: áreas y materias':'La distribución I–VII identifica el área organizativa; la titularidad de una delegación se estudia aparte y puede recaer en otra persona.',
'Ayuntamiento: sedes municipales':'Servicio y sede deben memorizarse juntos: servicios que pertenecen al Ayuntamiento pueden estar en edificios diferentes de la Casa Consistorial.',
'Ayuntamiento: otras administraciones':'Diputación, Junta, Universidad y Administración del Estado son instituciones distintas; no son delegaciones municipales por estar situadas en Cádiz.',
'Ayuntamiento: funciones y naturaleza':'Secretaría se relaciona con fe pública y asesoramiento; Intervención con control económico; Tesorería con cobros y pagos. La función distingue a cada unidad.',
'Ayuntamiento: organismos del manual':'El ámbito del servicio no sustituye la naturaleza jurídica: el manual diferencia organismos autónomos de sociedades como PROCASA, Aguas y Eléctrica.',
'Ayuntamiento: datos organizativos':'Firma, eficacia del decreto, composición del Pleno y composición del equipo de gobierno son datos diferentes del esquema municipal de los apuntes.',
'Archivo: clases documentales':'Decisión expresa voluntad; transmisión comunica; constancia acredita hechos; juicio aporta una valoración. La función del documento determina su clase.',
'Archivo: tipos de documento':'Una resolución decide, un informe valora y un acta deja constancia; que un documento se incorpore al mismo expediente no iguala sus funciones.',
'Archivo: fases y edades orientativas':'Las edades del manual son orientativas y dependen del uso y valor documental; superar una edad no autoriza automáticamente a destruir.',
'Archivo: organización':'Clasificar asigna una serie; ordenar fija secuencia; instalar coloca unidades; foliar numera hojas. Son operaciones sucesivas con finalidades diferentes.',
'Archivo: sistemas de ordenación':'La ordenación fija una secuencia según nombre, fecha, número o materia; el criterio indicado permite identificar el sistema empleado.',
'Archivo: préstamo y consulta':'El préstamo conserva trazabilidad de la salida y retorno: el vale registra destino y el testigo ocupa la ubicación para que no se confunda préstamo con pérdida.',
'Archivo: conservación material':'La conservación protege el soporte y la integridad. La antigüedad y la falta de espacio no sustituyen la autorización necesaria para eliminar.',
'Ortografía: reglas de acentuación':'La posición de la sílaba tónica y la terminación determinan la regla general; el hiato con vocal débil tónica tiene su propia regla de tilde.',
'Ortografía: abreviaturas':'Se conserva la escritura abreviada del manual, incluido el punto, las tildes y las letras voladas cuando corresponden.',
'Ortografía: acortamientos':'Abreviaturas, siglas y símbolos tienen convenciones diferentes: los símbolos no llevan punto abreviativo ni una s de plural.',
'Ortografía: usos administrativos':'Los nombres comunes de cargos y las denominaciones institucionales siguen usos distintos de mayúsculas; las mayúsculas también llevan tilde cuando corresponde.',
'Informática: programas':'Procesador de texto, hoja de cálculo, gestor de bases de datos y programa de presentaciones sirven a tareas diferentes; sistema operativo es otra categoría.',
'Informática: componentes':'RAM es memoria de trabajo volátil; ROM conserva información sin alimentación en la explicación del manual. Almacenamiento y memoria de trabajo no son sinónimos.',
'Informática: unidades':'Una unidad de capacidad no mide lo mismo que frecuencia o resolución. El manual utiliza la escala de 1.024 para KB, MB y GB.',
'Informática: extensiones':'La extensión identifica el formato habitual del archivo; una imagen, una hoja de cálculo y un documento de texto no son el mismo tipo de fichero.',
'Informática: redes y hojas de cálculo':'LAN, MAN y WAN se distinguen por alcance; intranet por su uso privado. En la hoja de cálculo, celda, rango, fórmula y función son conceptos distintos.',
'Reprografía: partes de fotocopiadora':'La bandeja aporta papel, el tambor recibe la imagen y el fusor fija el tóner con calor y presión; cada componente tiene una función diferente.',
'Reprografía: funciones y consumibles':'Alzado organiza juegos; dúplex utiliza dos caras. Tóner y tinta son consumibles diferentes y no deben confundirse con el formato o gramaje del papel.',
'Reprografía: tamaños DIN A':'Cada tamaño siguiente divide por la mitad la superficie del anterior. Girar la hoja intercambia orientación, pero no cambia sus medidas.',
'Digitalización: formatos y herramientas':'Escanear captura la imagen; OCR reconoce caracteres y permite trabajar con texto. La elección del formato depende de imagen, uso y conservación.',
'Máquinas auxiliares: componentes':'La función permite identificar la pieza: sujetar, cortar, guiar, recoger restos o controlar temperatura son tareas de componentes diferentes.',
'Máquinas auxiliares: seguridad':'Las actuaciones dependen de la máquina y sus instrucciones: desconectar y enfriar antes de limpieza; proteger la cuchilla; reservar reparaciones complejas al técnico.',
'Correo: protocolos y campos':'SMTP envía; POP3 descarga según configuración; IMAP sincroniza el buzón. Los protocolos no son campos de destinatarios como Para, Cc y Cco.',
'Correo: carpetas y riesgos':'Borradores aún no se ha enviado; salida está pendiente de envío; enviados ya ha salido, sin acreditar por sí solo que una persona haya leído el mensaje.',
'Cádiz: historia y fechas':'Las fechas se vinculan a hechos concretos: la Constitución de 1812 y el puente que lleva su nombre no pertenecen al mismo año.',
'Cádiz: nombres y protagonistas':'Gadir, Gades y Qādis identifican etapas diferentes. Los autores y monarcas citados se vinculan a la obra o hecho concreto de los apuntes.',
'Cádiz: barrios y rasgos':'Los rasgos históricos, monumentos y tradiciones permiten distinguir cada barrio; no se asignan todos al Pópulo por ser el núcleo medieval.',
'Cádiz: espacios culturales y dirección':'La dirección identifica el equipamiento: Museo de Cádiz, Museo de las Cortes y los distintos teatros son centros diferentes.',
'Cádiz: patrimonio y contenido':'El contenido distingue al lugar: la maqueta se vincula al Museo de las Cortes, los sarcófagos al Museo de Cádiz y Costus al ECCO.',
'Cádiz: características patrimoniales':'La forma, época, emplazamiento y uso permiten distinguir monumentos; Catedral Nueva y Catedral Vieja tampoco son dos nombres del mismo edificio.',
'Cádiz: fiestas y actos':'Cada celebración tiene fecha, escenario o finalidad propios; el programa de Carnaval distingue cabalgatas, pregón, carruseles y actuaciones callejeras.',
'Cádiz: geografía y cultura, cifras':'Son cifras y clasificaciones del cuadro del manual: modalidades, edades y fases del COAC se refieren a categorías diferentes.',
'Ayuntamiento: delegaciones complementarias':'Estas delegaciones mantienen la atribución concreta del decreto estudiado, aunque sus titulares también tengan otras responsabilidades municipales.',
'Ortografía: tilde diacrítica':'La tilde distingue funciones: pronombre y posesivo, verbo y preposición o adverbio y conjunción. La diferencia depende del uso en la oración.',
'Ortografía: signos de puntuación':'La puntuación organiza el texto: introducir una enumeración, insertar un inciso y separar elementos complejos requieren signos con funciones diferentes.',
'Aritmética: conjuntos y propiedades':'Un natural es entero y racional, pero las definiciones de los conjuntos tienen alcances distintos. La división entera debe cumplir la igualdad y la condición del resto.',
}

DETAILS = {
('Constitución: cifras','los títulos numerados, sin contar el preliminar'):'Son diez títulos I–X; al añadir el título preliminar resultan once bloques titulados, no once títulos numerados.',
('Constitución: garantías y conceptos','la tutela del artículo 53.2'):'La vía preferente y sumaria protege el artículo 14 y la sección primera del capítulo II; el amparo se extiende también a la objeción de conciencia del artículo 30.2.',
('Constitución: garantías y conceptos','la suspensión individual del artículo 55'):'Se exige ley orgánica, intervención judicial y control parlamentario; no es una suspensión de todos los derechos de una persona.',
('Igualdad: discriminación y protección','el acoso sexual'):'La conducta debe tener naturaleza sexual; puede ser verbal o física y basta el propósito o el efecto de atentar contra la dignidad en los términos del artículo 7.',
('Igualdad: discriminación y protección','el acoso por razón de sexo'):'El motivo es el sexo de la persona, sin exigir conducta de naturaleza sexual; no debe confundirse con el acoso sexual.',
('Igualdad: discriminación y protección','la acción positiva'):'Debe responder a una desigualdad de hecho, mantenerse mientras ésta subsista y ser razonable y proporcionada; no permite cualquier diferencia de trato.',
('Igualdad: cifras y plazos','el umbral de plantilla para plan empresarial obligatorio'):'El artículo 45 establece la obligación por plantilla desde cincuenta personas; también contempla otros supuestos, como convenio o acuerdo sancionador.',
('Igualdad: cifras y plazos','la preferencia formativa estatal tras reincorporación protegida'):'El artículo 60 de la LO 3/2007 vincula ese año a quienes se reincorporan tras los permisos o excedencias protegidos que enumera; no a toda la plantilla.',
('Igualdad: cifras y plazos','la reducción de multa del artículo 84 en sus condiciones'):'El porcentaje es treinta, sujeto a las condiciones del propio artículo 84; no se aplica automáticamente a cualquier infracción.',
('PRL: definiciones del artículo 4','riesgo grave e inminente'):'La materialización debe ser probable en un futuro inmediato y el daño potencial grave; no es necesario que ya exista una lesión.',
('PRL: derechos y obligaciones','la exposición inmediata a un agente peligroso'):'La exposición puede ser inmediata aunque la enfermedad o el daño grave se manifieste más tarde, según la precisión del artículo 4.4.º.',
('Atención: comunicación','el banco de niebla'):'Consiste en dar la razón en parte de la queja o reconocer el derecho a estar enfadado sin ceder a una exigencia contraria a la norma.',
('Atención: comunicación','el disco rayado'):'Se repite la postura o norma con voz pausada y sin entrar en discusiones; no consiste en elevar el tono ni añadir amenazas.',
('Notificaciones: plazos y condiciones','el plazo para cursar notificación desde dictado'):'Los apuntes precisan diez días hábiles desde que se dicta el acto. Cursar significa enviar, no que el destinatario tenga que recibir dentro de esos diez días.',
('Notificaciones: plazos y condiciones','el rechazo por no acceder cuando medio electrónico es obligatorio o elegido'):'Son diez días naturales desde la puesta a disposición sin acceso; aquí cuentan sábados, domingos y festivos. No se cuentan desde un aviso por correo.',
('Notificaciones: plazos y condiciones','la edad del receptor domiciliario distinto del interesado'):'El artículo 42.2 dice mayor de catorce años y exige que se encuentre en el domicilio y haga constar su identidad; la edad no es el único requisito.',
('Notificaciones: plazos y condiciones','el tiempo para repetir un intento domiciliario fallido'):'Se repite una sola vez, en hora distinta: si el primero fue antes de las 15:00, el segundo después, y viceversa, con al menos tres horas de diferencia.',
('Notificaciones: documentos y canales','el aviso por correo o dispositivo'):'La falta de ese aviso no invalida por sí sola la notificación: el aviso no sustituye el acceso al contenido o la práctica legal de la entrega.',
('Notificaciones: supuestos','Notificación contiene texto íntegro pero omite recursos.'):'La notificación surte efectos cuando el interesado realiza actuaciones que revelan conocimiento del contenido y alcance o interpone un recurso; no basta cualquier actuación irrelevante.',
('Invalidez: conceptos','la nulidad por incompetencia manifiesta'):'La causa de nulidad del artículo 47.1 b) exige incompetencia manifiesta por materia o territorio; no convierte cualquier defecto de competencia en nulidad de pleno derecho.',
('Ayuntamiento: otras administraciones','Rectorado de UCA en el tema 6'):'La dirección Ancha, 16 es la referencia solicitada del tema 6; el tema 10 recoge Paseo Carlos III. Se indica el tema para no presentar ambas como una única dirección.',
('Ayuntamiento: sedes municipales','Fundación Municipal de Cultura, referencia del tema 6'):'Se utiliza aquí la referencia del tema 6, avenida Juan Carlos I; el tema 10 sitúa la FMC en otro contexto del centro histórico.',
('Ayuntamiento: datos organizativos','el máximo de concejales de Junta para corporación de 27'):'El límite es un tercio del número legal de miembros: 27 ÷ 3 = 9. Son nueve concejales como máximo, además del alcalde que preside.',
('Archivo: organización','la foliación'):'Cada hoja recibe un número, aunque tenga anverso y reverso; numerar cada cara sería paginación, no foliación.',
('Archivo: organización','el expurgo autorizado'):'Exige valoración y autorización de eliminación; no es una decisión libre del subalterno por antigüedad o falta de espacio.',
('Ortografía: reglas de acentuación','la palabra día'):'La í es vocal cerrada tónica junto a la a abierta: forman hiato y la cerrada lleva tilde, con independencia de la regla general de llanas.',
('Ortografía: reglas de acentuación','la palabra guion según manual'):'La combinación se considera diptongo a efectos ortográficos; por ser monosílaba no lleva tilde, aunque pueda pronunciarse con hiato.',
('Ortografía: usos administrativos','la separación de sujeto y verbo'):'No se introduce coma sólo por hacer una pausa al hablar; sí pueden aparecer las dos comas que encierran un inciso.',
('Informática: componentes','firmware'):'Es software incorporado al dispositivo para controlar su funcionamiento; se distingue aquí por esa función específica, no por dejar de ser programación.',
('Informática: componentes','software'):'Es la categoría general de programas e instrucciones; el firmware es una forma específica de software incorporada al dispositivo.',
('Informática: componentes','memoria RAM'):'Sirve al trabajo en curso y pierde su contenido al quitar la alimentación; conservar archivos de forma permanente corresponde al almacenamiento.',
('Informática: extensiones','.exe'):'Identifica un ejecutable; no todos los ejecutables son maliciosos, pero un adjunto sospechoso no debe ejecutarse y se consulta por el canal seguro.',
('Reprografía: tamaños DIN A','A4'):'210 × 297 mm equivale a 21 × 29,7 cm. No debe confundirse el cambio de orientación con un cambio de tamaño.',
('Máquinas auxiliares: seguridad','destruir documentos con datos personales'):'Los apuntes recomiendan corte cruzado o microcorte y P-4 o superior para esta destrucción. La autorización de eliminar el documento se comprueba por separado.',
('Correo: protocolos y campos','Cco'):'Los demás receptores no ven las direcciones incluidas como copia oculta; el remitente sí conoce a quienes ha enviado el mensaje.',
('Cádiz: nombres y protagonistas','el arquitecto de Casa Consistorial escrito en manual'):'La respuesta mantiene exactamente la grafía Torcuato Benjumea de estos apuntes, porque la pregunta se refiere a lo escrito en ellos.',
}

def capital(s):return s[:1].upper()+s[1:]
def owners(g,value):return [key for key,v in g['rows'] if v==value]
def rule(g,key,value):
    detail=DETAILS.get((g['section'],key),CONTEXT[g['section']])
    return f'En «{g["section"]}», el temario relaciona «{key}» con «{value}». {detail}'

def fact_explanations(g,key,value,mode,correct,wrong):
    known=dict((capital(k),v) for k,v in g['rows'])
    target=rule(g,key,value)
    if mode=='negative':
        falsevalue=correct.split(' → ',1)[1]
        base=f'El enunciado pide la asociación incorrecta. «{correct}» es la que contiene el error: a «{capital(key)}» le corresponde «{value}», no «{falsevalue}». '+DETAILS.get((g['section'],key),CONTEXT[g['section']])
    else:base=target
    reasons=[];evidence=[]
    for option in wrong:
        if mode=='direct':
            if g['section']==SCOPE:
                specific=dict(SCOPE_DISTRACTORS[key])[option]
                reasons.append(f'Has elegido «{option}». {specific} {target}')
                evidence.append({'selected':option,'reason':specific,'target':[key,value]})
                continue
            other=owners(g,option)
            assert other,(g['section'],option)
            contrast=f'Has elegido «{option}». En esta clasificación del temario, esa respuesta corresponde a '+ ' o a '.join(f'«{k}»' for k in other)+f', mientras que se pregunta por «{key}». '
            why=contrast+target;evidence.append({'selectedOwners':other,'target':[key,value]})
        elif mode=='reverse':
            actual=known[option]
            why=f'Has elegido «{option}», que el temario relaciona con «{actual}». La descripción de la pregunta es «{value}» y corresponde a «{key}». '+DETAILS.get((g['section'],key),CONTEXT[g['section']])
            evidence.append({'selectedPair':[option,actual],'target':[key,value]})
        else:
            chosen_key,chosen_value=option.split(' → ',1);actual=known[chosen_key]
            if mode=='positive':
                assert actual!=chosen_value
                why=f'La asociación «{option}» cruza dos datos: a «{chosen_key}» le corresponde «{actual}», no «{chosen_value}». La asociación correcta es «{correct}». '+DETAILS.get((g['section'],key),CONTEXT[g['section']])
            else:
                assert actual==chosen_value
                why=f'Has elegido «{option}», una asociación verdadera: «{chosen_key}» sí corresponde a «{actual}». El enunciado pide la incorrecta, por eso esta opción no resuelve lo preguntado. '+base
            evidence.append({'selectedPair':[chosen_key,chosen_value],'actualValue':actual,'target':[key,value],'requested':mode})
        reasons.append(why)
    return base,reasons,{'method':'contraste de relaciones concretas del temario','target':[key,value],'mode':mode,'distractors':evidence}

# Significado de las alternativas legales, sin atribuir a una norma reglas ajenas al pasaje.
LEGAL_MEANINGS={
'procedimiento administrativo':'cauce de actuación de la Administración, distinto de un proceso penal, civil o laboral',
'gratuita':'sin exigir pago por la prestación indicada en el artículo',
'órganos de gobierno':'órganos que ejercen las funciones de gobierno de la institución',
'subordinación':'dependencia o sometimiento, que el pasaje distingue de la participación en igualdad',
'consejo general del poder judicial':'órgano de gobierno del Poder Judicial, distinto del Gobierno estatal',
'resoluciones judiciales':'decisiones de los órganos judiciales',
'recurso de alzada':'recurso administrativo ante el superior jerárquico en los supuestos previstos',
'incompetencia':'falta de competencia del órgano, con los efectos específicos que fija el supuesto',
'discriminación directa':'trato menos favorable por sexo en situación comparable',
'discriminación indirecta':'criterio aparentemente neutro que provoca desventaja injustificada',
'acción positiva':'medida razonable y proporcionada para corregir desigualdad de hecho',
'presencia equilibrada':'presencia de cada sexo entre el cuarenta y el sesenta por ciento en el criterio del manual',
'representación equilibrada':'representación de cada sexo dentro de los límites de equilibrio indicados en la ley',
'acoso sexual':'conducta de naturaleza sexual que atenta contra la dignidad por su propósito o efecto',
'acoso por razón de sexo':'conducta basada en el sexo que atenta contra la dignidad, sin exigir contenido sexual',
'violencia física':'daño corporal o riesgo de producirlo',
'violencia psicológica':'daño emocional o sometimiento mediante conductas psicológicas',
'violencia sexual':'conducta contra la libertad sexual sin consentimiento',
'violencia económica':'privación o control de recursos económicos en los términos descritos por el manual',
'igualdad de trato':'ausencia de discriminación por razón de sexo',
'igualdad de oportunidades':'igualdad en posibilidades de acceso y participación',
'perspectiva de género':'consideración de las diferencias y desigualdades entre mujeres y hombres en la actuación',
'impacto de género':'efecto diferenciado de una medida sobre mujeres y hombres',
'lenguaje no sexista':'expresión que evita un uso discriminatorio del lenguaje',
'corresponsabilidad':'responsabilidad compartida, en especial en las tareas familiares y de cuidados',
'conciliación':'compatibilización de la vida personal, familiar y laboral',
'negociación colectiva':'determinación colectiva de condiciones laborales mediante los sujetos correspondientes',
'planes de igualdad':'medidas organizadas de igualdad basadas en diagnóstico y con seguimiento',
'plan de igualdad':'instrumento organizado de medidas de igualdad',
'informes de impacto de género':'informes sobre los efectos de una medida en la igualdad entre mujeres y hombres',
'informe de impacto de género':'análisis de los efectos de una medida en la igualdad entre mujeres y hombres',
'desagregados por sexo':'datos separados para mujeres y hombres, que permiten analizar diferencias',
'derecho necesario mínimo indisponible':'garantía mínima que puede mejorarse pero no reducirse por convenio',
'protección colectiva':'protección del conjunto de personas frente al riesgo',
'protección individual':'protección de cada persona mediante equipos o medidas individuales',
'riesgo grave e inminente':'riesgo probable de materialización inmediata y daño grave',
'equipos de trabajo':'máquinas, aparatos, instrumentos o instalaciones utilizados en el trabajo',
'equipo de trabajo':'máquina, aparato, instrumento o instalación utilizado en el trabajo',
'equipos de protección individual':'equipos llevados o sujetados por la persona para protegerla frente a riesgos',
'equipo de protección individual':'equipo llevado o sujetado por la persona para protegerla frente a riesgos',
'condición de trabajo':'característica del puesto o su organización que puede influir en los riesgos',
'daño derivado del trabajo':'lesión, patología o enfermedad sufrida con motivo u ocasión del trabajo',
'carga de la prueba':'distribución de quién debe probar los hechos en el proceso',
'presunción de inocencia':'garantía de no anticipar culpabilidad',
'nulidad':'invalidez de pleno derecho por las causas tasadas del artículo 47 de la Ley 39/2015',
'anulabilidad':'invalidez del artículo 48 por infracción del ordenamiento, con las precisiones sobre forma y plazos',
'convalidación':'subsanación de vicios de un acto anulable',
'conversión':'aprovechamiento de elementos del acto inválido para producir los efectos de otro acto',
'conservación':'mantenimiento de actos o trámites cuyo contenido no habría cambiado sin la infracción',
'caducidad':'terminación por transcurso del plazo en el supuesto legal correspondiente',
'prescripción':'extinción por transcurso del tiempo de la responsabilidad o de la posibilidad de exigirla en los casos previstos',
'suspensión':'interrupción temporal de los efectos o del curso de un plazo según el pasaje',
'notificación':'comunicación del acto administrativo a su destinatario con las garantías exigidas',
'notificaciones':'comunicaciones de actos administrativos a sus destinatarios con las garantías exigidas',
'publicación':'difusión del acto en el medio previsto para el supuesto legal',
'publicaciones':'difusiones de actos en los medios previstos para los supuestos legales',
'publicidad':'posibilidad de conocimiento o difusión de la información, según el contexto del artículo',
'confidencialidad':'reserva de información para impedir su divulgación no autorizada',
'intimidad':'protección del ámbito personal y privado',
'certificación':'acreditación formal de hechos o extremos por quien tiene competencia',
'certificaciones':'acreditaciones formales por quien tiene competencia',
'digitalización':'obtención de una representación electrónica de un documento',
'registro':'anotación o instrumento registral, con la función concreta que establece el pasaje',
'registro electrónico':'medio de presentación y constancia electrónica de documentos',
'archivo histórico':'conservación de documentación con valor histórico',
'prevención':'actuación para evitar o reducir el riesgo antes de que se produzca el daño',
'formación':'adquisición de conocimientos o capacidades por las personas destinatarias',
'coeducación':'educación orientada a la igualdad y a superar estereotipos sexistas',
'participación':'intervención de las personas o entidades en la actuación descrita',
'accesibilidad':'eliminación de barreras para poder acceder y utilizar servicios o entornos',
'sanción':'consecuencia prevista por una infracción',
'sanciones':'consecuencias previstas por las infracciones',
'exclusión':'apartamiento del ámbito o acceso al que se refiere el pasaje',
'seguridad y salud':'protección preventiva de las personas trabajadoras',
'probabilidad':'posibilidad de que se produzca el daño',
'severidad':'gravedad del daño que puede producirse',
'ley orgánica':'tipo de ley reservado a las materias constitucionalmente previstas',
'derecho de petición':'petición individual o colectiva por escrito en los términos legales',
'recurso de amparo':'protección constitucional de los derechos a los que se extiende esa vía',
'seguridad jurídica':'certeza y previsibilidad del ordenamiento',
'jerarquía normativa':'orden de rango entre normas',
'libertad de empresa':'libertad de actividad empresarial en la economía de mercado',
'libertad de empresa':'libertad de actividad empresarial en la economía de mercado',
'servicio público':'actividad de interés público en el ámbito referido por el precepto',
'dominio público':'bienes destinados al uso o servicio público en los términos correspondientes',
'asistencia social integral':'atención social que incluye las actuaciones de apoyo y recuperación previstas',
'asistencia jurídica':'asesoramiento y defensa jurídica en los términos previstos',
'Administraciones públicas'.lower():'Administraciones a las que el artículo dirige la actuación o el deber',
'personas físicas':'personas individuales, distintas de entidades con personalidad jurídica',
'personas jurídicas':'entidades con personalidad jurídica propia, distintas de las personas individuales',
'medios electrónicos':'canales electrónicos de actuación o relación administrativa',
'resolución judicial':'decisión del órgano judicial, no una mera orden administrativa o privada',
'Consejo de Gobierno'.lower():'órgano de gobierno autonómico citado por el precepto',
'Consejo de Ministros'.lower():'órgano del Gobierno del Estado, distinto del Consejo de Gobierno autonómico',
'Tribunal Constitucional'.lower():'órgano de garantías constitucionales, distinto de los tribunales ordinarios',
'Tribunal de Cuentas'.lower():'órgano de control de cuentas públicas, distinto del tribunal de garantías constitucionales',
'Instituto Andaluz de la Mujer'.lower():'organismo andaluz de políticas de igualdad citado en el manual',
'Consejo Audiovisual de Andalucía'.lower():'órgano andaluz vinculado al ámbito audiovisual',
'Consejo Andaluz de Participación de las Mujeres'.lower():'órgano andaluz de participación y representación del movimiento de mujeres',
'Defensor del Pueblo'.lower():'alto comisionado de las Cortes Generales para la defensa de los derechos',
'Cortes Generales'.lower():'institución parlamentaria del Estado, integrada por Congreso y Senado',
'observatorio':'órgano o instrumento de observación y seguimiento identificado por el artículo',
'capacidad económica':'recursos o capacidad económica considerados por la regla concreta',
'maternidad':'situación protegida relacionada con ser madre',
'embarazo':'gestación, protegida específicamente por las normas del temario',
'lactancia':'situación protegida de alimentación del menor a la que se refiere el precepto',
'vivienda':'acceso o actuación en materia de vivienda',
'salud':'ámbito sanitario y protección de la salud',
'educación':'ámbito educativo y de enseñanza',
'cultura':'ámbito cultural y de creación o participación cultural',
'deporte':'actividad física y deportiva',
'empleo':'acceso, condiciones o actuación en el ámbito laboral',
'estadísticas':'datos que permiten conocer y analizar la situación',
'patrimonio':'bienes o patrimonio en el sentido que utiliza el pasaje',
}
MODALS={
'deberá':'obligación de realizar la actuación','deberán':'obligación de realizar la actuación',
'podrá':'facultad o posibilidad de realizar la actuación','podrán':'facultad o posibilidad de realizar la actuación',
'no podrá':'prohibición de realizar la actuación','no podrán':'prohibición de realizar la actuación',
'garantizará':'mandato de asegurar el resultado protegido','garantizarán':'mandato de asegurar el resultado protegido',
'promoverá':'mandato de impulsar la actuación','promoverán':'mandato de impulsar la actuación',
'fomentará':'mandato de favorecer la actuación','fomentarán':'mandato de favorecer la actuación',
'prohibirá':'mandato de impedir la actuación','prohibirán':'mandato de impedir la actuación',
'suspenderá':'mandato de interrumpir la actuación','suspenderán':'mandato de interrumpir la actuación',
'eliminará':'mandato de suprimir la actuación','eliminarán':'mandato de suprimir la actuación',
'restringirán':'mandato de limitar la actuación','evitará':'mandato de evitar la actuación','evitarán':'mandato de evitar la actuación',
'obligatoria':'carácter obligatorio','obligatorio':'carácter obligatorio','voluntaria':'carácter voluntario','voluntario':'carácter voluntario',
'prohibida':'carácter prohibido','prohibidos':'carácter prohibido',
'graves':'categoría de infracción grave','muy graves':'categoría de infracción muy grave','leves':'categoría de infracción leve',
'no sancionables':'ausencia de sanción',
}

def literal_explanations(q):
    correct=q['correct'];c=correct.lower();blank=q['prompt'].split('«',1)[1].rsplit('»',1)[0]
    restored=blank.replace('____',correct)
    assert restored in q['explanation'],q['prompt']
    article=q['coverage'];cmeaning=LEGAL_MEANINGS.get(c) or MODALS.get(c)
    quantitative=bool(re.search(r'\d',c) or c in ['diez días','quince días','tres meses','seis meses','cuatro años','cinco años','un año','dos años','tres años','dieciocho meses','doce meses','veinticuatro meses','setenta y dos horas','cuarenta por ciento','sesenta por ciento','treinta por ciento','setenta y cinco por ciento'])
    if c=='de oficio':
        if 'turno ____' in blank:cmeaning='el turno de asistencia jurídica profesional mencionado en la formación especializada de abogados; no describe aquí quién inicia un procedimiento administrativo'
        elif 'revisión ____' in blank:cmeaning='la denominación del procedimiento de revisión de oficio; no significa que todo procedimiento con ese nombre deba comenzar sin solicitud de un interesado'
        else:cmeaning='actuación por iniciativa de la propia Administración en el supuesto descrito'
    negative=re.search(r'\b(no|ni)\s+$',blank.split('____')[0]) if c in MODALS else None
    if negative:
        expression=f'{negative[1]} {correct}'
        cmeaning=f'la expresión completa «{expression}», con la negación que ya está escrita antes del hueco; la regla no permite la actuación que se niega'
    assert cmeaning or quantitative,(article,correct)
    prefix=f'La expresión que completa este punto del artículo es «{correct}».'
    if cmeaning:prefix+=f' Aquí se refiere a {cmeaning}.'
    base=prefix+f' La regla completa es: «{restored}»'
    wrongreasons=[]
    for wrong in q['wrong']:
        w=wrong.lower();wmeaning=LEGAL_MEANINGS.get(w) or MODALS.get(w) or DISTRACTOR_MEANINGS.get(w)
        if negative:
            contrast=f'Has elegido «{wrong}», que produciría «{negative[1]} {wrong}» en la frase. El texto del temario dice «{expression}». La negación está fuera del hueco y debe conservarse al interpretar la regla. Se pide reconstruir el texto literal, no sustituirlo por una reformulación.'
        elif quantitative:
            if re.search(r'\b(años?|meses?|días?|horas?)\b',c):
                contrast=f'Has elegido «{wrong}». El plazo de este supuesto es «{correct}», contado desde el hecho que indica el artículo. La alternativa introduce una duración distinta; no es el plazo que fija esta regla.'
            elif 'por ciento' in c:
                contrast=f'Has elegido «{wrong}». El porcentaje previsto en esta regla es «{correct}»: son proporciones diferentes. Hay que mantener además la base y las condiciones a las que el artículo aplica ese porcentaje.'
            elif 'euros' in restored.lower():
                contrast=f'Has elegido «{wrong}». La cuantía en euros que completa este punto es «{correct}»; la alternativa cambia el importe del tramo señalado en la regla. Los puntos de estas cifras separan miles.'
            elif re.search(r'por\s+____',blank):
                assert c=='100',(article,correct)
                contrast=f'Has elegido «{wrong}». La expresión porcentual es «por 100»: de cada cien. «Por {wrong}» cambia la base de la proporción; no reproduce el porcentaje indicado en este supuesto.'
            elif re.search(r'artículo\s+____',blank):
                contrast=f'Has elegido «{wrong}», pero la remisión de esta regla es al artículo «{correct}». Se pregunta por el número del precepto al que remite el texto, no por un plazo ni por una cantidad de personas.'
            elif re.search(r'____\s+de\s+(enero|febrero|marzo|abril|mayo|junio|julio|agosto|septiembre|octubre|noviembre|diciembre)',blank):
                month=re.search(r'____\s+de\s+(\w+)',blank)[1]
                contrast=f'Has elegido «{wrong}». La fecha citada en este pasaje es el día {correct} de {month}; {wrong} no es el día que corresponde a esa referencia del temario.'
            else:
                assert c=='50',(article,correct)
                contrast=f'Has elegido «{wrong}». El artículo fija «{correct}» personas trabajadoras en el punto señalado de la plantilla; «{wrong}» desplaza ese umbral. Se debe conservar el número y el supuesto empresarial de la frase.'
        elif c in MODALS and w in MODALS:
            contrast=f'«{wrong}» expresa {MODALS[w]}, mientras que este pasaje utiliza «{correct}», que expresa {MODALS[c]}. Hay que mantener también las negaciones y condiciones del resto de la frase.'
        elif wmeaning:
            contrast=f'Has elegido «{wrong}», que se refiere a {wmeaning}. En este punto el artículo utiliza «{correct}»: {cmeaning}.'
        elif c=='de oficio':
            contrast=f'«{wrong}» introduce una condición de iniciativa o decisión ajena que no figura en esta expresión. Aquí «de oficio» se refiere a {cmeaning}.'
        else:
            raise AssertionError(('Falta revisar esta alternativa legal',article,correct,wrong))
        wrongreasons.append(contrast+f' Texto del temario: «{restored}»')
    return base,wrongreasons,{'method':'reconstrucción del pasaje literal y contraste del término sustituido','article':article,'quote':restored,'target':correct,'distractors':q['wrong']}

def parse_num(s):return Fraction(s.replace(',','.'))
def nfmt(x):
    x=Fraction(x)
    if x.denominator==1:return str(x.numerator)
    return str(float(x)).replace('.',',') if x.denominator in [2,4,5,10,20,25,50,100] else str(x)

def math_explanations(q):
    prompt=q['prompt'];section=q['section'];nums=[int(x) for x in re.findall(r'\d+',prompt)]
    correct=q['correct'];answer=parse_num(correct);reasons={}
    if section=='Cálculo: inventario':
        a,b,c=nums
        base=f'Las entradas se suman y las entregas se restan: {a} + {b} = {a+b}; {a+b} − {c} = {a+b-c} carpetas.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==a+b+c:r=f'Ese resultado suma también las {c} carpetas entregadas, que deben salir del inventario.'
            elif v==a-b-c:r=f'Ese resultado resta las {b} carpetas recibidas; una recepción aumenta las existencias.'
            elif v==a+b:r=f'Ese resultado omite descontar las {c} carpetas que se entregan.'
            else:r=f'El movimiento neto es {b} − {c} = {b-c}; al aplicarlo a {a} no se obtienen {w} carpetas.'
            reasons[w]=r
    elif section=='Cálculo: jerarquía':
        a,b,c,d=nums;part=c-d
        base=f'Primero el paréntesis: {c} − {d} = {part}. Después el producto: {b} × {part} = {b*part}. Finalmente la suma: {a} + {b*part} = {a+b*part}.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==(a+b)*part:r=f'Sumar {a} y {b} antes de multiplicar cambia la expresión a ({a}+{b})×{part}; ese paréntesis no está en el enunciado.'
            elif v==a+b*c-d:r=f'Ese resultado corresponde a {a}+{b}×{c}−{d}, que deja la resta fuera del paréntesis original.'
            else:r=f'El producto que debe sumarse a {a} es {b*part}, no {nfmt(v-a)}.'
            reasons[w]=r
    elif section=='Cálculo: signos':
        a,b=nums;base=f'Un factor es negativo y el otro positivo: el producto es negativo. La magnitud es {a} × {b} = {a*b}; el resultado es −{a*b}.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==a*b:r='La magnitud del producto es esa, pero falta el signo negativo: los factores tienen signos distintos.'
            elif v==-a-b:r=f'Ese resultado corresponde a −{a}−{b}, una suma de negativos, no al producto pedido.'
            else:r=f'Ese valor no respeta el producto de las magnitudes {a} y {b} y su signo negativo.'
            reasons[w]=r
    elif section=='Cálculo: división y resto':
        total,div=nums;quot,rem=divmod(total,div)
        base=f'Se forman {quot} grupos completos: {div} × {quot} = {div*quot}. Sobran {total} − {div*quot} = {rem} sobres; el resto debe ser menor que {div}.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==0:r=f'La división no es exacta: los grupos completos utilizan {div*quot}, pero hay {total} sobres.'
            elif v>=div:r=f'Un resto no puede ser igual o mayor que {div}: todavía se podría formar otro grupo.'
            else:r=f'Con {quot} grupos y resto {w} se reconstruirían {nfmt(div*quot+v)} sobres, en vez de los {total} del enunciado.'
            reasons[w]=r
    elif section=='Cálculo: fracciones':
        a,b,c,d=nums;den=math.lcm(b,d);num=a*(den//b)+c*(den//d);f=Fraction(a,b);g=Fraction(c,d)
        base=f'El denominador común mínimo es {den}. {a}/{b} = {a*(den//b)}/{den} y {c}/{d} = {c*(den//d)}/{den}. Sumamos: {num}/{den}; al simplificar queda {correct}.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==f-g:r=f'Ese valor es la diferencia {a}/{b} − {c}/{d}; el signo del enunciado pide sumar.'
            elif v==f*g:r=f'Ese valor es el producto ({a}×{c})/({b}×{d}); se pide suma, no multiplicación.'
            elif v==Fraction(a+c,b+d):r=f'Sumar directamente numeradores y denominadores daría ({a}+{c})/({b}+{d}), que no es la regla de suma de fracciones.'
            else:r=f'Esa fracción no es equivalente al numerador {num} sobre el denominador común {den} obtenido al sumar.'
            reasons[w]=r
    elif section=='Cálculo: porcentajes':
        percent,total=nums;result=Fraction(total*percent,100)
        base=f'Un {percent} % son {percent} de cada 100. Se calcula {total} × {percent}/100 = {nfmt(result)} documentos.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==total-result:r=f'Ese valor representa lo que queda después de quitar el {percent} %, es decir, el {100-percent} % del total.'
            elif v==total//percent:r=f'Ese valor se obtiene dividiendo {total} entre {percent} y tomando la parte entera; un porcentaje se calcula multiplicando por {percent}/100.'
            elif v==total:r='Ese valor es el total inicial, que representa el 100 %, no la parte porcentual solicitada.'
            else:r=f'La parte pedida es {nfmt(result)}; {w} equivaldría al {nfmt(v/total*100)} % de {total}, un porcentaje distinto de {percent} %.'
            reasons[w]=r
    elif section=='Cálculo: porcentaje inverso':
        total,part=nums;result=Fraction(part*100,total);base=f'El porcentaje de asistencia usa asistentes dividido entre inscritos: {part}/{total} × 100 = 75 %. Los ausentes son {total-part}, el 25 %.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==25:r='Ese 25 % es el porcentaje de quienes no asisten; se pide el de asistentes.'
            elif v==100:r=f'Un 100 % supondría que asistieran las {total} personas inscritas; asisten sólo {part}.'
            else:r=f'Un {w} % supondría {nfmt(total*v/100)} asistentes, distinto de los {part} indicados.'
            reasons[w]=r
    elif section=='Cálculo: proporción directa':
        workers,total,other=nums;unit=Fraction(total,workers);result=other*unit
        base=f'En el mismo tiempo cada persona clasifica {total} ÷ {workers} = {nfmt(unit)} documentos. Con {other} personas: {nfmt(unit)} × {other} = {nfmt(result)}.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==total+other:r='Sumar un número de personas a un número de documentos mezcla magnitudes diferentes; se usa la producción por persona.'
            elif v==total*other:r=f'El total {total} ya corresponde a {workers} personas; antes de multiplicar por {other} hay que dividir por {workers}.'
            elif v==total:r=f'Ese valor conserva la producción de {workers} personas, aunque ahora trabajan {other} al mismo ritmo y tiempo.'
            else:r=f'Con {other} personas ese resultado implicaría {nfmt(v/other)} documentos por persona, no los {nfmt(unit)} del ritmo indicado.'
            reasons[w]=r
    elif section=='Cálculo: proporción inversa':
        workers,h,other=nums;result=Fraction(workers*h,other)
        base=f'El trabajo total es {workers} × {h} = {workers*h} horas-persona. Al repartirlo entre {other} personas, el tiempo es {workers*h} ÷ {other} = {nfmt(result)} horas.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==h*2:r='Ese valor aumenta el tiempo al aumentar el personal; con el mismo trabajo y rendimiento la proporción es inversa.'
            elif v==h:r='Ese valor no reduce el tiempo pese a duplicarse el número de personas con igual rendimiento.'
            else:r=f'Con {other} personas durante {w} horas se realizarían {nfmt(other*v)} horas-persona, no las {workers*h} necesarias.'
            reasons[w]=r
    elif section=='Cálculo: copias a doble cara':
        pages,sets=nums;sheets=math.ceil(pages/2);result=sheets*sets
        base=f'Cada juego tiene {pages} páginas: {pages//2} hojas llenas por ambas caras y una hoja para la última página impar, en total {sheets}. Como son {sets} juegos separados: {sheets} × {sets} = {result} hojas.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==pages*sets:r='Ese valor cuenta una hoja por página como si se copiara a una cara; el enunciado pide doble cara.'
            elif v==(pages*sets)//2:r='Ese valor divide todas las páginas juntas por dos; los juegos son separados y la última página impar de cada uno necesita su propia hoja.'
            elif v==result+sets:r=f'Ese valor añade una hoja extra a cada juego; las {sheets} hojas ya incluyen la última página impar.'
            else:r=f'Los {sets} juegos necesitan {result} hojas. Con {w} no se obtiene la suma de {sheets} hojas completas por cada juego separado.'
            reasons[w]=r
    elif section=='Cálculo: descuento':
        match=re.search(r'cuesta ([\d,]+) €.* (\d+) %',prompt);assert match
        price=Decimal(match[1].replace(',','.'));percent=int(match[2]);discount=price*Decimal(percent)/100;result=price-discount
        money=lambda x:f'{x:.2f}'.replace('.',',')
        base=f'El descuento es {money(price)} × {percent}/100 = {money(discount)} €. Se resta del precio inicial: {money(price)} − {money(discount)} = {money(result)} €.'
        for w in q['wrong']:
            v=Decimal(w.replace(',','.'))
            if v==price+discount:r=f'Ese valor suma el descuento {money(discount)} € al precio, como un recargo; debe restarlo.'
            elif v==discount:r='Ese valor es sólo el importe del descuento, no el precio final a pagar.'
            else:r=f'Ese precio dejaría una reducción de {money(price-v)} €, distinta del descuento de {money(discount)} € calculado al {percent} %.'
            reasons[w]=r
    elif section=='Cálculo: tiempo':
        h,mins=nums;base=f'Cada hora tiene 60 minutos: {h} × 60 = {h*60}. Se añaden los {mins} minutos restantes: {h*60} + {mins} = {h*60+mins} minutos.'
        for w in q['wrong']:
            v=parse_num(w)
            if v==h*100+mins:r='Ese resultado trata cada hora como cien minutos; una hora equivale a sesenta.'
            elif v==h+mins:r='Ese resultado suma horas y minutos sin convertirlos primero a la misma unidad.'
            elif v==h*60+mins+60:r='Ese valor incluye una hora adicional que no aparece en el enunciado.'
            else:raise AssertionError((prompt,w))
            reasons[w]=r
    else:raise AssertionError(section)
    expected={'Cálculo: inventario':lambda:a+b-c,'Cálculo: jerarquía':lambda:a+b*(c-d),'Cálculo: signos':lambda:-a*b,'Cálculo: división y resto':lambda:rem,'Cálculo: fracciones':lambda:f+g,'Cálculo: tiempo':lambda:h*60+mins}.get(section,lambda:result)()
    assert answer==Fraction(expected),(prompt,correct,expected)
    return base,[f'Has elegido «{w}». {reasons[w]} {base}' for w in q['wrong']],{'method':'operación y contraste numérico de cada distractor','operation':base,'target':correct,'distractors':q['wrong']}
