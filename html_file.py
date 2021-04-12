import json
with open("DetailsOfPhones.json","r") as f:
    data=json.load(f)
with open("Details.html","w") as f:
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<title>This is phone details list </title>")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write("<table border='2px'>\n")
    f.write("<tr>\n")
    f.write("<th>"+" Name "+"</th>")
    f.write("<th>"+" RAM "+"</th>")
    f.write("<th>"+"Desplay "+"</th>")
    f.write("<th>"+" Camera "+"</th>")
    f.write("<th>"+"Battery"+"</th>")
    f.write("</tr>")
    i=0
    while i<len(data):
        f.write("<tr>\n")
        f.write("<td>"+data[i]['Name']+"</td>")
        f.write("<td>"+data[i]['RAM']+"</td>")
        f.write("<td>"+data[i]['Display']+"</td>")
        f.write("<td>"+data[i]['Camera']+"</td>")
        f.write("<td>"+data[i]['Battery']+"</td>")
        f.write("</tr>")
        i=i+1
    f.write("</table>")
    f.write("</body>")
    f.write("</html>")
    f.close()