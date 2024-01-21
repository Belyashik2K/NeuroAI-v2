![NeuroAI v2](https://github.com/Belyashik2K/NeuroAI-v2/assets/126521808/33972e93-4b25-4dae-8a22-1934d753b847)
> [Telegram-бот](https://t.me/NeuroAItbot) для взаимодействия с нейросетями посредством [FutureForge API](https://api.futureforge.dev/docs#/). Обновлённая версия [NeuroAI](https://t.me/NeuroAIchannel).

## О боте
**Обновлённая** версия [NeuroAI](https://t.me/NeuroAIchannel) - бота, **окончательно** потерявшего шанс на существование после 31 июля 2023 года. Работает на основе **бесплатного** [FutureForge API](https://api.futureforge.dev/docs#/), поэтому распространяется **абсолютно бесплатно** и **не имеет никаких коммерческих целей**.

Бот **работает** на версии **aiogram v3.x.x**. Для работы с базой данных используется **SQLAlchemy**, что позволяет **быстро** менять используемую базу данных и драйвер. Бот **доступен** на 6 **языках**!

Выражаю **отдельную** **благодарность** [автору](https://t.me/futureforge_channel) API за такой **интересный** и **бесплатный** проект. Надеюсь, что **проект** и дальше **продолжит** **существовать** и **развиваться**!

## Преимущества
* **17** нейросетей, из которых на данный момент **полностью работают** **13**
  * **Работают**
    * _ChatGPT (GPT 3.5)_
    * _Claude AI_
    * _Google AI_
    * _LLaMA AI_
    * _Mistral AI (Medium)_
    * _Solar AI_
    * _Google Gemini Pro_
    * _StableDiffusionXL_
    * _Playground v2_
    * _Midjourney V4_
    * _DALL·E 3_
    * _StableDiffusion Video_
    * _TencentARC PhotoMaker_
    * _Whisper V3_
    * _RachelVoice_
  * **В ожидании восстановления работоспособности на стороне [FutureForge API](https://api.futureforge.dev/docs#/)**
    * _EnhanceImage_
    * _DALL·E 3_
    * _HighResolutionControlnetTile_
* **Мультиязычность** бота на основе библиотеки **aiogram_i18n** + **fluent****.****runtime**
  * **Доступные языки**
    * _Русский_
    * _Украинский_
    * _Английский_
    * _Немецкий_
    * _Китайский_
    * _Иврит_
* Режим **чата/одиночного запроса** для текстовых нейросетей, **поддержка** и **обработка** **изображений**
* Написан на **новейшей** версии **aiogram - v3.3.0**
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
pip install -r requirements.txt
pip install fluent.runtime
```
**3.** **Переименуйте** файл _.env.example_ в _.env_, **откройте** его любым текстовым редактором или IDE и **установите** свои значения, **например**:
```python
BOT_TOKEN="XXXXXXXXXXXXXXXXXXX" # Your bot token (@BotFather)
FUTURE_FORGE_API_KEY = "XXXXXXXXXXX" # Your API-key for FutureForgeAPI (@futureforgedev_bot)

technical_support = "@Belyashik2K" # Technical support username with @
ads = "@Belyashik2K" # Ads-manager/creator username with @

admin_chat = -1111111111111 # Admin user/chat id for notifications
admin_id = 123456789 # ID for first admin (for access to "👨‍💻 Панель администратора" button")

channel_link = "https://t.me/NeuroAIchannel" # Channel link for "📢 Наш канал" button
api_dev = "https://api.futureforge.dev/docs" # Please, don't change this link. Support the work of the author of the API. Thank you!

driver_name="postgresql+asyncpg"
postgres_user="postgres"
postgres_password="postgres"
postgres_host="localhost"
postgres_port="5432"
postgres_database="postgres"
sqlite_database="sqlite+aiosqlite:///bot/database/base.db" # Don't change this if you don't know what you're doing!

is_sqlite = True # If you want to use SQLite, set this to True, otherwise False
is_debug = False # If you want to use debug mode in logging, set this to True, otherwise False
```

**4.** **Совершите** необходимые **миграции**. Если вы используете **SQLite** - сначала **создайте** **файл** базы данных по пути из значения _sqlite_database_. **Запустите** миграцию.
```python
alembic upgrade head
```
**5.** **Откройте** и **запустите** файл _run.py_. **Бинго**, бот **работает**!

## Ссылки
* [Автор бота](https://t.me/belyashik2k)
* [Поставщик API](https://api.futureforge.dev/docs#/)
* [Пример бота](https://t.me/NeuroAItbot)
