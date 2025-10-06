/*
* Implémentation tri par insertion en javascript 
*/

function insertionSort(arr) {
  let n = arr.length;

  for (let i = 1; i < n; i++) {
    let key = arr[i];
    let j = i - 1;

    // Déplacement des éléments plus grands
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }

    arr[j + 1] = key;
  }

  return arr;
}

// exemple

console.log(insertionSort([5, 2, 4, 6, 1, 3]));

/*
* Utilisation: node insertion.js (deps: avoir node.js installé sur le système)
*/
