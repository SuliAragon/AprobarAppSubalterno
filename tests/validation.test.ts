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
