
#Python program to find product page where Product image is missing and save those product link in excel
# In[1]:


import urllib.request
import pandas as pd
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs               
base_url='https://yoshops.com'

blank=[]
ab=[]

for i in range(1,13):
    wp=urllib.request.urlopen('https://yoshops.com/products?page='+str(i))
    sp=bs(wp.read(),'html.parser')
    for result in sp.find_all('div',{'class':"product-thumb-inner"}):
        images=result.find_all('img')
        for img in images:
                c=img['src']
                ab.append(c)
for i in range(1,13):
    wp=urllib.request.urlopen('https://yoshops.com/products?page='+str(i))
    sp=bs(wp.read(),'html.parser')
    result=sp.find_all('div',{'class':"product-thumb-inner"})  
    for a in result:
        images=a.find_all('img')
        for img in images:
            x=img['src']
            if x.endswith('.png'):
                blank.append(x)
product_name=[]
relative_link=[]
for i in range(1,13):
    wp=urllib.request.urlopen('https://yoshops.com/products?page='+str(i))
    sp=bs(wp.read(),'html.parser')
    result=sp.find_all('div',attrs={'class':'product'})
    for resul in result:
        try:
            product_name.append(resul.find('span',attrs={'class':'product-title'}).get_text())
        except:
            product_name.append('n/a')
        try:
            relative_link.append(resul.find('a',attrs={'class':'product-link'}).get('href'))
        except:
            relative_link.append('n/a')
url_combined=[]
for link in relative_link:
    url_combined.append(urllib.parse.urljoin(base_url,link))
df1 = pd.DataFrame({'Product_Name':product_name,'url':url_combined,'image_link':ab})
df2=pd.DataFrame({'image_link':blank})
df3 = pd.merge(df1, df2, how='inner', left_on='image_link', right_on='image_link')
bool_series = df3.duplicated(keep='first')
df3 = df3[~bool_series]
print(df3)
df3.to_excel('products.xlsx',index=False)
time.sleep(100)


# In[ ]:




