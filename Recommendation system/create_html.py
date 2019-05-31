#Import panda and google_images_download library
import pandas as pd
from google_images_download import google_images_download  

def create_html(output,dataset,country):

    out=open(output,"r")
    txt=[]
    for line in out:
        line=line.strip("\n").split(",")
        txt.append(line)
    country=country
    couple=txt[0]
    family=txt[1]
    solo=txt[2]
    group=txt[3]
    hotel=txt[4:len(txt)]
    
    file=pd.read_csv(dataset)
    hotel_address=file["Hotel_Address"]
    negative_review=file["Negative_Review"]
    positive_review=file["Positive_Review"]
    nationality=file["Reviewer_Nationality"]
    tags=file["Tags"]
    hotel_test=file["Hotel_Name"]

    # Sort hotel score (descending order)
    hotel.sort(key=lambda hotel: hotel[3], reverse=True)

    # creating object 
    response = google_images_download.googleimagesdownload()
    search_queries=""
    print(hotel[0])
    for i in range(len(hotel)):
        if i==len(hotel)-1:
            search_queries+=hotel[i][0]
        else:
            search_queries+=hotel[i][0]+","    
    arguments = {"keywords": search_queries, "format": "jpg", "limit":1, "no_download":True}
    paths=response.download(arguments)
    page=output.replace("txt","html")
    f = open(page,'w')
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

    <h1 style="color:black;font-family:Times;text-align:center;font-size:60px ">Explore """
    message+=country+"""</h1>
    <body>

    <ul>
        <li><a href="Homepage.html">Home</a></li>
        <li><a href="Business.html">Business</a></li>
        <li><a href="Leisure.html">Leisure</a></li>
    </ul>
    </br>
    </br>
    
    """
    for i in range(len(hotel)):
        message+='<p></p><img src='
        name=hotel[i][0]
        for l in range(len(hotel)):
            if name in hotel[l]:
                first_id=int(hotel[l][1])
                score=hotel[l][3]
                break

        message+='"'+paths[0][name][0]+'" width=200 height=200><button class="collapsible"><p>'
        message+="Hotel Name: "+name+"</br>Address: "+hotel_address[first_id]+"</br>Score: "+score+"</p></button>"
        message+='''<div class="content">
            <p>
          <select onchange="myFunction'''
        message+=str(i)+'''(this)">
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
    }'''
    for i in range(len(hotel)):
        couple_hotel=[]
        family_hotel=[]
        solo_hotel=[]
        group_hotel=[]
        first_id=int(hotel[i][1])
        last_id=int(hotel[i][2])
        for l in range(first_id,last_id+1):
            x=tags[l].split()
            if x[5]=="Couple":
                couple_hotel.append(l)
            elif x[5]=="Family":
                family_hotel.append(l)
            elif x[5]=="Solo":
                solo_hotel.append(l)
            elif x[5]=="Group":
                group_hotel.append(l)

        message+='''
        function myFunction'''
        message+=str(i)+'''(selTag) {
          var x = selTag.options[selTag.selectedIndex].text;
          if (x=="Couple") {
                document.getElementById("demo'''
        message+=str(i)+'''").innerHTML = "<p>'''
        if len(couple_hotel)==0:
            message+='No couple stay here!</p>"'
        else:
            for k in range(len(couple_hotel)):
                index=int(couple_hotel[k])
                if k==len(couple_hotel)-1:
                    message+="Nationality of reviewer: " + nationality[index] + "</br></br>Positive: " +  positive_review[index] + "</br></br>Negative:" + negative_review[index] + '</p>";'
                else:
                    message+="Nationality of reviewer: " + nationality[index] + "</br></br>Positive: " +  positive_review[index] + "</br></br>Negative:" + negative_review[index] + "</br><hr>"

        message+='''
          }
          else if (x=="Family") {
                document.getElementById("demo'''
        message+=str(i)+'''").innerHTML = "<p>'''
        if len(family_hotel)==0:
            message+='No family stay here!</p>"'
        else:
            for k in range(len(family_hotel)):
                index=int(family_hotel[k])
                if k==len(family_hotel)-1:
                    message+="Nationality of reviewer: " + nationality[index] + "</br></br>Positive: " +  positive_review[index] + "</br></br>Negative:" + negative_review[index] + '</p>";'
                else:
                    message+="Nationality of reviewer: " + nationality[index] + "</br></br>Positive: " +  positive_review[index] + "</br></br>Negative:" + negative_review[index] + "</br><hr>"
        message+='''
          }
          else if (x=="Solo") {
                document.getElementById("demo'''
        message+=str(i)+'''").innerHTML = "<p>'''
        if len(solo_hotel)==0:
            message+='No solo stay here!</p>"'
        else:
            for k in range(len(solo_hotel)):
                index=int(solo_hotel[k])
                if k==len(solo_hotel)-1:
                    message+="Nationality of reviewer: " + nationality[index] + "</br></br>Positive: " +  positive_review[index] + "</br></br>Negative:" + negative_review[index] + '</p>";'
                else:
                    message+="Nationality of reviewer: " + nationality[index] + "</br></br>Positive: " +  positive_review[index] + "</br></br>Negative:" + negative_review[index] + "</br><hr>"
        message+='''
          }
          else if (x=="Group") {
                document.getElementById("demo'''
        message+=str(i)+'''").innerHTML = "<p>'''
        if len(group_hotel)==0:
            message+='No group stay here!</p>"'
        else:
            for k in range(len(group_hotel)):
                index=int(group_hotel[k])
                if k==len(group_hotel)-1:
                    message+="Nationality of reviewer: " + nationality[index] + "</br></br>Positive: " +  positive_review[index] + "</br></br>Negative:" + negative_review[index] + '</p>";'
                else:
                    message+="Nationality of reviewer: " + nationality[index] + "</br></br>Positive: " +  positive_review[index] + "</br></br>Negative:" + negative_review[index] + "</br><hr>"
        message+='''
          }
          else if (x=="") {
                document.getElementById("demo'''
        message+=str(i)+'''").innerHTML = "Please select one of the 4 groups!";
          }
        }
        '''
    message+="""
    </script></body></html>"""
    
    f.write(message)
    f.close()


create_html("Hotel_Austria_Business.txt","Austria_Business.csv","Austria")
create_html("Hotel_France_Business.txt","France_Business.csv","France")
create_html("Hotel_Italy_Business.txt","Italy_Business.csv","Italy")
create_html("Hotel_Kingdom_Business.txt","Kingdom_Business.csv","Kingdom")
create_html("Hotel_Netherlands_Business.txt","Netherlands_Business.csv","Netherlands")
create_html("Hotel_Spain_Business.txt","Spain_Business.csv","Spain")

create_html("Hotel_Austria_Leisure.txt","Austria_Leisure.csv","Austria")
create_html("Hotel_France_Leisure.txt","France_Leisure.csv","France")
create_html("Hotel_Italy_Leisure.txt","Italy_Leisure.csv","Italy")
create_html("Hotel_Kingdom_Leisure.txt","Kingdom_Leisure.csv","Kingdom")
create_html("Hotel_Netherlands_Leisure.txt","Netherlands_Leisure.csv","Netherlands")
create_html("Hotel_Spain_Leisure.txt","Spain_Leisure.csv","Spain")


