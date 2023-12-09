#!/usr/bin/env python
# coding: utf-8

# In[50]:


'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay=50000, tax_rate=0.15, expenses=20000):
    '''Savings.
    2 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    savings = (gross_pay-round(gross_pay*tax_rate))-expenses
    savings *=100
    print("Take Home Pay: " + str(savings) + " Centavos")
    return int(savings)
result = savings()


# In[46]:


savings()


# In[53]:


def material_waste(total_material=1000, material_units="L", num_jobs=10, job_consumption=10):
    '''Material Waste.
    2 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    material_waste= total_material - (num_jobs*job_consumption)
    print("Wasted Amount of Materials:" + str(material_waste) + material_units)
    return str(material_waste) + material_units
result=material_waste()


# In[54]:


material_waste()


# In[57]:


def interest(principal=5000000, rate=5, periods=10):
    '''Interest.
    3 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    principal/=100
    rate/=100
    interest=principal +(principal*rate*periods)
    print ("Final Investment Value:" + "PHP" + str(interest))
    return int(interest)
result=interest()


# In[58]:


interest()


# In[63]:


def body_mass_index(weight=123, height=[5,8]):
    '''Body Mass Index.
    3 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    height_feet =int(height [0])
    height_inches =(height [1])
    height_meters =(height_feet*12*0.0254 + height_inches*0.0254)
    weight*=0.453592
    body_mass_index= weight/(height_meters**2)
    print("Weight:" +str(weight) + "kg" + "\nHeight:" + str(height_meters) + "m" + "\nBody Mass Index:" + str(body_mass_index))
    return float(body_mass_index)
result=body_mass_index()


# In[64]:


body_mass_index()


# In[ ]:




