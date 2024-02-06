function solution(name, yearning, photo) {
    var answer = [];
    const obj = name.reduce((acc,cur,idx)=>{
        acc[cur] = yearning[idx];
        return acc;
    },{});
    photo.forEach((p)=>{
        let sum = 0;
        p.forEach((n)=> {
            if(n in obj) sum+=obj[n];
        })
        answer.push(sum);
        console.log('sum =',sum);
    });
    return answer;
}