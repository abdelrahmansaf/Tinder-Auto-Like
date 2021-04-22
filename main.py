from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager #You can change 'chrome' if you using another browser
from selenium import webdriver
from login import *
from selenium import webdriver


class AutoSwiper:

    ''' Open google chrome '''
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 6)

    ''' Open tinder.com '''
    def open_browser(self, url):
        self.driver.get(url)

    ''' This function takes every {span} using the span name '''
    def click_button(self, text):
        sleep(2)
        login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{text}']")))
        login_button.click()

    ''' Switching to the 2nd page (facebook login) '''
    def go_to_new_browser_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    ''' This function for input email , password  using the {id} '''
    def input_text(self, input_id, text):
        sleep(1)
        input_text = self.wait.until(EC.visibility_of_element_located((By.ID, f"{input_id}")))
        input_text.send_keys(text)

    ''' Accepting the cookies '''
    def skip_accept(self):
        skip_accept =self.driver.find_element_by_xpath('//*[@id="q-1726090805"]/div/div[2]/div/div/div[1]/button')
        skip_accept.click()  

    ''' clicking in login defined by name ''' 
    def click_login_button_fb(self):
        sleep(5)
        click_login_facebook = self.wait.until(EC.visibility_of_element_located((By.NAME, "login")))
        click_login_facebook.click()

    ''' get back to the first page (tinder) '''
    def go_back_to_main_browser_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    ''' clicking Like 1 time when we call the function '''
    def swipe_like(self):
        sleep(2)
        full_xpath_like = "(//div[@class='Mx(a) Fxs(0) Sq(70px) Sq(60px)--s']/button)[2]"
        swipe_like = self.wait.until(EC.visibility_of_element_located((By.XPATH, full_xpath_like)))
        swipe_like.click()

    ''' clicking Dislike 1 time when we call the function '''
    def swipe_dislike(self):
        dislike_btn = "(//div[@class='Mx(a) Fxs(0) Sq(70px) Sq(60px)--s']/button)[1]"
        swipe_dislike = self.wait.until(EC.visibility_of_element_located((By.XPATH, dislike_btn)))
        swipe_dislike.click()

    ''' function for auto swiping with a chance=60% to give a like to not get banned '''
    def auto_swipe(self):
        from random import random
        while True:
            sleep(0.5)
            try:
                roun = random()
                if roun < .60 :
                    self.swipe_like()
                    print('like')
                else :
                    self.swipe_dislike() 
                    print('dislike')     
            #skipping every popup possible (
            # give a super like = No thanks ,
            # Upload to tinder gold = not interested ,
            # add tinder to your home page = maybe later,
            # ..... etc )                 
            except Exception:
                try:
                    self.click_button('Not interested')
                except Exception:
                    try:
                        self.click_button('No Thanks')
                    except Exception:
                        self.click_button('Maybe Later')

    ''' This function for sending msgs automatically i want to seend 'Hi'
        But i get only one match so i just tested it one time and it didn't work 
        I have the idea but i can't apply it '''
    def send_msg(self):
        while True :
            #First thing you have to click in the match so This for cheching if there is a match ?
            #If yes you have a match this Part for opening the last match (top right)
            matches = self.driver.find_element_by_class_name('matchListItem')[1:]
            if len(matches) < 2 :
                break
            matches[0].click()
            sleep(0.5)

            #After clicking in the match i inserted 'Hi' into the message box
            write_msg  = self.driver.find_element_by_class_name('sendMessageForm_input')
            write_msg.send_keys('Hi')
            #Then click 'send' to send the message
            sned_hi = self.driver.find_element_by_xpath(xpathsend)
            sned_hi.click()
            sleep(1)

            #Get back to the matches_list because after sending a message you will be automatically replaced to the messages_list 
            list_matches = self.driver.find_elements_by_xpath('//*[@id="match-tab"]')
            list_matches.click()
            sleep (0.5)



if __name__ == '__main__':
    tinder = AutoSwiper()
    tinder.open_browser('https://tinder.com/')
    tinder.click_button('Log in')
    tinder.click_button('Login with Facebook')
    tinder.go_to_new_browser_window()
    tinder.input_text('email', FB_EMAIL)
    tinder.input_text('pass', FB_PASS)
    #Here maybe you have to manually 'Accept cookies' if you got stuck here just click on 'Accept All' i gave you 5-Sec to accept it
    tinder.click_login_button_fb()
    tinder.go_back_to_main_browser_window()
    tinder.click_button('Allow')
    tinder.skip_accept()
    tinder.click_button('Not interested')
    tinder.click_button('No Thanks')
    tinder.auto_swipe()
