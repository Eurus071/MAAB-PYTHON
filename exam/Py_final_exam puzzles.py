


# ----- Python Final Exam -----

# task 1
# ----------------------------------------------------------------------------------------------------
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.
def digit_sum(k):
    result=0
    while k!=0:
        result+=(k%10)
        k=k//10
    print(result)

k=int(input('Enter the number: '))
digit_sum(k)

# Misollar:
# Kiritish:
# 24 
# Natija:
# 6
# (Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

# Kiritish:
# 502
# Natija:
# 7
# (Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)
# ----------------------------------------------------------------------------------------------------

# task 2
# -----------------------------------------------------------------------------------------------------
#  Define a function `is_prime(n)` which returns `True` if the given n (n > 0) is prime number, otherwise returns `False`.

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
           return False
        else:
           return True



number=int(input('Enter positive number: '))
print(is_prime(number))

    


# ----------------------------------------------------------------------------------------------------
import pandas as pd
# task 3
# ----------------------------------------------------------------------------------------------------
# 1) Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
d = {
    'Name': ['Benjamin Sisko', 'Jadzia Dax', 'Kira Nerys'],
    'Species': ['Human', 'Trill', 'Bajoran'],
    'Age': [40, 300, 29]
    }
df_Roaster=pd.DataFrame(data=d)

# 2)  Populate your new table with the following values:

# | Name            | Species      | Age |
# |-----------------|--------------|-----|
# | Benjamin Sisko  | Human        |  40 |
# | Jadzia Dax      | Trill        | 300 |
# | Kira Nerys      | Bajoran      |  29 |
df_Roaster

# 3)  Display the Name and Age of everyone in the table classified as Bajoran.
df_bajoran=df_Roaster[df_Roaster['Species']=='Bajoran']

# task 4
# -----------------------------------------------------------------------------------------------------
import _json
# Update employees.json file by adding new worker's info. (Use Input command to get info)
df_employees=pd.read_json(r'D:\MAAB\PYTHON\hmw\MAAB-PYTHON\exam\employees.json')
df_employees.to_json



# task 5
# -----------------------------------------------------------------------------------------------------
# You have a dataset (customer_orders.csv) containing information about customer orders. The dataset has the following columns:
df_customer_order=pd.read_csv(r'D:\MAAB\PYTHON\hmw\MAAB-PYTHON\exam\customer_orders.csv')
df_customer_order
# OrderID: Unique identifier for each order.
# CustomerID: Unique identifier for each customer.
# Product: Name of the product ordered.
# Quantity: Number of units ordered.
# Price: Price per unit.
# Tasks:

# 1)Group the data by CustomerID and filter out customers who have made less than 20 orders.
#df1=df_customer_order.groupby(by='CustomerID')[df_customer_order[df_customer_order['Quantity'].sum()<20]]
df1=df_customer_order.groupby(by='CustomerID')[df_customer_order(df_customer_order['Quantity'].sum()<20)]
df1
# 2)Identify customers who have ordered products with an average price per unit greater than $120.   
df2=df_customer_order[(df_customer_order['Price']//df_customer_order['Quantity'])>120]
df2