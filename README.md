![NeuroAI v2](https://github.com/Belyashik2K/NeuroAI-v2/assets/126521808/33972e93-4b25-4dae-8a22-1934d753b847)
> [Telegram-бот](https://t.me/NeuroAItbot) для взаимодействия с нейросетями посредством [FutureForge API](https://api.futureforge.dev/docs#/) и [VisionCraft API](https://visioncraft-rs24.koyeb.app/docs). Обновлённая версия [NeuroAI](https://t.me/NeuroAIchannel).

# > Russian
## О боте
**Обновлённая** версия [NeuroAI](https://t.me/NeuroAIchannel) - бота, **окончательно** потерявшего шанс на существование после 31 июля 2023 года. Работает на основе **бесплатного** [FutureForge API](https://api.futureforge.dev/docs#/) и [VisionCraft API](https://visioncraft-rs24.koyeb.app/docs), поэтому распространяется **абсолютно бесплатно** и **не имеет никаких коммерческих целей**.

Данный [бот](https://t.me/NeuroAItbot), **базирующийся** на передовых **нейросетях**, создан для того, чтобы **упростить** ваше **взаимодействие** с **разнообразными** **аспектами** искусственного интеллекта. С легкостью и без лишних сложностей [NeuroAI v2](https://t.me/NeuroAItbot) поможет вам **освоить** возможности **текстовых**, **графических** и **звуковых** нейросетей. С его помощью вы можете **генерировать** различные виды **контента**, от **текстов** и идей до **изображений** и **звуков**. Создавайте **уникальные** **статьи**, **рассказы**, **посты** в социальных сетях или даже просто генерируйте **идеи** для вашего **проекта** или **бизнеса**. Создавайте идеи для **дизайна**, **фотографий**, **иллюстраций**, **логотипов** или **артов**. [NeuroAI v2](https://t.me/NeuroAItbot) поможет вам вдохновиться и создать **уникальные** визуальные концепции. Обрабатывайте **аудиофайлы**, генерируйте **речь** или **аудиодорожки** для ваших **проектов**, **видео** или **мультимедийных** приложений.  **Неважно**, **новичок** ли вы или **опытный** пользователь, наш бот предоставляет **интуитивно** **понятные** **интерфейсы**.

Бот **полностью асинхронный** и **работает** на версии **aiogram v3.x.x**. Для работы с базой данных используется **SQLAlchemy**, что позволяет **быстро** менять используемую базу данных и драйвер. В боте присутствует **полная локализация** и **возможность** быстрого **переключения** **между** одним из **6** **языков**.

Выражаю **отдельную** **благодарность** [автору](https://t.me/futureforge_channel) FutureForge API и [авторам](https://t.me/visioncraft_channel) VisionCraft API за разработку таких грандиозных проектов! Спасибо!

## Преимущества
* **69** нейросетей, из которых на данный момент **полностью работают** **61**
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
    * _StableDiffusion Video_
    * _TencentARC PhotoMaker_
    * _Whisper V3_
    * **_И многие другие..._**
  * **В ожидании восстановления работоспособности на стороне [FutureForge API](https://api.futureforge.dev/docs#/)**
    * _EnhanceImage_
    * _DALL·E 3_
    * _HighResolutionControlnetTile_
    * _Midjourney V6_
* **Мультиязычность** бота на основе библиотеки **aiogram_i18n** + **fluent.runtime**
  * **Доступные языки**
    * _Русский_
    * _Украинский_
    * _Английский_
    * _Немецкий_
    * _Китайский_
    * _Иврит_
* Режим **чата/одиночного запроса** для текстовых нейросетей, **поддержка** и **обработка** **изображений**
* Написан на **новейшей** версии **aiogram - v3.3.0**
* Полностью **асинхронная** работа с [FutureForge API](https://api.futureforge.dev/docs), [VisionCraft API](https://visioncraft-rs24.koyeb.app/docs) и базой данных с помощью **SQLAlchemy**
* **Анти-флуд**
* **Уведомления** **администраторам** об **ошибках** и **новых пользователях**
* **Многофункциональное** меню администратора с возможностью **ручного отключения/включения нейросетей**, системой выдачи админских **привилегий**, возможность **бана** пользователей и **включение/отключение режима технических работ**, **многофункциональное** меню **рассылки**
## Установка
### > Вручную (SQLite или PostgreSQL)
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
VISION_CRAFT_API_KEY = "XXXXXXXXXXX" # Your API-key for VisionCraftAPI (@VisionCraft_bot)

technical_support = "@Belyashik2K" # Technical support username with @
ads = "@Belyashik2K" # Ads-manager/creator username with @

admin_chat = -1111111111111 # Admin user/chat id for notifications
admin_id = 123456789 # ID for first admin (for "👨‍💻 Administrator Panel" button)

channel_link = "https://t.me/NeuroAIchannel" # Channel link for "📢 Наш канал" button

driver_name="postgresql+asyncpg"
postgres_user="postgres"
postgres_password="postgres"
postgres_host="localhost"
postgres_port="5432"
postgres_database="postgres"
sqlite_database="sqlite+aiosqlite:///bot/database/base.db" # Don't change this if you don't know what you're doing!

is_sqlite = True # If you want to use SQLite, set this to True, otherwise False
is_debug = False # If you want to use debug mode in logging, set this to True otherwise False
```

**4.** **Совершите** необходимые **миграции**. 
```python
alembic upgrade head
```
**_Внимание!_** Если вы используете **базу данных**, **отличную** от _SQLite_ - для начала **удалите** все **файлы** из папки _migrations/versions_, **создайте** новую **ревизию** с помощью **команды** <code>alembic revision --autogenerate -m 'Название ревизии'</code> и только **после** этого **совершайте** **миграцию**!

**5.** **Откройте** и **запустите** файл _run.py_. **Бинго**, бот **работает**!

### > Через Docker (только SQLite)

**1.** **Клонируйте** проект к себе на устройство
```
git clone https://github.com/Belyashik2K/NeuroAI-v2.git
```
**2.** **Переименуйте** файл _.env.example_ в _.env_, **откройте** его любым текстовым редактором или IDE и **установите** свои значения, **например**:
```python
BOT_TOKEN="XXXXXXXXXXXXXXXXXXX" # Your bot token (@BotFather)
FUTURE_FORGE_API_KEY = "XXXXXXXXXXX" # Your API-key for FutureForgeAPI (@futureforgedev_bot)
VISION_CRAFT_API_KEY = "XXXXXXXXXXX" # Your API-key for VisionCraftAPI (@VisionCraft_bot)

technical_support = "@Belyashik2K" # Technical support username with @
ads = "@Belyashik2K" # Ads-manager/creator username with @

admin_chat = -1111111111111 # Admin user/chat id for notifications
admin_id = 123456789 # ID for first admin (for "👨‍💻 Administrator Panel" button)

channel_link = "https://t.me/NeuroAIchannel" # Channel link for "📢 Наш канал" button

driver_name="postgresql+asyncpg"
postgres_user="postgres"
postgres_password="postgres"
postgres_host="localhost"
postgres_port="5432"
postgres_database="postgres"
sqlite_database="sqlite+aiosqlite:///bot/database/base.db" # Don't change this if you don't know what you're doing!

is_sqlite = True # Don't edit it if you are using Docker
is_debug = False # If you want to use debug mode in logging, set this to True otherwise False
```
**3.** **Запустите** контейнер. Бинго, бот работает!
```docker
docker-compose up
```

## Ссылки
* [Автор бота](https://t.me/belyashik2k)
* [FutureForge API](https://api.futureforge.dev/docs)
* [VisionCraft API](https://visioncraft-rs24.koyeb.app/docs)
* [Пример бота](https://t.me/NeuroAItbot)

# > English
## About the Bot
The **updated** version of [NeuroAI](https://t.me/NeuroAIchannel) bot, which has **finally** lost its chance of existence after July 31, 2023. It operates based on the **free** [FutureForge API](https://api.futureforge.dev/docs#/) and [VisionCraft API](https://visioncraft-rs24.koyeb.app/docs), so it is distributed **completely free** and has **no commercial purposes**.

This bot, **based** on advanced **neural networks**, is designed to **simplify** your **interaction** with various **aspects** of artificial intelligence. With ease and without unnecessary complexity, [NeuroAI v2](https://t.me/NeuroAItbot) will help you **master** the capabilities of **text**, **graphic**, and **audio** neural networks. With its assistance, you can **generate** various types of **content**, from **text** and ideas to **images** and **sounds**. Create **unique** **articles**, **stories**, and **posts** on social media, or simply generate ideas for your **projects** or **business**. Generate ideas for **design**, **photos**, **illustrations**, **logos**, or **art**. [NeuroAI v2](https://t.me/NeuroAItbot) will inspire you and help create **unique** visual concepts. Process **audio files**, generate **speech**, or create **audio tracks** for your **projects**, **videos**, or **multimedia** applications. Whether you are a **novice** or an **experienced** user, our bot provides **intuitive** and **user-friendly** interfaces.

The bot is **completely asynchronous** and runs on version **aiogram v3.x.x**. For database operations, **SQLAlchemy** is utilized, allowing for **quick** changes to the used database and driver. The bot features **full localization** and the **ability** to quickly **switch** **between** one of the **6** **languages**.

I express **special** **gratitude** to the [author](https://t.me/futureforge_channel) of the FutureForge API and the [authors](https://t.me/visioncraft_channel) of the VisionCraft API for developing such grand projects! Thank you!

## Advantages
* **69** neural networks, of which **61 are currently fully operational**
  * **Working**
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
    * _StableDiffusion Video_
    * _TencentARC PhotoMaker_
    * _Whisper V3_
    * **_And many others..._**
  * **Awaiting restoration of functionality on the [FutureForge API](https://api.futureforge.dev/docs#/) side**
    * _EnhanceImage_
    * _DALL·E 3_
    * _HighResolutionControlnetTile_
    * _Midjourney V6_
* **Multilingual** bot based on the **aiogram_i18n** library + **fluent.runtime**
  * **Available languages**
    * _Russian_
    * _Ukrainian_
    * _English_
    * _German_
    * _Chinese_
    * _Hebrew_
* **Chat/single request mode** for text neural networks, **support** and **processing** of **images**
* Written in the **latest** version of **aiogram - v3.3.0**
* Fully **asynchronous** operation with [FutureForge API](https://api.futureforge.dev/docs), [VisionCraft API](https://visioncraft-rs24.koyeb.app/docs) and database using **SQLAlchemy**
* **Anti-flood** mechanism
* **Notifications** to **administrators** about **errors** and **new users**
* **Multifunctional** administrator menu with the ability to **manually disable/enable neural networks**, a system for granting admin **privileges**, the ability to **ban** users, and **enable/disable maintenance mode**, **multifunctional** **broadcast menu**

## Installation
### > Manual (SQLite or PostgreSQL)
**1.** **Clone** the project to your device
```
git clone https://github.com/Belyashik2K/NeuroAI-v2.git
```
**2.** **Install** the necessary **dependencies**
```python
pip install -r requirements.txt
pip install fluent.runtime
```
**3.** **Rename** the _.env.example_ file to _.env_, **open** it with any text editor or IDE, and set your values, for example:
```python
BOT_TOKEN="XXXXXXXXXXXXXXXXXXX" # Your bot token (@BotFather)
FUTURE_FORGE_API_KEY = "XXXXXXXXXXX" # Your API-key for FutureForgeAPI (@futureforgedev_bot)
VISION_CRAFT_API_KEY = "XXXXXXXXXXX" # Your API-key for VisionCraftAPI (@VisionCraft_bot)

technical_support = "@Belyashik2K" # Technical support username with @
ads = "@Belyashik2K" # Ads-manager/creator username with @

admin_chat = -1111111111111 # Admin user/chat id for notifications
admin_id = 123456789 # ID for first admin (for "👨‍💻 Administrator Panel" button)

channel_link = "https://t.me/NeuroAIchannel" # Channel link for "📢 Наш канал" button

driver_name="postgresql+asyncpg"
postgres_user="postgres"
postgres_password="postgres"
postgres_host="localhost"
postgres_port="5432"
postgres_database="postgres"
sqlite_database="sqlite+aiosqlite:///bot/database/base.db" # Don't change this if you don't know what you're doing!

is_sqlite = True # If you want to use SQLite, set this to True, otherwise False
is_debug = False # If you want to use debug mode in logging, set this to True otherwise False
```

**4.** **Perform** the necessary **migrations**.
```python
alembic upgrade head
```
**_Attention!_** If you are using a **database** that is **different** from _SQLite_ - first **delete** all **files** from the _migrations/versions_ folder, **create** a new **revision** using the **command** <code>alembic revision --autogenerate -m 'Revision name'</code> and only **after** this **make** **migration**!

**5.** **Open** and **run** the _run.py_ file. Bingo, the bot is **running**!

### > Via Docker (only SQLite)

**1.** **Clone** the project to your device
```
git clone https://github.com/Belyashik2K/NeuroAI-v2.git
```
**2.** **Rename** the _.env.example_ file to _.env_, **open** it with any text editor or IDE, and set your values, for **example**:
```python
BOT_TOKEN="XXXXXXXXXXXXXXXXXXX" # Your bot token (@BotFather)
FUTURE_FORGE_API_KEY = "XXXXXXXXXXX" # Your API-key for FutureForgeAPI (@futureforgedev_bot)
VISION_CRAFT_API_KEY = "XXXXXXXXXXX" # Your API-key for VisionCraftAPI (@VisionCraft_bot)

technical_support = "@Belyashik2K" # Technical support username with @
ads = "@Belyashik2K" # Ads-manager/creator username with @

admin_chat = -1111111111111 # Admin user/chat id for notifications
admin_id = 123456789 # ID for first admin (for "👨‍💻 Administrator Panel" button)

channel_link = "https://t.me/NeuroAIchannel" # Channel link for "📢 Наш канал" button

driver_name="postgresql+asyncpg"
postgres_user="postgres"
postgres_password="postgres"
postgres_host="localhost"
postgres_port="5432"
postgres_database="postgres"
sqlite_database="sqlite+aiosqlite:///bot/database/base.db" # Don't change this if you don't know what you're doing!

is_sqlite = True # Don't edit it if you are using Docker
is_debug = False # If you want to use debug mode in logging, set this to True otherwise False
```
**3.** **Run** container. Bingo, the bot is **running**!
```docker
docker-compose up
```

## Links
* [Bot Author](https://t.me/belyashik2k)
* [FutureForge API](https://api.futureforge.dev/docs)
* [VisionCraft API](https://visioncraft-rs24.koyeb.app/docs)
* [Bot Example](https://t.me/NeuroAItbot)
