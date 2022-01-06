
const getPermutations = function(arr,selectNumber) {
  const results = [];
  if(selectNumber === 1){
    return arr.map((value)=>[value]);
  }
  arr.forEach((fixed,index,origin) => {
    const rest = [...origin.slice(0,index),...origin.slice(index + 1)]; // 현위치 인덱스 다음부터 끝까지
    const permutations = getPermutations(rest,selectNumber-1);
    const attached = permutations.map((permutations)=>[fixed,...permutations]);
    results.push(...attached);
  });

  return results;
}

const stages1 = [2, 1, 2, 6, 2, 4, 3, 3];
const set = new Set();
stages1.forEach((el)=>{
  set.add(el);
})
const arr = Array.from(set);
console.log(arr);
console.log(getPermutations(arr,3));