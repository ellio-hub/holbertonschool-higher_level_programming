#!/usr/bin/node
let a = 'C is fun\nPython is cool\nJavaScript is amazing\n';
let i;
for (i = 0; a[i]; i++) {
    process.stdout.write(a[i]);
}
