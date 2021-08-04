function stc(){    
    this.arr = []
    this.top = 0
    this.push = push
    this.pop = pop
    this.peek = peek
    this.print = print
}

function push(data){
    this.arr[this.top] = data
    this.top+=1
}

function pop(data){
    let temp = this.arr[this.top-1]
    this.top--
    console.log(temp)
}

function peek(data){
    console.log(this.arr[this.top-1])
}


function print(){
    for(let i=0; i<this.top; i++){
      console.log(this.arr[i])
}}

let obj = new stc()
obj.push("sam")
obj.push("sharan")
obj.peek()
obj.print()
obj.pop()
obj.print()
