const set = new Set();

set.add(1);
set.add(2);
set.add(2);

console.log(set.has(1));
console.log(set.has(2));
console.log(set.has(3));
console.log(set);
