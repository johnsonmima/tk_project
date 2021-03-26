########################################################
# Author:     Johnson Olusegun
# Course:     Advance CS topics (CSC 121, Spring 2021)
# Assignment: Italy & Covid reporting Assigment in 2020
# Python version: Python 3.8
########################################################

# Develop a user interface that shows region, population, case numbers and percentage
from tkinter import *
from core import *
from tkinter import *

from tkinter import ttk
from ttkthemes import themed_tk as tk

root = tk.ThemedTk()
root.get_themes()  # Returns a list of all themes that can be set
root.set_theme("radiance")  # Sets an available theme
# instance
core = Core()

# variables
selectedRegion = StringVar(root)
selectedEuropeanCountry = StringVar(root)

# stats variables
region = StringVar(root)
population = StringVar(root)
region_population = StringVar(root)
case_number = StringVar(root)
percentage = StringVar(root)
# italy placeholder
regionPlaceholder = StringVar(root)
italyTotalPopulationPlaceholder = StringVar(root)
regionTotalPopulationPlaceholder = StringVar(root)
regionCasePlaceholder = StringVar(root)
percentagePlaceholder = StringVar(root)

# country placeholder
countryPlaceholder = StringVar(root)
countryTotalPopulationPlaceholder = StringVar(root)
casePlaceholder = StringVar(root)
ratePlaceholder = StringVar(root)

# italy variable
primaryCountry = StringVar(root)
italyPopulation = StringVar(root)
italyCase = StringVar(root)
italyRate = StringVar(root)
# european countries variable
euroCountry = StringVar(root)
euroPopulation = StringVar(root)
euroCase = StringVar(root)
euroRate = StringVar(root)

# get regions
regions = core.get_region()
europeanCountry = core.get_european_countries()

# first Frame
firstFrame = Frame(root)
secondFrame = Frame(root)
thirdFrame = Frame(root)
fourthFrame = Frame(root)
fifthFrame = Frame(root)
sixthFrame = Frame(root)
sixthRightFrame = Frame(sixthFrame)
sixthLeftFrame = Frame(sixthFrame)


############################################
# message one
# label for notice
def displayNotice(frm, msg, color, fg):
    tpMsg = Label(frm, text=msg,
                  bg=color, fg=fg)
    tpMsg.pack(pady=10)


###############################################################
# select widget
def selection_widget():
    # set default region
    selectedRegion.set(regions[0])
    # create select region label
    reLabel = Label(secondFrame, text='Select region')
    # create select region option menu
    reOption = ttk.OptionMenu(secondFrame, selectedRegion, *regions)
    # create check button
    reBtn = ttk.Button(secondFrame, text="Check report", command=check_selected_region)
    # pack widgets to the left
    reLabel.pack(side=LEFT, padx=5)
    reOption.pack(side=LEFT, padx=5)
    reBtn.pack(side=LEFT, padx=5)
    # set default region


#################################################
# check selected region
def check_selected_region():
    # get country statistic called passing the name as argument
    stats = core.getRegionStats(selectedRegion.get())

    # set placeholder
    regionPlaceholder.set("Region")
    italyTotalPopulationPlaceholder.set("Italy total population")
    regionTotalPopulationPlaceholder.set("Region population")
    regionCasePlaceholder.set("Total Covid Case")
    percentagePlaceholder.set("Percentage")
    # set variables
    region.set(stats['region'])
    population.set(stats['population'])
    region_population.set(stats['region_population'])
    case_number.set(stats['case_number'])
    percentage.set(stats['percentage'])

    #####################################################
    # show statistics


def showStatistics():
    # region label
    LabelTextPlaceHolder(thirdFrame, regionPlaceholder)
    Label(thirdFrame, textvariable=region, font=("Calibri", 14)).pack()
    # population
    LabelTextPlaceHolder(thirdFrame, italyTotalPopulationPlaceholder)
    Label(thirdFrame, textvariable=population, font=("Calibri", 14)).pack()
    # # region population
    LabelTextPlaceHolder(thirdFrame, regionTotalPopulationPlaceholder)
    Label(thirdFrame, textvariable=region_population, font=("Calibri", 14)).pack()
    # # case number
    # # region population
    LabelTextPlaceHolder(thirdFrame, regionCasePlaceholder)
    Label(thirdFrame, textvariable=case_number, font=("Calibri", 14)).pack()
    # percentage
    LabelTextPlaceHolder(thirdFrame, percentagePlaceholder)
    Label(thirdFrame, textvariable=percentage, font=("Calibri", 14)).pack()


# european dropdown
def european_widget():
    # set european
    selectedEuropeanCountry.set(europeanCountry[0])
    # create select region label
    euLabel = Label(fifthFrame, text='Comparison between Italy and', font=("Verdana", 15))
    # create select region option menu
    euOption = ttk.OptionMenu(fifthFrame, selectedEuropeanCountry, *europeanCountry)
    # create check button
    euBtn = ttk.Button(fifthFrame, text="compare infection rates", command=compare_selected_country)
    # pack widgets to the left
    euLabel.pack(side=LEFT, padx=5)
    euOption.pack(side=LEFT, padx=5)
    euBtn.pack(side=LEFT, padx=5)


##################################
# compare selected country pressed
def compare_selected_country():
    # get italy infection rate
    # get italy stats
    italy_stats = core.getItalyStats("Italy")
    european_stats = core.getEuropeanCountryStats(selectedEuropeanCountry.get())

    # set place holder
    countryPlaceholder.set("Country")
    countryTotalPopulationPlaceholder.set("Total Population")
    casePlaceholder.set("Total Case")
    ratePlaceholder.set("Infection Rate")

    # set italy values
    primaryCountry.set(italy_stats['country'])
    italyPopulation.set(italy_stats['population'])
    italyCase.set(italy_stats['case'])
    italyRate.set(italy_stats['rate'])
    # set european
    euroCountry.set(european_stats['country'])
    euroPopulation.set(european_stats['population'])
    euroCase.set(european_stats['case'])
    euroRate.set(european_stats['rate'])


# text place holeder
# showComparisonStatistics place holder
def LabelTextPlaceHolder(frame, placeholder):
    Label(frame, textvariable=placeholder, font=("Verdana", 20, "bold")).pack(padx=10)


##################################
# show comparison widget
def showComparisonStatistics():
    # country stats
    LabelTextPlaceHolder(sixthLeftFrame, countryPlaceholder)
    Label(sixthLeftFrame, textvariable=primaryCountry, font=("Verdana", 14)).pack(padx=10)
    # population stats
    LabelTextPlaceHolder(sixthLeftFrame, countryTotalPopulationPlaceholder)
    Label(sixthLeftFrame, textvariable=italyPopulation, font=("Verdana", 14)).pack(padx=10)
    # case
    LabelTextPlaceHolder(sixthLeftFrame, casePlaceholder)
    Label(sixthLeftFrame, textvariable=italyCase, font=("Verdana", 14)).pack(padx=10)
    # rate
    LabelTextPlaceHolder(sixthLeftFrame, ratePlaceholder)
    Label(sixthLeftFrame, textvariable=italyRate, font=("Verdana", 14)).pack(padx=10)

    ##########################################################################################
    # european country
    LabelTextPlaceHolder(sixthRightFrame, countryPlaceholder)
    Label(sixthRightFrame, textvariable=euroCountry, font=("Verdana", 14)).pack(padx=10)

    # population stats
    LabelTextPlaceHolder(sixthRightFrame, countryTotalPopulationPlaceholder)
    Label(sixthRightFrame, textvariable=euroPopulation, font=("Verdana", 14)).pack(padx=10)
    # case
    LabelTextPlaceHolder(sixthRightFrame, casePlaceholder)
    Label(sixthRightFrame, textvariable=euroCase, font=("Verdana", 14)).pack(padx=10)
    # rate
    LabelTextPlaceHolder(sixthRightFrame, ratePlaceholder)
    Label(sixthRightFrame, textvariable=euroRate, font=("Verdana", 14)).pack(padx=10)


# execute all
# top notice
displayNotice(firstFrame, "NOTE: Wikipedia was used to get Italy Total population and Region population", 'yellow',
              'black')
selection_widget()
showStatistics()
# second notice
displayNotice(fourthFrame, "Italy Covid report against European countries", 'blue', 'white')
european_widget()
# showComparisonStatistics
showComparisonStatistics()

# packing main frames
firstFrame.pack(pady=5)
secondFrame.pack(pady=5)
thirdFrame.pack(pady=5)
fourthFrame.pack(pady=5)
fifthFrame.pack(pady=5)

# sixth frame
sixthLeftFrame.pack(side=LEFT, pady=10)
sixthRightFrame.pack(side=RIGHT, pady=10)
sixthFrame.pack(pady=5)


# on closing
def on_closing():
    root.destroy()


# set title
root.title("Italy & Covid reporting")
# screen size
root.minsize(800, 600)
# on closing
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
