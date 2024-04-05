import aiohttp
import base64

from typing import Optional

from ..enums import Neuro, Role


class Chatting:

    @staticmethod
    async def prepare_messages(content: str,
                         role: str,
                         message_list: list,
                         neuro: str,
                         image_url: Optional[str] = "",
                         max_len: Optional[int] = 6) -> list:
        
        if image_url == "to_delete":
            message_list = []
        
        message = {
            "role": role,
            "content": [{
                "type": "text",
                "text": content,
            }]
        } 
        
        if neuro != Neuro.LLAVA:
            message = {
                "role": role,
                "content": content
            }
        
        if image_url != "" and image_url != "to_delete":
            message_list = [message]
            if neuro == Neuro.LLAVA and role == Role.USER: 
                async with aiohttp.ClientSession() as session:
                    async with session.get(image_url) as response:
                        image = await response.read()
                
                base64_image = base64.b64encode(image).decode('utf-8')
                        
                image = {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                message['content'].append(image)
        message_list.append(message)
        
        return message_list if len(message_list) <= max_len else message_list[2:]
