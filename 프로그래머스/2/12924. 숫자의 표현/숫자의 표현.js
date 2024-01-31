function solution(n) {
    let answer=1;
    let sum=0;
    let tmp;
    for(let i=1;i<=n/2;i++){
        sum=0;
        tmp=i;
        while(sum<=n){
            sum+=tmp;
            //process.stdout.write(tmp+' ');
            if(sum===n){
                //process.stdout.write(' sum = '+sum);
                answer++;
                break;
            }
            tmp++;
        }
        //console.log();
    }
    return answer;
}