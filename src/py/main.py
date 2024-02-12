from pyscript import document
import js


myObject = {
    "name": "Harold",
    "age": 25
}


toJS = []
toJS.append(myObject)
print(toJS)
txt = document.querySelector("#python")
txt.innerText = toJS

