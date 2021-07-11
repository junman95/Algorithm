function Node(val){
  this.val = val;
  this.left = null;
  this.right = null;
}

function traversal(node){
  if (node === null){
    return ;
  }
  console.log('preorder', node.val);
  traversal(node.left);
  console.log('inorder', node.val);
  traversal(node.right);
  console.log('postorder', node.val);
}

let root = new Node(5);
let left = new Node(3);
let right = new Node(8);
root.left = left;
root.right = right;


traversal(root)