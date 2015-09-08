"""
GroceryListHelper.py: Helps user to plan meals to make based on the cost of meals and a budget.
User inputs meals he/she was considering to make and estamated cost for the month, and how much
he/she planned on spending. The script will then return a list of randomly generated meals that
are under the budgeted number.
Author: Clint Cochrane
4/10/2015
"""
from tkinter import *
from tkinter.messagebox import *
import random
class shoppingList(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Shopping List")
        self.grid()

        #scrolling list box to hold the grocery list after it has been made
        self._yScroll = Scrollbar(self, orient = VERTICAL)
        self._yScroll.grid(row = 0, column = 2, sticky = N+S)
        self.theList = Listbox(self, yscrollcommand = self._yScroll.set)
        self.theList.grid(row = 0, column = 1)

        #nested frame for the widgets to be placed in
        self.Nestedframe = Frame(self)
        self.Nestedframe.grid(row = 0, column = 0)
        
        #Entry Fields- meal, cost, budget, number of meals
        mealLabel = Label(self.Nestedframe, text = "Meal")
        mealLabel.grid(row = 0, column = 0,  columnspan = 3)
        self.MealVar = StringVar(value = "Enter meal here")
        self.Meal = Entry(self.Nestedframe, textvariable = self.MealVar, justify = "center", width = 40)
        self.Meal.grid(row = 1, column = 0, columnspan = 3)

        costLabel = Label(self.Nestedframe, text = "Cost")
        costLabel.grid(row = 2 , column = 0)
        self.CostVar = DoubleVar(value = 0.00)
        self.Cost = Entry (self.Nestedframe, textvariable = self.CostVar, width = 7, justify = "center")
        self.Cost.grid(row = 3, column = 0)

        self.BudgetLabel = Label(self.Nestedframe, text = "Budget") #the text here will change when process button is presssed
        self.BudgetLabel.grid(row = 2, column = 2)
        self.BudgetVar = DoubleVar (value = 0.00)
        self.Budget = Entry(self.Nestedframe, textvariable = self.BudgetVar, width = 7, justify = "center")
        self.Budget.grid(row = 3, column = 2)

        numberLabel = Label(self.Nestedframe, text = "Meals Needed")
        numberLabel.grid(row = 4, column = 1)
        self.NumberVar = IntVar()
        self.Number = Entry(self.Nestedframe, textvariable = self.NumberVar, width = 5, justify = "center")
        self.Number.grid(row = 5, column = 1,)

        
        #buttons- one to add the meal and cost to their individual lists, one to read file from list and another when done entering data
        self.addButton = Button(self.Nestedframe, text = "Add", command = self.addTolists)
        self.addButton.grid(row = 6, column = 0)
        self.readButton = Button (self.Nestedframe, text = "Read List From File", command = self.read)
        self.readButton.grid(row = 6, column = 1)
        self.processButton = Button(self.Nestedframe, text = "Give Me My List", command = self.process)
        self.processButton.grid(row = 6, column = 2)

        #the lists to hold meals and costs
        self.mealList = []
        self.costList = []
        
        
    def addTolists(self):
        """First ensures the user did not leave meal or cost blank (with default values)
        takes values from the Mealvar and CostVar and put them into a list."""
    
        if self.MealVar.get() == "Enter meal here":
            showinfo(message = "Please input a meal")
        elif self.CostVar.get() == 0.0:
            showinfo(message = "Please input the cost of the meal")
        else:
            self.mealList.append(self.MealVar.get())
            self.costList.append(self.CostVar.get())
            self.CostVar.set(0.00)
            self.MealVar.set("Enter meal here")
        
    def process(self):
        """sends items whose value is less than the budget"""
        if self.NumberVar.get() > len(self.mealList):
            showinfo(message = "Number of planned meals exceedes number of meals enterned.\
                    The total number of meals entered is " + str(len(self.mealList)))
        else:             
            randomlyChoseList = []
            TotalCost = 0
            while True:
                for count in range(self.NumberVar.get()):
                    index = random.randint(0, len(self.mealList)-1) 
                    randomlyChoseList.append(self.mealList[index])
                    TotalCost += self.costList[index]
                if TotalCost <= self.BudgetVar.get():
                    for meal in range(len(randomlyChoseList)):
                        self.theList.insert(END, randomlyChoseList[meal])
                        self.BudgetLabel["text"] = "Total"
                        self.BudgetVar.set(TotalCost)  
                break
    def read(self):
        """reads a file containing meals and prices (meal = cost).
    reads it as one list, then if it finds it to be a number it will add
    it so self.costList. Else it will add it to the meal list. Added 4/10/15"""
        filename = self.MealVar.get()
        f = open(filename,"r")
        lines = f.read()
        lines = lines.replace("\n", " = ").split(" = ")
        index = 0
        while True:
            try:
                if "." in lines[index] or lines[index].isdigit():
                    self.costList.append(float(lines.pop(index)))
                index += 1
            except IndexError:
                break
        self.mealList.append(lines)

def main():
    shoppingList().mainloop()
main()
