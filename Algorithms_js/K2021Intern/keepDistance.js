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
//4-2. 중간 칸막이 확인


function solution(places) {
  var answer = [];
  let place = new Array();
  place = places;
  //1. 대기실 Array 변환
  place.forEach((class_el, idx) => {
    class_el.forEach((row_el, row_idx) => {
      place[idx][row_idx] = row_el.split("");
    });
  });

  //2. 대기실 탐색하면서 P를 찾으면 범위탐색
  let loc_p = [];
  place.forEach((class_el) => {
    let illegal = false; //거리두기 지켰는지 판별할 변수
    class_el.forEach((row_el, row_idx) => {
      row_el.forEach((col_el, col_idx) => {
        //3. P를 찾았을때 P들의 위치를 전부 저장
        if (col_el === "P") loc_p.push([row_idx, col_idx]);
      });
    });
    //4. P값들 끼리의 거리비교
    let loc_p2 = loc_p.slice();
    for (let i = 0; i < loc_p.length; i++) {
      //자기자신 뺴기
      loc_p2.shift();
      for (let j = 0; j < loc_p2.length; j++) {
        const p1 = loc_p[i];
        const p2 = loc_p2[j];
        //맨하탄 값
        const manhattan = Math.abs(p1[0] - p2[0]) + Math.abs(p1[1] - p2[1]);
        const manhattan_row = Math.abs(p1[0] - p2[0]);
        const manhattan_col = Math.abs(p1[1] - p2[1]);
        // 거리두기 1이면 무조건 붙어있으므로
        if (manhattan < 3) {
          if (manhattan === 1) {
            answer.push(0);
            illegal = true;
            break;
          } else { // 맨하탄 거리 =2
            const mid_x = parseInt((p1[0] + p2[0]) / 2);
            const mid_y = parseInt((p1[1] + p2[1]) / 2);
            // 직선거리 2칸
            if (
              (manhattan_row === 2 || manhattan_col === 2) &&
              class_el[mid_x][mid_y] !== "X"
            ) {
              answer.push(0);
              illegal = true;
              break;
            }
            //대각거리 2칸
            else if(manhattan_row === 1 && manhattan_col === 1){
              const temp_sqr = [class_el[mid_x][mid_y],class_el[mid_x+1][mid_y],class_el[mid_x][mid_y+1],class_el[mid_x+1][mid_y+1]]
              const panel = temp_sqr.filter(word => word === 'X');
              if(panel.length !== 2){
                answer.push(0);
                illegal = true;
                break;
              }
            }
          }
        }
        if (illegal === true) break;
      }
      if (illegal === true) break;
    }
    //거리두기 완벽히 지켰는지 판별
    if (illegal === false) answer.push(1);
    illegal = false;
    loc_p = [];
  });

  return answer;
}

solution(places);
