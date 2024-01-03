# NeuroAI v2
> Telegarm-бот для взаимодействия с нейросетями посредством FutureForge API

## Преимущества
* 14 нейросетей, из которых на данный момент полностью работают 11
  * Работают
    * ChatGPT (GPT 3.5)
    * Claude AI
    * Google AI
    * LLaMA AI
    * Mistral AI (Medium)
    * Google Gemini Pro
    * StableDiffusionXL
    * Playground v2
    * Midjourney V4
    * DALL·E 3
    * RachelVoice
  * В ожидании восстановления работоспособности на стороне FutureForge API
    * EnhanceImage
    * StableDiffusion Video
    * Whisper V3
* Режим чата/одиночного запроса для текстовых нейросетей, поддержка и обработка изображений с помощью хостинга ImageBan
* Написан на новейшей версии aiogram - v3.2.0
* Полностью асинхронная работа с FutureForge API и базой данных с помощью SQLAlchemy
* Многофункциональное меню администратора с возможностью ручного отключения/включения нейросетей, системой выдачи админских привилегий, возможность бана пользователей и включение/отключение режима технических работ, многофункциональное меню рассылки
## Установка
* Клонируйте проект к себе на устройство
```
git clone https://github.com/Belyashik2K/NeuroAI-v2.git
```
* Установите необходимые зависимости
```
pip install --upgrade aiogram aiosqlite sqlalchemy[asyncio] python-dotenv cachetools
```
* Переименуйте файл .env.example в .env, откройте его любым текстовым редактором или IDE и установите свои значения
```
BOT_TOKEN="XXXXXXXXXXXXXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXX" # Токен бота из @BotFather
SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXX" # Ваш SECRET_KEY с сайта ImageBan (https://imageban.ru/u/profile >>> SECRET_KEY)
```
* Откройте файл config.py и установите свои значения
```python
technical_support = "@Belyashik2K" # Username технической поддержки (с @)
ads = "@Belyashik2K" # Username владельца бота (с @)

admin_chat = -1001111111 # ID чата/пользователя, куда/которому будут приходить уведомления об ошибках/новых пользователях
admin_id = 111111111 # ID первого администратора (для получения доступа в "👨‍💻 Админ-панель")

channel_link = "https://t.me/NeuroAIchannel" # Ссылка на канал для кнопки "📢 Наш канал"
api_dev = "https://api.futureforge.dev/docs" # Пожалуйста, уважайте труд автора API, не меняйте эту ссылку! Спасибо!
```
* Откройте и запустите файл start.py. Бинго!
