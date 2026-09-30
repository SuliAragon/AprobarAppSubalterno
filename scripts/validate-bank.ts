import { readFileSync } from 'node:fs';
import { validateBank } from '../src/bank.ts';
const bank = validateBank(JSON.parse(readFileSync(new URL('../public/questions.json', import.meta.url), 'utf8')));
const signatures = new Set(bank.map(q => JSON.stringify([q.prompt, [...q.options].sort()])));
if (signatures.size !== 3000) throw new Error('Hay preguntas duplicadas.');
for (let topic = 1; topic <= 10; topic++) {
 const questions = bank.filter(q => q.topic === topic);
 const counts = [0,1,2,3].map(letter => questions.filter(q => q.answer === letter).length);
 if (!counts.every(count => count === questions.length / 4)) throw new Error(`Reparto desigual en el tema ${topic}`);
 console.log(`Tema ${topic}: ${questions.length} preguntas; A/B/C/D: ${counts.join('/')}`);
}
console.log(`Banco válido: ${bank.length} preguntas, 750 por letra; ${bank.filter(q => q.source.kind === 'exam-adapted').length} adaptaciones de exámenes.`);
