// gta6-meme-x-01 entry (Node 22, standard library only).
// Copies POST.json (the X post's address) from beside this file to the
// output directory, plus the meme picture itself. No network, no wall
// clock, no files outside the repository; both runs write the same bytes.
// Run the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = fileURLToPath(new URL('.', import.meta.url));
const botDir = process.env.MAKEFUN_BOT_DIR ?? here;
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });
copyFileSync(join(botDir, 'POST.json'), join(outDir, 'POST.json'));
if (existsSync(join(botDir, 'meme.png'))) {
  copyFileSync(join(botDir, 'meme.png'), join(outDir, 'meme.png'));
}
