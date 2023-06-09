# PathFinder using UCS and A* Algorithm
Tugas Kecil III IF2211 Algorithm Strategies
<br />

## Table of Contents
* [General Info](#general-information)
* [Tampilan Program](#tampilan-program)
* [How To Run](#how-to-run)
* [Tech Stack](#tech-stack)
* [Project Structure](#project-structure)
* [Credits](#credits)

## General Information
Program ini dapat digunakan untuk mencari lintasan terdekat dari suatu simpul ke simpul yang lain pada suatu graf menggunakan algoritma Uniform Cost Search (UCS) dan algoritma A star (A*). Program mendapatkan grafnya berdasarkan input file text yang berisi matriks ketetanggaan beserta nilai heuristiknya.

## Tampilan Program
![Screenshot](assets/screenshot.jpg)

## How To Run
In terminal, move to src folder and run:
```shell
python main.py
```
A window will appear if the program is run successfully!

## Tech Stack
### Programming Languange
* Python

### Requirements
* Tkinter
* Pillow
* Networkx
* Matplotlib

## Project Structure
```bash
Tucil3_13521062_13521064
│
├───assets
│    ├──background.png
│    ├──graph.png
│    ├──logo.png
│    └──screenshot.jpg
│
├───doc
│    └──Tucil3_13521062_13521064.pdf
│
├───src
│    ├──Algorithm
│    │    ├──AStar.py
│    │    └──UCS.py
│    │
│    ├──Helper
│    │    ├──GraphDrawer.py
│    │    └──Parser.py
│    │
│    └──main.py
│
├───test
│    ├──tc1-KampusITB.txt
│    ├──tc2-AlunAlunBandung.txt
│    ├──tc3-BuahBatu.txt
│    ├──tc4-AlunAlunJember.txt
│    ├──tc5-Imaginary.txt
│    ├──tc6-BigImaginary.txt
│    └──tc7-WrongInput.txt
│
└───README.md
```

## Credits
This project is implemented by:
1. Go Dillon Audris (13521062)
2. Bill Clinton (13521064)