board1 = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
];
//900
board2 = [
  [0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 0, 1, 0],
  [0, 1, 0, 0, 0, 1, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0],
];
//3800
board3 = [
  [0, 0, 1, 0],
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [1, 0, 0, 0],
];
//2100
board4 = [
  [0, 0, 0, 0, 0, 0],
  [0, 1, 1, 1, 1, 0],
  [0, 0, 1, 0, 0, 0],
  [1, 0, 0, 1, 0, 1],
  [0, 1, 0, 0, 0, 1],
  [0, 0, 0, 0, 0, 0],
];
//3200
const dx = [-1, 1, 0, 0];
const dy = [0, 0, 1, -1];
var money = [];
const curcuit_dfs = (board, N, visited, position, direction) => {
  console.log(visited)
  const x = position[0];
  const y = position[1];
  //상하좌우
  for (let i = 0; i < 4; i++) {
    //판 내부로 들어오는지
    console.log("현재맵 정보", position, i);
    if (-1 < x + dx[i] && x + dx[i] < N && -1 < y + dy[i] && y + dy[i] < N && visited[x + dx[i]][y + dy[i]] === 0 && board[x + dx[i]][y + dy[i]] !== 1) {
      position[0] = x + dx[i];
      position[1] = y + dy[i];
      visited.forEach(element => {
        console.log(element);
      });
      //도착지 도착여부    
      if (x + dx[i] === N - 1 && y + dy[i] === N - 1) {
        //직진
        let sum =0;
        if (direction === i) {
          visited[x + dx[i]][y + dy[i]] = 1;
          let straight = [];
          let curved = [];
          for (let check = 0; check < N; check++) {
            straight = visited[check].filter((numbers) => {
              return numbers === 1;
            })
            curved = visited[check].filter((numbers) => {
              return numbers === 2;
            })
            let sum_temp = straight.length * 100 + curved.length * 500;
            sum += sum_temp;
            console.log(sum_temp);
            sum_temp=0;
          }
          console.log(sum, straight, curved);
          money = money.concat([sum]);
          sum =0;
        }
        //커브
        else {
          visited[x + dx[i]][y + dy[i]] = 2;
          let straight = [];
          let curved = [];
          for (let check = 0; check < N; check++) {
            straight = visited[check].filter((numbers) => {
              return numbers === 1;
            })
            curved = visited[check].filter((numbers) => {
              return numbers === 2;
            })
            let sum_temp = straight.length * 100 + curved.length * 500;
            sum += sum_temp;
            console.log(sum_temp);
            sum_temp=0;
          }
          
          console.log(sum, straight, curved);
          money = money.concat([sum]);
          sum =0;
        }
      }
      if (direction === i) {
        visited[x + dx[i]][y + dy[i]] = 1;
      }
      else {
        visited[x + dx[i]][y + dy[i]] = 2;
      }
      curcuit_dfs(board, N, visited, position, i);
 
    }
  }
  visited[x][y] = 0;
}
 
function solution(board) {
  const N = board.length;
  let visited = new Array(N);  //0:가지않은 길, 1:직진, 2:커브
  for (let i = 0; i < N; i++) {
    visited[i] = new Array(N);
    for (let j = 0; j < N; j++) {
      visited[i][j] = 0;
    }
  }
  visited[0][0] = 1;
  console.log(visited);
  let position = [0, 0];
  let direction = 1;  //0:상 1:하 2:좌 3:우
  //dfs로 만들어야한다. 전부탐색
  curcuit_dfs(board, N, visited, position, direction);
  console.log(money);
  var answer = Math.min.apply(null,money);
  return answer;
}
 
console.log(solution(board3));
 
