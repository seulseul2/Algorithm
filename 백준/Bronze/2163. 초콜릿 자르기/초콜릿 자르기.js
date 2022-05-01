const fs = require('fs');
const inputData = fs.readFileSync(0, 'utf8').toString().split(' ');

const A = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

const x = A-1
const y = (B-1) * A
console.log(x+y);