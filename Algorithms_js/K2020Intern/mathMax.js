// + - * 로만 이루어진 수식
// 연산자 재정의 후 최대의 숫자 제출

expression1 = "100-200*300-500+20"; //60420
expression2 = "50*6-3*2"; //300
expression3 = "200-300-500-600*40+500+500" //1248000

const getPermutations = (arr, selectSign) => {
  const results = [];
  if (selectSign === 1) return arr.map((value) => [value]);
  //          element,index,array   // origin : arr
  arr.forEach((cur_element, index, origin) => {
    //현재 요소 fixed를 제외한 나머지
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = getPermutations(rest, selectSign - 1);
    const attached = permutations.map((permutation) => [
      cur_element,
      ...permutation,
    ]);
    results.push(...attached);
  });
  return results;
};

function solution(expression) {
  var answer = 0;
  //----------------------------------------
  //숫자와 수식의 분리
  //----------------------------------------
  let expression_list = expression.split("");
  let pivot = 0;
  let numbers = [];
  let signs = [];

  for (let i = 0; i < expression_list.length + 1; i++) {
    const cur_chr = expression_list[i];
    //console.log(cur_chr);
    if (
      cur_chr === "*" ||
      cur_chr === "+" ||
      cur_chr === "-" ||
      cur_chr === undefined
    ) {
      let temp_num = expression_list.slice(pivot, i + 1);
      temp_num = parseInt(temp_num.join(""));
      numbers.push(temp_num);
      if (cur_chr !== undefined) signs.push(cur_chr);

      pivot = i + 1;
    }
  }

  //----------------------------------------
  // 수식 순열 생성
  //----------------------------------------
  //signs 중복제거 후 array 재변환
  const set_signs = Array.from(new Set(signs));
  const sign_permutations = getPermutations(set_signs, set_signs.length);
  //----------------------------------------
  // 순열의 수식 순서대로 현재 signs sort
  //----------------------------------------
  sign_permutations.forEach((element)=>{
    //----------------------------------------
    // signs순의 연산 후 answer값 도출
    //----------------------------------------
    console.log(signs);
    console.log(element);
    //깊은복사
    let temp_element = element.slice();
    let temp_numbers = numbers.slice();
    let temp_signs = signs.slice();

    let idx =0;
    //----------------------------------------
    // 순열들의 순서대로 반복문 돌리기
    //----------------------------------------
    temp_element.forEach((cur_sign)=>{
      while(temp_signs.includes(cur_sign)){
        console.log(cur_sign);
        console.log(temp_signs);
        console.log(temp_numbers);
        if (idx === temp_numbers.length) idx = 0;
        if(cur_sign === temp_signs[idx]){
          if (temp_signs[idx] === '*'){
            temp_numbers[idx] = temp_numbers[idx] * temp_numbers[idx+1];
          }
          else if (temp_signs[idx] === '+'){
            temp_numbers[idx] = temp_numbers[idx] + temp_numbers[idx+1];
          }
          else if (temp_signs[idx] === '-'){
            temp_numbers[idx] = temp_numbers[idx] - temp_numbers[idx+1];
          }
          temp_numbers.splice(idx+1,1);
          temp_signs.splice(idx,1);
          idx=-1;
        }
        idx++;
      }
    });
    if(Math.abs(temp_numbers[0]) > answer){
      answer = Math.abs(temp_numbers[0]);
    }
    console.log(answer);
  });
  console.log(answer);
  return answer;
}

solution(expression3);
