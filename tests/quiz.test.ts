import { test } from 'node:test';
import assert from 'node:assert/strict';
import { selectQuestions, type Question } from '../src/quiz.ts';
const q = (id: string, topic: number): Question => ({ id, topic, section: 'Prueba', prompt: id, options: ['A','B','C','D'], answer: 0, explanation: 'Explicación', optionExplanations: ['Explicación','Error B','Error C','Error D'], source: {kind:'manual',label:'Temario',reference:'p. 6'}, format:'concepto' });
test('selecciona sólo los temas pedidos, sin repeticiones y sin alterar el banco', () => {
  const bank=[q('a',1),q('b',2),q('c',1),q('d',3)];
  const original=bank.map(item=>item.id);
  const selected=selectQuestions(bank,[1],10,()=>0);
  assert.equal(selected.length,2);
  assert.ok(selected.every(item=>item.topic===1));
  assert.equal(new Set(selected.map(item=>item.id)).size,2);
  assert.deepEqual(bank.map(item=>item.id),original);
});
test('corrige por índice real, distingue letras y rechaza elecciones fuera de rango', async () => {
  const { gradeAnswer } = await import('../src/quiz.ts');
  const question = {...q('letra-c',1),answer:2 as const};
  assert.deepEqual(gradeAnswer(question,2),{correct:true,correctIndex:2});
  assert.deepEqual(gradeAnswer(question,0),{correct:false,correctIndex:2});
  assert.throws(()=>gradeAnswer(question,-1),RangeError);
});
test('el resultado refleja aciertos y fallos sin penalización oculta', async () => {
  const {summarizeAnswers}=await import('../src/quiz.ts');
  assert.deepEqual(summarizeAnswers([
    {questionId:'a',chosen:0,correct:true},
    {questionId:'b',chosen:1,correct:false},
    {questionId:'c',chosen:2,correct:false}
  ]),{correct:1,wrong:2,percent:33});
  assert.deepEqual(summarizeAnswers([]),{correct:0,wrong:0,percent:0});
});
import { QuizSession, summarizeAnswers } from '../src/quiz.ts';
test('bloquea una respuesta corregida y sólo avanza después de responder', () => {
 const session = new QuizSession([{...q('uno',1),answer:2}, {...q('dos',2),answer:1}]);
 assert.equal(session.next(),false);
 assert.equal(session.answer(2),true);
 assert.equal(session.answer(0),false);
 assert.equal(session.answers.length,1);
 assert.equal(session.answers[0]?.correct,true);
 assert.equal(session.next(),true);
 assert.equal(session.current.id,'dos');
 assert.equal(session.answer(0),true);
 assert.equal(session.next(),false);
 assert.deepEqual(summarizeAnswers(session.answers),{correct:1,wrong:1,percent:50});
});
