import type { Question } from './quiz.ts';
export function validateBank(data: unknown): Question[] {
  if (!Array.isArray(data) || data.length !== 3000) throw new Error('El banco debe contener 3.000 preguntas.');
  const ids = new Set<string>();
  const letters = [0, 0, 0, 0];
  const topics = new Set<number>();
  for (const raw of data) {
    const q = raw as Question | null;
    if (!q || typeof q !== 'object' || typeof q.id !== 'string' || ids.has(q.id) || !q.id) throw new Error('Identificador de pregunta inválido.');
    if (!Array.isArray(q.options) || q.options.length !== 4 || q.options.some(o => typeof o !== 'string' || !o.trim()) || new Set(q.options.map(o => o.trim().toLocaleLowerCase('es'))).size !== 4) throw new Error('Cada pregunta debe tener cuatro opciones diferentes.');
    if (!Number.isInteger(q.answer) || q.answer < 0 || q.answer > 3 || !Number.isInteger(q.topic) || q.topic < 1 || q.topic > 10) throw new Error('Respuesta o tema inválido.');
    if ([q.prompt, q.explanation, q.section, q.source?.reference, q.source?.label].some(s => typeof s !== 'string' || !s.trim()) || !['manual', 'exam-adapted'].includes(q.source?.kind)) throw new Error('Falta el enunciado, la explicación o la fuente.');
    if (!Array.isArray(q.optionExplanations) || q.optionExplanations.length !== 4 || q.optionExplanations.some(s => typeof s !== 'string' || !s.trim()) || new Set(q.optionExplanations).size !== 4 || q.optionExplanations[q.answer] !== q.explanation) throw new Error('Faltan explicaciones específicas y coherentes para las cuatro opciones.');
    ids.add(q.id); topics.add(q.topic); letters[q.answer]!++;
  }
  if (topics.size !== 10 || letters.some(n => n !== 750)) throw new Error('El banco debe cubrir diez temas y tener 750 respuestas por letra.');
  return data as Question[];
}
