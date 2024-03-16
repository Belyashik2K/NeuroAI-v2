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
    — <b>כולא כלום בחינם</b> ופועל על פי <a href="https://api.futureforge.dev/docs">API FutureForge</a> ו-<a href="https://api.visioncraft.top/docs">API VisionCraft</a>
    — כולל <b>קוד פתוח</b>, שאתה יכול למצוא במאגר הקוד שלי ב- <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a>

    🆘 תמיכה טכנית >>> { $technical_support }
    🥀 שותפות >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>שינוי שפה</b>

messages-lang_set = 🎉 שפה שונתה בהצלחה!

```Favourite neuros```

messages-favourite_neuro = 🌟 <b>נוירוסים מועדפים</b>
    <i>בחרו אחד מהנוירוסים המועדפים עליכם</i>

messages-no_favourite = 🌟 <b>נוירוסים מועדפים</b>
    😕 <i>אין לך נוירוסים מועדפים כרגע</i>

    <i>כדי להוסיף נוירוס למועדפים, בחרו אותו בתפריט <code>{ $select_neuro }</code> ולחצו על הכפתור</i> <code>{ $favourite_button }</code>

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
    רשתות עצב ליצירת טקסט:
    ├ רשתות עצב פעילות: <code>{ $text_working }</code>
    └ בתחזוקה טכנית: <code>{ $text_not_working }</code>

    רשתות עצב ליצירת ועיבוד תמונות:
    ├ רשתות עצב פעילות: <code>{ $image_working }</code>
    └ בתחזוקה טכנית: <code>{ $image_not_working }</code>

    רשתות עצב לעבוד עם שמע:
    ├ רשתות עצב פעילות: <code>{ $audio_working }</code>
    └ בתחזוקה טכנית: <code>{ $audio_not_working }</code>

messages-working = פעיל

messages-not_working = בתחזוקה טכנית

```Neuro categories```

messages-choose_neuro_category = <b>🔥 בחירת רשת עצבים</b>
    ❓ <i>בחר קטגוריה של רשת עצבים</i>
        
    📝 <code>טקסט</code> — רשתות שיוצרות טקסט.

    🖼 <code>תמונות</code> — רשתות שיוצרות תמונות.

    🎵 <code>אודיו</code> — רשתות שיוצרות אודיו.

```Neuro choose```

messages-choose_neuro = ❓ <b>בחר רשת עצבים</b>

messages-category_text = <i>בחרו אחת מהרשתות העצביות המוצגות למטה</i>

messages-category_image = <i>בחרו אחת מהרשתות העצביות המוצגות למטה</i>

messages-category_audio = <i>בחרו אחת מהרשתות העצביות המוצגות למטה</i>

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

messages-chat_answer = 🤖 

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

messages-admin_neuro_statuses = <b>🔥 לשנות את מצב הרשת העצבית</b>

    רשתות עצב ליצירת טקסט:
    ├ רשתות עצב פעילות: <code>{ $text_working }</code>
    └ בתחזוקה טכנית: <code>{ $text_not_working }</code>

    רשתות עצב ליצירת ועיבוד תמונות:
    ├ רשתות עצב פעילות: <code>{ $image_working }</code>
    └ בתחזוקה טכנית: <code>{ $image_not_working }</code>

    רשתות עצב לעבוד עם שמע:
    ├ רשתות עצב פעילות: <code>{ $audio_working }</code>
    └ בתחזוקה טכנית: <code>{ $audio_not_working }</code>


```Input field placeholders```

messages-main_menu = בחר פעולה בתפריט למטה או הקלד את הפקודה /start...