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
  let table = [];
  for (let i = 0; i < n; i++) {
    table.push(i);
  }
  let temp = [table.slice()];
  let temp_num = [];
  //2. 각 커맨드 경우 나누기
  const commands = new Map();
  commands.set("D", "+");
  commands.set("U", "-");
  commands.set("C", 0);
  commands.set("Z", temp[-1]);

  
  cmd.forEach((el, idx, arr) => {
    cmd[idx] = el.split(" "); // [[D,2][c][u,3]...]
  });
  //1. cmd의 순서대로 반복문 실시
  for (let idx = 0; idx < cmd.length; idx++) {
    console.log(table);
    const el = cmd[idx];
    if (el[0] === "U" || el[0] === "D") {
      console.log(el[0],k);
      k += eval(commands.get(el[0]) + el[1]);
    } 
    else if (el[0] === "C") {
      console.log(el[0],k,table[k]);
      temp.push(table.slice());
      temp_num.push(table.splice(k, 1));
      if (k === table.length) k = k-1;
    } 
    else if (el[0] === "Z") {
      console.log(el[0],k);
      table = temp.pop();
      console.log("tnum : ",temp_num);
      if(temp_num.pop() < k) k +=1;
    }
  }
  console.log(table);

  var answer = "";
  for(let i =0; i<n;i++){
    if(table.includes(i) === false) answer+='X';
    else answer += 'O';
  }

  return answer;
}

console.log(solution(n2, k2, cmd2));
