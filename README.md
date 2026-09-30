# Aprobar · Subalterno Cádiz

Web de estudio para el temario de Subalterno del Ayuntamiento de Cádiz, edición aportada de septiembre de 2026.

**Web:** https://suliaragon.github.io/AprobarAppSubalterno/

## Usar la web

Elige todo el temario o marca uno o varios temas. Indica entre una pregunta y el número disponible en tu selección, y empieza. Cada sesión mezcla las preguntas sin repetirlas. Las cuatro opciones conservan sus letras; al responder se señala el acierto o el fallo, se bloquea la elección y aparece la explicación con su referencia al manual o al examen.

El resultado muestra aciertos, fallos y porcentaje sin penalización. Puedes abrir cada fallo, repetir sólo esas preguntas, iniciar otro test aleatorio o cambiar los temas. Funciona en móvil y escritorio, sin registro. Atajos: 1–4 para responder e Intro para continuar. La sesión permanece en memoria mientras la página siga abierta; recargarla inicia de nuevo.

## Banco de preguntas

| Tema | Materia | Preguntas | Correctas por letra |
|---|---|---:|---:|
| 1 | Constitución Española | 240 | 60 |
| 2 | Igualdad y violencia de género | 780 | 195 |
| 3 | Prevención de riesgos laborales | 160 | 40 |
| 4 | Atención a la ciudadanía y procedimiento | 340 | 85 |
| 5 | Actos y notificaciones | 240 | 60 |
| 6 | Organización municipal | 280 | 70 |
| 7 | Documentos y archivos | 200 | 50 |
| 8 | Ortografía y cálculo | 300 | 75 |
| 9 | Informática y reprografía | 300 | 75 |
| 10 | Historia, patrimonio y cultura de Cádiz | 160 | 40 |
| **Total** | **10 temas** | **3.000** | **750 A / 750 B / 750 C / 750 D** |

El reparto equilibrado pertenece al banco completo y a cada tema; una sesión aleatoria concreta puede tener un reparto distinto.

Contenido: 743 preguntas de conceptos, 710 de reconstrucción de texto legal, 1.314 de relaciones, 160 de cálculo, 16 supuestos y 57 adaptaciones de exámenes. Las relaciones trabajan también un mismo concepto desde perspectivas distintas: identificar su atributo, reconocer la relación correcta o detectar una incorrecta. No son 3.000 conceptos independientes. Se incluyen los 759 hechos de las fichas redactadas y reglas de 306 artículos presentes en el material. La cobertura de secciones y cifras está en `data/bank-report.json`.

El contenido municipal y normativo sigue exclusivamente el **Temario Subalterno Ayuntamiento Cádiz 2026 SEPT**, de José Miguel Montalva Ortega, facilitado por el usuario. Las referencias `PDF n` corresponden a las páginas físicas del archivo de 332 páginas. No se incorporan noticias ni actualizaciones ajenas a esos apuntes. El PDF original no se publica en este repositorio. Cuando los apuntes ofrecen datos distintos entre los temas 6 y 10, la pregunta indica el tema al que se refiere.

### Exámenes utilizados

Las adaptaciones llevan la etiqueta «EXAMEN OFICIAL · ADAPTACIÓN» y enlace al cuestionario original. Se reformulan opciones dependientes de letras, se omiten las preguntas anuladas seleccionadas y se utiliza la corrección definitiva de la pregunta 27 de 2025.

- [12 plazas, turno libre, examen del 22 de febrero de 2025](https://institucional.cadiz.es/12-plazas-de-subalternoas-turno-libre-oep-202120222023).
- [3 plazas reservadas a personas con discapacidad, examen del 22 de febrero de 2025](https://institucional.cadiz.es/3-plazas-de-subalternoas-reservadas-personas-con-discapacidad-oep-20202021). Revisado como referencia; coincide ampliamente con el anterior.
- [Cuestionario de 9 plazas de estabilización, 17 de septiembre de 2024](https://institucional.cadiz.es/sites/default/files/tablon/archivos/CUESTIONARIO%20DE%20EXAMEN%209%20SUBALTERNOS%2C%20OEP%202022%20ESTABILIZACI%C3%93N%2C%20CONCURSO-OPOSICI%C3%93N.pdf).

También se revisó el examen de interinos por oferta SAE del 31 de enero de 2024 para orientar los supuestos. Las 57 adaptaciones incluidas proceden de los cuestionarios de febrero de 2025 y septiembre de 2024; no se atribuyen a exámenes las preguntas nuevas.

## Desarrollo

Requisitos: Node.js 24 o posterior, npm; Python 3 sólo para regenerar las preguntas.

```sh
npm ci
npm run dev
```

Abrir la dirección que muestra Vite, con la ruta `/AprobarAppSubalterno/`.

```sh
npm test
npm run validate:bank
npm run build
npm run preview
```

`src/quiz.ts` contiene selección, corrección y estado de sesión; `src/main.ts` la interfaz; `public/questions.json` el banco. El banco se valida también al cargar la web: una descarga incompleta o sin sus cuatro explicaciones no permite iniciar un test. `src/explanation.ts` selecciona la explicación de la opción marcada, tanto en la corrección inmediata como en el repaso de fallos.

Para regenerar el banco con la semilla fija y conservar el reparto:

```sh
python3 scripts/build_bank.py
npm test
npm run validate:bank
```

Los hechos redactados están en `scripts/facts.py`, las adaptaciones en `scripts/exam_seeds.py`, los cálculos en `scripts/math_seeds.py` y los candidatos legales extraídos del manual en `data/legal-candidates.json`. El extractor opcional `scripts/extract_legal.py` requiere los textos privados del manual en `../tmp/pdfs/tema1.txt` a `tema5.txt`; no es necesario para construir ni publicar la web.

## Publicación

GitHub Pages, mediante `.github/workflows/deploy.yml`. Cada cambio en `main` ejecuta pruebas, valida el banco y compila antes de publicar. Configuración del repositorio: Pages → Source → GitHub Actions. La ruta base se define en `vite.config.ts`.

## Revisión de explicaciones

Cada pregunta contiene cuatro explicaciones: una para el acierto y tres para los errores concretos. Las preguntas negativas aclaran cuándo la opción marcada es verdadera pero no responde a lo pedido. Los cálculos se resuelven de nuevo al generar el banco y se contrasta cada distractor con la operación. Las adaptaciones oficiales cuentan con razones redactadas para sus 171 alternativas equivocadas.

Las reconstrucciones literales conservan las condiciones y negaciones del pasaje completo. Sus citas se cotejaron con la extracción del PDF privado; `data/legal-evidence.json` conserva la huella y las páginas físicas de cada pasaje. Se separaron comentarios didácticos de las transcripciones de artículos y se evitaron cruces de categorías que comparten propiedades. `scripts/check_literal_sources.py` permite repetir el cotejo cuando está disponible `../tmp/pdfs/temario.txt`.

`data/explanation-audit.json` identifica las 3.000 preguntas revisadas, las relaciones o cálculos usados, la fuente y las huellas de las 12.000 explicaciones por opción. Es una trazabilidad del cotejo y la generación, no una garantía de infalibilidad ni una revisión externa independiente. Los significados concretos están en `scripts/explanations.py`, `scripts/legal_distractors.py` y `scripts/exam_explanations.py`; una alternativa legal sin contraste revisado detiene la generación. El PDF original no se modifica.
