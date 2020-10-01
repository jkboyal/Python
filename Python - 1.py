#!/usr/bin/env python
# coding: utf-8

# # Python - 1

# Create a variable to store your favorite number between 1 and 10. Print this variable. 

# In[118]:


x = 5 
print ("My favorite number is:", x)


# Square this number and store it back into the same variable. Print the new value of the variable.

# In[119]:


x = 5 ** 2
print ("Square of my favorite number is:", x)


# Create a new variable and store the string "The square of my favorite number is: " into this variable. Print the variable. 

# In[120]:


y = "The square of my favorite number is: "
print (y)


# Print the above string and the value of the square of your favorite number in one line. For example: "The square of my favorite number between 1 and 10 is X", replacing X with the value.

# In[16]:


z = "The square of my favorite number between 1 and 10 is 25"
print(z)


# Create four new variables and store four different numbers between 1 and 10. Print the four variables.

# In[18]:


a, b, c, d = 1, 2, 3, 4
print (a)
print (b)
print (c)
print (d)


# Calculate the squares for each of the above four numbers and store them in four new variables. Add all the squares, including your favorite number, and store the sum in a new variable. Print the sum. 

# In[121]:


a, b, c, d = 1, 2, 3, 4
e, f, g, h = a**2, b **2, c**2, d**2
square_sum = e + f + g + h + x        #x = 25 (Square of favorite number)
print("Squares of 5 variables are:", square_sum)


# Calculate the average of the square of the five numbers you have selected. Print the average.

# In[122]:


average = (square_sum)/5
print("Average of squares of 5 numbers:", average)


# Calculate the average of all EVEN numbers between 0 and 100. Print the average value and the count of the even numbers between 0 and 100. 

# In[67]:


l = 0 #To store sum of even numbers
count = 0 #To store count of even numbers
#Including both 0 and 100 
for i in range (0, 101):
    if (i % 2 == 0):
        count = count + 1
        l = l + i

print("Sum of even numbers between 0 and 100:", l)
print("Count of even numbers between 0 and 100:", count)
print("Average of even numbers between 0 and 100:", l//count )


# Research the statistics python library. Import the statistics library. Provide 2-3 simple examples of the use of the functions in this library. 

# In[89]:


#Statistics python library is used to perform statistical functions in our data
#These include calculating means of central location, spread of data and averages

import statistics as stat

#Data in consideration:
a1, a2, a3, a4, a5 = 10, 20, 30, 40, 50

#1. Calculating mean of data 
m1 = stat.mean([a1, a2, a3, a4, a5])
print("Mean of the data is:", m1)

#2. Calculating median of data
m2 = stat.median([a1, a2, a3, a4, a5])
print("Median of the data is:", m2)

#3. Calculating standard deviation of data
sd = stat.stdev([a1, a2, a3, a4, a5])
print("Standard Deviation of the data is:", sd)

#4. Calculating variance of data
v = stat.variance([a1, a2, a3, a4, a5], m1)
print("Variance of the data is:", v)


# In the code you wrote above to calculate the average of all EVEN numbers between 0 and 100, replace the relevant lines with the correct function from the statistics library and calculate the average. You should see the same answer for the average as before. 

# In[116]:


#considering both 0 and 100 
evenlist = []
for i in range(0, 101):
    if (i % 2 == 0):
        evenlist.append(i)
print(evenlist)        
              
m3 = stat.mean(evenlist)
print("\n")
print("Mean of even numbers between 0 and 100:" , m3)


# You have been put in charge of writing a function that prints the details of a pizza order. The function will take four inputs - name of the customer, type of crust (e.g. thin etc.), the size of the pizza (e.g. small etc.), and one favorite topping. Write this function assuming that the inputs will be provided in the same order as described above. In the print statement, please be clear on the input being printed (as we discussed in class). 

# In[161]:


def pizza_menu(customer_name, crust_type, size, topping):
    return{"customer_name" :customer_name, "crust_type" :crust_type, "size" :size, "topping" :topping}

print("Pizza order:")
print(pizza_menu(" ", " ", " ", " "))


# Call this function with some sample inputs and print the details of the pizza order 

# In[162]:


print("Pizza order:")
print(pizza_menu("Nancy", "Thin Crust", "Medium", "Chicken"))


# Modify your function to support the inputs being provided in random order. Demonstrate this by calling the function. 

# In[160]:


print("Pizza order: ")
print(pizza_menu(customer_name="Sky", size="Large", topping="Loaded" ,crust_type="Cheese-burst"))


# Assume that pineapple is everyone's favorite topping! Modify your function to not require this input to be provided each time. Demonstrate this by calling the function. 

# In[164]:


def pizza_menu_new(name_customer, type_crust, size_pizza, topping_pizza = "Pineapple"):
    print("name_customer: ", name_customer)
    print("type_crust: ", type_crust)
    print("size_pizza: ", size_pizza)
    print("topping_pizza: ", topping_pizza)
 
print("Pizza order: ")
pizza_menu_new(name_customer="Jen", type_crust="Thin", size_pizza="Medium")

