const n1 = 6;
const s1 = 4;
const a1 = 6;
const b1 = 2;
const fares1 = [
  [4, 1, 10],
  [3, 5, 24],
  [5, 6, 2],
  [3, 1, 41],
  [5, 1, 24],
  [4, 6, 50],
  [2, 4, 66],
  [2, 3, 22],
  [1, 6, 25],
];

function solution(n, s, a, b, fares) {
  var answer = 0;

  const path = Array.from({ length: n }, (_, i) => {
    return Array.from({ length: n }, (_, j) => (i === j ? 0 : Infinity));
  });
  fares.forEach(([a, b, fee]) => {
    path[a - 1][b - 1] = fee;
    path[b - 1][a - 1] = fee;
  });
  console.log(path);

  for (let mid = 0; mid < n; mid++) {
    for (let i = 0; i < n; i++) {
      for (let j = 0; j < n; j++) {
        path[i][j] = Math.min(path[i][j], path[i][mid] + path[j][mid]);
      }
    }
  }
  let min_fee = Infinity;
  for (let i = 0; i < n; i++) {
    const cur_fee = path[s-1][i] + path[i][a-1] + path[i][b-1];
    min_fee > cur_fee ? min_fee= cur_fee : null;
    console.log(min_fee);
  }
  console.log(path);
  console.log(min_fee);
  answer = min_fee;
  return answer;
}

solution(n1, s1, a1, b1, fares1);
