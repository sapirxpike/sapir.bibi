

function namefunction(){
   // var String x  ;
   // x=sapir-bibi;
    
    
    //console.log(x);
   // document.getElementById("demo2").innerHTML= end;
    //console.log(bool);
    
    
   // var user = {
    //    firstname: 'eli', 
    //    lastname: 'cohen' ,
    //    email: 'elicohen@gmail.com',
    //    age:25
    //}
  //  console.log(user);
   // console.log(user.email);
    //}


    
var user = {
    firstname: 'sapir', 
    lastname: 'bibi' ,
   
}
console.log(user);

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



