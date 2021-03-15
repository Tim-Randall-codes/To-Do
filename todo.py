from tkinter import Tk, Entry, Text, Label, Checkbutton, Button, BooleanVar, E, Toplevel
import csv
from datetime import date

win = Tk()

win.title("^_^     To Do!     ^_^")
win.geometry("400x400")
win.configure(bg="light blue")

# create list of variables: date, tasks, task complete or not
# make it so the list can be writen to a csv row
# make it so the user can read the csv and pull up the row from a date
# have this happen in a new window. 


Onecom = BooleanVar()
Twocom = BooleanVar()
Threecom = BooleanVar()
Fourcom = BooleanVar()
Fivecom = BooleanVar()
Sixcom = BooleanVar()
Sevencom = BooleanVar()
Eightcom = BooleanVar()
Ninecom = BooleanVar()
Tencom = BooleanVar()

def candl():
    now = date.today()
    t1 = task1e.get()
    t2 = task2e.get()
    t3 = task3e.get()
    t4 = task4e.get()
    t5 = task5e.get()
    t6 = task6e.get()
    t7 = task7e.get()
    t8 = task8e.get()
    t9 = task9e.get()
    t10 = task10e.get()
    onecom = Onecom.get()
    c1='error'
    if onecom == True:
        c1 = ':Completed'
    else:
        c1 = ':Incomplete'
    twocom = Twocom.get()
    if twocom == True:
        c2 = ':Completed'
    else:
        c2 = ':Incomplete'
    threecom = Threecom.get()
    if threecom == True:
        c3 = ':Completed'
    else:
        c3 = ':Incomplete'
    fourcom = Fourcom.get()
    if fourcom == True:
        c4 = ':Completed'
    else:
        c4 = ':Incomplete'
    fivecom = Fivecom.get()
    if fivecom == True:
        c5 = ':Completed'
    else:
        c5 = ':Incomplete'
    sixcom = Sixcom.get()
    if sixcom == True:
        c6 = ':Completed'
    else:
        c6 = ':Incomplete'
    sevencom = Sevencom.get()
    if sevencom == True:
        c7 = ':Completed'
    else:
        c7 = ':Incomplete'
    eightcom = Eightcom.get()
    if eightcom == True:
        c8 = ':Completed'
    else:
        c8 = ':Incomplete'
    ninecom = Ninecom.get()
    if ninecom == True:
        c9 = ': Completed, '
    else:
        c9 = ': Incomplete, '
    tencom = Tencom.get()
    if tencom == True:
        c10 = ': Completed.'
    else:
        c10 = ': Incomplete.'
    lst = [str(now), t1, c1, t2, c2, t3, c3, t4, c4, t5, c5, t6, c6, t7, c7,
           t8, c8, t9, c9, t10, c10]
    with open('/Users/timrandall/Projects/ToDo/storage.csv', mode='a') as file1:
        write1 = csv.writer(file1, delimiter=',')
        write1.writerow(lst)

def search_date():
    pass

def to_archive():
    newwin = Toplevel(win)
    newwin.title("^^  Archive  ^^")
    newwin.geometry("300x300")
    display0 = Text(newwin, height=10, width=30)
    display0.grid(column=0, row=0)
    archex = Label(newwin, text="Type date into box in yyyy-mm-dd format")
    archex.grid(column=0, row=1)
    archex2 = Label(newwin, text="Then press search to see tasks for that day")
    archex2.grid(column=0, row=2)
    datee = Entry(newwin)
    datee.grid(column=0, row=3)
    searchbb = Button(newwin, text="Search", command=search_date)
    searchbb.grid(column=0, row=4)

explain = Label(win, bg="light blue", text="Type in a task and tick the box when you finish it")
explain.grid(column=1, row=0)

task1e = Entry(win, bg="light yellow")
task1e.grid(column=1, row=1)

task2e = Entry(win, bg="light yellow")
task2e.grid(column=1, row=2)

task3e = Entry(win, bg="light yellow")
task3e.grid(column=1, row=3)

task4e = Entry(win, bg="light yellow")
task4e.grid(column=1, row=4)

task5e = Entry(win, bg="light yellow")
task5e.grid(column=1, row=5)

task6e = Entry(win, bg="light yellow")
task6e.grid(column=1, row=6)

task7e = Entry(win, bg="light yellow")
task7e.grid(column=1, row=7)

task8e = Entry(win, bg="light yellow")
task8e.grid(column=1, row=8)

task9e = Entry(win, bg="light yellow")
task9e.grid(column=1, row=9)

task10e = Entry(win, bg="light yellow")
task10e.grid(column=1, row=10)

task1c = Checkbutton(win, variable=Onecom, onvalue=True, offvalue=False)
task1c.grid(column=0, row=1)

task2c = Checkbutton(win, variable=Twocom, onvalue=True, offvalue=False)
task2c.grid(column=0, row=2, sticky=E)

task3c = Checkbutton(win, variable=Threecom, onvalue=True, offvalue=False)
task3c.grid(column=0, row=3)

task4c = Checkbutton(win, variable=Fourcom, onvalue=True, offvalue=False)
task4c.grid(column=0, row=4)

task5c = Checkbutton(win, variable=Fivecom, onvalue=True, offvalue=False)
task5c.grid(column=0, row=5)

task6c = Checkbutton(win, variable=Sixcom, onvalue=True, offvalue=False)
task6c.grid(column=0, row=6)

task7c = Checkbutton(win, variable=Sevencom, onvalue=True, offvalue=False)
task7c.grid(column=0, row=7)

task8c = Checkbutton(win, variable=Eightcom, onvalue=True, offvalue=False)
task8c.grid(column=0, row=8)

task9c = Checkbutton(win, variable=Ninecom, onvalue=True, offvalue=False)
task9c.grid(column=0, row=9)

task10c = Checkbutton(win, variable=Tencom, onvalue=True, offvalue=False)
task10c.grid(column=0, row=10)

clearl = Label(win, text="Click to clear your entries and save them to archive", bg="light blue")
clearl.grid(column=1, row=12)

clearb = Button(win, text="Clear and Archive", command=candl)
clearb.grid(column=1, row=11)

archb = Button(win, text="To Archive", command=to_archive)
archb.grid(column=1, row=13)

archl = Label(win, text="Click to access the archive", bg="light blue")
archl.grid(column=1, row=14)

win.mainloop()
