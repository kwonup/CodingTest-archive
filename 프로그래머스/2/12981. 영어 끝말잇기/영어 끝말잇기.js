function solution(n, words) {
    var answer = [];
    let failNum=0,failOrder=0;
    // words.forEach((elem,idx)=>{
    //     lastWord = words[idx-1];//배열의 이전 단어
    //     if(idx!==0 && 
    //        (elem[0]!==lastWord[lastWord.length-1] || words.slice(0,idx).includes(elem))){ 
    //         failNum = (idx+1)%n===0 ? n:(idx+1)%n;
    //         failOrder = (idx+1)%n===0 ? (idx+1)/n : parseInt((idx+1)/n)+1;
    //         //console.log(`failNum=${failNum}, failOrder=${failOrder}`);
    //     }
    // });
    
    for(let i=0;i<words.length;i++){
        lastWord = words[i-1];//배열의 이전 단어
        if(i!==0 && 
           (words[i][0]!==lastWord[lastWord.length-1] || words.slice(0,i).includes(words[i]))){ 
            failNum = (i+1)%n===0 ? n:(i+1)%n;
            failOrder = (i+1)%n===0 ? (i+1)/n : parseInt((i+1)/n)+1;
            break;
        }
    }
    answer = [failNum,failOrder];
    return answer;
}