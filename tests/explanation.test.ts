import { test } from 'node:test';
import assert from 'node:assert/strict';
import { explainAnswer } from '../src/explanation.ts';
import type { Question } from '../src/quiz.ts';
test('al fallar muestra la razón correspondiente a la opción elegida, también si se pide la asociación incorrecta', () => {
  const question: Question & { optionExplanations: [string,string,string,string] } = {
    id: 'negativa', topic:7, section:'Documentos', prompt:'Señala la asociación incorrecta.',
    options:['Informe → decisión','Acta → constancia','Oficio → transmisión','Resolución → decisión'], answer:0,
    explanation:'Informe es juicio, no decisión.', format:'relación',source:{kind:'manual',label:'Temario',reference:'PDF 193–197'},
    optionExplanations:['Informe es juicio, no decisión.','Acta acredita hechos: esta asociación es verdadera; se pedía la incorrecta.','Oficio comunica: esta asociación es verdadera; se pedía la incorrecta.','Resolución expresa una decisión: esta asociación es verdadera; se pedía la incorrecta.']
  };
  assert.equal(explainAnswer(question,1),question.optionExplanations[1]);
  assert.equal(explainAnswer(question,2),question.optionExplanations[2]);
});
test('evita cruces de asociaciones entre categorías que se solapan y distingue definición específica de propiedad compartida', () => {
 const bank = JSON.parse(readFileSync(new URL('../public/questions.json',import.meta.url),'utf8')) as Question[];
 const sections = ['Informática: componentes','Aritmética: conjuntos y propiedades','Igualdad: discriminación y protección','PRL: ámbito de aplicación'];
 for (const q of bank.filter(q=>sections.includes(q.section))) {
   assert.ok(!q.prompt.startsWith('En «') && !q.prompt.startsWith('Al repasar «'),q.id);
   if (q.section === 'PRL: ámbito de aplicación') assert.equal(q.format,'concepto',q.id);
   if (q.prompt.includes('específica ofrece el temario de software')) {
     assert.ok(!q.options.includes('Programación incorporada al dispositivo') && !q.options.includes('Comunicación entre sistema operativo y dispositivo'));
   }
 }
});
import { readFileSync } from 'node:fs';
test('las 3.000 preguntas explican por separado sus cuatro opciones sin repetir la explicación del acierto en los fallos', () => {
 const bank = JSON.parse(readFileSync(new URL('../public/questions.json',import.meta.url),'utf8')) as Question[];
 for (const question of bank) {
   assert.equal(question.optionExplanations?.length,4,question.id);
   assert.equal(new Set(question.optionExplanations).size,4,question.id);
   assert.equal(question.optionExplanations?.[question.answer],question.explanation,question.id);
   question.optionExplanations?.forEach((reason,i) => {
     assert.ok(reason.length >= 60,`${question.id} ${i}`);
     if (i !== question.answer) assert.ok(reason.includes(question.options[i]!),`${question.id} no explica la opción ${i}`);
   });
 }
});
test('cada alternativa legal tiene un contraste concreto en lugar de un mensaje genérico de sustitución', () => {
 const bank = JSON.parse(readFileSync(new URL('../public/questions.json',import.meta.url),'utf8')) as Question[];
 for (const q of bank.filter(q=>q.format==='literal')) {
   for (const reason of q.optionExplanations!) assert.ok(!reason.includes('otro destinatario, finalidad o instrumento'),q.id);
 }
});
test('interpreta el término legal dentro de la frase: conserva negaciones y la revisión de oficio solicitada por interesados', () => {
 const bank = JSON.parse(readFileSync(new URL('../public/questions.json',import.meta.url),'utf8')) as Question[];
 const cost = bank.find(q=>q.prompt.includes('El coste de las medidas') && q.options[q.answer]==='deberá')!;
 assert.ok(cost.explanation.includes('negación'),cost.id);
 assert.ok(!cost.explanation.includes('obligación de realizar la actuación'),cost.id);
 const review = bank.find(q=>q.prompt.includes('revisión ____ iniciados a solicitud'))!;
 assert.ok(review.explanation.includes('solicitud'),review.id);
 assert.ok(!review.explanation.includes('iniciativa de la propia Administración'),review.id);
});
test('las explicaciones numéricas legales identifican la magnitud en vez de mezclar cifras, plazos y porcentajes', () => {
 const bank = JSON.parse(readFileSync(new URL('../public/questions.json',import.meta.url),'utf8')) as Question[];
 for (const q of bank.filter(q=>q.format==='literal')) {
   for (const reason of q.optionExplanations) assert.ok(!reason.includes('la cifra, el plazo o el porcentaje'),q.id);
 }
});
