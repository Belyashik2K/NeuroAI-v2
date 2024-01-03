from .request import HTTPClient
from .errors import *

from texts import IB

class Neuros(HTTPClient):

    def __init__(self) -> None:
        super().__init__()

        self._neuros = {
            IB.Callback.Neuros.gpt: 'chatgpt',
            IB.Callback.Neuros.claude: 'claude-instant',
            IB.Callback.Neuros.google: 'google-palm',
            IB.Callback.Neuros.llama: 'llama-2-70b',
            IB.Callback.Neuros.gemini: 'gemini_pro',
            IB.Callback.Neuros.mistral: 'mistral_medium'
        }

        self._image_neuros = {
            IB.Callback.Neuros.stable: 'image/sdxl',
            IB.Callback.Neuros.playground: 'image/playgroundv2',
            IB.Callback.Neuros.midjourney: 'image/openjourneyv4',
            IB.Callback.Neuros.sdv: 'image/svd',
            IB.Callback.Neuros.dalle3: 'image/dalle3',
            IB.Callback.Neuros.enhance: 'enhance-image'
        }

        self._voice_neuros = {
            IB.Callback.Neuros.whisper: 'voice/take/whisperv3',
            IB.Callback.Neuros.bender: 'voice/rachel',
        }

    async def text_neuro(self,
                         neuro: str,
                         message: str,
                         mode: str,
                         chat_code: str = None
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
        uri = self._URI + neuro_name
        json_data = {'message': message}
        
        if mode == IB.Callback.Mode.one_request:
            result = await self._request(neuro, self._method, uri + '/create', json=json_data)
        else:
            json_data['chatCode'] = chat_code
            result = await self._request(neuro, self._method, uri + '/chat', json=json_data)
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
            str: Image in base64 format."""
        params = {}

        if neuro == IB.Callback.Neuros.playground:
            params['prompt'] = prompt
            params['negative_prompt'] = 'not'
        elif neuro == IB.Callback.Neuros.dalle3:
            params['prompt'] = prompt
        else:
            params = {'text': prompt}

        neuro_name = self._image_neuros[neuro]
        uri = self._URI + neuro_name
        
        if neuro != IB.Callback.Neuros.dalle3:
            result = await self._request(neuro, self._method, uri, params=params)
        else:
            result = await self._request(neuro, self._method, uri, json=params)
        return result['image_base64']

    async def bender_neuro(self,
                           neuro: str,
                           text: str
                           ) -> str:
        neuro_name = self._voice_neuros[neuro]
        uri = self._URI + neuro_name

        json = {'text': text[:330]}
        headers = { 
            'accept': 'audio/mpeg', 
            'Content-Type': 'application/json' 
        } 
        result = await self._voice_request(neuro, self._method, uri, headers=headers, json=json)
        return result

    async def enchance_image_neuro(self,
                                   neuro: str,
                                   image_url: str
                                  ) -> str:
        neuro = self._image_neuros[neuro]
        uri = self._URI + neuro

        # Not available now on FutureForge API
        # TODO: handling result
        return None 
    
    async def sdv_neuro(self,
                        neuro: str,
                        image_url: str
                        ) -> str:
        neuro = self._image_neuros[neuro]
        uri = self._URI + neuro

        # Not available now on FutureForge API
        # TODO: handling result
        return None 
    
    async def whisper_neuro(self,
                            neuro: str,
                            file_url: str
                            ) -> str:
        neuro = self._voice_neuros[neuro]
        uri = self._URI + neuro

        # Not available now on FutureForge API
        # TODO: handling result
        return None