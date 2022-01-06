orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"];
courses1 = [2, 3, 4];
orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"];
courses2 = [2, 3, 5];
orders3 = ["XYZ", "XWY", "WXA"];
courses3 = [2, 3, 4];

function getCombinations(arr, num) {
  let result = new Array();
  if (num === 1) return arr.map((ele) => [...ele]);

  arr.forEach((element, index, arr) => {
    const rest = arr.slice(index + 1);
    const combinations = getCombinations(rest, num - 1);
    const attached = combinations.map((combi) => [element, ...combi]);
    result.push(...attached);
  });
  return result;
}
function solution(orders, courses) {
  var answer = [];
  for (let i = 0; i < courses.length; i++) {
    let combi = [];
    for (let j = 0; j < orders.length; j++) {
      const cur_combi = getCombinations(orders[j].split(""), courses[i]);
      cur_combi.forEach((val, idx) => {
        cur_combi[idx].sort();
        cur_combi[idx] = val.join("");
      });
      console.log(cur_combi);
      combi.push(...cur_combi);
    }
    console.log(combi);
    let biggest = 0;
    let temp = [];
    for (let k = 0; k < combi.length; k++) {
      let counter = 0;
      for (let l = k + 1; l < combi.length; l++) {
        if (combi[k] === combi[l]) counter += 1;
      }
      //console.log("전",counter,biggest);
      if (counter >= biggest && counter > 0) {
        biggest = counter;
        temp.push([combi[k], counter + 1]);
      }
    }
    console.log(temp);
    let check = true;
    if (temp.length > 1) {
      while (check) {
        if (temp[0][1] < biggest + 1) temp.shift();
        else check = false;
      }
    }
    temp.forEach((el) => {
      answer.push(el[0]);
    });
  }
  console.log(answer);
}

solution(orders3, courses3);
