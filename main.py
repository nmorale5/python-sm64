from KillBot import KillBot

if __name__ == "__main__":
    print("[*] Starting bot(s). Press Ctrl + Shift + X to stop.")

    ######## Configure bots here ########
    bots = [
        KillBot(),
    ]
    #####################################

    for bot in bots:
        bot.run()

    print("[*] Bot(s) stopped.")
