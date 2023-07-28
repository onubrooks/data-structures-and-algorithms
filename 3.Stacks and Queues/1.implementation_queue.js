class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  class QueueLinkedList {
    constructor(){
      this.first = null;
      this.last = null;
      this.length = 0;
    }
    peek() {
        return this.first;
    }
    enqueue(value){
      const node = new Node(value);
      if(this.length === 0){
        this.first = node;
        this.last = node;
      } else {
        this.last.next = node;
        this.last = node;
      }
      this.length++;
      return this;
    }
    dequeue(){
        if(!this.first){ // or this.length === 0
            return null;
        }
        if(this.first === this.last){ // or this.length === 1
            this.last = null;
        }
        const temp = this.first;
        this.first = this.first.next;
        this.length--;
        return temp;
    }
    isEmpty(){
      return this.length === 0;
    }
  }
  
  const myQueue = new QueueLinkedList();
  myQueue.enqueue('Joy');
  myQueue.enqueue('Matt');
  myQueue.enqueue('Pavel');
  myQueue.enqueue('Samir');
  console.log(myQueue.peek());
  console.log(myQueue.dequeue());
  console.log(myQueue.dequeue());
  console.log(myQueue.peek());
  
  