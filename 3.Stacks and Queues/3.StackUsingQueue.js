class StackUsingQueue {
    constructor() {
        this.mainQueue = [];
        this.tempQueue = [];
    }

    push(value) {
        while (this.mainQueue.length !== 0) {
            // Move all elements from mainQueue to tempQueue using shift operation
            this.tempQueue.push(this.mainQueue.shift());
        }
    
        this.mainQueue.push(value);
    
        while (this.tempQueue.length !== 0) {
            // Move all elements from tempQueue to mainQueue using shift operation
            this.mainQueue.push(this.tempQueue.shift());
        }
    }

    pop() {
        if (this.mainQueue.length === 0) {
            return -1;
        }
        return this.mainQueue.shift();
    }

    top() {
        if (this.mainQueue.length === 0) {
            return -1;
        }
        return this.mainQueue[0];
    }

    empty() {
        return this.mainQueue.length === 0;
    }
}