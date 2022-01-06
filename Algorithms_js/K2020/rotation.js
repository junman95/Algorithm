const arr = [[1,2,3],[4,5,6],[7,8,9]];
const temp = arr.map(el=>el.slice());
console.log(temp);
for(let i =0;i<arr.length;i++){
  for(let j = 0; j<arr.length;j++){
    temp[i][j] = arr[arr.length-1-j][i];
  }
}
console.log(arr);
console.log(temp);

console.log(arr[4]);