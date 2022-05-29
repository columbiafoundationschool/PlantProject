import qrcode

url = "https://columbiafoundationschool.github.io/PlantProject/Website/neem/neem.html"

img = qrcode.make(url)

img.save('neem.png')
