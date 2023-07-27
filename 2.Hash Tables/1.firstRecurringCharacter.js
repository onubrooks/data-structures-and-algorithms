//Google Question
//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return undefined

function firstRecurringCharacterQuadratic(input) {
    for (let i = 0; i < input.length; i++) {
      for (let j = i + 1; j < input.length; j++) {
        if(input[i] === input[j]) {
          return input[i];
        }
      }
    }
    return undefined
  }

function firstRecurringCharacter(input) {
    let map = {};
    for (let i = 0; i < input.length; i++) {
        if (map[input[i]]) {
            return input[i];
        } else {
            map[input[i]] = true;
        }
    }
    return undefined;
} //O(n)

function firstRecurringCharacterSet(input) {
    let set = new Set();
    for (let i = 0; i < input.length; i++) {
        if (set.has(input[i])) {
            return input[i];
        } else {
            set.add(input[i]);
        }
    }
    return undefined;
}

//Bonus... What if we had this:
// [2,5,5,2,3,5,1,2,4]
// return 5 because the pairs are before 2,2
console.log(firstRecurringCharacter([2,5,1,2,3,5,1,2,4]));
console.log(firstRecurringCharacter([2,1,1,2,3,5,1,2,4]));
console.log(firstRecurringCharacter([2,3,4,5]));
console.log(firstRecurringCharacter([2, 5, 5, 2, 3, 5, 1, 2, 4]));