# animation

**Version 1.0.0**

Code files and classes needed to implement an animated and interactive aquarium.

To test it, clone this repository and run main.py on any IDE. I use Pycharm.

This program uses GRAPHICS from John Zelle. Since I started developing this in repl.it, I had to dwonload it from https://pypi.org/project/graphics.py/ and copy the file graphics.py in the project folder, next to main.py. Since I didn't want to have two different versions of this program, I decided to leave it this way, as it wokrs fine both on- and offline. 

---

## Contents

- main.py
- fish.py
- bubble.py
- graphics.py --> downloaded from https://pypi.org/project/graphics.py/
- README.md

---

## How it works

- user places 3 fishes by clicking on the aquarium at the desired position
- fishes are generated with random colors, randomly pointing left or right, and with a random speed setting (number of pixels it moves per cycle)
- fourth click starts the animation. Fishes swim forward describing a sine form
- When fish reach an edge of the quarium, they change direction 180 degrees and keep swimming
- By pressing the key 'f' a piece of food is placed at a random position.
- The fish that is closest to the food starts swimming towards it in a direct direction to it, but still with a superposed sine form. For example diagonal but in a sine shaped movement.
- Once a fish ate the food, it keeps moving horizontally at it's initial speed.
- A click on the aquarium represents tapping the glass.
- When tapping, all fishes close to the tap coordinate swim away for 50 cycles at speed 3 horizontally. They even change direction if needed to go away form the tap.
  
---

## Required modules

- graphics --> downloaded from https://pypi.org/project/graphics.py/

---

## Contributors

- Carlos Valverde <carlos_valverdeb@hotmail.com>

---
## Licence and copyright

© Carlos Valverde

