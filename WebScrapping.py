from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://500.co/companies"
driver = webdriver.Firefox()  
driver.get(url)


all_job_list = []
for i in range(1, 15):
    selector = f'div.table-row:nth-child({i})'
    job = driver.find_element(By.CSS_SELECTOR, selector)
    company = job.find_element(By.CSS_SELECTOR, f'{selector} > div:nth-child(1) > div:nth-child(1)').text.strip()
    industry = job.find_element(By.CSS_SELECTOR, f'{selector} > div:nth-child(2) > div:nth-child(2)').text.strip()
    sub_industry = job.find_element(By.CSS_SELECTOR, f'{selector}> div:nth-child(3) > div:nth-child(2)').text.strip()
    country = job.find_element(By.CSS_SELECTOR, f'{selector} > div:nth-child(4) > div:nth-child(2)').text.strip()

    all_job_info = {
            'Company_name':company,
            'Industry':industry,
            'Sub-Industry':sub_industry,
            'Country':country
            }
    all_job_list.append(all_job_info)

df1 = pd.DataFrame(all_job_list)

df1.to_csv('companies_data.csv', index=False)

driver.quit()