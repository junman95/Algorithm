const code = [
  "a=3",
  "..a=4",
  "..b=3",
  "..print a",
  ".......a=6",
  ".......print a",
  ".......print b",
  "..print a",
  "....a=7",
  "....print a",
  "print a",
  "print b",
  "a=4",
  "print a",
  "...print a",
];

function solution(code) {
  var answer = [];
  const indentStack = [];
  const varStack = [];
  const varMap = new Map();
  code.forEach((element) => {
    if (element.indexOf("print") !== -1) {
      let tempKey = element.replace("print","");
      tempKey = tempKey.match(/\w/)[0];
      if(varMap.get(tempKey) == undefined)
        answer.push("error");
      else
        answer.push(tempKey+varMap.get(tempKey));
    } 
    else {
      let dots = element.match(/\./g);
      console.log(varStack);
      if(dots !== null) {
        if(indentStack[-1] !== undefined && indentStack[indentStack.length-1] > dots.length )
          while(indentStack[indentStack.length-1] <= dots.length){
            indentStack.pop();
            varStack.pop();
          }
        else
          indentStack.push(dots.length);
       }else{
         indentStack.push(0);
       }

      const varName = element.match(/\w/);
      const varValue = element.match(/\d+/) ;

      varStack.push([varName[0],Number(varValue[0])])
      varMap.set(varName[0],'='+varValue[0]);
    }
  });
  console.log(varStack);
  console.log(varMap);
  console.log(answer);
  return answer;
}

solution(code);


