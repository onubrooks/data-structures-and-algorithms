class Node {
    constructor(value){
      this.value = value;
      this.next = null;
    }
  }
  
  class StackLinkedList {
    constructor(){
      this.top = null;
      this.bottom = null;
      this.length = 0;
    }
    peek() {
        return this.top;
    }
    push(value){
        let node = new Node(value);
        if(this.length === 0){
            this.top = node;
            this.bottom = node;
        } else {
            let temp = this.top;
            this.top = node;
            this.top.next = temp;
        }
        this.length++;
        return this;
    }
    pop(){
        if(!this.top){
            return null;
        }
        if(this.top === this.bottom){
            this.bottom = null;
        }
        let temp = this.top;
        this.top = this.top.next;
        this.length--;
        return temp;
    }
    isEmpty () {
        return this.length === 0;
    }
  }
  
  const myStack = new Stack();
    myStack.push('google');
    myStack.push('udemy');
    myStack.push('discord');
    console.log(myStack.pop());
    console.log(myStack.peek());
    console.log(myStack.isEmpty());
    console.log(myStack);
  
class StackArray {
    constructor(){
        this.data = [];
    }

    peek() {
        return this.data[this.data.length - 1];
    }

    push(value){
        this.data.push(value);
        return this;
    }

    pop(){
        this.data.pop();
        return this;
    }

    isEmpty () {
        return this.data.length === 0;
    }
}
  