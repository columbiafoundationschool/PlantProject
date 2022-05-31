import qrcode

url = "https://columbiafoundationschool.github.io/PlantProject/Website/vitex/vitex.html"

img = qrcode.make(url)

img.save('vitex.png')
