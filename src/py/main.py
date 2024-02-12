from pyscript import document
import js
import json
planet = open("/planet.json")
toJS = json.lod(planet)
print(toJS)
txt = document.querySelector("#python")
txt.innerText = toJS

