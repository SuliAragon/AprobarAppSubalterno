import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { validateBank } from '../src/bank.ts';
test('rechaza un banco incompleto o una opción duplicada antes de iniciar un test', () => {
 assert.throws(() => validateBank([]), /3.000/);
 const bank = JSON.parse(readFileSync(new URL('../public/questions.json', import.meta.url),'utf8'));
 bank[0].options[1] = bank[0].options[0];
 assert.throws(() => validateBank(bank), /opciones/);
});
test('rechaza explicaciones por opción ausentes, vacías, repetidas o que no coincidan con el acierto', () => {
 const original = JSON.parse(readFileSync(new URL('../public/questions.json', import.meta.url),'utf8'));
 for (const invalid of [undefined, ['a','','c','d'], ['igual','igual','igual','igual'], ['a','b','c','d']]) {
   const bank = structuredClone(original);
   bank[0].optionExplanations = invalid;
   assert.throws(() => validateBank(bank), /explicaciones/,String(invalid));
 }
});
