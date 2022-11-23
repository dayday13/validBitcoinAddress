

import json


class User:
    
    def __init__(self, user_json):
        self.id = user_json["id"]
        self.is_bot = user_json["is_bot"]
        self.first_name = user_json["first_name"]
        
        self.last_name = user_json.get("last_name")
        self.username = user_json.get("username")
        self.language_code = user_json.get("language_code")
        self.is_premium = user_json.get("is_premium")
        self.added_to_attachment_menu = user_json.get("added_to_attachment_menu")
        self.can_join_groups = user_json.get("can_join_groups")
        self.can_read_all_group_messages = user_json.get("can_read_all_group_messages")
        self.supports_inline_queries = user_json.get("supports_inline_queries")
    
    def has_changed(self, user):
        
        if self.first_name != user.first_name:
            return True
        
        if self.last_name != user.last_name:
            return True
        
        if self.username != user.username:
            return True
        
        return False
    
    def get_mention_link(self):
        s = "<a href=\"tg://user?id={}\">_{}_</a>".format(self.id, self.first_name)
        return s
        
        
    def get_silent(self):
        return f"{self.first_name}" +  f" (@ {self.username})" if self.username else ""

    
    def __str__(self):
        name = f"{self.first_name}"
        return name +  (f" (@{self.username})" if self.username else "")
                
'''
This object represents a Telegram user or bot.
'''


class Chat:
    
    def __init__(self, chat_json):
        
        self.id = chat_json["id"]
        self.type = chat_json["type"]
        self.title = chat_json.get("title")
        self.username = chat_json.get("username")
        self.first_name = chat_json.get("first_name")
        self.last_name = chat_json.get("last_name")
        # self.photo (not implemented yet)
        
        self.bio = chat_json.get("bio")
        self.has_private_forwards = chat_json.get("has_private_forwards")
                
        self.has_restricted_voice_and_video_messages = chat_json.get("has_restricted_voice_and_video_messages")
        self.join_to_send_messages = chat_json.get("join_to_send_messages")
        self.join_by_request = chat_json.get("join_by_request")
        self.description = chat_json.get("description")
        self.invite_link = chat_json.get("invite_link")
        
        pinned_message = chat_json.get("pinned_message")
        self.pinned_message = Message(pinned_message) if pinned_message else None
        #self.permissions = chat_json.get("permissions")
        self.slow_mode_delay = chat_json.get("slow_mode_delay")
        self.message_auto_delete_time = chat_json.get("message_auto_delete_time")
        self.has_protected_content = chat_json.get("has_protected_content")
        self.sticker_set_name = chat_json.get("sticker_set_name")
        self.can_set_sticker_set = chat_json.get("can_set_sticker_set")
        self.linked_chat_id = chat_json.get("linked_chat_id")
        #self.location = chat_json.get("location")

'''
Chat
This object represents a chat.
'''

class Message:
    
    def __init__(self, message_json):
        self.message_id = message_json["message_id"]
        self.user = User(message_json["from"])
        
        sender_chat = message_json.get("sender_chat")
        self.sender_chat = Chat(sender_chat) if sender_chat else None
        
        self.date = message_json["date"]
        self.chat = Chat(message_json["chat"])
        
        forward_from = message_json.get("forward_from")
        self.forward_from = User(forward_from) if forward_from else None
        
        forward_from_chat = message_json.get("forward_from_chat")
        self.forward_from_chat = forward_from_chat if forward_from_chat else None
        
        # self.forward_from_message_id
        # self.forward_signature
        # self.forward_sender_name
        # self.forward_date
        # self.is_automatic_forward
        # self.reply_to_message
        # self.via_bot
        # self.edit_date
        # self.has_protected_content
        # self.media_group_id
        # self.author_signature
        
        text = message_json.get("text")
        self.text = text if text else None
        
        self.photos = []
        
        photo = message_json.get("photo")
        
        if message_json.get("photo"):
            self.photos = PhotoSizeArray(message_json["photo"])
        
        # self.entities
        # self.animation
        # self.audio
        
        document = message_json.get("document")
        self.document = Document(document) if document else None
        
        #types of a documents - 
        # self.photo
        # self.sticker
        # self.video
        # self.video_note
        # self.voice
        # self.caption
        # self.caption_entities
        # self.contact
        # self.dice
        # self.game
        # self.poll
        # self.venue
        # self.location
        # self.new_chat_members
        # self.left_chat_member
        # self.new_chat_title
        # self.new_chat_photo
        # self.delete_chat_photo
        # self.group_chat_created
        # self.supergroup_chat_created
        # self.channel_chat_created
        # self.message_auto_delete_timer_changed
        # self.migrate_to_chat_id
        # self.migrate_from_chat_id
        # self.pinned_message
        # self.invoice
        # self.successful_payment
        # self.connected_website
        # self.passport_data
        # self.proximity_alert_triggered
        # self.video_chat_scheduled
        # self.video_chat_started
        # self.video_chat_ended
        # self.video_chat_participants_invited
        # self.web_app_data
        # self.reply_markup
        
        self.json_data = message_json
        
'''
Message
This object represents a message.
'''
 

class InlineQuery:

    def __init__(self, inline_query_json):
        self.id = inline_query_json["id"]
        self.user = User(inline_query_json["from"])
        self.text = inline_query_json["query"]
        self.offset = inline_query_json["offset"]

        self.chat_type = inline_query_json.get("chat_type")
        self.location = inline_query_json.get("location")


'''
InlineQuery
This object represents an incoming inline query. When the user sends an empty query, your bot could return some default or trending results.
'''


class PhotoSize:
    
    def __init__(self, photo_size_json):
        self.file_id = photo_size_json["file_id"]
        self.file_unique_id = photo_size_json["file_unique_id"]
        self.width = photo_size_json["width"]
        self.height = photo_size_json["height"]
        self.file_size = photo_size_json.get("file_size")
       
'''PhotoSize
This object represents one size of a photo or a file / sticker thumbnail.
'''

class PhotoSizeArray:
    
    
    def __init__(self, array_photo_size_json):
        self.array = []
        for photo_json in array_photo_size_json:
            self.array.append(PhotoSize(photo_json))
            
            
    def get_highest_res(self):
        return max(self.array, key= lambda x : x.file_size)
    
    def get_lowsest_res(self):
        return min(self.array, key= lambda x : x.file_size)
    


class File:
    
    def __init__(self, file_json):
        self.file_id = file_json["file_id"]
        self.file_unique_id = file_json["file_unique_id"]
        self.file_size = file_json.get("file_size")
        self.file_path = file_json.get("file_path")
        
        
        
'''File
This object represents a file ready to be downloaded. The file can be downloaded via the link https://api.telegram.org/file/bot<token>/<file_path>. It is guaranteed that the link will be valid for at least 1 hour. When the link expires, a new one can be requested by calling getFile.

The maximum file size to download is 20 MB'''


class InputMedia:
    
    def __init__(self, media_json):
        self.type = media_json["type"]
        self.media = media_json["media"]
        self.caption = media_json.get("caption")
        self.parse_mode = media_json.get("parse_mode")
        self.caption_entities = media_json.get("caption_entities")
    

'''
InputMedia
This object represents the content of a media message to be sent. It should be one of

InputMediaAnimation
InputMediaDocument
InputMediaAudio
InputMediaPhoto
InputMediaVideo'''


class Document:
    
    def __init__(self, document_json):
        self.file_id = document_json["file_id"]
        self.file_unique_id = document_json["file_unique_id"]
        
        self.thumb = document_json.get("thumb")
        self.file_name = document_json.get("file_name")
        self.mime_type = document_json.get("mime_type")
        self.file_size = document_json.get("file_size")

'''
Document
This object represents a general file (as opposed to photos, voice messages and audio files).'''

