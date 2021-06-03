# pycoffee

Python based web app for coffee tasting with taste profile visualization and comparison.

## App Layout

![layout](pycoffee-draft-v01.png)

## TODO

- [ ] GUI - Aestas  
- [ ] Pandas database - Talon  
- [ ] Taste wheel - Zorin
- [ ] Discord user autenthication

## Database Structure

- **Entry Info**
  - **Date**
  - **User**
- **Bean Info**
  - **Country** - Kenya, Brazil, Ethiopia, Blend,...
  - **Name** - Kiwami, Diamond, Selva Negra, Valentina,...
  - **Roaster** - Motmot, Father's, Laura Coffee,...
  - **Processing** - natural, washed, honey, carbon,...
  - **Roast Level** - light to dark (1-5)
  - **Type** - Arabica/Robusta ratio
  - **Variety** - Heirloom, Tabi, Bourbon, Caturra,...
  - **Brewing Method** - espresso, V60, Aeropress, moka, frenchpress, phin,...
  - **Brewing Recipe** - inverted aeropress, ristretto, 40:60 dripper,...
- **Tasting**
  - **Rating (Hodnocení)** - bad to excellent (1-10)
  - **Sour (Kyselá)** - low to high (1-10)
  - **Sweet (Sladká)**
  - **Salty (Slaná)**
  - **Bitter (Hořká)**
  - **Note (Poznámka)** - optional text input

## Resources

- Tasting
  - [Proč a jak degustovat kávu?](https://coffeetohome.cz/proc-a-jak-degustovat-kavu)
- GUI
  - [PySimpleGUI Demos](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms)
  - [PySimpleGUI Playlist](https://youtube.com/playlist?list=PLl8dD0doyrvF1nLakJJ7sl8OX2YSHclqn)
  - [Colors](https://www.wikipython.com/tkinter-ttk-tix/summary-information/colors/)
  - [Themes](https://media.geeksforgeeks.org/wp-content/uploads/20200511200254/f19.jpg)
- [Pandas Basics Video](https://youtu.be/vmEHCJofslg)
- [Matplotlib Basics Video](https://www.youtube.com/watch?v=DAQNHzOcO5A)
