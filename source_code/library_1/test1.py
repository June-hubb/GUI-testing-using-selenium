import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.by import By

# from pytime import time


browser = webdriver.Safari()
browser.get("file:///Users/juuuu/Desktop/library_1/login.html")
class TestStringMethods(unittest.TestCase):
    maxDiff = None

    #Login page
    #test1- Checking image location and size
    def test1(self):
        try:
            l = browser.find_element(By.ID, "lib_login_img")
            s = l.text
            location = l.location
            size = l.size
            w, h = size["width"], size["height"]
            tw = 328
            th = 193
            xcor = 236
            ycor = 115
            x = location.get("x")
            y = location.get("y")
            #print("width - ", w)
            #print("height - ", h)
            #print("xcor - ", x)
            #print("ycor - ", y)
            self.assertEqual((w, h), (tw, th))
            self.assertEqual((x, y), (xcor, ycor))
            print("Testcase 1 Passed")

        except NoSuchElementException:
            print("Test case 1 failed")
    
    #test2- Username label size and location and text
    def test2(self):
        try:
            l = browser.find_element(By.ID, "login_user_l")
            s = l.text
            location = l.location
            size = l.size
            w, h = size["width"], size["height"]
            tw = 79
            th = 25
            xcor = 236
            ycor = 323
            x = location.get("x")
            y = location.get("y")
            #print("width - ", w)
            #print("height - ", h)
            #print("xcor - ", x)
            #print("ycor - ", y)
            self.assertEqual((w, h), (tw, th))
            self.assertEqual((x, y), (xcor, ycor))
            value = "Username:"
            self.assertEqual(s.strip(), value.strip())
            print("Testcase 2 Passed")

        except NoSuchElementException:
            print("Test Case 2 failed")
    #test3- Password label size and location and text
    def test3(self):
        try:
            l = browser.find_element(By.ID, "login_pass_l")
            s = l.text
            location = l.location
            size = l.size
            w, h = size["width"], size["height"]
            tw = 75
            th = 25
            xcor = 236
            ycor = 409
            x = location.get("x")
            y = location.get("y")
            #print("width - ", w)
            #print("height - ", h)
            #print("xcor - ", x)
            #print("ycor - ", y)
            self.assertEqual((w, h), (tw, th))
            self.assertEqual((x, y), (xcor, ycor))
            value = "Password:"
            self.assertEqual(s.strip(), value.strip())
            print("Testcase 3 Passed")

        except NoSuchElementException:
            print("Test Case 3 failed")
    #test4- Username input box size and location
    def test4(self):
        try:
            l = browser.find_element(By.ID, "username")
            s = l.text
            location = l.location
            size = l.size
            w, h = size["width"], size["height"]
            tw = 328
            th = 39
            xcor = 236
            ycor = 355
            x = location.get("x")
            y = location.get("y")
            #print("width - ", w)
            #print("height - ", h)
            #print("xcor - ", x)
            #print("ycor - ", y)
            self.assertEqual((w, h), (tw, th))
            self.assertEqual((x, y), (xcor, ycor))
            print("Testcase 4 Passed")

        except NoSuchElementException:
            print("Test Case 4 failed")
    #test5- Password input box size and location
    def test5(self):
        try:
            l = browser.find_element(By.ID, "password")
            s = l.text
            location = l.location
            size = l.size
            w, h = size["width"], size["height"]
            tw = 328
            th = 39
            xcor = 236
            ycor = 441
            x = location.get("x")
            y = location.get("y")
            #print("width - ", w)
            #print("height - ", h)
            #print("xcor - ", x)
            #print("ycor - ", y)
            self.assertEqual((w, h), (tw, th))
            self.assertEqual((x, y), (xcor, ycor))
            print("Testcase 5 Passed")

        except NoSuchElementException:
            print("Test Case 5 failed")
    #test6- Login button size and location
    def test6(self):
        try:
            l = browser.find_element(By.ID, "login_btn")
            s = l.text
            location = l.location
            size = l.size
            w, h = size["width"], size["height"]
            tw = 66
            th = 39
            xcor = 498
            ycor = 639
            x = location.get("x")
            y = location.get("y")
            #print("width - ", w)
            #print("height - ", h)
            #print("xcor - ", x)
            #print("ycor - ", y)
            self.assertEqual((w, h), (tw, th))
            self.assertEqual((x, y), (xcor, ycor))
            print("Testcase 6 Passed")

        except NoSuchElementException:
            print("Test Case 6 failed")
    #test7- Keep me signed in checkbox size and location
    def test7(self):
        try:
            l = browser.find_element(By.ID, "keepSignedIn")
            s = l.text
            location = l.location
            size = l.size
            w, h = size["width"], size["height"]
            tw = 12
            th = 13
            xcor = 236
            ycor = 644
            x = location.get("x")
            y = location.get("y")
            #print("width - ", w)
            #print("height - ", h)
            #print("xcor - ", x)
            #print("ycor - ", y)
            self.assertEqual((w, h), (tw, th))
            self.assertEqual((x, y), (xcor, ycor))
            print("Testcase 7 Passed")

        except NoSuchElementException:
            print("Test Case 7 failed")
    
    #test8- Entering the credentials and logging in. Checking the flow 
    def test8(self):
        try:
            username = browser.find_element(By.ID, "username")
            username.clear()
            username.send_keys("Junaita")

            password = browser.find_element(By.ID, "password")
            password.clear()
            password.send_keys("library123")
            
            browser.find_element(By.ID, "login_btn").click()
            
            i = 0
            while i < 20:
                i = i + 1

            l = browser.find_element(By.ID, "profile-pic")

            print("Testcase 8 Passed")

        except:
            print("Testcase 8 Failed")
    def test9(self):
        try:
            l = browser.find_element(By.ID, "add-genre")
            s = l.text
            location = l.location
            size = l.size
            w, h = size["width"], size["height"]
            tw = 139
            th = 24
            xcor = 415
            ycor = 412
            x = location.get("x")
            y = location.get("y")
            #print("width - ", w)
            #print("height - ", h)
            #print("xcor - ", x)
            #print("ycor - ", y)
            self.assertEqual((w, h), (tw, th))
            self.assertEqual((x, y), (xcor, ycor))
            print("Testcase 9 Passed")

        except NoSuchElementException:
            print("Test Case 9 failed")
    
     
    
if __name__ == "__main__":
    unittest.main()

