#!/usr/bin/node
const fs = require('fs');
const f1p = process.argv[2];
const f2p = process.argv[3];
const f3p = process.argv[4];
const f1 = fs.readfileSync(f1p);
const f2 = fs.readfileSync(f2p);
fs.writefileSync(f3p, f1 + f2);
