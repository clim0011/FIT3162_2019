//window.addEventListener('load', testing, false);
//window.addEventListener('load', testing2, false);
//window.addEventListener('load', testing, false);

var http=require('http');
function testing(){
  const fs = require('fs') 
  fs.readFile('test.txt', (err, data) => { 
      if (err) throw err; 
      console.log(data.toString())
      //document.getElementById("demo").innerHTML = "ok";
      return data.toString();
      //document.getElementById("demo").innerHTML = console.log(data.toString()); 
  })
}
/*
function readTextFile(file)
{
    console.log("hi");
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
            if(rawFile.status === 200 || rawFile.status == 0)
            {
              console.log("naninaninani");
                var allText = rawFile.responseText;
                alert(allText);
            }
        }
    }
    rawFile.send(null);
}

document.getElementById('file').onchange = function(){

    var file = this.files[0];
  
    var reader = new FileReader();
    reader.onload = function(progressEvent){
      // Entire file
      console.log(this.result);
  
      // By lines
      var lines = this.result.split('\n');
      for(var line = 0; line < lines.length; line++){
        console.log(lines[line]);
      }
    };
    reader.readAsText(file);
  };




function testing(){
    document.getElementById("demo").innerHTML = "ok";
}

function testing2(){

    const fs = require('fs') 
    fs.readFile('test.txt', (err, data) => { 
        if (err) throw err; 
        console.log(data.toString())
        return data.toString();
        //document.getElementById("demo").innerHTML = console.log(data.toString()); 
    })
}

var x = testing2();
document.getElementById("demo").innerHTML = x;
console.log(x);
*/

document.getElementById("demo").innerHTML=testing();