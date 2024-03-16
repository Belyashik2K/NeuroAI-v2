from typing import Optional

from ..enums import Neuro, Role


class Chatting:

    @staticmethod
    def prepare_messages(content: str,
                         role: str,
                         message_list: list,
                         neuro: str,
                         image_url: Optional[str] = "",
                         max_len: Optional[int] = 4) -> list:
        message = {
            "role": role,
            "content": content
        }
        
        if neuro == Neuro.LLAVA and role == Role.USER:
            message['image'] = image_url
        message_list.append(message)

        return message_list if len(message_list) <= max_len else message_list[1:]
