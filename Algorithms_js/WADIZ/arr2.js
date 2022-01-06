const arr1 = [1, 2, 4, 8, 4, 2, 1]	;
const arr2 =[1, 3, 5, 7, 6, 8, 9, 5, 1]	;
const arr3 =[10, 0, 10, 0, 10, 0]	;
const arr4 =[5, 4, 5, 4, 5, 5];

var count = 0;
function recursion(postArr,i,j,value,arr){
  console.log("시작 : -----------",arr);
  let temp_min = 0;
  let next_postArr = [];
  let next_arr = [];
  let next_i = undefined;
  let next_j = undefined;
  let next_val = Infinity;
  for(let a = 0; a<postArr.length ; a++){
    postArr[a]+=value;
    if(postArr[a]<arr[a]){
      //최소합 밸류 갱신
      if(arr[a] - postArr[a] < next_val) next_val = arr[a] - postArr[a];
      //다음 배열 생성
      next_postArr.push(postArr[a]);

      if(next_i === undefined) {
        console.log("i값 설정 : ",postArr[a],arr[a],i,a)
        next_i = a;
      }
      //끝까지  해당할때
      if(next_j === undefined && a === postArr.length - 1) {
        next_j = a;
        next_postArr = postArr.slice(next_i,next_j+1) ;
        count +=1;
        next_arr = arr.slice(next_i,next_j+1);
        console.log("끝까지 자르기",next_postArr,next_i,next_j,next_val,next_arr);
        recursion(next_postArr,next_i,next_j,next_val,next_arr);
        next_i = undefined;
        next_j = undefined;
        next_val = Infinity;
      }
    }
    //중간에 초치면
    else{
      //i값이 있을때
      if(next_i !== undefined) {
        next_j = a-1;
        next_postArr = postArr.slice(next_i,next_j+1) ;
        count +=1;
        next_arr = arr.slice(next_i,next_j+1);
        console.log("중간에 자르기" ,next_postArr,next_i,next_j,next_val,next_arr);
        recursion(next_postArr,next_i,next_j,next_val,next_arr);
        next_i = undefined;
        next_j = undefined;
        next_val = Infinity;
      }
    }
  }
  return;
}

function solution(arr) {
  var answer = -1;
  let isCheck = true;
  let postArr = Array.from({length : arr.length},()=>0);
  const arrMax = Math.max(...arr);
  console.log(postArr);
  recursion(postArr,0,arr.length,0,arr);
  console.log(count);
  return count;
}


solution(arr4);