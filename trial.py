from getpass import getpass
from os import sep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path 
import streamlit as st


input_data = st.form( 'form',)


model_running = st.container()

col1= st.columns(1)








with input_data :
    page = st.text_input('page link',) 
    num_reuired_hashs = st.number_input('number of hashtags' ,value=0, step= 1) 
    submitted = st.form_submit_button()

 
    




 


with model_running:
    
    

    st.title('ًWelcome! wait till data is loaded...')
    

    

    
    if submitted:
        try: 
            

            driver = Chrome("./chromedriver")
            driver.set_window_position(-7000,0)


            driver.get(page)
            time.sleep(5)
            
        except:
            print('check internet connection!') 



        hashtags_ = []

        last_height = driver.execute_script('return document.body.scrollHeight')


        while  num_reuired_hashs > len(hashtags_) :
            driver.execute_script('window.scrollTo(0 , document.body.scrollHeight);')

            time.sleep(5)

            new_height = driver.execute_script('return document.body.scrollHeight')

            if new_height == last_height:
                break 
            last_height = new_height

            hash_tags = driver.find_elements_by_xpath('//a [@class="css-4rbku5 css-18t94o4 css-901oao css-16my406 r-1cvl2hr r-1loqt21 r-1k78y06 r-bcqeeo r-qvutc0 r-1vmecro"]')
            for hashtag in hash_tags :

                element = hashtag.text
                hashtags_.append(element)
            # hashtags_ = list(set(hashtags_))
        
        hashtags = pd.DataFrame(hashtags_)  
        csv = hashtags.to_csv()
        st.download_button( label="حمل الهاشتاجات",  data=csv,  file_name='هاشتاج تويتر.csv', mime='text/csv',)
        if num_reuired_hashs <= len(hashtags_) & len(hashtags_) != 0 :
            st.title( 'الهاشتاجات')
            st.write(hashtags_)
            
            
            driver.quit()
        elif len(hashtags_) == 0 |  len(hashtags_) < num_reuired_hashs:
            st.text('  تأكد من اتصال جيد بالانترنت و أعد الضغط على الزر مرة أخرى')
            st.text('أو تفقد الصفحة على تويتر ربما هذا هو العدد المتاح من الهاشتاجات ')
            st.write(hashtags_)
            driver.quit()



       



        

    



    










