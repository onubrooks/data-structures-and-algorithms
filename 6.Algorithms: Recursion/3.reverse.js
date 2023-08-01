//Implement a function that reverses a string using iteration...and then recursion!
function reverseStringIter(str) {
    let rev = '';
    for(let i = str.length - 1; i >= 0; i--){
      rev += str[i];
    }
    return rev;
  }
  
  function reverseStringRecur(str) {
    if(str.length === 1){
      return str;
    }
    return reverseStringRecur(str.slice(1)) + str[0];
  }
  
  console.log(reverseStringIter('yoyo mastery'))
  console.log(reverseStringRecur('yoyo mastery'))
  //should return: 'yretsam oyoy'