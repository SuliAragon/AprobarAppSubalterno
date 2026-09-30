"""Distractores específicos para ámbitos solapados; evita equiparar tabla y exclusividad."""
SPECIFIC_SECTIONS={'Informática: componentes','Aritmética: conjuntos y propiedades','Igualdad: discriminación y protección'}
SCOPE='PRL: ámbito de aplicación'
SCOPE_DISTRACTORS={
'las relaciones laborales ordinarias':[
 ('Exclusión por trabajar en empresa privada','El artículo 3 incluye las relaciones laborales ordinarias; el carácter privado de la empresa no las excluye.'),
 ('Aplicación sólo después de sufrir un accidente','La prevención se aplica antes de que exista daño; no se condiciona a un accidente previo.'),
 ('Aplicación sólo si la empresa la acepta voluntariamente','La aplicación no depende de una aceptación voluntaria de la empresa.')],
'el personal administrativo o estatutario público':[
 ('Exclusión de todo el personal por pertenecer a una Administración','El artículo 3 incluye relaciones administrativas o estatutarias con sus particularidades; ser empleado público no supone exclusión general.'),
 ('Aplicación sólo a quienes tengan contrato laboral privado','La inclusión alcanza relaciones administrativas o estatutarias, no únicamente contratos laborales.'),
 ('Prevención únicamente cuando el empleado pague las medidas','Las medidas preventivas no pueden condicionarse al pago por el personal; el ámbito incluye esta relación pública.')],
'los socios trabajadores de cooperativas':[
 ('Exclusión automática por ser socios y no asalariados','La ley incluye a los socios de cooperativas cuando prestan trabajo personal; ser socio no basta para excluirlos.'),
 ('Inclusión sólo de socios que no prestan trabajo personal','El presupuesto citado es precisamente que el socio preste trabajo personal.'),
 ('Aplicación únicamente si la cooperativa pertenece al Estado','La regla de inclusión no exige titularidad estatal de la cooperativa.')],
'actividades policiales cuyas particularidades impiden aplicar la ley':[
 ('Exclusión de cualquier actividad de cualquier empleado policial','La excepción depende de las particularidades que impiden aplicar la ley a la actividad; no excluye en bloque al personal policial.'),
 ('Ausencia de cualquier principio preventivo en estas actividades','La ley inspira la normativa específica destinada a proteger a las personas en estas actividades; la excepción no elimina los principios preventivos.'),
 ('Aplicación ordinaria sin atender a las particularidades descritas','El enunciado dice que las particularidades impiden esa aplicación; corresponde regulación específica inspirada en los principios de la ley.')],
'actividades militares de Fuerzas Armadas o Guardia Civil':[
 ('Exclusión de todo trabajo civil realizado en un establecimiento militar','La exclusión citada se refiere a actividades militares; los establecimientos militares tienen otra regla de aplicación con especialidades.'),
 ('Aplicación general idéntica, sin la exclusión del artículo 3','El artículo 3 enumera las actividades militares de Fuerzas Armadas y Guardia Civil dentro de los supuestos excluidos en sus términos.'),
 ('Exclusión general de cualquier centro penitenciario','Los centros penitenciarios tienen una regla de adaptación; no son el supuesto de actividades militares que pregunta el enunciado.')],
'protección civil en grave riesgo o catástrofe incompatible con ley':[
 ('Exclusión de toda actividad de protección civil sin condiciones','La excepción se refiere a actividades cuyas particularidades impiden la aplicación en los supuestos de grave riesgo, catástrofe o calamidad pública.'),
 ('Aplicación general sin atender a la incompatibilidad de la actividad','El supuesto descrito es precisamente la excepción por particularidades que impiden aplicar la ley; no puede ignorarse esa condición.'),
 ('Exclusión de todo trabajador por existir cualquier riesgo leve','La excepción no se activa por cualquier riesgo leve de cualquier trabajador, sino por el ámbito y las particularidades que describe el artículo 3.')],
'los establecimientos militares':[
 ('Exclusión automática de toda actividad por la ubicación militar','El artículo 3 prevé aplicación con particularidades para establecimientos militares; no los excluye en bloque por su ubicación.'),
 ('Aplicación sólo a empresas privadas sin incluir estos establecimientos','La ley incluye expresamente los establecimientos militares con sus particularidades.'),
 ('Aplicación idéntica sin posibilidad de normativa específica','El manual señala especialidades previstas en la normativa específica; negar esas particularidades altera la regla.')],
'los centros penitenciarios':[
 ('Exclusión automática de todo el personal penitenciario','El artículo 3 prevé adaptación de actividades en centros penitenciarios; no una exclusión automática de todo su personal.'),
 ('Aplicación sin ninguna posibilidad de adaptación','El manual contempla adaptación para actividades cuyas características justifiquen regulación especial en los términos de la ley.'),
 ('Aplicación únicamente a las actividades militares','La regla pregunta por centros penitenciarios, que tienen una adaptación propia y no se identifican con las actividades militares.')],
}

def safe_values(g,key,value):
    rows=g['rows']
    if g['section']==SCOPE:return [v for v,reason in SCOPE_DISTRACTORS[key]]
    exclude={value}
    if g['section']=='Informática: componentes':
        if key=='software':exclude.update(['Programación incorporada al dispositivo','Comunicación entre sistema operativo y dispositivo'])
        elif key=='hardware':return [v for k,v in rows if k in ['software','firmware','controlador o driver']]
        else:exclude.update(['Elementos físicos del equipo','Programas e instrucciones lógicas'])
    if g['section']=='Igualdad: discriminación y protección':
        if key=='la discriminación directa':exclude.add('Discriminación directa por razón de sexo')
        if key=='la discriminación por embarazo o maternidad':exclude.add('Trato menos favorable por sexo en situación comparable')
    return list(dict.fromkeys(v for k,v in rows if v not in exclude))
