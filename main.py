########################################################
# Author:     Johnson Olusegun
# Course:     Advance CS topics (CSC 121, Spring 2021)
# Assignment: Italy & Covid reporting Assigment in 2020
# Python version: Python 3.8
########################################################

# Develop a user interface that shows region, population, case numbers and percentage
# import tkinter
from tkinter import *
from tkinter import messagebox
import pandas as pd


class App(Frame):

    # constructor
    def __init__(self, master=None):
        super().__init__(master)
        # initial layout setup
        self.master = master
        self.pack()

        # variables
        self.notificationVar = StringVar(self.master)
        self.selectedRegion = StringVar(self.master)

        # read all the csv file
        fileList = self.read_files()
        # get regions
        self.regions = self.get_region(fileList)

        self.selection_widget()

    # this function reads all the files
    def read_files(self):
        # read the growth rate csv
        try:
            # read growth rate
            growth_rate = pd.read_csv('./Italy_Covid_2020/growth_rate.csv')
            # read case by infection
            case_by_infection = pd.read_csv('./Italy_Covid_2020/cases_by_infection.csv')
        except FileNotFoundError as e:
            # set notification error
            self.notificationVar.set(f"error reading {e.filename}")
            # display notification label
            self.notification_label("red")
            return []
        else:
            self.notificationVar.set(" ")
            # display notification label
            self.notification_label("white")
            return [growth_rate, case_by_infection]

    # get region function
    # this function gets and return all the regions
    def get_region(self, data):
        if len(data) > 0:
            return data[0]['region'].unique()
        return ["None"]

    ################################################################
    # notification widget
    def notification_label(self, color):
        msg_label = Label(self, text=self.notificationVar.get(), bg=color)
        msg_label.pack()

    ################################################################
    # select widget
    def selection_widget(self):
        # set default region
        self.selectedRegion.set(self.regions[0])
        # create select region label
        select_lbl = Label(self, text='Select region')
        # create select region option menu
        dropMenu = OptionMenu(self, self.selectedRegion, *self.regions)
        # create check button
        select_btn = Button(self, text=f"Check report", fg="green", command=self.check_selected_region)
        # pack widgets to the left
        select_lbl.pack(side="left")
        dropMenu.pack(side="left")
        select_btn.pack(side="left")

    # check selected region
    def check_selected_region(self):
        print(self.selectedRegion.get())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Tk()

    # app
    myapp = App(master=root)
    # set the title
    myapp.master.title("Italy & Covid reporting")
    # set the default frame
    myapp.master.minsize(800, 400)
    # main loop
    myapp.mainloop()
