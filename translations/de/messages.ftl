```Start```

messages-start = 🙋 Hallo, { $name }!
    
    <b>Um die Arbeit mit dem Bot fortzusetzen, wähle bitte eine der untenstehenden Sprachen aus 👇</b>

    ⚠️ <i>Nach der Auswahl der Sprache kannst du sie im Abschnitt</i> <code>👤 Mein Konto</code> <i>ändern</i>

messages-info = 🙋 Willkommen in der Welt der neuronalen Netze, { $name }!
    
    Ich bin { $self }, eine aktualisierte Version des Bots NeuroAI, der dir helfen wird, bequem und effizient mit neuronalen Netzen zu arbeiten!

    <b>Meine Vorteile:</b>
    — Ich antworte auf deine Fragen im Format eines <b>Dialogs</b> oder einer <b>einzigen Nachricht</b>
    — Ich generiere <b>Fotos</b> auf Anfrage
    — Ich generiere Audio-Dateien auf Anfrage und übersetze sie
    — <b>Absolut kostenlos</b> und funktioniert auf Basis von <a href="https://api.futureforge.dev/docs">API FutureForge</a> und <a href="https://api.visioncraft.top/docs">API VisionCraft</a>
    — Ich habe <b>offenen</b> Quellcode, den du in meinem Repository auf <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a> finden kannst

    🆘 Technischer Support >>> { $technical_support }
    🥀 Zusammenarbeit >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>Sprache ändern</b>

messages-lang_set = 🎉 Sprache erfolgreich geändert!

```Favourite neuros```

messages-favourite_neuro = 🌟 <b>Favorisierte neuronale Netzwerke</b>
    <i>Wählen Sie eines Ihrer favorisierten neuronalen Netzwerke aus</i>

messages-no_favourite = 🌟 <b>Favorisierte neuronale Netzwerke</b>
    😕 <i>Sie haben derzeit keine favorisierten neuronalen Netzwerke</i>

    <i>Um ein neuronales Netzwerk zu den Favoriten hinzuzufügen, wählen Sie es im Menü <code>{ $select_neuro }</code> aus und drücken Sie die Taste</i> <code>{ $favourite_button }</code>

```Profile info```

messages-my_profile = 👤 <b>Mein Konto</b>
    <i>Grundlegende Informationen</i>

    👤 Name >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ Anzahl der durchgeführten Generierungen >>> <code>{ $request_counter }</code>

    📅 Anmeldedatum >>> <code>{ $join_date }</code>

```Stats```

messages-stats = ✨ <b>Statistiken</b>
    <i>Am { $date }</i>

    👤 Benutzer: <code>{ $users_count }</code>
    🔎 Generierungen durch Benutzer des Bots: <code>{ $requests_count }</code>

```About + Neuro statuses```

messages-about = 💬 <b>Über den Service</b>
    <i>Grundlegende Informationen und Links</i>

    🤖 Gesamtanzahl der neuronalen Netze: <code>{ $neuro_count }</code>
    🆘 Technischer Support: { $support }
    🥀 Zusammenarbeit: { $ads }

    🤔 <b>Status der neuronalen Netze</b>
    Neuronale Netzwerke zur Textgenerierung:
    ├ Arbeitende neuronale Netzwerke: <code>{ $text_working }</code>
    └ In technischer Wartung: <code>{ $text_not_working }</code>

    Neuronale Netzwerke zur Bildgenerierung und -verarbeitung:
    ├ Arbeitende neuronale Netzwerke: <code>{ $image_working }</code>
    └ In technischer Wartung: <code>{ $image_not_working }</code>

    Neuronale Netzwerke zur Audiobearbeitung:
    ├ Arbeitende neuronale Netzwerke: <code>{ $audio_working }</code>
    └ In technischer Wartung: <code>{ $audio_not_working }</code>

messages-working = Funktioniert

messages-not_working = In Wartung

```Neuro categories```

messages-choose_neuro_category = <b>🔥 Auswahl des neuronalen Netzwerks</b>
    ❓ <i>Wählen Sie die Kategorie des neuronalen Netzwerks aus</i>
        
    📝 <code>Text</code> — neuronale Netzwerke, die Text generieren.

    🖼 <code>Bilder</code> — neuronale Netzwerke, die Bilder generieren.

    🎵 <code>Audio</code> — neuronale Netzwerke, die Audio generieren.

```Neuro choose```

messages-choose_neuro = ❓ <b>Wählen Sie das neuronale Netzwerk aus</b>

messages-category_text = <i>Wählen Sie eines der unten aufgeführten neuronalen Netzwerke</i>

messages-category_image = <i>Wählen Sie eines der unten aufgeführten neuronalen Netzwerke</i>

messages-category_audio = <i>Wählen Sie eines der unten aufgeführten neuronalen Netzwerke</i>

messages-mode = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    ❓ <b>Wählen Sie den Arbeitsmodus aus</b>
        
    🔥 <code>Einzelanfrage</code> — der Bot generiert eine einzelne Antwort auf Ihre Anfrage und sendet sie Ihnen.

    👥 <code>Chat-Bot</code> — der Bot antwortet auf Ihre Nachrichten, bis Sie den Dialog beenden.

messages-header = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>
    <i>❓ Ausgewählter Modus:</i> <code>{ $mode }</code>

messages-one_request_mode = <b>Geben Sie Ihre Anfrage ein</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

messages-start_gen_image = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>
        
    <b>Geben Sie Ihre Anfrage ein</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

    <b>Schreiben Sie auf Englisch und lesen Sie unbedingt die Anleitung zur Erstellung von Anfragen → <a href="https://telegra.ph/Pamyatka-kak-sostavit-idealnyj-zapros-12-26">Klick</a></b>

messages-tencentmaker = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    <b>Senden Sie ein Foto mit einer ausführlichen Beschreibung dessen, was Sie auf dem Foto sehen möchten</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

    ⚠️ <i>Ein Foto ohne Unterschrift wird nicht verarbeitet!</i>

messages-enchance_image = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    <b>Senden Sie ein Foto, das verbessert werden soll</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

messages-sdv_video = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    <b>Senden Sie ein Foto, das animiert werden soll</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

messages-whisper_voice = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>
    <i>❓ Ausgewählter Modus:</i> <code>{ $mode }</code>

    <b>Senden Sie die Audiodatei zur Verarbeitung</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

messages-whisper_mode = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    <b>Wählen Sie den Betriebsmodus aus</b>

    ⚠️ <i>Die Übersetzung von Text aus Audio unterstützt nur die englische Sprache!</i>

messages-bender_voice = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    <b>Geben Sie den Text ein, der vertont werden soll</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

```Requests```

messages-request_processing = <b>Ihre Anfrage:</b> <code>{ $request }</code>

    😌 <i>Verarbeitung der Anfrage, bitte warten...</i>

messages-request_result = <b>Ihre Anfrage:</b> <code>{ $request }</code>
    <i>Antwort des neuronalen Netzwerks: </i>

messages-image_processing = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    <b>Ihre Anfrage:</b> <code>{ $prompt }</code>

    😌 <i>Verarbeitung der Anfrage, bitte warten...</i>

messages-other_processing = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    😌 <i>Verarbeitung der Anfrage, bitte warten...</i>

messages-whisper_processing = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>
    <i>❓ Ausgewählter Modus:</i> <code>{ $mode }</code>

    😌 <i>Verarbeitung der Anfrage, bitte warten...</i>

messages-whisper_result = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>
    <i>❓ Ausgewählter Modus:</i> <code>{ $mode }</code>

    <i>Antwort des neuronalen Netzwerks:</i> <code>{ $result }</code>

messages-image_result = 🤖 _Ausgewähltes neuronales Netzwerk:_ `{ $neuro }`

    _Ihre Anfrage:_ `{ $prompt }`

messages-other_result = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

messages-answer = <i>Antwort des neuronalen Netzwerks:</i> <code>{ $result }</code>

```Chat mode```

messages-starting_chat = 🔄 Erstelle einen neuen Dialog, bitte warten Sie...

messages-chat_mode = 🎉 <b>Dialog mit dem Bot gestartet.</b> Um den Dialog zu beenden, drücken Sie die Taste <code>{ $end_button }</code>.

messages-in_work = 😌 Einen Moment bitte, ich bearbeite Ihre Anfrage...

messages-chat_answer = 🤖 

messages-stop_chatting = 👋 Der Dialog mit dem Bot wurde beendet, Sie werden zum Hauptmenü zurückgebracht.

```Admin panel```

messages-admin_panel = 👨‍💻 Administratorpanel

messages-admin_find_user = 🔍 <b>Benutzersuche</b>
    
    Geben Sie die NeuroID des Benutzers ein, den Sie finden möchten.

messages-admin_user_info = 👤 <b>Benutzerinformationen</b>
    <i>Grundlegende Informationen</i>

    👤 Name >>> { $name }
    💬 NeuroID >>> <code>{ $neuro_id }</code>
    ⚙️ Anzahl der durchgeführten Generierungen >>> <code>{ $request_counter }</code>

    📅 Registrierungsdatum >>> <code>{ $join_date }</code>

messages-admin_success_edit = ✅ Benutzerstatus erfolgreich geändert.

messages-admin_success = ✅ Netzwerkstatus erfolgreich geändert.

messages-admin_success_maintenance = ✅ Wartungsstatus erfolgreich geändert.

messages-admin_neuro_statuses = <b>🔥 Ändere den Netzwerkstatus</b>

messages-admin_neuro_statuses = <b>🔥 Den Status des neuronalen Netzwerks ändern</b>

    Neuronale Netzwerke zur Textgenerierung:
    ├ Arbeitende neuronale Netzwerke: <code>{ $text_working }</code>
    └ In technischer Wartung: <code>{ $text_not_working }</code>

    Neuronale Netzwerke zur Bildgenerierung und -verarbeitung:
    ├ Arbeitende neuronale Netzwerke: <code>{ $image_working }</code>
    └ In technischer Wartung: <code>{ $image_not_working }</code>

    Neuronale Netzwerke zur Audiobearbeitung:
    ├ Arbeitende neuronale Netzwerke: <code>{ $audio_working }</code>
    └ In technischer Wartung: <code>{ $audio_not_working }</code>

```Input field placeholders```

messages-main_menu = Wählen Sie eine Aktion im Menü unten oder geben Sie den Befehl /start ein...