function mergeSortedArrays(array1, array2){
    if(array1.length === 0) {
      return array2;
    }
    if(array2.length === 0) {
      return array1;
    }
    const mergedArray = [];
    let i = 0;
    let j = 0;    
  
    while (i < array1.length || j < array2.length){
     if(array2[j] == undefined || array1[i] <= array2[j]){
       mergedArray.push(array1[i]);
       i++;
     } else {
        mergedArray.push(array2[j]);
        j++;
      }
    }
    return mergedArray;
  }
  
  console.log(mergeSortedArrays([0,3,4,31], [3,4,6,30]));