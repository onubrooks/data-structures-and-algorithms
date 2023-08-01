// 1. have a base case
// 2. hava a recursive case
// 3. get closer and closer to the base case, and return when needed. Usually you have 2 returns

function findFactorialRecursive(number) {
    //code here
    if (number < 3) {
        return number;
    } else {
        return number * findFactorialRecursive(number - 1);
    }
  }
  
  function findFactorialIterative(number) {
    let answer = 1;
    if(number === 2 || number === 1) {
        return number;
    }
    for(let i = 2; i <= number; i++) {
        answer = answer * i;
    }
  }