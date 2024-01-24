from typing import Optional

from .request import HTTPClient
from .errors import *

from ..keyboards import data

class Neuros(HTTPClient):

    def __init__(self) -> None:
        super().__init__()

        self._method = 'POST'

        self._neuros = {
            data.Neuros.gpt: 'gpt-3-5',
            data.Neuros.claude: 'claude-instant',
            data.Neuros.google: 'google-palm',
            data.Neuros.llama: 'llama-2-70b',
            data.Neuros.gemini: 'gemini-pro',
            data.Neuros.mistral: 'mistral-medium',
            data.Neuros.solar: 'solar-0-70b'
        }

        self._image_neuros = {
            data.Neuros.stable: 'image/sdxl',
            data.Neuros.playground: 'image/playgroundv2',
            data.Neuros.midjourney: 'image/openjourneyv4',
            data.Neuros.sdv: 'svd',
            data.Neuros.dalle3: 'image/dalle3',
            data.Neuros.enhance: 'image/enhance-image',
            data.Neuros.tencentmaker: 'image/photomaker/'
        }

        self._voice_neuros = {
            data.Neuros.whisper: 'voice/take/whisperv3',
            data.Neuros.bender: 'voice/rachel',
        }

    async def text_neuro(self,
                         neuro: str,
                         message: str,
                         mode: str,
                         chat_code: Optional[str] = None
                        ) -> list:
        """Generate text with prompt.
        
        Args:
            neuro (str): Neuro name.
            message (str): Prompt.
            mode (str): Mode.
            chat_code (str, optional): Chat code. Defaults to None.
        Raises:
            FutureForgeError: If error occured.
        Returns:
            list: Generated text and chat code."""
        neuro_name = self._neuros[neuro]
        json_data = {'message': message, 
                     'model': neuro_name}
        
        if mode == data.Mode.one_request:
            result = await self._request(self._method,
                                         neuro, 
                                         self._URI + 'chat/create', 
                                         json=json_data
                                         )                           
        else:
            json_data['chatCode'] = chat_code
            result = await self._request(self._method,
                                         neuro, 
                                         self._URI + 'chat/chat', 
                                         json=json_data)
        return result['message'].strip(), result['chatCode']
     
    async def image_neuro(self,
                          neuro: str,
                          prompt: str
                         ) -> str:
        """Generate image with prompt.
        
        Args:
            neuro (str): Neuro name.
            prompt (str): Prompt.
        Raises:
            FutureForgeError: If error occured.
        Returns:
            str: Image URL."""
        params = {}
        if neuro == data.Neuros.playground:
            params['prompt'] = prompt
            params['negative_prompt'] = 'not'
        elif neuro == data.Neuros.dalle3:
            params['prompt'] = prompt
        else:
            params = {'text': prompt}

        neuro_name = self._image_neuros[neuro]
        uri = self._URI + neuro_name
        
        if neuro != data.Neuros.dalle3:
            result = await self._request(self._method,
                                         neuro, 
                                         uri, 
                                         params=params)
        else:
            result = await self._request(self._method,
                                         neuro, 
                                         uri, 
                                         json=params)
        return result['image_url']

    async def bender_neuro(self,
                           neuro: str,
                           text: str
                           ) -> str:
        """Generate voice with prompt.
        
        Args:
            neuro (str): Neuro name.
            text (str): Prompt.
        Raises:
            FutureForgeError: If error occured.
        Returns:
            str: Voice URL."""
        neuro_name = self._voice_neuros[neuro]
        uri = self._URI + neuro_name

        json = {'text': text[:330]}
        headers = { 
            'accept': 'audio/mpeg', 
            'Content-Type': 'application/json' 
        } 
        result = await self._voice_request(self._method,
                                           neuro, 
                                           uri, 
                                           headers=headers, 
                                           json=json)
        return result

    async def enchance_image_neuro(self,
                                   neuro: str,
                                   image_url: str
                                  ) -> str:
        """Enhance image.
        
        Args:
            neuro (str): Neuro name.
            image_url (str): Image URL.
        Raises:
            FutureForgeError: If error occured.
        Returns:
            str: Image URL."""
        neuro = self._image_neuros[neuro]
        uri = self._URI + neuro

        # Not available now on FutureForge API
        raise FutureForgeError('Not available now on FutureForge API')
        return None 
    
    async def sdv_neuro(self,
                        neuro: str,
                        image_url: str
                        ) -> str:
        """Generate video with prompt.
        
        Args:
            neuro (str): Neuro name.
            image_url (str): Image URL.
        Raises:
            FutureForgeError: If error occured.
        Returns:
            str: Video URL."""
        neuro_name = self._image_neuros[neuro]
        uri = self._URI + neuro_name
        params = {}
        params['image_url'] = image_url
        params['num_videos'] = 1

        result = await self._request(self._method,
                                     neuro, 
                                     uri, 
                                     params=params)
        return result['video_links'][0]
    
    async def whisper_neuro(self,
                            neuro: str,
                            file_url: str
                            ) -> str:
        """Voice to text.
        
        Args:
            neuro (str): Neuro name.
            file_url (str): Voice URL.
        Raises:
            FutureForgeError: If error occured.
        Returns:
            str: Text."""
        neuro_name = self._voice_neuros[neuro]
        uri = self._URI + neuro_name

        result = await self._request(self._method,
                            neuro, 
                            uri, 
                            params={'filepath': file_url})
        return result['response_data']
    
    async def tencentmaker(self,
                         image_url: str,
                         prompt: str) -> str:
        """Generate image with prompt.
        
        Args:   
            image_url (str): Image URL.
            prompt (str): Prompt.
        Raises:
            FutureForgeError: If error occured.
        Returns:
            str: Image URL."""
        neuro_name = self._image_neuros[data.Neuros.tencentmaker]
        uri = self._URI + neuro_name

        params = {
            'image_url': image_url,
            'prompt': prompt,
            'negative_prompt': 'not'
        }

        result = await self._request(self._method,
                                     data.Neuros.tencentmaker,
                                     uri,
                                     params=params)
        return result['image_url']