from typing import Optional


class Chatting:

    @staticmethod
    def prepare_messages(content: str,
                         role: str,
                         message_list: list,
                         max_len: Optional[int] = 4) -> list:
        message = {
            "role": role,
            "content": content
        }
        message_list.append(message)

        return message_list if len(message_list) <= max_len else message_list[1:]
