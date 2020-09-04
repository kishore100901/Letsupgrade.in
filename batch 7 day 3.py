#!/usr/bin/env python
# coding: utf-8

# # DAY - 3 BATCH-7

# # OPERATORS

# In[1]:


a = 737


# In[2]:


b = 473


# In[3]:


a + b


# In[5]:



a * b 


# In[6]:


a - b


# In[7]:


a / b 


# In[8]:


a // b


# In[9]:


a % b


# In[10]:


a ** b


# In[11]:


22 / 7


# In[12]:


a = b


# In[13]:


a 


# In[14]:


b


# In[15]:


a == b


# In[16]:


a = 12


# In[17]:


b = 234


# In[18]:


a == b


# In[19]:


a != b


# In[20]:


a > b


# In[21]:


a < b


# In[22]:


a & b


# In[23]:


a | b


# In[24]:


a >= b


# In[25]:


a <= b


# # LOGICAL COMPARISION STATEMENTS

# #When you have two differnt conditions, and want to check them for your logical collabrative conditions we use Logical Comp. Ops
# 
# 

# # NOT OR AND

# In[27]:


jee = False


# In[28]:


board_exam = True


# In[29]:


eligibleFor = jee and board_exam


# In[30]:


eligibleFor


# In[31]:


eligibleFor = jee or board_exam


# In[32]:


eligibleFor


# In[34]:


not jee


# #or

# In[36]:


science = True 


# In[37]:


commerce = False


# In[38]:


arts = True


# In[39]:


c = science or commerce or arts


# In[40]:


c


# In[41]:


science and commerce and arts


# In[42]:


not science


# In[43]:


not commerce


# In[44]:


not arts


# In[45]:


not science or not commerce or not arts


# In[46]:


science or commerce and arts


# In[47]:


science and commerce or arts


# # Chained Comprassion Ops
# 

# In[48]:


science = 79


# In[49]:


commerce = 89


# In[50]:


arts = 32


# In[52]:


science > 75 and commerce > 85 and arts > 30


# In[53]:


science > commerce


# In[59]:


type(science)


# # DECISION MAKING STATEMENT

# In[ ]:


# if elif else........


# In[ ]:


maths = 90


# In[56]:


science = 89


# In[58]:


social = 93


# if maths > 90:

# In[61]:



maths = 95

science = 80



if maths > 90:
    print("Go to science")
    print("You may choose enginnering streem")
elif science >85:
    print("Go to commerce")
    print("u can become bank manager and finicier")
else:
    print("Go to arts")
    print("U can become best person")


# In[63]:


maths = int(input("Enter the marks u scored in maths :"))
science = int(input("Enter the marks u scored in science :"))

print(" ")
print("\nThanks For giving your details\n")

if maths >= 90:
    print("Go to science :")
    print("if u wish to become an engineer in futhure")
elif science >= 90:
    print("Go to science")
    print("IF your dream is to do medicien take pcmb")
elif maths >75:
    print("Go to commerce ")
    print(" u can become best in industry field")
else:
    print("Go to arts")


# # TAKING INPUT FROM KEYBOARD

# In[65]:


a = input("Enter the first name:")
b = input("Enter the last name")
c = input("Enter your address")
d = int(input("Enter the mobile no:"))
e = float(input("Enter the sgpa u scored in enginnering :"))
print("NAME :", a + b, sep="_")
print("ADDRESS:", c)
print("Mobile number:", d)
print("SGPA:", e)


# In[66]:


#checking odd no


# In[67]:


num = int(input("Enter the number   :"))

if num % 2 == 0:
    print("IT is even number:")
else:
    print("IT is odd number: ")


# In[74]:


num = int(input("Enter the number   :"))

if num % 3 == 0:
    print("IT is even number:")
else:
    print("IT is odd  number: ")


# # LOOPS

# # loops are used for performing the set of statements repeat untill the condition is not satisfied
# 

# # for iteraing over the different elements of the Objects like List ,Dict, Tuple, Set and more
# # Two types of LOOPS - { FOR and While }
# 

# In[75]:


lst = [12,34,4,5,5,6,"kishore",2.34,42]


# In[76]:


lst


# In[77]:


for i in lst:
    print(i)


# In[78]:


type(lst)


# In[79]:


lst = [1,2,3,4,5,6,7,8,9,0]


# In[80]:


lst


# In[82]:


for i in lst:
    if i %  2 == 0:
        print(i,"is even")
    else:
        print(i, "is odd")


# In[83]:


lst.pop(9)


# In[84]:


lst


# In[85]:


lst[0]


# In[86]:


lst


# In[89]:


for i in lst:
    num = 9
    print(num, "X",i,"=",num * i)
else:
    print("  ")
    print("HEY i  am done with multipel app....")


# In[92]:


for i in range(1,11):
    print(i)
else:
    print("THe loop is finised")


# In[94]:


for i in range(3,8):
    print(i)
else:
    print("The loop is done")


# In[104]:


for  i in range(1,21):
    print("9", "X",i,"=", 9*i)


# # ASSIGNMENT -1 - DAY -  2

# In[107]:


# 1 
altitude = int(input("Enter the the altitude of the plane :"))

if altitude <= 1000:
    print("Land the plane safely")
if altitude >1000 <=5000:
    print("Come down to 1000ft")
if altitude > 5000:
    print("Go around and try later to land ")


# In[108]:


altitude = int(input("Enter the the altitude of the plane :"))

if altitude <= 1000:
    print("Land the plane safely")
if altitude >1000 <=5000:
    print("Come down to 1000ft")
if altitude > 5000:
    print("Go around and try later to land ")


# In[111]:


altitude = int(input("Enter the the altitude of the plane :"))

if altitude <= 1000:
    print("Land the plane safely")
if altitude > 1000 < 5000:
    print("Come down to 1000ft")
if altitude > 5000:
    print("Go around and try later to land ")


# In[ ]:




