import qrcode

url = "https://columbiafoundationschool.github.io/PlantProject/Website/giloy/giloy.html"

img = qrcode.make(url)

img.save('giloy.png')
