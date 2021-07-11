function Node(val){
  this.val = val;
  this.prev = null;
  this.next = null;
}

let head = new Node(0);
let node1 = new Node(1);
let node2 = new Node(2);

head.next = node1;
node1.prev = head;
node1.next = node2;
node2.prev = node1;

console.log(head.val)
console.log(head.next.val)
console.log(head.next.prev.val)