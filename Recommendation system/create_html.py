import pandas as pd


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
    hotel=txt[4:len(txt)]
    #print(hotel)
    #couple[2] for austria hotel should give us 5
    #print(couple[2])

    file=pd.read_csv(dataset)
    hotel=file["Hotel_Name"]
    unique_hotel=hotel.unique()
    #print(hotel[1])
    couple_hotel=[]
    for i in range(1,len(couple)):
        hotel_name=hotel[int(couple[i])]
        if hotel_name not in couple_hotel:
            couple_hotel.append(hotel_name)
    #print(couple_hotel)
    #print(hotel[int(couple[1])])
    page=output.replace("txt","html")
    #print(page)
    f = open(page,'r')
    for line in f:
        print("hi")
        print(line)
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


    </style>

    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">

    <h1 style="color:black;font-family:Times;text-align:center;font-size:60px ">Explore Austria</h1>
    <body>

    <ul>
        <li><a href="page.html">Home</a></li>
        <li><a href="Business.html">Business</a></li>
        <li><a href="Leisure.html">Leisure</a></li>
    </ul>
    <button id="Couple">Couple</button><button id="Family">Family</button><button id="Solo">Solo</button><button id="Group">Group</button>
    </br>
    </br>
    <div id="Couple_hotel"></div>
    
    
"""
    message+='<script>document.getElementById("Couple").onclick=function() {document.getElementById("Couple_hotel").innerHTML='
    for i in range(len(couple_hotel)):
        if i == 0:
            message+='"'
        if i == len(couple_hotel)-1:
            message+=couple_hotel[i]+'"'
        else:
            message+=couple_hotel[i]+"<br><br>"
    message+="; }</script>"
    message+="<a href="
    
    message+="</a>"
    message+="<p>"+str(couple[1:5])+"</p>"
    message+="</body>"
    
    f.write(message)
    f.close()


create_html("Hotel_Austria_Business.txt","Austria_Business.csv")
