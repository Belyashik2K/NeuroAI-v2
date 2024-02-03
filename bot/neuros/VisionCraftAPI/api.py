from asyncio import sleep

from .request import VisionCraftRequest

from ...config import config
from ...keyboards import data


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
            data.Neuros.animeart: "anime-art-diffusion-xl",
            data.Neuros.juggernaut: "juggernaut-xl-V5",
            data.Neuros.dynavision: "dynavision-xl-all-in-one-stylized",
            data.Neuros.stable: "sdxl-base"
        }

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
        if result['job_id']:
            image = await self.check_job_status(neuro=neuro,
                                                job_id=result['job_id'])
            await sleep(1.5)
            while not image:
                image = await self.check_job_status(neuro=neuro,
                                                    job_id=result['job_id'])
                await sleep(1.5)
        return image             
    
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
