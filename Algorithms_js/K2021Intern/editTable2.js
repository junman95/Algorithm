
n1 = 8;
k1 = 2;
cmd1 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"];
//	"OOOOXOOO"
n2 = 8;
k2 = 2;
cmd2 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"];
//  "OOXOXOOO"

//1. cmd의 순서대로 반복문 실시
//2. 각 커맨드 경우 나누기
function solution(n, k, cmd) {
  //2. 각 커맨드 경우 나누기
  const commands = new Map();
  commands.set("D", "+");
  commands.set("U", "-");
  commands.set("C", 0);

  let temp = []; // temp = [[cur_pos,total_num]....]
  let cur_num = n;

  for (let idx = 0; idx < cmd.length; idx++) {
    const cur_cmd = cmd[idx].charAt(0);
    console.log(typeof cmd[idx]);
    const move_pos = String(cmd[idx]).substr(2);

    if (cur_cmd === "U" || cur_cmd === "D") {
      k += eval(commands.get(cur_cmd) + move_pos);
    }
    else if (cur_cmd === "C") {
      temp.push([k, cur_num]);
      cur_num -= 1;
      if (cur_num === k) k -= 1;
    } 
    else if (cur_cmd === "Z") {
      const last_pos = temp.pop();
      cur_num += 1;
      if (last_pos[0] <= k) k += 1;
    }
  }
  console.log(cur_num);
  let answer = [];
  for(let i = 0; i<cur_num;i++){
    answer.push('O');
  }
  while(temp.length){
    const last_one = temp.pop();
    answer.splice(last_one[0], 0, 'X');
  }
  return answer.join('');
}

solution(n1,k1,cmd1);
