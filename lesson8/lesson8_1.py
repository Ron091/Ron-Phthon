import tools
while True:
    tools.playGame()
    again = input("您是否要再來一次?(y/n)")
    if again == "n":
        break           
print("應用程式結束")