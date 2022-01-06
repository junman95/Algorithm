places = [
  ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
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

//1. 대기실 Array 변환
//2. 대기실 탐색하면서 P를 찾으면 범위탐색
//3. P들의 위치를 전부 저장
//4. P값들 끼리의 거리비교
//4-1. 맨하탄 거리 =<2 확인
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

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
        if (col_el === "P") loc_p.push([row_idx, col_idx]);
        else if (col_el === "X") visited[row_idx][col_idx] = true;
      });
      for(let i = 0; i<loc_p.length;i ++){
        const target = [loc_p[i]];
        let depth = 0;
        while(target.length!==0 && depth <3){
          let cur_pos = target.shift();
          visited[cur_pos[0]][cur_pos[1]] = true;
          for(let j = 0;j<4;j++){
            const pos_x = cur_pos[0]+dx[j];
            const pos_y = cur_pos[1]+dy[j];
            if(0<=pos_x<row_el.length && 0<=pos_y<row_el.length){
              if(visited[pos_x][pos_y] !== true){
                visited[pos_x][pos_y] = true;
                target.push([pos_x,pos_y]);

                if(class_el[pos_x][pos_y] == "P") {
                  answer.push(1);
                  break;
                }
              }
            }
          }
          depth+=1;
        }
      }
    });
  });
  return answer;
}

console.log(solution(places));
