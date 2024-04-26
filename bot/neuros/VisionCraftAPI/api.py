import asyncio
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
            Neuro.GOUFENG: "4GuoFeng4XL-v12fp32",
            Neuro.ABSOLUTEREALITY: "AbsoluteReality-V16",
            Neuro.AMIREAL: "AmiReal-v44",
            Neuro.ANYTHING: "Anything-45",
            Neuro.ABYSSORANGEMIX: "nabyssorange-v1",
            Neuro.BLAZINGDRIVE: "BlazingDriveRealistic-_V01e",
            Neuro.CETUSMIX: "AniCetus-V1",
            Neuro.COUNTERFEIT: "xmattarcounterfeitmix-v10",
            Neuro.CUTEYUKIMIX: "CuteYukiMixadorablestyle-v40",
            Neuro.CYBERREALISTIC: "Cyberrealistic-V42",
            Neuro.DELIBERATE2: "Deliberate-v6",
            Neuro.DREAMSHAPER: "DreamShaper-8",
            Neuro.EOR: "EdgeOfRealism-V20",
            Neuro.EIMISANIMEDIFFUSION: "EimisAnimeDiffusion-V20",
            Neuro.ELLDRETHS: "ElldrethsVividMix-v10",
            Neuro.EPICREALISM: "EpiCRealism-pureEvo",
            Neuro.CANTBELIEVE: "ICBINP-ICantBelieveItsNotPhotographyLCM-Final-LCM",
            Neuro.JUGGERNAUTAFTERMATH: "Juggernaut-Aftermath",
            Neuro.LOFI: "LOFI-V4",
            Neuro.LYRIEL: "lyriel_with_resha-v10",
            Neuro.MAJICMIXREALISTIC: "majicMIXrealistic-v7",
            Neuro.MEJINAMIX: "MeinaMix-V11",
            Neuro.PASTELMIXSTYLIZED: "AnimelinerPastelMix-v1",
            Neuro.PORTRAITPLUS: "FantasyPortraitbyAderek-SDXLF32",
            Neuro.PROTOGEN: "Protogenything-1",
            Neuro.REALISTICVISION: "Absoluterealisticvision-V20",
            Neuro.RUNDIFFUSIONFX: "RunDiffusionFXphotorealistic-1",
            Neuro.SHONINSBEAUTIFUL: "ShoninPhotoreal-v1",
            Neuro.TIMELESS: "CopaxTimelessXLV5-V5",
            Neuro.SDXL: "StableDiffusionXLSDXL-base09",
            Neuro.JUGGERNAUT: "JuggernautXLTensorArtExclusive-75RD",
            Neuro.ANIMEART: "AnimagineXL-V3",
            Neuro.DREAMSHAPERXL: "DreamShaperXL10-alpha2",
            Neuro.REALISMENGINE: "RealismEngineSDXL-v30",
            Neuro.TURBOVISION: "TurboVisionXL-SuperFastXLbasedonnewSDXLTurbo-3-5stepqualityoutputathighresolutions-TVXL-V2",
            # Neuro.PLAYGROUND: "playground-V2.5"
            Neuro.MEINAHENT: "MeinaHentai",
            Neuro.LUCIDDREAM: "LucidDreamRealistic-v10",
            Neuro.CAMELLA: "CamelliaMix-V3",
            Neuro.KIZUKI: "Kizuki-AnimeHentai-V3",
            Neuro.DIVINE: "DivineAnimeMix-v2",
            Neuro.CREEPY: "2D_CreepySDXL-v11",
            Neuro.RETROANIME: "TQ-RetroAnime-v10",
            Neuro.SDXLMIDJOURNEY: "MidjourneyV10-Stable",
            Neuro.VOIDMIX: "VoidMix-V5",
            Neuro.ARCHINTER: "architecture_Interior_SDlife_Chiasedamme_V40-40",
            Neuro.THINKDIFF: "ThinkDiffusionXL-10",
            Neuro.CYBERTOKYO: "CyberTokyoXL-1",
            Neuro.REALBOY: "RealboyDarkness-10"     
        }

        self._llm_neuros = {
            Neuro.CAPYBARA: "nous-capybara-7b",
            Neuro.ZEPHYR: "zephyr-orpo-141b-A35b-v0.1",
            Neuro.OPENCHAT: "openchat_3.5",
            Neuro.MYTHOMIST: "mythomist-7b",
            Neuro.CINEMATIKA: "cinematika-7b",
            Neuro.RWKV5WORLD: "rwkv-5-world-3b",
            Neuro.RWKV5AITOWN: "rwkv-5-3b-ai-town",
            Neuro.LZLV: "lzlv_70b_fp16_hf",
            Neuro.PYGMALION: "pygmalion-13b-4bit-128g",
            Neuro.AIRBOROS: "airoboros-70b",
            Neuro.YICHAT: "Yi-34B-Chat",
            Neuro.DOLPHIN: "dolphin-2.6-mixtral-8x7b",
            Neuro.CHRONOSHERMES: "chronos-hermes-13b-v2",
            Neuro.GEMMA: 'gemma-1.1-7b-it',
            Neuro.LLAVA: "llava-1.5-7b-hf",
            Neuro.GPT4: "gpt-4",
            Neuro.CHATGPT: "gpt-3.5-turbo-16k",
            Neuro.GEMINI: "gemini-pro",
            Neuro.CLAUDE: "claude-instant",
            Neuro.SONNET: "claude-3-sonnet",
            Neuro.HAIKU: "claude-3-haiku",
            Neuro.MIXTRAL: "Mixtral-8x7B-Instruct-v0.1",
            Neuro.STARCODER: "starcoder2-15b",
            Neuro.DBRX: "dbrx-instruct",
            Neuro.NETGPT: "net-gpt-3.5-turbo",
            Neuro.WIZARD: "WizardLM-2-8x22B"
        }

        self._xl_neuros = {
        }

    @staticmethod
    def prepare_answer(answer: str) -> str:
        return answer.replace('USER:', '').strip()

    async def chatting(self,
                       neuro: str,
                       messages: list
                       ) -> list[str]:
        neuro_name = self._llm_neuros[neuro]
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.__KEY,
        }
        
        data = {
            "model": neuro_name,
            "messages": messages,
            "max_tokens": 4096,
        }

        result = await self._request(neuro=neuro,
                                     uri=self._URL + 'v1/chat/completions',
                                     method=self._METHOD,
                                     headers=headers,
                                     json=data)
        return [self.prepare_answer(answer=result['choices'][0]['message']['content'])]

    async def dalle(self,
                    prompt: str) -> bytes:
        data = {
        "prompt": prompt,
        "token": self.__KEY
        }
        
        result = await self._upscale_request(neuro=Neuro.DALLE3,
                            uri=self._URL + 'dalle',
                            method=self._METHOD,
                            json=data)
        return result
    
    async def midjourney(self,
                         prompt: str) -> str:
        
        data = {
            "prompt": prompt,
            "token": self.__KEY
        }
        
        answer = await self._request(neuro=Neuro.MIDJOURNEYV6,
                                      uri=self._URL + "midjourney",
                                      method=self._METHOD,
                                      json=data)
        task_id = answer['data']
        photo_url = str()
        
        data = {
            "task_id": str(task_id),
            "token": self.__KEY
            }
        
        while not photo_url:
            result: dict = await self._request(neuro=Neuro.MIDJOURNEYV6,
                                                uri=self._URL + "midjourney/result",
                                                method=self._METHOD,
                                                json=data)
            photo_url = result.get("URL", "")
            await asyncio.sleep(15)   
        return photo_url

    async def image_neuro(self,
                          neuro: str,
                          prompt: str) -> str:
        # if neuro in self._image_neuros:
        #     neuro_name = self._image_neuros[neuro]
        # elif neuro == Neuro.DALLE3:
        #     return await self.dalle(prompt=prompt)
        # elif neuro == Neuro.MIDJOURNEYV6:
        #     return await self.midjourney(prompt=prompt)
        # else:
        #     return await self.xl_image_neuro(neuro=neuro, prompt=prompt)
        data = {"model": self._image_neuros[neuro],
                "sampler": "DPM++ 2M",
                "prompt": prompt,
                "negative_prompt": self.__negative,
                "token": self.__KEY,
                "cfg_scale": 10,
                "steps": 30,
                }
        result = await self._upscale_request(neuro=neuro,
                                     uri=self._URL + 'sd',
                                     method=self._METHOD,
                                     json=data)
        return result

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