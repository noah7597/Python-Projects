from bs4 import BeautifulSoup
import requests
import pandas as pd


url = input('Paste a link from indeed:') +'&limit=50'


npo_jobs = {}
num_of_jobs = 0


response = requests.get(url)
data = response.text
soup = BeautifulSoup(data,'html.parser')
job = soup.find_all('div',{'class':'row'})
    

for div in job:
    for a in div.find_all('a',{'data-tn-element':'jobTitle'}):
        jobs = (a['title'])
            
    company = div.find('span',{'class':'company'})
        
        
    location_tag = div.find('div',{'class':'location'})
    location = location_tag.text.strip() if location_tag else div.find('span',{'class':'location'}).text.strip()
        
    salary_tag = div.find('span',{'class':'salaryText'})
    salary = salary_tag.text.strip() if salary_tag else 'N/A'
        
        
    for b in div.find_all('a',{'class':'jobtitle turnstileLink'}):
        link = 'https://www.indeed.com' + b.get('href')     
    div_response = requests.get(link)
    div_data = div_response.text
    div_soup = BeautifulSoup(div_data,'html.parser')
        
    job_description = div_soup.find('div',{'class':'jobsearch-jobDescriptionText'})
        
    num_of_jobs = num_of_jobs + 1
        
    npo_jobs[num_of_jobs] = [jobs, company.text.strip(), location, salary, link, job_description.text.strip()]
    
    print('Company:', company.text.strip(),'\n','\nJob:', jobs,'\n','\nLocation:', location,'\n','\nSalary:', salary,'\n','\nLink:', link ,'\n' ,'\nDescription:', job_description.text.strip(),'\nJob Number:',num_of_jobs,'\n------------------')
    
    
    
               
npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index', columns = ['Company','Job','Location','Salary','Link','Job Description'] )     
npo_jobs_df.head()
npo_jobs_df.to_csv('npo_jobs_indeed.csv')   









