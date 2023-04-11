from tkinter import *
from tkinter.filedialog import askopenfilename
from Helper.Parser import *
from Helper.GraphDrawer import *
from Algorithm.UCS import *
from Algorithm.AStar import *
from PIL import Image, ImageTk

"""========================================== INITIALIZE SEGMENT =========================================="""
# Root Window
root = Tk()
root.title("PathFinder - Using UCS and A*")
root.resizable(0,0)

# Center the Window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 1080
window_height = 608
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y - 30}")

# Canvas
background = PhotoImage(file="../assets/background.png")
canvas = Canvas(root, width = 1080, height=608)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image = background, anchor = "nw")

# Basic UI Label and Shape
canvas.create_text(400, 10, anchor="nw", text= "\u2605 Path Finder \u2605", font=("Segoe Script", 25, 'bold'), fill="#FFB3C1")
canvas.create_text(70, 160, anchor="nw", text= "Choose your graph file!", font=("Georgia", 16), fill="#FFFFFF")
canvas.create_text(70, 270, anchor="nw", text= "Choose the path to find!", font=("Georgia", 16), fill="#FFFFFF")
canvas.create_text(70, 300, anchor="nw", text= "Start Node: ", font=("Georgia", 16), fill="#FFFFFF")
canvas.create_text(70, 340, anchor="nw", text= "Goal Node: ", font=("Georgia", 16), fill="#FFFFFF")
canvas.create_text(70, 420, anchor="nw", text= "Choose the algorithm!", font=("Georgia", 16), fill="#FFFFFF")
canvas.create_rectangle(0, 70, 1440, 75, fill="#EE1AEF")
canvas.create_rectangle(0, 80, 1440, 85, fill="#EE1AEF")
canvas.create_rectangle(400, 85, 405, 1080, fill="#EE1AEF")

"""========================================= FILE CHOOSING SEGMENT ========================================="""
# Global Variables needed
parser = Parser("")
drawer = GraphDrawer([], -1, [[]])
valid = False

# File Name Label
fileName = StringVar()
fileName.set("")
fileNameLabel = Label(canvas, textvariable=fileName, fg="#000000", bg="#FFB3C1", font=("Times New Roman", 16), borderwidth=2, anchor="w", height= 1, width=20, relief="ridge")
fileNameWindow = canvas.create_window(70, 195, anchor="nw", window=fileNameLabel)

# Parsing Exception Label
parseExceptionLabel = canvas.create_text(70, 240, text = "", font=("Times New Roman", 11), fill="#FFFFFF", anchor="w")

# Procedure when the choose file button is clicked
def askFileName():
    global valid, parser, drawer, fileName, canvas, parseExceptionLabel
    valid = False
    graphFile = askopenfilename()
    temp = graphFile.split("/")[len(graphFile.split("/")) - 1]
    if (len(temp) > 19):
        fileName.set(temp[:19] + "...")
    else:
        fileName.set(temp)
    if (graphFile != ""):
        try:
            parser = Parser(graphFile)
            parser.openAndParse()
            drawer = GraphDrawer(parser.getNodeName(), parser.getRow(), parser.getMap())
            updateOptionNode(parser.getRow())
            updateResult([], "", 0, 0)
            canvas.itemconfigure(parseExceptionLabel, text="")
            valid = True
        except ValueError:
            canvas.itemconfigure(parseExceptionLabel, text="Unknown symbol in the map/graph file")
        except Exception as error:
            canvas.itemconfigure(parseExceptionLabel, text=error)

# File Chooser Button
fileChooserButton = Button(canvas, text="\u2b60", font=("Times New Roman", 11), command=askFileName, height= 1, width=4, bg="#EE1AEF")
fileChooserWindow = canvas.create_window(275, 195, anchor="nw", window=fileChooserButton)

"""========================================= NODE CHOOSING SEGMENT ========================================="""
# The Option Chosen
startChosen = StringVar()
goalChosen = StringVar()
node = [0]

# Start Node Option Menu
startNodeOption = OptionMenu(canvas, startChosen, *node)
startNodeOption.config(height=1, width=5, background="#FFB3C1")
startNodeWindow = canvas.create_window(190, 300, anchor="nw", window=startNodeOption)

# Goal Node Option Menu
goalNodeOption = OptionMenu(canvas, goalChosen, *node)
goalNodeOption.config(height=1, width=5, background="#FFB3C1")
goalNodeWindow = canvas.create_window(190, 340, anchor="nw", window=goalNodeOption)

# Update the nodes option according to the graph file
def updateOptionNode(row):
    global startChosen, goalChosen, startNodeOption, goalNodeOption
    node = [i+1 for i in range(row)]
    menu1 = startNodeOption["menu"]
    menu2 = goalNodeOption["menu"]
    menu1.delete(0, "end")
    menu2.delete(0, "end")
    for i in node:
        menu1.add_command(label=i, command= lambda value=i: startChosen.set(value))
        menu2.add_command(label=i, command= lambda value=i: goalChosen.set(value))

"""========================================= PATH FINDING SEGMENT ========================================="""
# Running Algorithm Exception Label
algorithmExceptionLabel = canvas.create_text(70, 500, text = "", font=("Times New Roman", 11), fill="#FFFFFF", anchor="w")

# Check if the algorithm can be run
def validateInput():
    global valid, startChosen, goalChosen, canvas, algorithmExceptionLabel
    if (not valid):
        raise Exception("Please input a valid graph file")
    elif ((len(startChosen.get())==0 or int(startChosen.get()) == 0 or int(startChosen.get()) > parser.getRow()) and (len(startChosen.get())==0 or int(goalChosen.get()) == 0 or int(goalChosen.get()) > parser.getRow())):
        raise Exception("Please input a valid start/goal node")
    canvas.itemconfigure(algorithmExceptionLabel, text="")

# Start the UCS Algorithm
def findUCSPath():
    global parser, canvas, algorithmExceptionLabel
    try:
        validateInput()
        ucs = UCS(parser.getMap(), int(startChosen.get())-1, parser.getNodeName())
        ucs.find_path_UCS(int(goalChosen.get())-1)
        if (ucs.getFoundPath()):
            updateResult(ucs.getPathResult(), ucs.printPathResult(), ucs.getDistance(), 0)
        else:
            canvas.itemconfigure(algorithmExceptionLabel, text="The path does not exist") 
    except Exception as error:
        canvas.itemconfigure(algorithmExceptionLabel, text=error)

# UCS Button    
ucsButton = Button(canvas, text="UCS", font=("Times New Roman", 15, 'bold'), command=findUCSPath, height=1, width=8, bg="#EE1AEF")
ucsWindow = canvas.create_window(70, 450, anchor="nw", window=ucsButton)

# Start the A* Algorithm
def findAStarPath():
    global parser, canvas, algorithmExceptionLabel
    try:
        validateInput()
        aStar = AStar(parser.getNodeName(), parser.getMap(), parser.getHeuristicMap())
        aStar.findPath(int(startChosen.get())-1, int(goalChosen.get())-1)
        if (aStar.getFound()):
            updateResult(aStar.getResultPath() ,aStar.getPathName(), aStar.getDistance(), 1)
        else:
           canvas.itemconfigure(algorithmExceptionLabel, text="The path does not exist") 
    except Exception as error:
        canvas.itemconfigure(algorithmExceptionLabel, text=error)

# A* Button
aStarButton = Button(canvas, text="A*", font=("Times New Roman", 15, 'bold'), command=findAStarPath, height=1, width=8, bg="#EE1AEF")
aStarWindow = canvas.create_window(205, 450, anchor="nw", window=aStarButton)

"""========================================= SHOWING RESULT SEGMENT ========================================="""
# Graph Image
graphImage = PhotoImage(file="../assets/logo.png")
graphWindow = canvas.create_image(500, 125, anchor="nw", image=graphImage)

# Algorithm Used Label
algorithmUsedLabel = canvas.create_text(500, 510, text = "", font=("Georgia", 12), fill="#FFFFFF", anchor="w")

# Result Path Label
resultPathLabel = canvas.create_text(500, 540, text = "", font=("Georgia", 12), fill="#FFFFFF", anchor="w")

# Distance Label
distanceLabel = canvas.create_text(500, 570, text = "", font=("Georgia", 12), fill="#FFFFFF", anchor="w")

# Update result according to parameter
def updateResult(resultPath, pathName, distance, flag):
    global drawer, canvas, graphImage, graphWindow, resultPathLabel, distanceLabel
    if (resultPath != []):
        drawer.drawGraphResult(resultPath)
        if (flag == 0):
            canvas.itemconfigure(algorithmUsedLabel, text="Using UCS Algorithm")
        else:
            canvas.itemconfigure(algorithmUsedLabel, text="Using A* Algorithm")
        canvas.itemconfigure(resultPathLabel, text=f"Result Path: {pathName}")
        canvas.itemconfigure(distanceLabel, text=f"Distance      : {distance}")
    else:
        drawer.drawGraph()
        canvas.itemconfigure(algorithmUsedLabel, text="")
        canvas.itemconfigure(resultPathLabel, text="")
        canvas.itemconfigure(distanceLabel, text="")
    # graphImage = PhotoImage(file="../assets/graph.png")
    # Open the image file
    image = Image.open("../assets/graph.png")

    # Calculate the new size
    new_width = int(image.width * 0.75)
    new_height = int(image.height * 0.75)

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)
    graphImage = ImageTk.PhotoImage(resized_image)
    canvas.itemconfigure(graphWindow, image=graphImage)


root.mainloop()