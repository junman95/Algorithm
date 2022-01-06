const record1 = [
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan",
];
//result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

// 각 커맨드에 대한 구현


function solution(record) {
  let record_map = new Map();
  let record_set = new Set();
  let src_idx = [];
  let answer = [];
  for (let i = 0; i < record.length; i++) {
    //레코드 배열 내부 값  map 자료구조로 할당
    record[i] = record[i].split(" ");
    
    let cur_command = record[i][0];
    let cur_uid = record[i][1];
    let cur_nickname = record[i][2];
    
    if(cur_command === "Enter"){
      record_map.set(cur_uid,cur_nickname);
      answer.push([cur_uid,"님이 들어왔습니다."]);
    }else if(cur_command === "Change"){
      record_map.set(cur_uid,cur_nickname);
    }else if(cur_command === "Leave"){
      answer.push([cur_uid,"님이 나갔습니다."]);
    } 
  }
  console.log(answer);
  for(let i = 0; i<answer.length;i++){
    const fixed_nick = record_map.get(answer[i][0]);
    answer[i][0] = fixed_nick;
    answer[i] = answer[i].join('');
  }
  
  console.log(answer);
  return answer;
}

console.log(solution(record1))