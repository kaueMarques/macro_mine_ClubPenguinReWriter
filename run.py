import pyautogui
import random
import time

#configuração da macro
def iniciar_macro():
    print("Você tem 5 segundos para clicar na tela da mina")
    time.sleep(5)
    print("\n\nRodando a macro...")
    while(True):

        #os numeros são referentes ao x inicial e final do quadrado
        mine_place_x = random.randrange(365, 405)

        #os numeros são referentes ao y inicial e final do quadrado
        mine_place_y = random.randrange(518, 631)
    
        random_timer = random.randrange(3, 5)


        #mining 

        #Closing badge
        pyautogui.click(556, 276)

        pyautogui.click(mine_place_x, mine_place_y)
        pyautogui.click(mine_place_x, mine_place_y)
        time.sleep(random_timer)
        pyautogui.press("d")
        pyautogui.press("d")

        #tempo minerando (tempo minimo, tempo maximo)
        time.sleep(random.randrange(5, 14))

        #Trowing snowball
        for i in range(0, 7):
        
            pyautogui.press("t")
            #tempo em que ele passa jogando as bolas
            time.sleep(0.008)
            #jogando as bolas
            pyautogui.click(741, 183)

        pyautogui.press("d")

def menu():
    
    print("""\n\n
    ================================================================\n
    \t\t\tMacro Club Penguin\n
    ================================================================\n
    Opcoes:\n
    1 - iniciar
    2 - Pegar posições para editar o script
    """)

    opcao = str(input("> "))

    if opcao == "1":
        iniciar_macro()
    
    if opcao == "2":
        for i in range (0, 2):
            print("coloque o mouse para saber a posicao ", i+1, "\nlembre que isso é para desenhar um quadrado")
            time.sleep(3)
            print(pyautogui.position(),"\n") 
        print("agora arrume o script")  


menu()
