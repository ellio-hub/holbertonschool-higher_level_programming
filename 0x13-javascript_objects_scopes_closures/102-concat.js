#!/usr/bin/node
const fs = require('fs');
const f1p = process.argv[2];
const f2p = process.argv[3];
const f3p = process.argv[4];
const f1 = fs.readfsSync(f1p);
const f2 = fs.readfsSync(f2p);
fs.writefsSync(f3p, f1 + f2);
