function solution(s) {
    let cnt=0;//올바른 괄호문자열의 갯수
    let arr = [...s]; //s가 문자열이므로 spread문으로 배열로 변환
    for(let i=0;i<s.length;i++){
        let firstIdx = arr.shift(); //shift메소드는 배열의 첫번째 요소를 제거하고 그 요소를 반환함
        arr.push(firstIdx);
        //arr이 올바른 괄호 문자열이라면 cnt++
        if(isCorrectBracket(arr)) cnt++;
    }
    return cnt;
}
const isCorrectBracket = (s)=>{
    let stack =[]; //괄호를 담을 스택배열
    //괄호 문자열 객체
    let brackets={ 
        '(':')',
        '[':']',
        '{':'}'
    }
    for(let elem of s){
        //여는괄호라면
        if(brackets[elem]) stack.push(elem);
        else{ //닫는괄호라면
            if(stack.length===0)return false;//스택이 비어있으면 괄호호응 실패이므로 false반환
            let last = stack.pop(); //스택의 마지막 원소를 pop으로 제거하고 반환
            if (brackets[last]!==elem) return false; //반환된 원소와 짝지어진 괄호가 elem과 다르면 false반환
        }
    }
    //스택의 길이가 0이면 참 반환
    return stack.length===0? true:false;
}