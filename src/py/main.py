from pyscript import document
import js
import json
planet = {
    "name": "Sun",
    "radius": "140000000",
    "isGreatAttractor": "True",
    "Appearance": {
        "color": "red",
        "material": "metal"
    },
    "GravitationalParameters": {
        "mass": "720000000000000000000000000000",
        "density": "2"
    }
}
toJS = []
toJS.append(planet)
print(toJS)
txt = document.querySelector("#python")
txt.innerText = toJS

