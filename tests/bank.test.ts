import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import type { Question } from '../src/quiz.ts';
test('el banco tiene 3.000 preguntas únicas, cuatro opciones y 750 correctas por letra', () => {
  const bank=JSON.parse(readFileSync(new URL('../public/questions.json',import.meta.url),'utf8')) as Question[];
  assert.equal(bank.length,3000);
  assert.equal(new Set(bank.map(q=>q.id)).size,3000);
  const signatures=bank.map(q=>JSON.stringify([q.prompt,[...q.options].sort()]));
  assert.equal(new Set(signatures).size,3000);
  const letters=[0,0,0,0];
  for(const q of bank){
    assert.equal(q.options.length,4);
    assert.equal(new Set(q.options.map(s=>s.trim().toLocaleLowerCase('es'))).size,4);
    assert.ok(Number.isInteger(q.answer)&&q.answer>=0&&q.answer<4);
    assert.ok(q.prompt.trim()&&q.explanation.trim()&&q.source.reference.trim());
    assert.ok(q.topic>=1&&q.topic<=10);
    letters[q.answer]!++;
  }
  assert.deepEqual(letters,[750,750,750,750]);
  assert.equal(new Set(bank.map(q=>q.topic)).size,10);
  assert.ok(bank.some(q=>q.source.kind==='exam-adapted'));
});
