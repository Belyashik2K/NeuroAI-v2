![NeuroAI v2](https://github.com/Belyashik2K/NeuroAI-v2/assets/126521808/33972e93-4b25-4dae-8a22-1934d753b847)
> [Telegram-бот](https://t.me/NeuroAItbot) для взаимодействия с нейросетями посредством [FutureForge API](https://api.futureforge.dev/docs#/). Обновлённая версия [NeuroAI](https://t.me/NeuroAIchannel).

## О боте
**Обновлённая** версия [NeuroAI](https://t.me/NeuroAIchannel) - бота, **окончательно** потерявшего шанс на существование после 31 июля 2023 года. Работает на основе **бесплатного** [FutureForge API](https://api.futureforge.dev/docs#/), поэтому распространяется **абсолютно бесплатно** и **не имеет никаких коммерческих целей**.

Бот **работает** на версии **aiogram v3.x.x**. Для работы с базой данных используется **SQLAlchemy**, что позволяет **быстро** менять используемую базу данных и драйвер. Для **обработки** **фотографий** в текстовых моделях используется **бесплатный** фотохостинг [ImageBan](https://imageban.ru/). 

Выражаю **отдельную** **благодарность** [автору](https://t.me/futureforge_channel) API за такой **интересный** и **бесплатный** проект. Надеюсь, что **проект** и дальше **продолжит** **существовать** и **развиваться**!

## Преимущества
* **15** нейросетей, из которых на данный момент **полностью работают** **12**
  * **Работают**
    * _ChatGPT (GPT 3.5)_
    * _Claude AI_
    * _Google AI_
    * _LLaMA AI_
    * _Mistral AI (Medium)_
    * _Google Gemini Pro_
    * _StableDiffusionXL_
    * _Playground v2_
    * _Midjourney V4_
    * _DALL·E 3_
    * _StableDiffusion Video_
    * _RachelVoice_
  * **В ожидании восстановления работоспособности на стороне [FutureForge API](https://api.futureforge.dev/docs#/)**
    * _EnhanceImage_
    * _Whisper V3_
    * _HighResolutionControlnetTile_
* Режим **чата/одиночного запроса** для текстовых нейросетей, **поддержка** и **обработка** **изображений** с помощью фотохостинга [ImageBan](https://imageban.ru/)
* Написан на **новейшей** версии **aiogram - v3.x.x**
* Полностью **асинхронная** работа с [FutureForge API](https://api.futureforge.dev/docs#/) и базой данных с помощью **SQLAlchemy**
* **Анти-флуд**
* **Уведомления** **администраторам** об **ошибках** и **новых пользователях**
* **Многофункциональное** меню администратора с возможностью **ручного отключения/включения нейросетей**, системой выдачи админских **привилегий**, возможность **бана** пользователей и **включение/отключение режима технических работ**, **многофункциональное** меню **рассылки**
## Установка
**1.** **Клонируйте** проект к себе на устройство
```
git clone https://github.com/Belyashik2K/NeuroAI-v2.git
```
**2.** **Установите** необходимые **зависимости**
```python
pip install --upgrade aiogram aiosqlite sqlalchemy[asyncio] python-dotenv cachetools
```
**3.** **Переименуйте** файл _.env.example_ в _.env_, **откройте** его любым текстовым редактором или IDE и **установите** свои значения, **например**:
```python
BOT_TOKEN="XXXXXXXXXXXXXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXX" # Токен бота из @BotFather
SECRET_KEY="XXXXXXXXXXXXXXXXXXXXX" # Ваш SECRET_KEY с сайта ImageBan (https://imageban.ru/u/profile >>> SECRET_KEY)
```
**4.** **Откройте** файл _config.py_ и **установите** свои **значения**, **например:**
```python
technical_support = "@Belyashik2K" # Username технической поддержки (с @)
ads = "@Belyashik2K" # Username владельца бота (с @)

admin_chat = -1001111111 # ID чата/пользователя, куда/которому будут приходить уведомления об ошибках/новых пользователях
admin_id = 111111111 # ID первого администратора (для получения доступа в "👨‍💻 Админ-панель")

channel_link = "https://t.me/NeuroAIchannel" # Ссылка на канал для кнопки "📢 Наш канал"
api_dev = "https://api.futureforge.dev/docs" # Пожалуйста, уважайте труд автора API, не меняйте эту ссылку! Спасибо!
```
5. **Откройте** и **запустите** файл start.py. **Бинго**, бот **работает**!

## Ссылки
* [Автор бота](https://t.me/belyashik2k)
* [Поставщик API](https://api.futureforge.dev/docs#/)
* [Пример бота](https://t.me/NeuroAItbot)
