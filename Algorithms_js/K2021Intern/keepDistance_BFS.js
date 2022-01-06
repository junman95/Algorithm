places = [
  ["POOOP", 
  "OXXOX", 
  "OPXPX", 
  "OOXOX", 
  "POXXP"],
  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], // => [p,o,o,]
  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
];
//[(1, 0, 1, 1, 1)];
//맨해튼 거리 |a1 - a2|+|b1 - b2| > 2
//조건
//대기실은 5개이며, 각 대기실은 5x5 크기입니다.
//거리두기를 위하여 응시자들 끼리는 맨해튼 거리가 2 이하로 앉지 말아 주세요.
//단 응시자가 앉아있는 자리 사이가 파티션으로 막혀 있을 경우에는 허용합니다.
//P : 응시자가 앉은 자리
//O : 빈 테이블
//X : 파티션
const drow = [-1, 1, 0, 0];
const dcol = [0, 0, -1, 1];

function solution(place) {
  var answer = [];
  place.forEach((class_el, idx) => {
    let loc_p = [];
    let visited = [];
    class_el.forEach((row_el, row_idx) => {
      place[idx][row_idx] = row_el.split("");
      const temp = new Array(row_el.length).fill(false);
      visited.push(temp);
    });
    class_el.forEach((row_el, row_idx) => {
      row_el.forEach((col_el, col_idx) => {
        // P를 찾았을때 P들의 위치를 전부 저장
        if (col_el === "P") loc_p.push([row_idx, col_idx,0]);
        else if (col_el === "X") visited[row_idx][col_idx] = true;
      });
    });
    //bfs
    console.log("클래스 구분");
    for (let i = 0; i < loc_p.length; i++) { //p의 좌표들을 전부 돈다
      let depth = loc_p[0][2];
      const queue =[loc_p[i]];
      const class_visited = visited.slice();
      console.log(class_visited);
      // BFS 시작
      while (queue.length !== 0 && queue[0][2] < 2) {
        console.log(queue);
        let cur_pos = queue.shift(); // queue 왼쪽뽑기
        if (cur_pos[2] === 2) return ;
        class_visited[cur_pos[0]][cur_pos[1]] = true;
        for (let j = 0; j < 4; j++) {
          const pos_x = cur_pos[0] + drow[j];
          const pos_y = cur_pos[1] + dcol[j];
          if (0 <= pos_x  && 0 <= pos_y && pos_x < class_el.length && pos_y < class_el[0].length) {
            if (class_visited[pos_x][pos_y] !== true) {
              //console.log(class_visited);
              if (class_el[pos_x][pos_y] == "P") {
                console.log("illegal : ",pos_x,pos_y);
                answer.push(0);
                return;
              }
              queue.push([pos_x, pos_y,cur_pos[2]+1]);
            }
          }
        }
      }
    }
    if(answer[idx] === undefined) answer.push(1);
  });
  return answer;
}

console.log(solution(places));