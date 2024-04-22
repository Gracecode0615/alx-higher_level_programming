#!/usr/bin/node
const me = 'C is fun';
let integer = parseInt(process.argv[2]);
if (Number.isNaN(integer)) {
  console.log('Missing number of occurrences');
} else {
  while (integer > 0) {
    console.log(me);
    integer--;
  }
}
