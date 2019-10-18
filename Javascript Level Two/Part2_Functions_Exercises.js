//problem 1: Sleeping In
function sleepIn(weekday,vacation){
  if(!weekday && !vacation){
    return true;
  }else if(weekday && !vacation){
    return false;
  }else if(!weekday && vacation){
    return true;
  }
}

//problem 2: Monky trouble
function monkeyTrouble(a,b){
  if(!a && !b){
    return true;
  }else if(a && b){
    return true;
  }else if(a && b){
    return false;
  }
}


// problem 3: STRING TIMES
function stringTimes(str, n){
  var i = 0;
  var string = "";
  while(i < n){
    string += str;
    i++;
  }
  // console.log(string);
  return string;
}

function luckySome(a,b,c) {
  cnt = 0;
  if(a === 13){
    cnt++;
  }
  if(b === 13){
    cnt++;
  }
  if(c === 13){
    cnt++;
  }
  return a+b+c - 13*cnt;
}

// problem 4:caught_speeding

function caught_speeding(speed, is_birthday){
  if(is_brithday){
    speed -= 5;
  }
  if(speed <= 60){
    return 0;
  }
  if(60<speed <= 80){
    return 1;
  }
  return 2;
}

// problem 5: makeBricks
// I don't understand this problem . It's just copy

function makeBricks(small, big, goal){
  return goal%5 >= 0 && goal%5 - small <= 0 && small + 5*big >= goal;
}
