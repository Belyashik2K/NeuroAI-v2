from typing import Optional, Tuple, Any

from .request import FutureForgeRequest
from .errors import *

from ...enums import *


class FutureForge(FutureForgeRequest):

    def __init__(self) -> None:
        super().__init__()

        self._URL = 'https://api.futureforge.dev/'
        self._METHOD = 'POST'
        
        self.__negative = """Ugly, Disfigured, Deformed, Low quality,
                            Pixelated, Blurry, Grains, Text, 
                            Watermark, Signature, Out of frame, 
                            Disproportioned, Bad proportions, Gross proportions, 
                            Bad anatomy, Duplicate, Cropped, Extra hands, 
                            Extra arms, Extra legs, Extra fingers, 
                            Extra limbs, Long neck, Mutation, Mutilated, 
                            Mutated hands, Poorly drawn face, Poorly drawn hands, 
                            Missing hands, Missing arms, Missing legs, Missing fingers, 
                            Low resolution, Morbid."""

        self._neuros = {
            Neuro.CHATGPT: 'gpt-3-5',
            Neuro.GPT4: 'gpt-4',
            Neuro.CLAUDE: 'Claude-2-100k',
            Neuro.GOOGLE: 'google-palm',
            Neuro.LLAMA: 'llama-2-70b',
            Neuro.GEMINI: 'gemini-pro',
            Neuro.MISTRAL: 'mistral-medium',
            Neuro.SOLAR: 'solar-0-70b',
            Neuro.OPUS: 'Claude-3-Opus-200k',
            Neuro.SONNET: 'Claude-3-Sonnet-200k'
        }

        self._image_neuros = {
            Neuro.SDXL: 'image/sdxl',
            Neuro.PLAYGROUND: 'image/playgroundv2-5',
            Neuro.MIDJOURNEYV4: 'image/openjourneyv4',
            Neuro.VIDEODIFFUSION: 'svd',
            Neuro.DALLE3: 'image/dalle3',
            Neuro.ENHANCE: 'image/enhance-image',
            Neuro.TENCENTMAKER: 'image/photomaker/',
            Neuro.MIDJOURNEYV6: 'midjourney-v6'
        }

        self._voice_neuros = {
            Neuro.WHISPER: 'whisper',
            Neuro.BENDER: 'bender'
        }

    async def text_neuro(self,
                         neuro: str,
                         message: str,
                         mode: str,
                         chat_code: Optional[str] = None
                         ) -> tuple[str, str]:
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

        if mode == Mode.ONE:
            result = await self._request(method=self._METHOD,
                                         neuro=neuro,
                                         uri=self._URL + 'chat/create',
                                         json=json_data
                                         )
        else:
            json_data['chatCode'] = chat_code
            result = await self._request(method=self._METHOD,
                                         neuro=neuro,
                                         uri=self._URL + 'chat/chat',
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
        if neuro == Neuro.PLAYGROUND:
            params['prompt'] = prompt
            params['negative_prompt'] = self.__negative
        elif neuro == Neuro.DALLE3:
            params['prompt'] = prompt
        else:
            params = {'text': prompt}

        neuro_name = self._image_neuros[neuro]
        uri = self._URL + neuro_name

        if neuro != Neuro.DALLE3:
            result = await self._request(method=self._METHOD,
                                         neuro=neuro,
                                         uri=uri,
                                         params=params)
        else:
            result = await self._request(method=self._METHOD,
                                         neuro=neuro,
                                         uri=uri,
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
        uri = self._URL + neuro_name

        json = {'text': text[:330]}
        headers = {
            'accept': 'audio/mpeg',
            'Content-Type': 'application/json'
        }
        result = await self._voice_request(method=self._METHOD,
                                           neuro=neuro,
                                           uri=uri,
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
        uri = self._URL + neuro

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
        uri = self._URL + neuro_name
        params = {}
        params['image_url'] = image_url
        params['num_videos'] = 1

        result = await self._request(method=self._METHOD,
                                     neuro=neuro,
                                     uri=uri,
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
        uri = self._URL + neuro_name

        result = await self._request(method=self._METHOD,
                                     neuro=neuro,
                                     uri=uri,
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
        neuro_name = self._image_neuros[Neuro.TENCENTMAKER]
        uri = self._URL + neuro_name

        params = {
            'image_url': image_url,
            'prompt': prompt,
            'negative_prompt': 'not'
        }

        result = await self._request(method=self._METHOD,
                                     neuro=Neuro.TENCENTMAKER,
                                     uri=uri,
                                     params=params)
        return result['image_url']

    async def midjourneyv6(self,
                           prompt: str) -> str:
        """Generate image with prompt.
        
        Args:
            prompt (str): Prompt.
        Raises:
            FutureForgeError: If error occured.
        Returns:
            str: Image URL."""
        neuro_name = self._image_neuros[Neuro.MIDJOURNEYV6]
        uri = self._URL + neuro_name

        params = {
            'prompt': prompt,
        }

        result = await self._request(method=self._METHOD,
                                     neuro=Neuro.MIDJOURNEYV6,
                                     uri=uri,
                                     params=params)
        return result['upscaled_image_urls']
