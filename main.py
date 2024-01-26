#Project step by step


# Step 1 - Login to the company system
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time


pyautogui.PAUSE = 0.5

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

# click -> pyautogui.click()
# write -> pyautogui.write()
# press -> pyautogui.press()
# hotkey -> pyautogui.hotkey()
# scroll -> pyautogui.scroll()



pyautogui.press('win')

pyautogui.write('opera')

pyautogui.press('enter')

pyautogui.click(x=350, y=64)

pyautogui.hotkey('ctrl' + 'a')

pyautogui.write(link)

pyautogui.press('enter')

#wait 5 seconds ONLY IN THIS LINE

time.sleep(5)


# Step 2 - Login

pyautogui.click(x=815, y=388)

# Enter email

pyautogui.write('example@gmail.com')

pyautogui.press('tab')

pyautogui.write('Password123')

pyautogui.click(x=977, y=546)

time.sleep(3)

# Step 3 - Import database
import pandas

table = pandas.read_csv('produtos.csv')
print(table)


for linha in table.index: 

    # Step 4 - Register a product

    pyautogui.click(x=757, y=270)

    # code
    code = table.loc[linha, 'code']    #[linha, coluna]
    pyautogui.write(code)                 #pyautogui.write(tabela.loc[linha, 'codigo'] ) <-- another option
    pyautogui.press('tab')

    # brend
    pyautogui.write(table.loc[linha, 'brend'])
    pyautogui.press('tab')

    # type
    pyautogui.write(table.loc[linha, 'type'])
    pyautogui.press('tab')

    # category
    pyautogui.write(str(table.loc[linha, 'category'])) # '1'
    pyautogui.press('tab')

    # unit_price
    pyautogui.write(str(table.loc[linha, 'unit_price']))
    pyautogui.press('tab')

    # cost
    pyautogui.write(str(table.loc[linha, 'cost']))
    pyautogui.press('tab')

    #obs

    obs = table.loc[linha, 'obs']
    if not pandas.isna(obs):        #"if panda is not empty"
        pyautogui.write(obs)

    #send the product

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(1000)


# Step 5 - Repeat this until the database is finished
