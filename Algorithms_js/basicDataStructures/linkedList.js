var LinkedList = (function() {
  function LinkedList(){
    this.length = 0;
    this.head = null;
  }

  function Node(data){
    this.data = data;
    this.next = null;
  }

  LinkedList.prototype.add = (value)=>{
    var node = new Node(value);
    var current = this.head;
    if(!current){
      this.head = node;
      this.length++;
      return node;
    }
    else{
      while(current.next){
        current = current.next;
      }
      current.next = node;
      this.length++;
      return node;
    }
  }
  LinkedList.prototype.search = (position)=>{
    var current = this.head;
    var count = 0;
    while(current.next){
      current = current.next;
      count++;
    } 
    return current.data;
  }
})