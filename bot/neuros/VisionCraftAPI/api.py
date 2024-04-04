import base64
import aiohttp

from .request import VisionCraftRequest
from ...config import config
from ...enums import Neuro


class VisionCraft(VisionCraftRequest):
    def __init__(self) -> None:
        super().__init__()

        self._URL = 'https://visioncraft.top/'
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
            Neuro.GOUFENG: "3guofeng3_v3.4",
            Neuro.ABSOLUTEREALITY: "absolutereality_v1.8.1",
            Neuro.AMIREAL: "amIReal_v4.1",
            Neuro.ANALOGDIFFUSION: "analog_diffusion_v1",
            Neuro.ANYTHING: "anything_V5",
            Neuro.ABYSSORANGEMIX: "abyss_orangemix_v3",
            Neuro.BLAZINGDRIVE: "blazing_drive_v10g",
            Neuro.CETUSMIX: "cetusmix_v35",
            Neuro.CHILDRENSSTORIES3D: "childrensStories_v1_3D",
            Neuro.CHILDRENSSTORIESSEMI: "childrensStories_v1_SemiReal",
            Neuro.CHILDRENSSTORIESTOON: "childrensStories_v1_ToonAnime",
            Neuro.COUNTERFEIT: "Counterfeit_v3.0",
            Neuro.CUTEYUKIMIX: "cuteyukimix_midchapter3",
            Neuro.CYBERREALISTIC: "cyberrealistic_v3.3",
            Neuro.DALCEFO: "dalcefo_v4",
            Neuro.DELIBERATE2: "deliberate_v3",
            Neuro.DREAMLIKEANIME: "dreamlike_anime_v1.0",
            Neuro.DREAMLIKEDIFFUSION: "dreamlike_diffusion_v1.0",
            Neuro.DREAMLIKEPHOTOREAL: "dreamlike_photoreal_v2.0",
            Neuro.DREAMSHAPER: "dreamshaper_v8",
            Neuro.EOR: "edgeOfRealism_eor_v2.0",
            Neuro.EIMISANIMEDIFFUSION: "EimisAnimeDiffusion_v1",
            Neuro.ELLDRETHS: "elldreths-vivid",
            Neuro.EPICREALISM: "epicrealism_natural_Sin_RC1",
            Neuro.CANTBELIEVE: "ICantBelieveItsNotPhotography_seco",
            Neuro.JUGGERNAUTAFTERMATH: "juggernaut_aftermath",
            Neuro.LOFI: "lofi_v4",
            Neuro.LYRIEL: "lyriel_v1.6",
            Neuro.MAJICMIXREALISTIC: "majicmixRealistic_v4",
            Neuro.MECHAMIX: "mechamix_v1.0",
            Neuro.MEJINAMIX: "meinamix_v11",
            Neuro.NEVERENDINGDREAM: "neverendingDream_v1.22",
            Neuro.PASTELMIXSTYLIZED: "pastelMixStylizedAnime_pruned",
            Neuro.PORTRAITPLUS: "portraitplus_v1.0",
            Neuro.PROTOGEN: "protogen_x3.4",
            Neuro.REALISTICVISION: "Realistic_Vision_v5.0",
            Neuro.REDSHIFTDIFFUSION: "redshift_diffusion_v1.0",
            Neuro.REVANIMATED: "revAnimated_v1.2.2",
            Neuro.RUNDIFFUSIONFX: "rundiffusionFX_photorealistic_v1.0",
            Neuro.SHONINSBEAUTIFUL: "shoninsBeautiful_v1.0",
            Neuro.THEALLYSMIX: "theallys_mix_v2",
            Neuro.TIMELESS: "timeless_v1.0",
            Neuro.TOONYOU: "toonyou_beta6"
        }

        self._llm_neuros = {
            Neuro.CAPYBARA: "nous-capybara-7b",
            Neuro.ZEPHYR: "zephyr-7b-beta",
            Neuro.OPENCHAT: "openchat-7b",
            Neuro.MYTHOMIST: "mythomist-7b",
            Neuro.CINEMATIKA: "cinematika-7b",
            Neuro.RWKV5WORLD: "rwkv-5-world-3b",
            Neuro.RWKV5AITOWN: "rwkv-5-3b-ai-town",
            Neuro.LZLV: "lzlv_70b_fp16_hf",
            Neuro.PYGMALION: "pygmalion-13b-4bit-128g",
            Neuro.AIRBOROS: "airoboros-l2-70b-gpt4-1.4.1",
            Neuro.YICHAT: "Yi-34B-Chat",
            Neuro.DOLPHIN: "dolphin-2.6-mixtral-8x7b",
            Neuro.CHRONOSHERMES: "chronos-hermes-13b-v2",
            Neuro.GEMMA: 'gemma-7b',
            Neuro.LLAVA: "llava-1.5-7b-hf",
            Neuro.GPT4: "gpt-4",
            Neuro.CHATGPT: "gpt-3.5-turbo",
            Neuro.GEMINI: "gemini-pro",
            Neuro.CLAUDE: "claude-instant",
            Neuro.SONNET: "claude-3-sonnet",
            Neuro.HAIKU: "claude-3-haiku"
        }

        self._xl_neuros = {
            Neuro.SDXL: "sdxl-base",
            Neuro.JUGGERNAUT: "juggernautXL",
            Neuro.DYNAVISION: "dynavisionXL",
            Neuro.ANIMEART: "animagineXL",
            Neuro.CASCADE: "stable-cascade",
            Neuro.DREAMSHAPERXL: "dreamshaperXL",
            Neuro.REALISMENGINE: "realismEngineSDXL",
            Neuro.REALVISION: "realvisxl",
            Neuro.TURBOVISION: "turbovisionXL",
            Neuro.PLAYGROUND: "playground-V2.5"
        }

    @staticmethod
    def prepare_answer(answer: str) -> str:
        return answer.replace('USER:', '').strip()

    async def chatting(self,
                       neuro: str,
                       messages: list
                       ) -> list[str]:
        neuro_name = self._llm_neuros[neuro]
        data = {
            "token": self.__KEY,
            "model": neuro_name,
            "messages": messages,
            "max_new_tokens": 10000,
        }

        result = await self._request(neuro=neuro,
                                     uri=self._URL + 'llm',
                                     method=self._METHOD,
                                     json=data)
        return [self.prepare_answer(answer=result['choices'][0]['message']['content'])]

    async def dalle(self,
                    prompt):
        data = {
        "prompt": prompt,
        "token": self.__KEY
        }
        
        result = await self._upscale_request(neuro=Neuro.DALLE3,
                            uri=self._URL + 'dalle',
                            method=self._METHOD,
                            json=data)
        return result

    async def image_neuro(self,
                          neuro: str,
                          prompt: str) -> str:
        if neuro in self._image_neuros:
            neuro_name = self._image_neuros[neuro]
        elif neuro == Neuro.DALLE3:
            return await self.dalle(prompt=prompt)
        else:
            return await self.xl_image_neuro(neuro=neuro, prompt=prompt)
        data = {"model": neuro_name,
                "sampler": "DPM++ 2M",
                "prompt": prompt,
                "negative_prompt": self.__negative,
                "image_count": 4,
                "token": self.__KEY,
                "cfg_scale": 10,
                "steps": 30,
                "loras": {"more_details_v10": "more_details_v10"},
                "watermark": False,
                "nsfw_filter": False
                }
        result = await self._request(neuro=neuro,
                                     uri=self._URL + 'generate',
                                     method=self._METHOD,
                                     json=data)
        return result['images']

    async def xl_image_neuro(self,
                             neuro: str,
                             prompt: str) -> str:
        neuro_name = self._xl_neuros[neuro]
        data = {
            "model": neuro_name,
            "prompt": prompt,
            "negative_prompt": self.__negative,
            "token": self.__KEY,
            "height": 1024,
            "width": 1024,
            "steps": 30,
            "cfg_scale": 10,
            "watermark": False,
            "nsfw_filter": False,
            "image_count": 4,
            "sampler": "DPM++ 3M SDE Karras"
        }

        result = await self._request(neuro=neuro,
                                     uri=self._URL + 'generate-xl',
                                     method=self._METHOD,
                                     json=data)
        return result['images']

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
                               job_id: str) -> str | bool:
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
    
    
    async def whisper(self,
                      audio: str,
                      task: str) -> str:
        data = {
            "audio": audio,
            "task": task,
            "token": self.__KEY,
            "language": "auto"
        }
        
        result = await self._request(neuro=Neuro.WHISPER,
                                    uri=self._URL + 'whisper',
                                    method=self._METHOD,
                                    json=data)
        return result['text']
    
    async def text2gif(self,
                       text: str) -> str:
        data = {
            "sampler": "DPM++ 2M",
            "prompt": text,
            "negative_prompt": self.__negative,
            "token": self.__KEY,
            "cfg_scale": 10,
            "steps": 50,
    }
        
        result = await self._request(neuro=Neuro.T2G,
                                    uri=self._URL + 'generate-gif',
                                    method=self._METHOD,
                                    json=data)
        return result["images"][0]

    async def image2image(self,
                          image_url: str,
                          prompt: str) -> bytes:
        
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                bytes_ = await response.read()

        data = {
            "image": base64.b64encode(bytes_).decode('utf-8'),
            "token": self.__KEY,
            "prompt": prompt,
            "negative_prompt": "bad quality",
            "scheduler": "DDIM",
            "steps": 50,
            "strength": 0.8,
            "refiner": "expert_ensemble_refiner"
        }
        
        result = await self._upscale_request(neuro=Neuro.I2I,
                                            uri=self._URL + 'img2img',
                                            method=self._METHOD,
                                            json=data)
        return result