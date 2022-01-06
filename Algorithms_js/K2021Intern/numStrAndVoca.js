s1 = "one4seveneight"; //1478
s2 = "23four5six7"; //234567
s3 = "2three45sixseven"; //234567
s4 = "123"; //123
//1. 숫자와 해당하는 문자를 MAP구조로 만들기
//2. 배열에 문자열의 문자 하나씩 입력 후 맵과 대조
//2-1. 문자열을 한 문자 씩 배열화하기
//2-2. 문자열 순차탐색 및 배열에 한 문자씩 입력
//2-3. 단어장 MAP의 키값 대조
function solution(s) {
  var answer = [];
  //1. 숫자와 해당하는 문자를 MAP구조로 만들기
  const voca_map = new Map();
  const num = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
  ];
  num.forEach((element, index) => {
    voca_map.set(element, index);
  });
  
  //2. 배열에 문자열의 문자 하나씩 입력 후 대조
  //2-1. 문자열을 한 문자 씩 배열화하기
  let comp_arr = [];
  const str_parse = s.split("");
  //2-2. 문자열 순차탐색 및 배열에 입력
  str_parse.forEach((el) => {
    comp_arr.push(el);
    if (isNaN(el) === true) {
      // 숫자가 아닐 경우
      if (voca_map.has(comp_arr.join("")) === true) {
        answer.push(voca_map.get(comp_arr.join("")));
        comp_arr = [];
      }
    } else {
      // 숫자일경우
      answer.push(el);
      comp_arr = [];
    }
  });
  return eval(answer.join(""));
}

console.log(solution(s1));
