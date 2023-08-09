let calculations = 0;
function fibonacci(n) {
    calculations++;
    if(n < 2) {
        return n;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

console.log(fibonacci(15)) // O(2^n) time
console.log('bad fib', calculations)

let calculations2 = 0;
function fibonacciBetter() {
    let cache = {}
    return function fib(n) {
        calculations2++;
        if(n in cache) {
            return cache[n]
        } else {
            if(n < 2) {
                return n;
            } else {
                cache[n] = fib(n-1) + fib(n-2);
                return cache[n];
            }
        }
    }
}

const fibDynamic = fibonacciBetter();
console.log(fibDynamic(15)) // O(n) time
console.log('good fib', calculations2)

function fibonacciBottomUp(n) {
    let arr = [0, 1];
    for(let i = 2; i <= n; i++) {
        arr.push(arr[i-1] + arr[i-2]);
    }
    return arr.pop();
}

console.log(fibonacciBottomUp(15))