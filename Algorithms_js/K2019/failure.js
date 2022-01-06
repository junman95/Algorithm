const N1 = 5;
const stages1 = [2, 1, 2, 6, 2, 4, 3, 3];
const result1 = [3,4,2,1,5];

const N2 = 4;
const stages2 = [4,4,4,4,4];
const result2 = [4,1,2,3];


function solution(N, stages) {
  var rate = new Map();
  //스테이지 내림차순
  stages.sort((a,b)=>{
    return b-a;
  })

  for(let i = 1;i<=N;i++){
    let check = true;
    let counter = 0;
    let formal_len = stages.length;
    //실패율 집계

    const stages1 = [2, 1, 2, 6, 2, 4, 3, 3];
    =>[6, 4, 3, 3,2, 2, 2, 1]
    while(check){
      if(stages[stages.length-1] === i){
        stages.pop();
        counter +=1;
      }
      else{
        console.log(counter,formal_len);
        rate.set(i,counter/formal_len);
        check= false;
      }
    }
  }
  console.log(rate);
  //배열로 변경
  rate = Array.from(rate);
  console.log(rate);
  //rate내림차순 나열
  rate.sort((a,b)=>{
    return b[1] - a[1];
  })
  console.log(rate);

  var answer = [];
  rate.forEach((el)=>{
    answer.push(el[0]);
  })
  return answer;
}

console.log(solution(N1,stages1));