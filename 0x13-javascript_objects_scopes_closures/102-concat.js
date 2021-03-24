#!/usr/bin/node
let file;
const f1p = process.argv[2];
const f2p = process.argv[3];
const f3p = process.argv[4];
const f1 = file.readFileSync(f1p);
const f2 = file.readFileSync(f2p);
file.writeFileSync(f3p, f1 + f2);
