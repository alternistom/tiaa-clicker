import pyautogui
import pyperclip
import time
import io

# v1.0 initial release
# v2.0 now only selects table not the whole damn monstrous page
# v2.1 changed 0.2 sleep to 0.4 for proper page load and changed the while to a for loop based on page number
# v2.2 added clicks to step to next then prev page to wake the table, modified the selection so now it selects the page number as well, down the road implement to chack is page number is right as it is advancing on pages

print( """

████████╗██╗ █████╗  █████╗                        
╚══██╔══╝██║██╔══██╗██╔══██╗                       
   ██║   ██║███████║███████║                       
   ██║   ██║██╔══██║██╔══██║                       
   ██║   ██║██║  ██║██║  ██║                       
   ╚═╝   ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝                       
                                                   
 ██████╗██╗     ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔════╝██║     ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║     ██║     ██║██║     █████╔╝ █████╗  ██████╔╝
██║     ██║     ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╗███████╗██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝╚══════╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ 
 
 v.2.1 by tamas.fabian@dealogic.com
 last updated on:      Feb-21-2019
 initially created on: Jan-28-2019
 
╔────────────────────────────ATTENTION!─────────────────────────────╖
║ Make sure the script window is on the right screen and on the left║
║ the first page of the TIAA is opened up with 50% zoom.            ║
╚────────────────────────────ATTENTION!─────────────────────────────╜
 
""")


tobefilename = input("► What should we name out txt file? ")

pyautogui.doubleClick(1204, 151)
pyautogui.hotkey("ctrl", "c")
pages = pyperclip.paste()

#pages = input("► How many pages of report? ")

actualpages = int(pages)

filename = tobefilename + ".txt"
f = open(filename, "a", encoding="utf-8")

#pyautogui.click(1479, 434) #activates TIAA window


print("")
print("Please don't touch ANYTHING on your computer till you are prompted to do so!")
print("")

time.sleep(1)

savedPagesCounter = 1

pyautogui.click(1242, 150)
time.sleep(1)
pyautogui.click(1136, 151)
time.sleep(1)


for _ in range(int(pages)):

#while actualpages >= 0:
	pyautogui.click(801, 139)
	pyautogui.dragTo(1270, 1166, duration = 0)
	pyautogui.hotkey("ctrl", "c")
	pyautogui.click(1479, 434)
	page_data = pyperclip.paste()
	f.write((str(page_data)) + "\n")	
	#pyperclip.copy('')
	#time.sleep(2)
	pyautogui.click(1242, 150)
	actualpages = actualpages - 1
	print("Page " + str(savedPagesCounter) + " appended to txt file.")
	savedPagesCounter = savedPagesCounter + 1
	time.sleep(0.4)
	
	
print("")
print("File SAVED. Now exiting...")
print("")

f.close()