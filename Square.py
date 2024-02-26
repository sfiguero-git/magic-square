# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 13:34:11 2022

@author: Saul Figueroa
"""

import pyautogui, time
distance = 200 # distance per line.
length = 0.001 # How quick the pencil moves.

def draw(): # In MS Paint View >> Uncheck Status Bar:
    
    # Draw the magic square's 16 x 16 grid (Choose drawing tool manually):
   
    pyautogui.click(200, 200);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(400, 200);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(600, 200);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(800, 200);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(200, 400);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(400, 400);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(600, 400);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(800, 400);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(200, 600);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(400, 600);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(600, 600);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(800, 600);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up

    pyautogui.click(200, 800);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(400, 800);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(600, 800);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    pyautogui.click(800, 800);
    pyautogui.dragRel(distance, 0, duration=length) # right
    pyautogui.dragRel(0, distance, duration=length) #down
    pyautogui.dragRel(-distance, 0, duration=length) #left
    pyautogui.dragRel(0, -distance, duration=length) #up
    
    text = pyautogui.locateCenterOnScreen('Images/text.png', confidence = 0.8) 
    pyautogui.click(text)
    
    x = 280
    y = 300
    
    pyautogui.click(x, y)
    pyautogui.write(A)
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("1")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("12")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("7")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    x = 280
    y = y + 200
    
    pyautogui.click(x, y)
    pyautogui.write("11")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("8")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write(D)
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("2")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    x = 280
    y = y + 200
    
    pyautogui.click(x, y)
    pyautogui.write("5")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("10")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("3")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write(C)
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    x = 280
    y = y + 200
    
    pyautogui.click(x, y)
    pyautogui.write("4")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write(B)
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("6")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
    pyautogui.click(x, y)
    pyautogui.write("9")
    time.sleep(0.5)  
    pyautogui.click(x + 50, y + 50) # Click out of textbox.
    x = x + 200
    time.sleep(0.5)
    
chosenNumber = pyautogui.prompt(text='Choose a number between 22 and 99: ', title='Choose a number! (default: 22)' , default='22')

A = str(int(chosenNumber)-20)
B = str(int(A)+1)
C = str(int(B)+1)
D = str(int(A)-1) 

pyautogui.alert("Press OK or close this window to start: ")
time.sleep(0.5) # Small delay before starting the script.
draw()
