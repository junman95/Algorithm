const info = [
  "java backend junior pizza 150",
  "python frontend senior chicken 210",
  "python frontend senior chicken 150",
  "cpp backend senior pizza 260",
  "java backend junior chicken 80",
  "python backend senior chicken 50",
];
const query = [
  "java and backend and junior and pizza 100",
  "python and frontend and senior and chicken 200",
  "cpp and - and senior and pizza 250",
  "- and backend and senior and - 150",
  "- and - and - and chicken 100",
  "- and - and - and - 150",
];
 
function solution(info, query) {
  var answer = [];
 
  info.forEach((element, index) => {
    let temp = [];
    temp.push(...element.split(" "));
    info[index] = temp;
  });
 
  info.sort((a,b)=>(a[a.length-1] - b[b.length-1]));
 
  console.log(query);
  console.log(info);
  query.forEach((element, index) => {
    let temp = [];
    temp.push(...element.split(" and "));
 
    let temp_last = temp[temp.length - 1].split(" ");
    temp.pop();
    temp.push(...temp_last);
 
    query[index] = temp;
  });
//------------------------------------------------------------------//
  var isCheck = true;
 
  for (let i = 0; i < query.length; i++) {
    let candidate = 0;
    console.log("i" , i);
    let low = 0;
    let high = info.length-1;
    let mid;
    const target = query[i][query[i].length-1];

    let count = 0;
    while(low<=high){
      count+=1;
      //console.log(count);
      mid = parseInt((low+high)/2);
      const scoreIdx = info[mid].length-1; 
      //console.log("mid : ",mid,"score : ",info[mid][scoreIdx],"target : ",target,"low : ",low,"high : ",high);
      //목표 점수보다 작을 때
      if(Number(info[mid][scoreIdx]) < Number(target)){
        low = mid + 1;
      }
      //목표 점수보다 클 때
      else{
        high = mid-1;
      }
      //console.log(high,low)
    }

    console.log("real mid : ",mid);
    
  
    for (let j = mid-1; j < info.length; j++) {
      const scoreIdx = info[j].length-1;
      
      info[j].forEach((element,index)=>{
        //console.log(element,query[i][index]);
        //고려조건 '-' , ===, NaN
        //문자이면서 쿼리가 - 가 아닐때
        if(isNaN(element) === true && query[i][index] !== '-'){
          if(query[i][index] !== element){
            isCheck = false;
          }
        }
        //숫자일때
        else if(isNaN(element) === false){
          if(Number(element) < Number(query[i][index])){
            isCheck = false;
          }
        }
        if(isCheck === false) return;
      })

      if( isCheck === true ) {
        candidate += 1;
      }
      isCheck = true;
    }
    answer.push(candidate);
  }
  console.log(answer);
  return answer;
}
 
solution(info, query);




