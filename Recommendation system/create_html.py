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

    # creating object 
    response = google_images_download.googleimagesdownload()
    search_queries=""
    for i in range(len(unique_hotel)):
        if i==len(unique_hotel)-1:
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
    for i in range(len(unique_hotel)):
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
    couple_index=1
    family_index=1
    solo_index=1
    group_index=1
    for i in range(len(unique_hotel)):
        name=unique_hotel[i]
        for l in range(len(hotel_score)):
            if name in hotel_score[l]:
                first_id=int(hotel_score[l][1])
                last_id=int(hotel_score[l][2])
                break
        couple_hotel=[]
        family_hotel=[]
        solo_hotel=[]
        group_hotel=[]
        print(name)
        print(int(couple[couple_index]))
        print(i)
        print(first_id)
        print(last_id)
        while True:
            if int(couple[couple_index])>=first_id and int(couple[couple_index])<=last_id:
                couple_hotel.append(couple[couple_index])
                if couple_index==len(couple)-1:
                    break
                else:
                    couple_index+=1
            elif int(family[family_index])>=first_id and int(family[family_index])<=last_id:
                family_hotel.append(family[family_index])
                if family_index==len(family)-1:
                    break
                else:
                    family_index+=1
            elif int(solo[solo_index])>=first_id and int(solo[solo_index])<=last_id:
                solo_hotel.append(solo[solo_index])
                if solo_index==len(solo)-1:
                    break
                else:
                    solo_index+=1
            elif int(group[group_index])>=first_id and int(group[group_index])<=last_id:
                group_hotel.append(group[group_index])
                if group_index==len(group)-1:
                    break
                else:
                    group_index+=1
            else:
                break

        print("coupleHotel: "+str(couple_hotel))
        print("familyHotel: "+str(family_hotel))
        print("soloHotel: "+str(solo_hotel))
        print("groupHotel: "+str(group_hotel))
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
      
    '''
    for i in range(len(hotel)):
        if i==len(hotel)-1:
            message+="Reviewer's nationality: " + nationality[i] + "</br></br>Positive: " +  positive_review[i] + "</br></br>Negative:" + negative_review[i] + '</p>";'
        else:
            message+="Reviewer's nationality: " + nationality[i] + "</br></br>Positive: " +  positive_review[i] + "</br></br>Negative:" + negative_review[i] + "</br><hr>"
    '''
    message+="""
    </script>"""
    message+="</body></html>"
    
    f.write(message)
    f.close()


create_html("Hotel_Austria_Business.txt","Austria_Business.csv")
