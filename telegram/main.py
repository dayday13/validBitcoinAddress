
import json
import traceback
import os

# my imports
import Updater
import TelegramObjects as tg_obj
import BotCommands
import Bot
import Functions

# =============================================================================
# Bot
# =============================================================================


class validBitcoinAddressBot(Bot.Bot):
    
    help_message = "Please send a Bitcoin address or a QR photo to check it balance."
    
    def __init__(self):
        super().__init__()
        
        self.bot_commands = BotCommands.BotCommandList()
        
        self.bot_commands.add_command(self,
                                      "/start",
                                      lambda chat_id: self.start_message(chat_id),
                                      "")
        
    
    
    def start_message(self, chat_id):
        # message sent when the command start is given
        
        text = "<b>Welcome to the validBitcoinAddress bot</b>\n"
        text += self.help_message
        
        self.sendMessage(chat_id, text)
        

    def handle_updates(self, new_updates):
        ''' This function manages the updates received from Telegram'''
        
        for update in new_updates:
            
            
            if "message" in update:
                message = tg_obj.Message(update["message"])
                
                if message.text and message.chat.type == "private":
                    
                    if self.bot_commands["/start"] == message.text:
                        print("User started bot")
                        self.bot_commands["/start"].fire([message.chat.id])
                    
                    else:
                        check = Functions.Functions.balance_btc(message.text) #return if bitcoin addrsess is valid
                        self.sendMessage(message.chat.id, check)
               
                elif message.photos:
                    print("User sent an QR photo to decode")
                
                    file_id = message.photos.get_highest_res().file_id 
                    image_filename = self.get_image_filename(file_id) #download the photo
                    
                    dirPath = './download_pictures'
                    Files = os.listdir(dirPath)
                    imgPath = None
                    for File in Files:
                        imgPath = os.path.join(dirPath, File)
                        print(imgPath)
                        
                    
                    ans = Functions.Functions.check_QR(imgPath)
                    
                    self.sendMessage(message.chat.id, ans)
                    
                
                else:
                    self.sendMessage(message.chat.id, 
                                    self.help_message)

       
     
# =============================================================================
# main
# =============================================================================
        
if __name__ == "__main__":
    
    # main updater
    
    updater = Updater.Update()
    
    # bot
    bot = validBitcoinAddressBot()

    # updates cycle
    while True:
        
        new_updates = updater.getUpdates()

        try:
            bot.handle_updates(new_updates)
            

        except KeyError as e:
            print("key:", e)
            print(traceback.format_exc())
            
            print("message parsing error")
            print(json.dumps(new_updates, indent=4))


