const numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0];

function bubbleSort(array) {
  const last = array.length
  for(let j = 0; j< last; j++) {
    for(let i = 0;i<last;i++) {
        if(array[i] > array[i+1]) {
            let temp = array[i+1]
            array[i+1] = array[i]
            array[i] = temp
        }
      }
  }
}

bubbleSort(numbers);
console.log(numbers);

function selectionSort(array) {
  for(let i = 0;i < array.length;i++) {
    let min = i;
    temp = array[i]
    for(let j = i+1;j < array.length;j++) {
        if(array[j] < array[min]) {
            min = j
        }
    }
    array[i] = array[min];
    array[min] = temp;
  }
  return array;
}

console.log(selectionSort(numbers));

function insertionSort(array) {
    for (let i = 0; i < array.length; i++) {
        if(array[i] < array[0]) {
            // move number to the first position
            array.unshift(array.splice(i, 1)[0]);
        } else {
            // find where the number should go
            for(let j = 1; j < i; j++) {
                if(array[i] > array[j-1] && array[i] < array[j]) {
                    // move the number to the correct spot
                    array.splice(j,0,array.splice(i,1)[0]);
                }
            }
        }
    }
    return array;
  }
  
console.log(insertionSort(numbers));

function mergeSort (array) {
    if (array.length === 1) {
      return array
    }
    // Split Array in into right and left
    const length = array.length;
    const middle = Math.floor(length / 2);
    const left = array.slice(0, middle);
    const right = array.slice(middle);
  
    return merge(
      mergeSort(left),
      mergeSort(right)
    )
  }
  
  function merge(left, right){
    let combined = [];
    let i = 0;
    let j = 0;
    while(i < left.length && j < right.length) {
        if(left[i] <= right[j]) {
            combined.push(left[i]);
            i++;
        } else {
            combined.push(right[j]);
            j++;
        }
    }
    if(left[i]){
        combined.concat(left.slice(i));
    }
    if(right[j]){
        combined.push(right.slice(j));
    }
  }
  
  
  const answer = mergeSort(numbers);
  console.log(answer);