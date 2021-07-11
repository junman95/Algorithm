const stack = [];

stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);
stack.pop();

console.log(stack);
console.log(stack[0]);
console.log(stack[stack.length -1]);
stack.forEach((each)=>{
  console.log(each)
})
for( let each=0;each<stack.length;each++){
  console.log(stack[each])
}

// [ 1, 2, 3 ]
// 1
// 3