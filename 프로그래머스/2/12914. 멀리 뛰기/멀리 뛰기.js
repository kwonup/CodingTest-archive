//각각의 경우의 수 직접 세어 본 다음 규칙성 발견해서 피보나치수열인것 확인
function solution(n) {
    let a=1,b=1;
    let mod=1234567;
    for(let i=2;i<=n;i++){
        let next = a%mod + b%mod;
        a=b;
        b=next;
    }
    let answer = n===1? 1:b;
    return answer%1234567;
}