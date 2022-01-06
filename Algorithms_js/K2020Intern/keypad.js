numbers1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5];
hand1 = "right";
//"LRLLLRLLRRL"
numbers2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2];
hand2 = "left";
//"LRLLRRLLLRR"
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
hand3 = "right";
//"LLRLLRLLRL"

function solution(numbers, hand) {
  const keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ["*", 11, "#"],
  ];
  
  for(let i=0; i<numbers.length;i++){
    if (numbers[i] === 0){
      numbers[i] = 11;
    }
  }
  let answer = [];
  let l_cursor = [3, 0];
  let r_cursor = [3, 2];

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 3 === 1) {
      //왼쪽 키패드
      answer.push("L");
      l_cursor = [parseInt((numbers[i] - 1) / 3), (numbers[i] - 1) % 3];
    } else if (numbers[i] % 3 === 0) {
      //오른쪽 키패드
      answer.push("R");
      r_cursor = [parseInt((numbers[i] - 1) / 3), (numbers[i] - 1) % 3];
    } else {
      //
      for (let j = 0; j < keypad.length; j++) {
        //키패드 첫째줄부터 마지막줄 까지 중 현재 숫자값의 인덱스가 1(중간)인 경우 찾기
        if (keypad[j].indexOf(numbers[i]) === 1) {
          //중간좌표
          const temp_pos = [j, 1];
          //왼쪽 오른쪽 손가락과의 거리
          const left_sum =
            Math.abs(temp_pos[0] - l_cursor[0]) +
            Math.abs(temp_pos[1] - l_cursor[1]);
          const right_sum =
            Math.abs(temp_pos[0] - r_cursor[0]) +
            Math.abs(temp_pos[1] - r_cursor[1]);
          //좌우 손가락과 다이얼의 거리가 같으면 우선하는 손으로
          if (left_sum === right_sum) {
            if (hand === "left") {
              l_cursor = temp_pos;
              answer.push("L");
            } else {
              r_cursor = temp_pos;
              answer.push("R");
            }
          //왼쪽이 값이 클때(오른쪽이 더 가까울때)
          } else if (left_sum > right_sum) {
            r_cursor = temp_pos;
            answer.push("R");
          //오른쪽이 값이 클때(왼쪽이 더 가까울때)
          } else {
            l_cursor = temp_pos;
            answer.push("L");
          }
          break;
        }
      }
    }
  }
  return answer.join('');//쉼표 제거 문자열 반환
}

console.log(solution(numbers2, hand2));
