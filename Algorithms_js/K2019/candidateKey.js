
//const relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]];
const relation = [['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']];


const getCombinations = function(arr,num){
  const results = [];
  if(num === 1) return arr.map((value)=>[value]);

  arr.forEach((picked,idx,origin) => {
    const rest = origin.slice(idx+1);
    const combinations = getCombinations(rest,num-1);
    const attachment = combinations.map((combinations)=>[picked,...combinations]);
    results.push(...attachment);
  });
  return results;
}
function solution(relation) {
  var answer = 0;

  const keys = relation[0].length;
  var key_types = new Array();
  relation[0].forEach((el,idx)=>key_types.push(idx));
  let candidate = [];

  for(let i = 0; i<keys; i++){
    if(key_types.length<i+1) break;
    const combi = getCombinations(key_types,i+1);
    console.log(i+1,combi);
    //combination 순차 탐색
    combi.forEach((el,idx)=>{
      let temp = new Array();
      //조합의 인덱스 셋에 추가
      const cur_keys = el.join('');
      for(let j = 0; j<relation.length;j++){
        let temp_str = "";
        el.forEach((cur_el)=>{
          temp_str+=(relation[j][cur_el]);
        })
        console.log("compare:",temp_str, temp);
        if(temp.find(el => el === temp_str) !== undefined){
          console.log("found same val");
          break;
        }
        else temp.push(temp_str);
      }
      
      console.log("temp&curkeys",temp,cur_keys);
      if (temp.length === relation.length){
        let check_val = 0;
        candidate.forEach((el)=>{
          console.log("key & el",cur_keys,el);
          if(cur_keys.indexOf(el) >= 0) check_val = 1;
        })
        if(check_val !== 1) {
          console.log("push",cur_keys,candidate);
          candidate.push(cur_keys);
        }
      }
    })
  }
  console.log(candidate);
  answer = candidate.length;
  return answer;
}

console.log(solution(relation));


console.log("123".indexOf("23"));