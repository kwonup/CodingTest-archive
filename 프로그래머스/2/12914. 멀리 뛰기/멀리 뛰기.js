//각각의 경우의 수 직접 세어 본 다음 규칙성 발견해서 피보나치수열인것 확인
function solution(n) {
    let a=1,b=1;
    let mod=1234567;
    for(let i=2;i<=n;i++){
        let next = a%mod + b%mod; // 나머지연산의 이유 : 큰 수의 오버플로우를 방지하고, JavaScript에서 안전한 정수 범위 내에서 계산을 유지하도록 도와줍니다.
        a=b;
        b=next;
    }
    let answer = n===1? 1:b;
    return answer%1234567;
}
