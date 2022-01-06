const n1 = 5;
const build_frame1 = [
  [1, 0, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 0, 1],
  [2, 2, 1, 1],
  [5, 0, 0, 1],
  [5, 1, 0, 1],
  [4, 2, 1, 1],
  [3, 2, 1, 1],
];

const n2 = 5;
const build_frame2 = [
  [0, 0, 0, 1],
  [2, 0, 0, 1],
  [4, 0, 0, 1],
  [0, 1, 1, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 1],
  [3, 1, 1, 1],
  [2, 0, 0, 0],
  [1, 1, 1, 0],
  [2, 2, 0, 1],
];

//벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
//바닥에 보를 설치 하는 경우는 없습니다.
//구조물이 겹치도록 설치하는 경우와, 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.

//구조물이 타당한지?
function checkFunc(list, arr) {
  console.log(list);
  let bool = true;
  const type = list[2];
  const pos_x = list[0];
  const pos_y = list[1];

  // 기둥
  if (type === 0) {
    //기둥의 위치가 바닥이 아닐때
    if (pos_y > 0) {
      //왼쪽 벽
      if (pos_x === 0) {
        //아래가 기둥이 아닐 경우
        if (arr[pos_x][pos_y - 1] !== 0) {
          bool = false;
          return;
        }
      }
      //나머지
      else {
        //아래가 기둥이 아니거나 왼쪽 아래가 보가 아닐 때
        if (arr[pos_x][pos_y - 1] !== 0 || arr[pos_x - 1][pos_y]) {
          bool = false;
          return;
        }
      }
    }
  }
  // 보
  else if (type === 1) {
    //좌우 아래가 기둥이 아닐때
    if (arr[pos_x][pos_y - 1] !== 0 && arr[pos_x + 1][pos_y - 1] !== 0) {
      if (pos_x > 0) {
        if (arr[pos_x - 1][pos_y] === 1 && arr[pos_x + 1][pos_y] === 1)
          bool = true;
        else {
          bool = false;
          return;
        }
      }
    }
  }
}

function solution(n, build_frame) {
  var answer = [];
  const task_num = build_frame.length;

  const board = [];
  for (let i = 0; i <= n; i++) {
    const temp = [];
    for (let j = 0; j <= n; j++) {
      temp.push(-1);
    }
    board.push(temp);
  }

  for (let task = 0; task < task_num; task++) {
    console.log(build_frame[task]);
    const pos = [build_frame[task][0], build_frame[task][1]];
    const type = build_frame[task][2];
    const action = build_frame[task][3];

    // 추가 동작
    if (action === 1) {
      //일단 넣고
      board[pos[0]][pos[1]] = type;
      answer.push([pos[0], pos[1], type]);
      //체크

      if (checkFunc(answer[answer.length-1], board) !== true) {
        answer.pop();
      } else continue;
    }
    // 제거 동작
    else if (action === 0) {
      //일단 빼고
      board[pos[0]][pos[1]] = -1;
      const out = answer.findIndex(
        (val) =>{
          console.log(val[0],val[1]);
          val[0] === pos[0] && val[1] === pos[1]}
      );
      console.log("out",out);
      let temp = answer[out];
      //체크
      if (checkFunc(temp, board) === true) {
        answer.splice(out, 1);
      } else continue;
    }
    console.log(board);
  }
  answer.sort((a, b) => a[0] - b[0]);
  return answer;
}

console.log(solution(n2, build_frame2));
