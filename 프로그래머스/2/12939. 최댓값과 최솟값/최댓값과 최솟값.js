function solution(s) {
    let arr = s.split(' ').map(elem=>parseInt(elem));
    let max=arr[0],min=arr[0];
    arr.forEach((elem)=>{
        if(elem>max) max = elem;
        if(elem<min) min = elem;
    })
    return min+' '+max;
}