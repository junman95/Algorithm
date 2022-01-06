const graph = [
  [0,1,2,4], //0
  [1,0,2],//1
  [2,1,3],//2
  [3,2,4],//3
  [4,0,2,3]//4
]
const queue = [];
const visited = [];
graph.forEach(()=>{
  visited.push(false);
})
console.log(visited);
const BFS = (graph,start,visited,queue)=>{
  queue.push(start);
  visited[start] = true;
  while(queue.length !== 0){
    console.log(visited);
    console.log(queue);
    v = queue.shift();
    graph[v].forEach((element,index)=>{
      if (visited[element] !== true){
        queue.push(element);
        visited[element] = true;
      }
    })
  }
}
//BFS

BFS(graph,0,visited,queue);