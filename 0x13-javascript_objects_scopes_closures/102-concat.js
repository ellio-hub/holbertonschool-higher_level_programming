#!/usr/bin/node
const fs = require('fs');
const f1p = process.argv[2];
const f2p = process.argv[3];
const f3p = process.argv[4];
const f1 = fs.readFileSync(f1p, 'utf-8');
const f2 = fs.readFileSync(f2p, 'utf-8');
fs.writeFileSync(f3p, f1 + f2);
