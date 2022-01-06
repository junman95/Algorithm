const record1 = [
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan",
];

const solution = (record) => {
  
  let record_arr = [];
  for(let i =0;i<record.length;i++){
    let temp = record[i].split(" ");
    let command = temp[0];
    let uid = temp[1];
    let name = temp[2];
    let ans_stack = [];
    if (command[0] === "E"){
      ans_stack.push([uid,name,"님이 들어왔습니다."]);
    }
    else if(command[0] === "L"){
      ans_stack.push([uid,name,"님이 나갔습니다."]);
    }else{
      ans_stack.push([uid,name]);
    }

  }

}

solution(record1);