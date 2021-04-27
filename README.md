# day-27-tk-inter-mile-km-converter
## Challenge: Build a mile to kilomemter caclulator using [tkinter library]('https://docs.python.org/3/library/tkinter.html')
1. Define `button_clicked` function
```
def button_clicked():
    km = round(float(miles_input.get()) * 1.609344)
    km_output.delete(0, END)
    km_output.insert(0, km)
```

2. Set up the screen
```
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=220, height=100)

...

window.mainloop()
```
3. Show texts in the GUI
```
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()
```
4. Create a "calculate" button
```
button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)
```
