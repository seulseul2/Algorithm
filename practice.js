const fs = require('fs');
for (i=0; i<5; i++) {
    const inputData = fs.readFileSync(0, 'utf8').toString();
    console.log(inputData)
}


const N = parseInt(inputData[0]);
const B = parseInt(inputData[1]);

const x = A-1
const y = (B-1) * A
console.log(x+y);