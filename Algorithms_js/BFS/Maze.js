
const graph = [
  [0,1,2,4], //0
  [1,0,2],//1
  [2,1,3],//2
  [3,2,4],//3
  [4,0,2,3]//4
]
console.log(graph.length);
const queue = []; //탐색을 할 큐
const visited = []; //이미 탐색한 지점을 표현
//초기 Node들의 visited상태는 false로 표현
graph.forEach(()=>{
  visited.push(false);
})
console.log(visited);

const BFS = (graph,start,visited,queue)=>{
  queue.push(start); // 시작지점 지정
  visited[start] = true;
  while(queue.length !== 0){ // 큐가 비어있을때까지 루프돌린다.
    console.log(visited);
    console.log(queue);
    v = queue.shift(); //가장 처음으로 들어온 노드 뽑기
    graph[v].forEach((element,index)=>{
			//현위치가 방문하지 않은 자리만 탐색
      if (visited[element] !== true){ 
        queue.push(element); //방문할 노드를 큐에 등록
        visited[element] = true; //방문상태 변경
      }
    })
  }
}
//BFS

BFS(graph,0,visited,queue);