let txt = "abcdefghijklmnopqrstuvwxyz";
let txt0 = txt.length;
console.log(txt0);

let txt1 = "please visit";
let txt2 = txt1.replace("please" ,"bgu");
console.log(txt2);

let txt3 = txt1.concat(" and ", txt2);
console.log(txt3);

const d =new Date();
//console.log(d);


function greet(){

    const d = new Date();
    var h = d.getHours();
    //console.log(h);
    if(h<12){
        let greeting = "good morning";
        console.log(greeting);
        document.getElementById("1").innerHTML = greeting;
    }
    else if(h<18){
        let greeting2 = "good afternoon";
        console.log(greeting2);
        document.getElementById("1").innerHTML = greeting2;
    }
    else{
        let greeting3 = "good evening";
        console.log(greeting3);
        document.getElementById("1").innerHTML = greeting3;
    }

}


let car =['toyota','honda','mazda'];
console.log(car);
text = "";
var i;
for(i=0; i<car.length; i++){

    text += car[i] + " " ;
    console.log(text);
}


var imgs = [
      "imgs/pug.png",
      "imgs/worldmap.jpg",
      "imgs/sea.jpg"
    ];
      

var i=0;

function stopmotion(){
    
    setTimeout(() => {
         document.getElementById("SMimg").src =imgs[i];
         i++;
         if(i<imgs.length){
             stopmotion();
         }
         else{
            i=0;
         }
    }, 400);

}

var person = {firstName: "sapir",lastName:"bibi" , id: "305159980" ,
fullName: function() {return this.firstName + " " + this.lastName;}
};
console.log(person.fullName());

