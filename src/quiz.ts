export type Question = {
  id: string;
  topic: number;
  section: string;
  prompt: string;
  options: [string, string, string, string];
  answer: 0 | 1 | 2 | 3;
  explanation: string;
  source: { kind: 'manual' | 'exam-adapted'; label: string; reference: string; url?: string };
  format: 'concepto' | 'relación' | 'literal' | 'supuesto' | 'cálculo' | 'examen';
};
export function selectQuestions(bank: readonly Question[], topics: readonly number[], count: number, random: () => number = Math.random): Question[] {
  if (!Number.isInteger(count) || count < 0) throw new RangeError('Número de preguntas inválido');
  const selectedTopics = new Set(topics);
  const pool = bank.filter(question => selectedTopics.has(question.topic));
  for (let i = pool.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1));
    const item = pool[i]!;
    pool[i] = pool[j]!;
    pool[j] = item;
  }
  return pool.slice(0, count);
}
export function gradeAnswer(question: Question, chosen: number): { correct: boolean; correctIndex: number } {
  if (!Number.isInteger(chosen) || chosen < 0 || chosen > 3) throw new RangeError('Respuesta inválida');
  return { correct: chosen === question.answer, correctIndex: question.answer };
}
export type AnswerRecord = { questionId: string; chosen: number; correct: boolean };
export function summarizeAnswers(answers: readonly AnswerRecord[]): { correct: number; wrong: number; percent: number } {
  const correct = answers.filter(answer => answer.correct).length;
  return { correct, wrong: answers.length - correct, percent: answers.length ? Math.round(correct / answers.length * 100) : 0 };
}
export class QuizSession {
  questions: readonly Question[];
  index = 0;
  answers: AnswerRecord[] = [];
  constructor(questions: readonly Question[]) {
    if (!questions.length) throw new Error('Selecciona al menos una pregunta.');
    this.questions = [...questions];
  }
  get current(): Question { return this.questions[this.index]!; }
  get answered(): boolean { return this.answers.length > this.index; }
  answer(chosen: number): boolean {
    if (this.answered) return false;
    this.answers.push({ questionId: this.current.id, chosen, correct: gradeAnswer(this.current, chosen).correct });
    return true;
  }
  next(): boolean {
    if (!this.answered || this.index === this.questions.length - 1) return false;
    this.index++;
    return true;
  }
}
