const id1 = "...!@BaT#*..y.abcdefghijklm"	;
const id2 = "z-+.^."	;
const id3 = "=.="	;
const id4 = "123_.def"	;
const id5 = "abcdefghijklmn.p"	;


function solution(id){
  //1단계
  let suggestion = id.toLowerCase();
  //2단계
  suggestion = suggestion.replace(/[^\w\.\-]/g,"");
  //3단계
  suggestion = suggestion.replace(/\.{2,}/g,".");
  //4단계
  suggestion = suggestion.replace(/^\.|\.$/g,"");
  //5단계
  if(suggestion === "") suggestion = "a";
  //6단계
  suggestion = suggestion.substr(0,15);
  suggestion = suggestion.replace(/^\.|\.$/g,"");
  //7단계
  let temp_last = suggestion.substring(suggestion.length,suggestion.length);
  while(suggestion.length<3){
    suggestion+=temp_last;
  }
  //console.log(array);
  console.log(suggestion);
  return suggestion;
}

solution(id1);