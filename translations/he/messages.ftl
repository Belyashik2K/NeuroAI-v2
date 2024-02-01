```Start```

messages-start = 🙋 שלום, { $name }!
    
    <b>כדי להמשיך לעבוד עם הבוט, אנא בחר שפה מתוך השפות הבאות 👇</b>

    ⚠️ <i>לאחר בחירת השפה, תוכל לשנות אותה בקטגוריה</i> <code>👤 החשבון שלי</code>

messages-info = 🙋 ברוך הבא לעולם הרשתות העצביות, { $name }!
    
    אני — { $self }, גרסה מעודכנת של בוט NeuroAI, שיעזור לך לעבוד בצורה נוחה ויעילה עם רשתות עצבים!

    <b>היתרונות שלי:</b>
    — מגיב לשאלות שלך בפורמט של <b>דיאלוג</b> או <b>הודעה יחידה</b>
    — יוצר <b>תמונות</b> לפי בקשה
    — יוצר קבצי <b>אודיו</b> לפי בקשה ומתרגם אותם
    — <b>כולא כלום בחינם</b> ופועל על פי <a href="https://api.futureforge.dev/docs">API FutureForge</a> ו-<a href="https://visioncraft-rs24.koyeb.app/docs">API VisionCraft</a>
    — כולל <b>קוד פתוח</b>, שאתה יכול למצוא במאגר הקוד שלי ב- <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

    🆘 תמיכה טכנית >>> { $technical_support }
    🥀 שותפות >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>שינוי שפה</b>

messages-lang_set = 🎉 שפה שונתה בהצלחה!

```Profile info```

messages-my_profile = 👤 <b>החשבון שלי</b>
    <i>מידע בסיסי</i>

    👤 שם >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ מספר בקשות שבוצעו >>> <code>{ $request_counter }</code>

    📅 תאריך הרשמה >>> <code>{ $join_date }</code>

```Stats```

messages-stats = ✨ <b>סטטיסטיקה</b>
    <i>ב-{ $date }</i>

    👤 משתמשים: <code>{ $users_count }</code>
    🔎 בקשות שבוצעו על ידי משתמשים: <code>{ $requests_count }</code>

```About + Neuro statuses```

messages-about = 💬 <b>על השירות</b>
    <i>מידע בסיסי וקישורים</i>

    🆘 תמיכה טכנית: { $support }
    🥀 שותפות: { $ads }

    🤔 <b>מצבי הרשתות העצביות</b>
    רשתות ליצירת טקסט:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    רשתות ליצירת ועיבוד תמונות:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    ├ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>
    ├ JuggernautXL V5: <code>{ $juggernaut }</code>
    ├ DynaVisionXL: <code>{ $dynavision }</code>
    └ AnimeArt: <code>{ $animeart }</code>

    רשתות לעבודה עם אודיו:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>

messages-working = פעיל

messages-not_working = בתחזוקה טכנית

```Neuro categories```

messages-choose_neuro_category = <b>🔥 בחירת רשת עצבים</b>
    ❓ <i>בחר קטגוריה של רשת עצבים</i>
        
    📝 <code>טקסט</code> — רשתות שיוצרות טקסט.
    <i>רשימת רשתות:</i>
    ├ <code>💭 ChatGPT (GPT 3.5)</code>
    ├ <code>☁️ Claude AI</code>
    ├ <code>📱 Google AI</code>
    ├ <code>🦙 LLaMA AI</code>
    ├ <code>💻 Mistral AI (Medium)</code>
    ├ <code>🌤 Solar AI</code>
    └ <code>📚 Google Gemini Pro</code>

    🖼 <code>תמונות</code> — רשתות שיוצרות תמונות.
    <i>רשימת רשתות:</i>
    ├ <code>🎨 StableDiffusionXL</code>
    ├ <code>🎮 Playground v2</code>
    ├ <code>📷 Midjourney V4</code>
    ├ <code>🔥 Midjourney V6</code>
    ├ <code>✨ EnhanceImage</code>
    ├ <code>📹 StableDiffusion Video</code>
    ├ <code>🖼 DALL·E 3</code>
    ├ <code>🖌 TencentARC PhotoMaker</code>
    ├ <code>🦾 JuggernautXL V5</code>
    ├ <code>👁️ DynaVisionXL</code>
    └ <code>🧝🏻‍♀️ AnimeArt</code>

    🎵 <code>אודיו</code> — רשתות שיוצרות אודיו.
    <i>רשימת רשתות:</i>
    ├ <code>🎤 Whisper V3</code>
    └ <code>🗣️ RachelVoice</code>

```Neuro choose```

messages-choose_neuro = ❓ <b>בחר רשת עצבים</b>

messages-category_text = <code>💭 ChatGPT (GPT 3.5)</code> — אחת מהרשתות הכי יציבות ליצירת טקסט. היא מסוגלת ליצור טקסט, לכתוב קוד, לענות על שאלות ועוד. יכולה לעבד קישורים לאתרים.

    <code>☁️ Claude AI</code> — מסייע AI מדור של Anthropic המבוסס על המחקרים שלהם בהכשרת מערכות AI שימושיות, כנונות ולא מזיקות. Claude מסוגל לבצע מגוון רחב של משימות עיבוד שפה וטקסט כשהוא שומר על רמה גבוהה של אמינות והיחס שלו. פועל בעיקר עם שפה אנגלית.

    <code>📱 Google AI</code> — רשת עצבים מ-Google שיכולה ליצור טקסטים, בעיקר באנגלית.

    <code>🦙 LLaMA AI</code> — מודל שפה גדול (LLM) באתר Meta AI בגודל של שבעה מיליארד פרמטרים. נלמדו מודלים בגדלים שונים בטווח של 7 עד 65 מיליארד פרמטרים.

    <code>💻 Mistral AI (Medium)</code> — מודל שפה גדול בלמידת מכונה בפרמטרים של שבעה מיליארדים. תשובות ברמה של ChatGPT, אך עם איכות גבוהה יותר. פועל בעיקר עם שפה אנגלית.

    <code>🌤 Solar AI</code> - המודל של Upstage מתפרסם במקום הראשון בדירוג HuggingFace Open LLM והוא גרסה משופרת של המודל LLaMA 2.

    <code>📚 Google Gemini Pro</code> — אחת מהרשתות המתקדמות ביותר, שהושקה על ידי Google. היא מסוגלת ליצור טקסטים, לצפות בתמונות ולענות על שאלות גם באנגלית וגם ברוסית.

messages-category_image = <code>🎨 StableDiffusionXL</code> — רשת עצבים שיכולה ליצור תמונות לפי בקשה. נותנת תמונות ממוקדות ואיכותיות עם שימוש בפרומפט טוב.

    <code>🎮 Playground v2</code> — אחת מהרשתות הטובות ביותר ליצירת תמונות. מסוגלת ליצור תמונות לפי בקשה.

    <code>📷 Midjourney V4</code> — רשת עצבים שיכולה ליצור תמונות לפי בקשה. נותנת תמונות ממוקדות ואיכותיות עם שימוש בפרומפט טוב.

    <code>🔥 Midjourney V6</code> — הרשת העצבים הטובה ביותר ליצירת תמונות כרגע. גרסה משופרת של <code>📷 Midjourney V4</code>

    <code>✨ EnhanceImage</code> — רשת עצבים שיכולה לשדרג את איכות התמונות.

    <code>📹 StableDiffusion Video</code> — רשת עצבים שיכולה ליצור וידאו לפי תמונה שהתקבלה.

    <code>🖼 DALL·E 3</code> — אחת מהרשתות המתקדמות ביותר ליצירת תמונות מבית OpenAI.

    <code>🖌 TencentARC PhotoMaker</code> — רשת עצבים שיכולה ליצור כל דימוי עם כל פנים על פי בקשה מסוימת. מסנן NSFW אינו קיים.

    <code>🦾 JuggernautXL V5</code> — רשת נוירונים המיועדת ליצירת נופים, תמונות אדריכלות ותמונות מפורטות מאוד.

    <code>👁️ DynaVisionXL</code> — רשת נוירונים שיכולה ליצור תמונות על פי בקשה מסוימת. סופקות תמונות ברורות ובאיכות גבוהה כאשר משתמשים בבקשה טובה.

    <code>🧝🏻‍♀️ AnimeArt</code> — רשת נוירונים המתמקדת ביצירת תמונות אנימה. תוצאות טובות כאשר משתמשים בבקשה באיכות.

messages-category_audio = <code>🎤 Whisper V3</code> — רשת עצבים שיכולה לתרגם קובץ אודיו לטקסט.

    <code>🗣 RachelVoice</code> — רשת עצבים שיכולה ליצור קבצי אודיו לפי טקסט מסוים.

messages-mode = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>

    ❓ <b>בחר מצב עבודה</b>
        
    🔥 <code>בקשה יחידה</code> — הבוט ייצור תשובה אחת לבקשתך וישלח אותה לך.

    👥 <code>שיחת בוט</code> — הבוט יענה על הודעותיך עד שתסיים את השיחה.

messages-header = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>
    <i>❓ המצב שנבחר:</i> <code>{ $mode }</code>

messages-one_request_mode = <b>הזן את הבקשה שלך</b> או לחץ על <code>⬅️ אחורה</code> כדי לבטל את הבקשה.

messages-start_gen_image = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>
        
    <b>הזן את הבקשה שלך</b> או לחץ על <code>⬅️ אחורה</code> כדי לבטל את הבקשה.

    <b>כתוב באנגלית ווודא שקראת את המדריך ליצירת בקשות → <a href="https://telegra.ph/Pamyatka-kak-sostavit-idealnyj-zapros-12-26">לחץ כאן</a></b>

messages-tencentmaker = 🤖 <i>הרשת העצבית שנבחרה:</i> <code>{ $neuro }</code>

    <b>שלח תמונה עם תיאור מפורט של מה שאתה רוצה לראות בתמונה</b> או ללחוץ על הכפתור <code>⬅️ אחורה</code> כדי לבטל את הבקשה.

    ⚠️ <i>תמונה בלעדי כיתוב לא תעובד!</i>

messages-enchance_image = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>

    <b>שלח תמונה שברצונך לשפר</b> או לחץ על <code>⬅️ אחורה</code> כדי לבטל את הבקשה.

messages-sdv_video = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>

    <b>שלח תמונה שברצונך להנפיק אנימציה</b> או לחץ על <code>⬅️ אחורה</code> כדי לבטל את הבקשה.

messages-whisper_voice = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>

    <b>שלח קובץ אודיו שברצונך לתרגם לטקסט</b> או לחץ על <code>⬅️ אחורה</code> כדי לבטל את הבקשה.

messages-bender_voice = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>

    <b>הזן טקסט שברצונך להקליט</b> או לחץ על <code>⬅️ אחורה</code> כדי לבטל את הבקשה.

```בקשות```

messages-request_processing = <b>הבקשה שלך:</b> <code>{ $request }</code>

    😌 <i>מעבד את הבקשה, אנא המתן...</i>

messages-request_result = <b>הבקשה שלך:</b> <code>{ $request }</code>
    <i>תשובת הרשת: </i>

messages-image_processing = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>

    <b>הבקשה שלך:</b> <code>{ $prompt }</code>

    😌 <i>מעבד את הבקשה, אנא המתן...</i>

messages-other_processing = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>

    😌 <i>מעבד את הבקשה, אנא המתן...</i>

messages-image_result = 🤖 _הרשת הנבחרת:_ `{ $neuro }`

    _הבקשה שלך:_ `{ $prompt }`

messages-other_result = 🤖 <i>הרשת הנבחרת:</i> <code>{ $neuro }</code>

messages-answer = <i>תשובת הרשת:</i> <code>{ $result }</code>

```מצב צ'אט```

messages-starting_chat = 🔄 יוצר דיאלוג חדש, אנא המתן...

messages-chat_mode = 🎉 <b>הדיאלוג עם הבוט התחיל.</b> כדי לסיים את הדיאלוג, לחץ על <code>{ $end_button }</code>.

messages-in_work = 😌 רגע, אנא המתן, אני מעבד את הבקשה שלך...

messages-chat_answer = 🤖 { $answer }

messages-stop_chatting = 👋 סיום דיאלוג עם הבוט, אני מחזיר אותך לתפריט הראשי.

```לוח הניהול של מנהלי המערכת```

messages-admin_panel = 👨‍💻 לוח הניהול

messages-admin_find_user = 🔍 <b>חיפוש אחר משתמש</b>
    
    הזן את NeuroID של המשתמש שברצונך למצוא.

messages-admin_user_info = 👤 <b>מידע על המשתמש</b>
    <i>מידע בסיסי</i>

    👤 שם >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ מספר בקשות שהושלמו >>> <code>{ $request_counter }</code>

    📅 תאריך הרשמה >>> <code>{ $join_date }</code>

messages-admin_success_edit = ✅ מעמד המשתמש עודכן בהצלחה.

messages-admin_success = ✅ מעמד הרשת עודכן בהצלחה.

messages-admin_success_maintenance = ✅ מצב התחזוקה טכנית עודכן בהצלחה.

messages-admin_neuro_statuses = <b>🔥 שנה את מצב הרשת</b>

    רשתות ליצירת טקסט:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    רשתות ליצירת ועיבוד תמונות:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    ├ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>
    ├ JuggernautXL V5: <code>{ $juggernaut }</code>
    ├ DynaVisionXL: <code>{ $dynavision }</code>
    └ AnimeArt: <code>{ $animeart }</code>

    רשתות לעבוד עם אודיו:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>

```Input field placeholders```

messages-main_menu = בחר פעולה בתפריט למטה או הקלד את הפקודה /start...