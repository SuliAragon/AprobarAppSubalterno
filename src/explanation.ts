import type { Question } from './quiz.ts';
export function explainAnswer(question: Question, chosen: number): string {
  if (!Number.isInteger(chosen) || chosen < 0 || chosen > 3) throw new RangeError('Respuesta inválida');
  return question.optionExplanations[chosen]!;
}
