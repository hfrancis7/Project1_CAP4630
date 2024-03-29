"""
This module contains the class State
and its subsequent functions, including
an initializer, getter&setter methods,
a __str__ method and a __gt__ method.

The __str__ method prints the state's
information to be formatted properly when
printing reports in the main project.

__gt__ is used to compare the states based
on their names.

Author: Hailey Francis
Version: 2/3/22
Email: n01402670@unf.edu
"""
class State:
    """""
    This class takes the information from a line (presumably given by States.csv)
    and turns them into State objects. This contains all of the information, 
    and there are getters and setters for every data attribute (although not all
    of them are used in printing the report.)
    """""
    # INITIALIZER #
    def __init__(state, name, capitol, reigon, houseSeats, population, covidCases, covidDeaths, fullVax, medHouseIncome, violentCrimeRate):
        state.name = name
        state.capitol = capitol
        state.reigon = reigon
        state.houseSeats = houseSeats
        state.population = population
        state.covidCases = covidCases
        state.covidDeaths = covidDeaths
        state.fullVax = fullVax
        state.medHouseIncome = medHouseIncome
        state.violentCrimeRate = violentCrimeRate.replace('\n','')
    
    # GETTER METHODS #
    def getName(state):
        return state.name
    
    def getCapitol(state):
        return state.capitol
    
    def getReigon(state):
        return state.reigon

    def getHouseSeats(state):
        return state.houseSeats

    def getPopulation(state):
        return state.population
    
    def getCovidCases(state):
        return state.covidCases

    def getCovidDeaths(state):
        return state.covidDeaths

    def getFullVax(state):
        return state.fullVax

    def getMedHouseIncome(state):
        return state.medHouseIncome

    def getViolentCrimeRate(state):
        return float(state.violentCrimeRate)

    def getMortalityRate(state): #case fatality rate
        return float(state.covidDeaths) / float(state.covidCases)

    def getCaseRate(state):
        return float(state.covidCases) / float(state.population) * 100000
    
    def getDeathRate(state):
        return float(state.covidDeaths) / float(state.population) * 100000

    def getFullVaxRate(state):
        return float(state.fullVax) / 100
    # END OF GETTER METHODS #

    # SETTER METHODS #
    def setName(state, newName):
        state.name = newName

    def setCapitol(state, newCapitol):
        state.capitol = newCapitol

    def setReigon(state, newReigon):
        state.reigon = newReigon

    def setHouseSeats(state, newHouseSeats):
        state.houseSeats = newHouseSeats

    def setPopulation(state, newPopulation):
        state.population = newPopulation

    def setCovidCases(state, newCovidCases):
        state.covidCases = newCovidCases

    def setCovidDeaths(state, newCovidDeaths):
        state.covidDeaths = newCovidDeaths

    def setFullVax(state, newFullVax):
        state.fullVax = newFullVax

    def setMedHouseIncome(state, newMedHouseIncome):
        state.medHouseIncome = newMedHouseIncome

    def setViolentCrimeRate(state, newviolentCrimeRate):
        state.violentCrimeRate = newviolentCrimeRate
    # END OF SETTER METHODS #

    #__gt__ and __str__
    def __str__(state):
        return f"{state.getName() : <20}{state.getMedHouseIncome() : <20}{state.getViolentCrimeRate() : <20}{format(state.getMortalityRate(), '.6f') : <20}{format(state.getCaseRate(), '.2f') : <20}{format(state.getDeathRate(), '.2f') : <20}{format(state.getFullVaxRate(), '.3f') : <20}"

    def __gt__(state, other):
        return state.name > other.name