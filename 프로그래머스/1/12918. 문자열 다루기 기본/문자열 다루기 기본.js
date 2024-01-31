function solution(s) {
    if(s.length!==4 && s.length!==6) return false;
    else return [...s].every(char => (char>='0' && char<='9'));
}