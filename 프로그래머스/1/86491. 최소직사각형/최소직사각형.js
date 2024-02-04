function solution(sizes) {
    let max_w=0,max_h=0;
    for(let i=0;i<sizes.length;i++){
        if(sizes[i][0]<sizes[i][1]) [sizes[i][0],sizes[i][1]]=[sizes[i][1],sizes[i][0]];
        max_w = sizes[i][0]>max_w? sizes[i][0]:max_w;
        max_h = sizes[i][1]>max_h? sizes[i][1]:max_h;       
    }
    return max_w*max_h;
}