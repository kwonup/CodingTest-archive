function solution(array, commands) {
    let answer = [];
    for(let i=0;i<commands.length;i++){
        let I = commands[i][0];
        let J = commands[i][1];
        let K = commands[i][2];
        let tmp =[];
        for(let j=I-1;j<=J-1;j++){
            tmp.push(array[j]);
        }
        tmp.sort((a,b)=>a-b);
        answer.push(tmp[K-1]);
    }
    return answer;
}