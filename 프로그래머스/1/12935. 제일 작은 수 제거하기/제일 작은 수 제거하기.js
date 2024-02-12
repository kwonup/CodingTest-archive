function solution(arr) {
    let min = arr[0];
    let min_idx = 0;
    for(let i=0;i<arr.length;i++){
        if(arr[i]<min) {
            min = arr[i];
            min_idx = i;
        }
    }
    arr.splice(min_idx,1);
    return arr.length===0? [-1]:arr; 
}