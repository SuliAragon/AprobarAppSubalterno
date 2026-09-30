import './style.css';
import { validateBank } from './bank.ts';
import { explainAnswer } from './explanation.ts';
import { QuizSession, selectQuestions, summarizeAnswers, type Question } from './quiz.ts';

const topics = [
  ['Constitución Española', 'Principios, derechos y garantías'],
  ['Igualdad y violencia de género', 'Normativa estatal, andaluza y protocolo'],
  ['Prevención de riesgos laborales', 'Seguridad, protección y acción preventiva'],
  ['Atención a la ciudadanía', 'Información y procedimiento administrativo'],
  ['Actos y notificaciones', 'Eficacia, plazos e invalidez de los actos'],
  ['Organización municipal', 'Áreas, delegaciones, organismos y sedes'],
  ['Documentos y archivos', 'Clasificación, ordenación y conservación'],
  ['Ortografía y cálculo', 'Lengua, operaciones y supuestos numéricos'],
  ['Informática y reprografía', 'Equipos, correo, digitalización y máquinas'],
  ['Conoce Cádiz', 'Historia, patrimonio, cultura y fiestas'],
];
const letters = ['A', 'B', 'C', 'D'];
const app = document.querySelector<HTMLDivElement>('#app')!;
let bank: Question[] = [];
let selected = new Set<number>();
let whole = true;
let count = 30;
let session: QuizSession | undefined;
let phase: 'home' | 'quiz' | 'results' = 'home';
let retryMode = false;
const escape = (s: string) => s.replace(/[&<>"']/g, ch => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[ch]!));
const number = (n: number) => n.toLocaleString('es-ES');
const activeTopics = () => whole ? topics.map((_, i) => i + 1) : [...selected];
const available = () => bank.filter(q => activeTopics().includes(q.topic)).length;
const allSelected = () => whole;
function focus(selector: string) { document.querySelector<HTMLElement>(selector)?.focus({ preventScroll: true }); }
function top() { window.scrollTo({ top: 0, behavior: 'instant' }); }
function source(q: Question) {
  const link = q.source.url && /^https:\/\/institucional\.cadiz\.es\//.test(q.source.url) ? ` · <a href="${escape(q.source.url)}" target="_blank" rel="noopener noreferrer">Ver examen ↗</a>` : '';
  return `<p class="source">${escape(q.source.label)} · ${escape(q.source.reference)}${link}</p>`;
}
function renderHome() {
  phase = 'home';
  app.innerHTML = `<div class="intro"><div><p class="eyebrow">UN POCO CADA DÍA, UN PASO MÁS CERCA</p><h1 tabindex="-1">Prepara tu test<span class="title-dot">.</span></h1><p class="lead">Elige qué repasar. Responde a tu ritmo y aprende de cada fallo.</p></div><div class="bank-count"><strong>3.000</strong><span>preguntas · 10 temas</span></div></div>
  <div class="setup"><section aria-labelledby="topics-title"><div class="section-head"><h2 id="topics-title">01 <span>¿Qué quieres repasar?</span></h2><button class="text-button" id="all" aria-pressed="${allSelected()}">Todo el temario ${allSelected() ? '✓' : '+'}</button></div><p class="section-note">Puedes seleccionar uno o varios temas.</p>
  <div class="topic-grid">${topics.map(([name, description], i) => `<label class="topic ${(!whole && selected.has(i + 1)) ? 'selected' : ''}"><input type="checkbox" value="${i + 1}" ${(!whole && selected.has(i + 1)) ? 'checked' : ''}><span class="topic-number">${String(i + 1).padStart(2, '0')}</span><span class="topic-info"><strong>${name}</strong><span>${description}</span><small>${number(bank.filter(q => q.topic === i + 1).length)} preguntas</small></span><span class="check" aria-hidden="true">${(!whole && selected.has(i + 1)) ? '✓' : '+'}</span></label>`).join('')}</div></section>
  <aside class="setup-side"><section class="test-config" aria-labelledby="length-title"><p class="eyebrow">A TU RITMO</p><h2 id="length-title">Tu próxima sesión</h2><div class="selection-summary"><span>Materia seleccionada</span><strong id="selection-label">${allSelected() ? 'Todo el temario' : `${selected.size} ${selected.size === 1 ? 'tema' : 'temas'}`}</strong><small>${number(available())} preguntas disponibles</small></div><label class="count-label" for="count">Número de preguntas</label><div class="presets">${[10,20,30,60].map(n => `<button data-count="${n}" class="preset ${count === n ? 'active' : ''}" aria-pressed="${count === n}">${n}</button>`).join('')}</div><div class="count-custom"><input id="count" type="number" min="1" max="${available()}" value="${count}" inputmode="numeric" aria-describedby="count-help"><span>preguntas</span></div><p id="count-help" class="config-help">${available() ? `De 1 a ${number(available())}. Sin límite de tiempo.` : "Selecciona al menos un tema para empezar."}</p><button id="start" class="primary" ${!activeTopics().length || count > available() || count < 1 || !Number.isInteger(count) ? 'disabled' : ''}>Empezar test <span aria-hidden="true">→</span></button><p class="config-bottom">Orden aleatorio · Corrección al responder</p></section><div class="study-note"><span class="note-icon" aria-hidden="true">↗</span><div><strong>Que cada pregunta cuente.</strong><p>Al responder verás la explicación y su fuente. Al terminar podrás repetir sólo tus fallos.</p></div></div><details class="about"><summary>Sobre las preguntas</summary><p>Banco basado en los diez temas de tus apuntes de septiembre de 2026. Incluye 57 adaptaciones identificadas de exámenes oficiales de Cádiz de 2024 y 2025, y preguntas de elaboración propia.</p><p>Hay preguntas de conceptos, relaciones, texto legal y supuestos. Se conservan los datos municipales del manual. El banco completo reparte las respuestas correctas por igual: 750 A, 750 B, 750 C y 750 D. Cada test aleatorio puede tener un reparto distinto.</p></details></aside></div>`;
  app.querySelectorAll<HTMLInputElement>('.topic input').forEach(input => input.addEventListener('change', () => {
    const topic = Number(input.value);
    if (whole) { whole = false; selected = new Set([topic]); }
    else if (input.checked) selected.add(topic);
    else selected.delete(topic);
    renderHome(); focus(`.topic input[value="${topic}"]`);
  }));
  app.querySelector('#all')!.addEventListener('click', () => { whole = true; selected.clear(); renderHome(); focus('#all'); });
  app.querySelectorAll<HTMLButtonElement>('[data-count]').forEach(button => button.addEventListener('click', () => { count = Number(button.dataset.count); renderHome(); focus(`[data-count="${count}"]`); }));
  app.querySelector<HTMLInputElement>('#count')!.addEventListener('input', event => {
    const input = event.target as HTMLInputElement;
    count = input.valueAsNumber;
    const valid = activeTopics().length > 0 && Number.isInteger(count) && count >= 1 && count <= available();
    app.querySelector<HTMLButtonElement>('#start')!.disabled = !valid;
    app.querySelectorAll<HTMLButtonElement>('[data-count]').forEach(b => { b.classList.toggle('active', Number(b.dataset.count) === count); b.setAttribute('aria-pressed', String(Number(b.dataset.count) === count)); });
    input.setAttribute('aria-invalid', String(!valid));
  });
  app.querySelector('#start')!.addEventListener('click', () => start(selectQuestions(bank, activeTopics(), count)));
}
function start(questions: Question[], retry = false) {
  session = new QuizSession(questions); retryMode = retry; phase = 'quiz'; renderQuiz(); top(); focus('#question');
}
function choose(chosen: number) {
  if (phase !== 'quiz' || !session?.answer(chosen)) return;
  renderQuiz(); focus('#feedback');
}
function next() {
  if (phase !== 'quiz' || !session?.answered) return;
  if (session.next()) { renderQuiz(); top(); focus('#question'); }
  else { renderResults(); top(); focus('#result-title'); }
}
function renderQuiz() {
  const s = session!;
  const q = s.current;
  const record = s.answers[s.index];
  const totals = summarizeAnswers(s.answers);
  app.innerHTML = `<div class="quiz-top"><button class="text-button" id="leave">← Cambiar test</button><span>${retryMode ? 'REPASO DE FALLOS' : 'SESIÓN DE ESTUDIO'}</span><div class="live-score"><span class="good">${totals.correct} ${totals.correct === 1 ? "acierto" : "aciertos"}</span><span class="bad">${totals.wrong} ${totals.wrong === 1 ? "fallo" : "fallos"}</span></div></div><section class="quiz-shell" aria-label="Test"><div class="progress-head"><span>Pregunta <strong>${s.index + 1}</strong> de ${s.questions.length}</span><span>${Math.round(s.answers.length / s.questions.length * 100)} % completado</span></div><progress value="${s.answers.length}" max="${s.questions.length}" aria-label="Preguntas respondidas"></progress><div class="question-area"><div class="question-tags"><span class="tag">TEMA ${String(q.topic).padStart(2,'0')} · ${escape(topics[q.topic - 1]![0]!)}</span>${q.source.kind === 'exam-adapted' ? '<span class="tag exam-tag">EXAMEN OFICIAL · ADAPTACIÓN</span>' : ''}</div><h1 id="question" tabindex="-1">${escape(q.prompt)}</h1><p class="answer-hint">${record ? 'Respuesta registrada. Revisa la explicación y continúa.' : 'Selecciona una respuesta. Sólo una opción es correcta.'}</p><div class="options">${q.options.map((option, i) => {
    const correct = !!record && i === q.answer;
    const wrong = !!record && i === record.chosen && !record.correct;
    return `<button class="option ${correct ? 'correct' : ''} ${wrong ? 'wrong' : ''}" data-answer="${i}" ${record ? 'disabled' : ''}><span class="letter">${letters[i]}</span><span class="option-text">${escape(option)}</span>${correct || wrong ? `<span class="answer-state">${correct ? '✓ Correcta' : '✕ Tu respuesta'}</span>` : ''}</button>`;
  }).join('')}</div>${record ? `<div id="feedback" class="feedback ${record.correct ? 'success' : 'failure'}" role="status" tabindex="-1"><strong>${record.correct ? '✓ Has acertado' : `✕ Has fallado · La correcta es ${letters[q.answer]}`}</strong><p>${escape(explainAnswer(q, record.chosen))}</p>${source(q)}</div>` : ''}<div class="question-bottom"><span class="keyboard">Teclado: 1–4 para responder · Intro para continuar</span><button class="primary next" id="next" ${!record ? 'disabled' : ''}>${s.index === s.questions.length - 1 ? 'Ver resultado' : 'Siguiente pregunta'} <span aria-hidden="true">→</span></button></div></div></section>`;
  app.querySelectorAll<HTMLButtonElement>('[data-answer]').forEach(button => button.addEventListener('click', () => choose(Number(button.dataset.answer))));
  app.querySelector('#next')!.addEventListener('click', next);
  app.querySelector('#leave')!.addEventListener('click', () => {
    const dialog = document.createElement('dialog');
    dialog.innerHTML = '<h2>Cambiar de test</h2><p>Esta sesión terminará y volverás a la selección de temas.</p><div class="dialog-actions"><button class="secondary" id="keep">Seguir estudiando</button><button class="primary" id="exit">Cambiar test</button></div>';
    document.body.append(dialog); dialog.showModal();
    dialog.querySelector('#keep')!.addEventListener('click', () => dialog.close());
    dialog.querySelector('#exit')!.addEventListener('click', () => { dialog.close(); renderHome(); top(); focus('h1'); });
    dialog.addEventListener('close', () => dialog.remove());
  });
}
function renderResults() {
  phase = 'results';
  const s = session!;
  const result = summarizeAnswers(s.answers);
  const failed = s.questions.filter((_, i) => !s.answers[i]!.correct);
  app.innerHTML = `<section class="result-header"><p class="eyebrow">SESIÓN COMPLETADA</p><h1 id="result-title" tabindex="-1">${failed.length ? 'Cada fallo es un nuevo repaso.' : '¡Pleno de aciertos!'}</h1><p class="lead">Has respondido ${s.questions.length} ${s.questions.length === 1 ? 'pregunta' : 'preguntas'}. Sigue construyendo lo que sabes.</p><div class="result-stats"><div class="percent"><strong>${result.percent}<small>%</small></strong><span>de aciertos</span></div><div><strong class="good">${result.correct}</strong><span>Aciertos</span></div><div><strong class="bad">${result.wrong}</strong><span>Fallos</span></div></div><div class="result-actions">${failed.length ? '<button id="retry-wrong" class="primary">Repasar mis fallos ↗</button>' : ''}<button id="new-test" class="${failed.length ? 'secondary' : 'primary'}">Nuevo test aleatorio</button><button id="configure" class="text-button">Elegir otros temas →</button></div></section><section class="review" aria-labelledby="review-title"><div class="section-head"><h2 id="review-title">${failed.length ? 'Tus fallos, explicados' : 'Todo correcto en esta sesión'}</h2><span>${failed.length ? `${failed.length} para repasar` : 'Buen trabajo'}</span></div>${s.questions.map((q, i) => {
    const a = s.answers[i]!;
    if (a.correct) return '';
    return `<details class="review-item"><summary><span class="review-number">${i + 1}</span><span>${escape(q.prompt)}</span><span class="review-plus" aria-hidden="true">+</span></summary><div class="review-body"><p class="bad"><strong>Tu respuesta ${letters[a.chosen]}:</strong> ${escape(q.options[a.chosen]!)}</p><p class="good"><strong>Correcta ${letters[q.answer]}:</strong> ${escape(q.options[q.answer])}</p><p>${escape(explainAnswer(q, a.chosen))}</p>${source(q)}</div></details>`;
  }).join('')}</section>`;
  app.querySelector('#retry-wrong')?.addEventListener('click', () => start(selectQuestions(failed, topics.map((_, i) => i + 1), failed.length), true));
  app.querySelector('#new-test')!.addEventListener('click', () => start(selectQuestions(bank, activeTopics(), count)));
  app.querySelector('#configure')!.addEventListener('click', () => { renderHome(); top(); focus('h1'); });
}
document.addEventListener('keydown', event => {
  if (phase !== 'quiz' || document.querySelector('dialog[open]') || event.ctrlKey || event.metaKey || event.altKey || ['INPUT','TEXTAREA','SELECT'].includes((event.target as HTMLElement).tagName)) return;
  if (/^[1-4]$/.test(event.key)) { event.preventDefault(); choose(Number(event.key) - 1); }
  // Buttons already activate on Enter; don't advance again after an option click.
  if (event.key === 'Enter' && !(event.target instanceof HTMLButtonElement) && !(event.target instanceof HTMLAnchorElement)) { event.preventDefault(); next(); }
});
async function load() {
  app.innerHTML = '<p role="status" class="loading">Cargando tus 3.000 preguntas…</p>';
  try {
    const response = await fetch(`${import.meta.env.BASE_URL}questions.json`);
    if (!response.ok) throw new Error('No se ha podido descargar el banco.');
    bank = validateBank(await response.json()); renderHome();
  } catch {
    app.innerHTML = '<section class="load-error" role="alert"><h1>No se han podido cargar las preguntas</h1><p>Comprueba tu conexión y vuelve a intentarlo.</p><button id="reload" class="primary">Volver a cargar</button></section>';
    app.querySelector('#reload')!.addEventListener('click', load);
  }
}
void load();
