#Import panda and google_images_download library
import pandas as pd
from google_images_download import google_images_download  

def create_html(output,dataset):

    out=open(output,"r")
    txt=[]
    for line in out:
        line=line.strip("\n").split(",")
        txt.append(line)

    couple=txt[0]
    family=txt[1]
    solo=txt[2]
    group=txt[3]
    hotel_score=txt[4:len(txt)]
    #print(hotel)
    #couple[2] for austria hotel should give us 5
    #print(couple[2])
    
    file=pd.read_csv(dataset)
    hotel=file["Hotel_Name"]
    hotel_address=file["Hotel_Address"]
    negative_review=file["Negative_Review"]
    positive_review=file["Positive_Review"]
    nationality=file["Reviewer_Nationality"]
    unique_hotel=hotel.unique()
    #print(hotel[1])
    couple_hotel=[]
    for i in range(1,len(couple)):
        hotel_name=hotel[int(couple[i])]
        if hotel_name not in couple_hotel:
            couple_hotel.append(hotel_name)
    #print(couple_hotel)
    #print(hotel[int(couple[1])])

    # creating object 
    response = google_images_download.googleimagesdownload()
    search_queries=""
    for i in range(3):
        if i==2:
            search_queries+=unique_hotel[i]
        else:
            search_queries+=unique_hotel[i]+","    

    arguments = {"keywords": search_queries, "format": "jpg", "limit":1, "no_download":True}
    paths=response.download(arguments)
    #print(paths)
    #print(paths[0]["Hotel Bellevue Wien"])
    page=output.replace("txt","html")
    #print(page)
    #f = open(page,'r')
    #for line in f:
        #print("hi")
        #print(line)
    f = open("testing.html",'w')
    message = """<!--
    Author: Teh Run Xun
    CSS from: W3Schools (https://www.w3schools.com/w3css/w3css_downloads.asp)
    -->

    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
    <style>

    ul {
      list-style-type: none;
      margin: 0;
      padding: 0;
      overflow: hidden;
      background-color: #c19a6b;
    }

    li {
      float: left;
    }

    li a {
      display: block;
      color: white;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
    }

    li a:hover {
      background-color: #8b5a2b;
    }

    .button {
        background-color: #c19a6b;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 6px 18px;
        cursor: pointer;
    }

    .collapsible {
      position: absolute;
      right: 0;
      width: 1700px;
      height: 200px;
      border: 3px solid black;
      background-color: white;
      color: black;
      cursor: pointer;
      padding: 20px;
      text-align: left;
      outline: none;
      font-size: 18px;
    }

    .content {
        padding: 0 18px;
        display: none;
        overflow: hidden;
        background-color: white;
        border: 2px solid black
    </style>

    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

    <h1 style="color:black;font-family:Times;text-align:center;font-size:60px ">Explore Austria</h1>
    <body>

    <ul>
        <li><a href="page.html">Home</a></li>
        <li><a href="Business.html">Business</a></li>
        <li><a href="Leisure.html">Leisure</a></li>
    </ul>
    </br>
    </br>
    
"""
    for i in range(3):
        message+='<p></p><img src='
        name=unique_hotel[i]
        for l in range(len(hotel_score)):
            if name in hotel_score[l]:
                first_id=int(hotel_score[l][1])
                score=hotel_score[l][3]
                break
        message+='"'+paths[0][name][0]+'" width=200 height=200><button class="collapsible"><p>'
        message+="Hotel Name: "+name+"</br>Address: "+hotel_address[first_id]+"</br>Score: "+score+"</p></button>"
        message+='''<div class="content">
            <p>
          <select onchange="myFunction(this)">
          <option></option>
          <option>Couple</option>
          <option>Family</option>
          <option>Solo</option>
          <option>Group</option>
         </select>

         <p id="demo'''
        message+=str(i)+'">Please select one of the option</p></p></div>'
        
    """
    for i in range(len(couple_hotel)):
        if i == 0:
            message+='"'
        if i == len(couple_hotel)-1:
            message+=couple_hotel[i]+'"'
        else:
            message+=couple_hotel[i]+"<br><br>"

    message+="<p>"+str(couple[1:5])+"</p>"
    """
    message+='''<script>
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
          content.style.display = "none";
        } else {
          content.style.display = "block";
        }
      });
    }
    function myFunction(selTag) {
      var x = selTag.options[selTag.selectedIndex].text;
      if (x=="Couple") {
            document.getElementById("demo0").innerHTML = "Hotel 1";'''
    """
    for i in range(len(unique_hotel)):
        name=unique_hotel[i]
        first_id=int(hotel_score[i][1])
        last_id=int(hotel_score[i][2])
        x=1
        add=False
        while x>=1:
            index=int(couple[x])
            print(index)
            if index>=first_id and index<=last_id:
                if add==True:
                    message+="</br><hr>"
                else:
                    message+="Reviewer's nationality: " + nationality[i] + "</br></br>Positive: " +  positive_review[i] + "</br></br>Negative:" + negative_review[i]
                    add=True
                    x+=1
            else:
                message+='</p>";'
                break"""
                
    message+='''
      }
      else if (x=="Family") {
            document.getElementById("demo0").innerHTML = "Hotel 2";
      }
      else if (x=="Solo") {
            document.getElementById("demo0").innerHTML = "Hotel 3";
      }
      else if (x=="Group") {
            document.getElementById("demo0").innerHTML = "Hotel 4";
      }
      else if (x=="") {
            document.getElementById("demo0").innerHTML = "Hotels";'''
    '''
    for i in range(len(hotel)):
        if i==len(hotel)-1:
            message+="Reviewer's nationality: " + nationality[i] + "</br></br>Positive: " +  positive_review[i] + "</br></br>Negative:" + negative_review[i] + '</p>";'
        else:
            message+="Reviewer's nationality: " + nationality[i] + "</br></br>Positive: " +  positive_review[i] + "</br></br>Negative:" + negative_review[i] + "</br><hr>"
    '''
    message+="""
      }
    }
    </script>"""
    message+="</body></html>"
    
    f.write(message)
    f.close()


create_html("Hotel_Austria_Business.txt","Austria_Business.csv")
