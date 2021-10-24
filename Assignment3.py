#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Poem

print( "Twinkle, twinkle, little star,\n"  +
          "  " +"How i wonder what you are!\n"  +
                   "  " + "  " +"Up above the world so high,\n"  +
                   "  " + "  " +"Like a diamond in the sky. \n"  +
        "Twinkle, twinkle, little star,\n"  +
                   "  " +"How i wonder what you are!")


# In[ ]:





# In[27]:


from platform import python_version
print(python_version())


# In[ ]:





# In[43]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ", now.strftime("%Y-%d-%m" + " and " + "%H:%M"))


# In[ ]:





# In[65]:


r = float(input("Enter the value of a radius :"));
area = 3.14 * (r**2);
print("Area=",area);


# In[ ]:





# In[53]:


firstname = input("Enter your First Name :");
lastname = input("Enter your Last Name :");
print(lastname + firstname);


# In[ ]:





# In[59]:


a = int(input("Enter the first value :"));
b = int(input("Enter the second value :"));
c = a+b;
print("sum of two value is :", c);


# In[ ]:





# In[66]:


math = int(input("Enter your math marks"));
isl = int(input("Enter your islamiat marks"));
comp = int(input("Enter your computer marks"));
eco = int(input("Enter your economics marks"));
eng = int(input("Enter your english marks"));

total = math + isl + comp + eco + eng;
per = (total/500)*100;
if per > 79 and per < 101:
    print("Grade A+", per, "%");
elif per > 69 and per < 80:
    print("Grade A", per, "%");
elif per > 59 and per < 70:
    print("Grade B", per, "%");
elif per > 49 and per < 60:
    print("Grade C", per, "%");
if per > 79 and per < 101:
    print("Fail", per, "%");
else:
    print("incorrect numbers");


# In[ ]:





# In[71]:


a = int(input("Enter the first value :"));
b = a%2
if b == 0:
    print(a, "" , "is an even number");
elif b == 1:
    print(a, "" , "is an odd number");
else:
    print("ncorrect numbers");


# In[ ]:





# In[75]:


list = ["Zaid", "Hassan", "Khadija"];
length = len(list);
print(length);


# In[ ]:





# In[78]:


arr = [5, 13, 34, 115];
n = len(arr);
ans = sum(arr);
print("sum of a list is :" , ans);


# In[ ]:





# In[81]:


lsit = [50, 24, 31, 101];
a = len(list);
ans = largest(a);
print("Largest in given array is :",Ans);


# In[ ]:




