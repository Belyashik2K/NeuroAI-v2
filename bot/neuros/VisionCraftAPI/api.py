from asyncio import sleep

from .request import VisionCraftRequest, VisionCraftError

from ...config import config
from ...enums import Neuro


class VisionCraft(VisionCraftRequest):
    def __init__(self) -> None:
        super().__init__()

        self._URL = 'https://visioncraft-rs24.koyeb.app/'
        self._METHOD = 'POST'

        self.__KEY = config.VISION_CRAFT_API_KEY.get_secret_value()
        
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

        self._image_neuros = {
            Neuro.ANIMEART: "anime-art-diffusion-xl",
            Neuro.JUGGERNAUT: "juggernaut-xl-V5",
            Neuro.DYNAVISION: "dynavision-xl-all-in-one-stylized",
            Neuro.SDXL: "sdxl-base"
        }

        self._llm_neuros = {
            Neuro.CAPYBARA: "nous-capybara-7b",
            Neuro.ZEPHYR: "zephyr-7b-beta",
            Neuro.OPENCHAT: "openchat-7b",
            Neuro.MYTHOMIST: "mythomist-7b",
            Neuro.CINEMATIKA: "cinematika-7b",
            Neuro.RWKV5WORLD: "rwkv-5-world-3b",
            Neuro.RWKV5AITOWN: "rwkv-5-3b-ai-town"
        }

    @staticmethod
    def prepare_answer(answer: str) -> str:
        return answer.replace('USER:','').strip()

    async def chatting(self,
                       neuro: str,
                       messages: list
                       ) -> str:
        neuro_name = self._llm_neuros[neuro]
        data = {
            "token": self.__KEY,
            "model": neuro_name,
            "messages": messages
            }

        result = await self._request(neuro=neuro,
                                     uri=self._URL + 'llm',
                                     method=self._METHOD,
                                     json=data)
        return [self.prepare_answer(answer=result['choices'][0]['message']['content'])]

    async def image_neuro(self,
                                neuro: str,
                                prompt: str) -> str:
        neuro_name = self._image_neuros[neuro]
        data = {
            "model": neuro_name,
            "prompt": prompt,
            "negative_prompt": self.__negative,
            "token": self.__KEY,
            "height": 1024,
            "width": 1024,
            "steps": 30,
            "cfg_scale": 10
            }
        
        result = await self._request(neuro=neuro,
                                    uri=self._URL + 'generate-xl',
                                    method=self._METHOD,
                                    json=data)
        if result['job_id'] != None:
            image = await self.check_job_status(neuro=neuro,
                                                job_id=result['job_id'])
            await sleep(1.5)
            while not image:
                image = await self.check_job_status(neuro=neuro,
                                                    job_id=result['job_id'])
                await sleep(1.5)
            return image 
        else:
            raise VisionCraftError(f"Error (JobID is none) while requesting {self._URL + 'generate-xl'} with {data}")            
    
    async def enchance_image(self,
                             neuro: str,
                             photo_url: str) -> bytes:

        data = {
            "image": photo_url,
            "token": self.__KEY,
        }

        result = await self._upscale_request(method=self._METHOD,
                                             neuro=neuro,
                                             uri=self._URL + 'upscale',
                                             json=data)
        return result

    async def check_job_status(self,
                               neuro: str,
                               job_id: str) -> str:
        data = {
            "job_id": job_id,
            "nsfw_filter": False,
            "watermark": False
            }
        result = await self._request(neuro=neuro,
                                     uri=self._URL + 'job-status',
                                     method=self._METHOD,
                                     json=data)
        if result['status'] == 'success':
            return result['image']
        return False
