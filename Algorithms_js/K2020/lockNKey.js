const key1 = [
  [0, 0, 0],
  [1, 0, 0],
  [0, 1, 1],
];

const lock1 = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1],
];

//1. 자물쇠 사이즈 키우기
//2. 자물쇠 할당
//3. 키 꽂기
//4. 키 회전

function solution(key, lock) {
  const lock_size = lock.length;
  const key_size = key.length;
  let big_lock = new Array();
  const big_lock_size = lock_size + 2 * key_size;
  //2. 자물쇠 할당
  for (let i = 0; i < big_lock_size; i++) {
    let temp_row = [];
    for (let j = 0; j < big_lock_size; j++) {
      temp_row.push(0);
    }
    big_lock.push(temp_row);
  }

  for (let i = key_size; i < key_size + lock_size; i++) {
    let temp_row = [];
    for (let j = key_size; j < key_size + lock_size; j++) {
      big_lock[i][j] = lock[i - key_size][j - key_size];
    }
  }

  console.log(big_lock);
  let x_pos = 0;
  let y_pos = 0;
  var answer = false;

  for (let rot = 0; rot < 4; rot++) {
    for (let i = 0; i < big_lock_size - key_size; i++) {
      for (let j = 0; j < big_lock_size - key_size; j++) {
        let temp_big_lock = big_lock.map(v=>v.slice());
        
        for (let k = 0; k < key_size; k++) {
          for (let l = 0; l < key_size; l++) {
            temp_big_lock[i+k][j+l] += key[k][l];
          }
        }
        console.log(temp_big_lock);
        console.log("============",i,j,"=====================");
        let sum = 0;
        let count =0;
        for (let k = key_size; k < key_size + lock_size; k++) {
          for (let l = key_size; l < key_size + lock_size; l++) {
            if(temp_big_lock[k][l] === 1) sum+=1;
          }
        }
        if (sum === lock_size * lock_size) {
          answer = true;
          break;
        }
      }
    }
    //rotate
    const temp_key = key.map(el=>el.slice());
    for (let k = 0; k < key_size; k++) {
      for (let l = 0; l < key_size; l++) {
        key[k][l] = temp_key[l][key_size-k-1];
      }
    }
    console.log(key);
  }
  return answer;
}

console.log(solution(key1, lock1));
