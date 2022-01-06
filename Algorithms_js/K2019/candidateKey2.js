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
  
  for(let i = 0; i<keys; i++){
    if(key_types.length<i+1) break;
    const combi = getCombinations(key_types,i+1);
    let candidate = [];
    //combination 순차 탐색
    combi.forEach((el,idx)=>{
      let temp = new Array();
      //조합의 인덱스 셋에 추가
      for(let j = 0; j<relation.length;j++){
        let temp_str = "";
        el.forEach((cur_el)=>{
          temp_str+=(relation[j][cur_el]);
        })
        if(temp.find(el => el === temp_str) !== undefined){
          break;
        }
        else temp.push(temp_str);
      }
      if (temp.length === relation.length){
        answer+=1;
        el.forEach((cur_el)=>{
          const erase = key_types.indexOf(cur_el);
          key_types.splice(erase,1);
        })
      }
      
    })
  }
  return answer;
}