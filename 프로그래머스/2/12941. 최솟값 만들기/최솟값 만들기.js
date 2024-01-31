function solution(A,B){
    var answer = 0;
    let len = A.length;
    let min=0;
    
    A.sort((a,b)=>(a-b));
    B.sort((a,b)=>(b-a));
    
    min = A.reduce((acc,cur,idx)=> acc+(cur*B[idx]),0);

    return min;
}