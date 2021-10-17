let STACK = [];
let RELATION = {};

const solution = (record) => {

  for(let i = 0; i < record.length; i++) {
    let stm_split = record[i].split(' ');
    let uuid = stm_split[1];
    if(stm_split.length === 2) {
      leave(uuid);
      continue;
    }
    (stm_split[0] === 'Enter') ? enter(uuid, stm_split[2]) : change(uuid, stm_split[2]);
  }

  let answer = new Array(STACK.length);
  for(let i = 0; i < STACK.length; i++){
    let action = STACK[i][0];
    let uuid = STACK[i][1];
    let name = RELATION[uuid];
    let str = name+"님이 ";
    action === 'ENTER' ? str += "들어왔습니다." : str += "나갔습니다.";
    answer[i] = str;
  }

  return answer;
}

const enter = (uuid, name) => {
  RELATION[uuid] = name;
  STACK.push(['ENTER', uuid]);
}

const leave = (uuid) => {
  STACK.push(['LEAVE', uuid]);
}

const change = (uuid, name) => {
  RELATION[uuid] = name;
}
