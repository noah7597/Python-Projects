#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[ ]:





# In[3]:


url = "https://boston.craigslist.org/search/sof"


# In[4]:


response = requests.get(url)


# In[5]:


response


# In[6]:


data = response.text


# In[7]:


soup = BeautifulSoup(data,'html.parser')


# In[8]:


jobs = soup.find_all('p',{'class':'result_info'})


# In[64]:


#Job Details Wrapper
for job in jobs:
    title = job.find('a',{'class':'result-title'}).text #.text is used to get rid of unnecessary data that would print
    location_tag = job.find('span',{'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else "N/A" #extract location text if found otherwise 'N/A'
    date = job.find('time',{'class':'result-date'}).text
    link = job.find('a',{'class':'result-title'}).get('href')
    
    
    print('Job Title:', title, '\nLocation', location, '\nDate:', date, '\nLink:', link, '\n---')


# In[ ]:





# In[ ]:





# In[68]:


#Job Description Page
for job in jobs:
    title = job.find('a',{'class':'result-title'}).text #.text is used to get rid of unnecessary data that would print
    location_tag = job.find('span',{'class':'result-hood'})
    location = location_tag.text[2:-1] if location_tag else "N/A" #extract location text if found otherwise 'N/A'
    date = job.find('time',{'class':'result-date'}).text
    link = job.find('a',{'class':'result-title'}).get('href')
    
    job_response = requests.get(link)
    job_data = job_response.text
    job_soup = BeautifulSoup(job_data,'html.parser')
    job_description = job_soup.find('section', {'id':'postingbody'}).text
    job_attributes_tag = job_soup.find('p',{'class':'attrgroup'})
    job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
    
    print('Job Title:', title, '\nLocation', location, '\nDate:', date, '\nLink:', link, '\n---', job_attributes, '\nJob Description:', job_description, '\n---')


# In[9]:


url = "https://boston.craigslist.org/search/npo"


# In[10]:


#Crawling and Scraping Next Pages
job_no = 0
while True:

    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data,'html.parser')
    jobs = soup.find_all('p',{'class':'result-info'})

    for job in jobs:
        title = job.find('a',{'class':'result-title'}).text #.text is used to get rid of unnecessary data that would print
        location_tag = job.find('span',{'class':'result-hood'})
        location = location_tag.text[2:-1] if location_tag else "N/A" #extract location text if found otherwise 'N/A'
        date = job.find('time',{'class':'result-date'}).text
        link = job.find('a',{'class':'result-title'}).get('href')
    
        job_response = requests.get(link)
        job_data = job_response.text
        job_soup = BeautifulSoup(job_data,'html.parser')
        job_description = job_soup.find('section', {'id':'postingbody'}).text
        job_attributes_tag = job_soup.find('p',{'class':'attrgroup'})
        job_attributes = job_attributes_tag.text if job_attributes_tag else "N/A"
        job_no+=1
        print('Job Title:', title, '\nLocation', location, '\nDate:', date, '\nLink:', link, '\n---', job_attributes, '\nJob Description:', job_description, '\n---')
    url_tag = soup.find('a',{'title':'next page'})
    if url_tag.get('href'):
        url = 'https://boston.craigslist.org' + url_tag.get('href')
        print(url)
    else:
        break
    
        

print("Total Jobs:", job_no)


# In[12]:


type(url_tag.get)


# In[ ]:




