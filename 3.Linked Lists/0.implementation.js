class LinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null
        }
        this.tail = this.head;
        this.length = 1;
    }

    append(value){
        const node = new Node(value);
        this.tail.next = node;
        this.tail = node;
        this.length++;
        return this;
    }

    prepend(value){
        const node = new Node(value);
        node.next = this.head;
        this.head = node;
        this.length++;
        return this;
    }

    traverseToIndex(index){
        let counter = 0;
        let current = this.head;
        while(counter !== index){
            current = current.next;
            counter++;
        }
        return current;
    }

    insert(index, value){
        if(index >= this.length){
            return this.append(value);
        }
        if (index === 0){
            return this.prepend(value);
        }
        const node = new Node(value);
        const current = this.traverseToIndex(index - 1);
        node.next = current.next;
        current.next = node;
        this.length++;
        return this;
    }

    remove(index){
        if(index >= this.length){
            throw new Error('Index out of bounds');
        }
        if (index === 0){
            this.head = this.head.next;
            this.length--;
            return this;
        }
        const current = this.traverseToIndex(index - 1);
        let toremove = current.next;
        current.next = toremove.next;
        this.length--;
    }

    printList(){
        const array = [];
        let currentNode = this.head;
        while(currentNode !== null){
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }
}

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

let myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);myLinkedList.prepend(1);
myLinkedList.insert(2, 99);
myLinkedList.insert(20, 88);
myLinkedList.remove(2);

class DoublyLinkedList {
    constructor(value) {
        this.head = {
            value: value,
            next: null,
            prev: null
        }
        this.tail = this.head;
        this.length = 1;
    }

    printList(){
        const array = [];
        let currentNode = this.head;
        while(currentNode !== null){
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }

    traverseToIndex(index){
        let counter = 0;
        let current = this.head;
        while(counter !== index){
            current = current.next;
            counter++;
        }
        return current;
    }

    append(value){
        const node = new DoubleNode(value);
        this.tail.next = node;
        node.prev = this.tail;
        this.tail = node;
        this.length++;
        return this;
    }

    prepend(value){
        const node = new DoubleNode(value);
        node.next = this.head;
        this.head.prev = node;
        this.head = node;
        this.length++;
        return this;
    }

    insert(index, value){
        if(index >= this.length){
            return this.append(value);
        }
        if (index === 0){
            return this.prepend(value);
        }
        const node = new DoubleNode(value);
        const current = this.traverseToIndex(index - 1);
        const follower = current.next;
        node.next = follower;
        node.prev = current;
        follower.prev = node;
        current.next = node;
        this.length++;
        return this;
    }

    remove(index){
        if(index >= this.length){
            throw new Error('Index out of bounds');
        }
        if (index === 0){
            this.head = this.head.next;
            this.length--;
            return this;
        }
        const current = this.traverseToIndex(index - 1);
        let toremove = current.next;
        current.next = toremove.next;
        current.next.prev = current;
        this.length--;
    }

    reverse(){
        if(!this.head.next){
            return this.head;
        }
        let first = this.head;
        this.tail = this.head;
        let second = first.next;
        while(second){
            const third = second.next;
            second.next = first;
            first = second;
            second = third;
        }
        this.head.next = null;
        this.head = first;
        return this;
    }
}

class DoubleNode {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}