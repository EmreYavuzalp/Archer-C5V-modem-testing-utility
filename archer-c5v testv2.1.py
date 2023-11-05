#from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import ttk
from tkinter import *
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By 
from tkinter import messagebox
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains

#This program now only works for Linux. There is a windows version incoming.
i=9300
#this i number is needed for labeling. Not neccessary for normal use.
service=Service(r'/usr/bin/chromedriver')
service2=Service(r'/usr/bin/chromedriver')
driver = Chrome(service=service)
driver2 = Chrome(service=service2)

def wifimac():

    global i
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Durum"))).click()
    time.sleep(0.5)
    sver = driver.find_element(By.ID,"sver")
    hver = driver.find_element(By.ID,"hver")
    
    sernum = driver.find_element(By.ID,"sernum")
    time.sleep(0.1)
    macadres = driver.find_element(By.ID,"lanmac")
    time.sleep(0.1)
    #System.out.println("Printing " + TxtBoxContent.getAttribute("value"));
    print(macadres.get_attribute("innerHTML")) 
    time.sleep(0.1)
    print(sernum.get_attribute("innerHTML")) 
    time.sleep(0.1)
    print(sver.get_attribute("innerHTML")) 
    time.sleep(0.1)
    print(hver.get_attribute("innerHTML")) 
    time.sleep(0.1)
    mac=macadres.get_attribute("innerHTML")
    time.sleep(0.1)
    serino=sernum.get_attribute("innerHTML")
    time.sleep(0.1)
    sver2=sver.get_attribute("innerHTML")
    time.sleep(0.1)
    hver2=hver.get_attribute("innerHTML")
    time.sleep(0.1)
    

    #WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Kolay Menü"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Kablosuz Ayarları"))).click()

    time.sleep(2)

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    
    ssid = driver.find_element(By.ID,"ssid")
    print(ssid.get_attribute("value"))
    sifrewifi = driver.find_element(By.ID,"ssid1_password")
    print(sifrewifi.get_attribute("value"))
    print("")
    ssidad=ssid.get_attribute("value")
    sifrewifi2=sifrewifi.get_attribute("value")

    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"5g"))).click()
    
    ssid5g = driver.find_element(By.ID,"ssid")
    print(ssid5g.get_attribute("value"))
    sifrewifi5g = driver.find_element(By.ID,"ssid1_password")
    print(sifrewifi5g.get_attribute("value"))
    print("")
    ssidad5g=ssid.get_attribute("value")
    sifrewifi5g=sifrewifi.get_attribute("value")
    
    dosya=open("/home/emre/Belgeler/macler.txt","a")
    dosya.write("\n" + ssidad + "," + sifrewifi2 + "," + mac + "," + serino + "," + dt_string + "," + sver2 + "," + hver2)
    dosya2=open("/home/emre/Belgeler/maclerbaskaarcher.txt","a")
    i2=str(i)
    dosya2.write("\n" + i2 + "\n\n\n" + ssidad + "\n" + ssidad5g + "\n\n" + sifrewifi2  + "\n\n")
    
    i=i+1
    dosya.close()
    dosya2.close()
    print("")


def sadece_login():
    driver.get("http://192.168.1.1")
    admin=driver.find_element(By.ID, "userName")
    admin.send_keys("admin")
    sifre=driver.find_element(By.ID, "pcPassword")
    sifre.send_keys("admin")
    
    time.sleep(0.25)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"loginBtn"))).click()
    #login buton olmak zorunda zaten o yüzden gerek yok.
    time.sleep(0.25)

    try:
        driver.find_element(By.ID, "note")
        #uyarı var mı
    except NoSuchElementException:
        #şifre yanlış uyarısı yok geç
        pass
    else:
        driver.get("http://192.168.1.1")
        admin=driver.find_element(By.ID, "userName")
        admin.send_keys("admin")
        sifre=driver.find_element(By.ID, "pcPassword")
        sifre.send_keys("ttnet")
        time.sleep(0.25)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"loginBtn"))).click()
        time.sleep(0.25)
    try:
        driver.find_element(By.ID, "note")
        #uyarı var mı
    except NoSuchElementException:
        #şifre yanlış uyarısı yok geç
        pass
    else:
        messagebox.showwarning("Şifre farklı", "Şifre turktelekom veya ttnet değil, hard reset deneyin.")
#this sometimes gives false positive warnings.
        
    try:
        driver.find_element(By.ID,"skipBtn")
        #div butonu var mı
    except NoSuchElementException:
        #böyle bişey yok geç.
        pass
    else:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"skipBtn"))).click()

    driver.switch_to.alert.accept()
    time.sleep(0.5)
        
    try:
        driver.find_element(By.CSS_SELECTOR,'div.btn')
        #div butonu var mı
    except NoSuchElementException:
        #böyle bişey yok geç.
        pass
    else:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.btn"))).click()
    
    

    
def kur():
    global i
    driver.get("http://192.168.1.1")
    admin=driver.find_element(By.ID, "userName")
    admin.send_keys("admin")
    sifre=driver.find_element(By.ID, "pcPassword")
    sifre.send_keys("admin")
    
    time.sleep(0.25)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"loginBtn"))).click()
    #login buton olmak zorunda zaten o yüzden gerek yok.
    time.sleep(0.25)

    try:
        driver.find_element(By.ID, "note")
        #uyarı var mı
    except NoSuchElementException:
        #şifre yanlış uyarısı yok geç
        pass
    else:
        driver.get("http://192.168.1.1")
        admin=driver.find_element(By.ID, "userName")
        admin.send_keys("admin")
        sifre=driver.find_element(By.ID, "pcPassword")
        sifre.send_keys("ttnet")
        time.sleep(0.25)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"loginBtn"))).click()
        time.sleep(0.25)
    try:
        driver.find_element(By.ID, "note")
        #uyarı var mı
    except NoSuchElementException:
        #şifre yanlış uyarısı yok geç
        pass
    else:
        messagebox.showwarning("Şifre farklı", "Şifre turktelekom veya ttnet değil, hard reset deneyin.")

    try:
        driver.find_element(By.ID,"skipBtn")
        #div butonu var mı
    except NoSuchElementException:
        #böyle bişey yok geç.
        pass
    else:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"skipBtn"))).click()

    driver.switch_to.alert.accept()
    time.sleep(0.5)
        
    try:
        driver.find_element(By.CSS_SELECTOR,'div.btn')
        #div butonu var mı
    except NoSuchElementException:
        #böyle bişey yok geç.
        pass
    else:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.btn"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Durum"))).click()

    time.sleep(0.25)
    sver = driver.find_element(By.ID,"sver")
    hver = driver.find_element(By.ID,"hver")
    
    sernum = driver.find_element(By.ID,"sernum")
    time.sleep(0.2)    
    wlmac0 = driver.find_element(By.ID,"wlmac0")
    wlmac1 = driver.find_element(By.ID,"wlmac1")
    macadres24G=wlmac0.get_attribute("innerHTML")
    macadres5G=wlmac1.get_attribute("innerHTML")
    print(macadres24G)
    print(macadres5G)
    #System.out.println("Printing " + TxtBoxContent.getAttribute("value"));
    time.sleep(0.1)
    print(sernum.get_attribute("innerHTML")) #bu çalıştı
    time.sleep(0.1)
    print(sver.get_attribute("innerHTML")) #bu çalıştı
    time.sleep(0.1)
    print(hver.get_attribute("innerHTML")) #bu çalıştı
    time.sleep(0.1)
    serino=sernum.get_attribute("innerHTML")
    time.sleep(0.1)
    sver2=sver.get_attribute("innerHTML")
    time.sleep(0.1)
    hver2=hver.get_attribute("innerHTML")
    time.sleep(0.1)
    
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Kolay Menü"))).click()
    time.sleep(0.25)    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Kolay Kurulum"))).click()
    time.sleep(0.25)
    #ileri tuşuna bas
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"button"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"button.T.T_ttnetChgDoamin"))).click()
    
    modemkul=driver.find_element(By.ID,"usr")
    modemkul.clear()
    modemkul.send_keys("yourispusername@yourisp")
    #this is classified information so it's randomized
    modemsifre=driver.find_element(By.ID,"pwd")
    modemsifre.clear()
    modemsifre.send_keys("your_pass")
    #this is classified information so it's randomized   
    modemsifretekrar=driver.find_element(By.ID,"cfm")
    modemsifretekrar.clear()
    modemsifretekrar.send_keys("your_pass")
    #this is classified information so it's randomized
    time.sleep(0.25)

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"button.L.T.T_next"))).click()
    time.sleep(0.25)
    
    ssidalt = driver.find_element(By.ID,"ssid")
    sifrewifialt = driver.find_element(By.ID,"pwd")
    print(ssidalt.get_attribute("value"))
    print(sifrewifialt.get_attribute("value"))
    ssid24G=ssidalt.get_attribute("value")
    password24G=sifrewifialt.get_attribute("value")
    ssidalt.clear()
    ssidalt.send_keys("testwifi")
    sifrewifialt.clear()
    sifrewifialt.send_keys("testpass")
    time.sleep(0.25)
    


    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"button.L.T.T_next"))).click()
    
    time.sleep(0.25)
    #TEST ŞEYSİ SONRA SİL
    ssidalt = driver.find_element(By.ID,"ssid")
    sifrewifialt = driver.find_element(By.ID,"pwd")
    print(ssidalt.get_attribute("value"))
    print(sifrewifialt.get_attribute("value"))
    ssid5G=ssidalt.get_attribute("value")
    password5G=sifrewifialt.get_attribute("value")
    ssidalt.clear()
    ssidalt.send_keys("testwifi5GHz")
    sifrewifialt.clear()
    sifrewifialt.send_keys("testpass5GHz")

    time.sleep(0.25)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"button.L.T.T_next"))).click()
    time.sleep(0.25)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"button.L.T.T_save"))).click()
    time.sleep(15)
    driver2.get("http://fast.com")
    dosya=open("/home/emre/Belgeler/macler.txt","a")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("date and time =", dt_string)
    dosya.write("\n" + ssid24G + "," + password24G + "," + ssid5G + "," + password5G + "," + macadres24G + "," + macadres5G + "," + serino + "," + dt_string + "," + sver2 + "," + hver2)
    #dosya2=open("/home/emre/Belgeler/maclerbaskaarcher.txt","a")
    #i2=str(i)
    #dosya2.write("\n" + i2 + "\n\n\n" + ssid24G + "\n" + ssidad5g + "\n\n" + password24G  + "\n\n")
    
    i=i+1
    dosya.close()
    #dosya2.close()
    print("")

def reset():
    
    
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Sistem Araçları"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Fabrika Ayarları"))).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME,"button.XL.T"))).click()
    time.sleep(0.25)
    driver.switch_to.alert.accept()
    time.sleep(5)
    print("reset yapıldı!")
    print("")
    
def oturum_kapat():
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"Oturumu Kapat"))).click()
    time.sleep(0.25)
    driver.switch_to.alert.accept()

    
master = tk.Tk()
master.title('Archer C5V test v2.1')

tk.Button(master,
          text='Kur',
          command=kur).grid(row=3,
                                       column=0,
                                       sticky=tk.W,
                                       pady=2,
                                       )
tk.Button(master,
          text='Resetle', command=reset).grid(row=3,
                                                    column=1,
                                                    sticky=tk.W,
                                                    pady=2)

tk.Button(master,
          text='Oturumu kapat', command=oturum_kapat).grid(row=4,
                                                    column=0,
                                                    sticky=tk.W,
                                                    pady=2)
tk.Button(master,
          text='Sadece login', command=sadece_login).grid(row=4,
                                                    column=1,
                                                    sticky=tk.W,
                                                    pady=2)
tk.Button(master,
          text='Wifimac çek', command=wifimac).grid(row=5,
                                                    column=1,
                                                    sticky=tk.W,
                                                    pady=2)





tk.mainloop()



 #Buraya mesela, wifi başarısız yazarsa uyarı işareti versin öyle bir şey yapabiliriz. Fakat bu archer routerlarda olmuyor 9970 de oluyor.
##    try:
##        driver.find_element_by_id("note")
##        #uyarı var mı
##    except NoSuchElementException:
##        #şifre yanlış uyarısı yok geç
##        pass
##    else:
##        messagebox.showwarning("Şifre farklı", "Password is neither ttnet or turktelekom, try hard reset.")
