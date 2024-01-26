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
    — <b>Völlig kostenlos</b> und basiere auf der <a href="https://api.futureforge.dev/docs">API FutureForge</a>
    — Ich habe <b>offenen</b> Quellcode, den du in meinem Repository auf <a href="https://github.com/Belyashik2K/NeuroAI-v2">GitHub</a> finden kannst

    🆘 Technischer Support >>> { $technical_support }
    🥀 Zusammenarbeit >>> { $ads }

```Set language```

messages-choose_language = 🌐 <b>Sprache ändern</b>

messages-lang_set = 🎉 Sprache erfolgreich geändert!

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

    🆘 Technischer Support: { $support }
    🥀 Zusammenarbeit: { $ads }

    🤔 <b>Status der neuronalen Netze</b>
    Neuronale Netze für die Textgenerierung:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    Neuronale Netze für die Bildgenerierung und -verarbeitung:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    Neuronale Netze für die Audiobearbeitung:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>

messages-working = Funktioniert

messages-not_working = In Wartung

```Neuro categories```

messages-choose_neuro_category = <b>🔥 Auswahl des neuronalen Netzwerks</b>
    ❓ <i>Wählen Sie die Kategorie des neuronalen Netzwerks aus</i>
        
    📝 <code>Text</code> — neuronale Netzwerke, die Text generieren.
    <i>Liste der neuronalen Netzwerke:</i>
    ├ <code>💭 ChatGPT (GPT 3.5)</code>
    ├ <code>☁️ Claude AI</code>
    ├ <code>📱 Google AI</code>
    ├ <code>🦙 LLaMA AI</code>
    ├ <code>💻 Mistral AI (Medium)</code>
    ├ <code>🌤 Solar AI</code>
    └ <code>📚 Google Gemini Pro</code>

    🖼 <code>Bilder</code> — neuronale Netzwerke, die Bilder generieren.
    <i>Liste der neuronalen Netzwerke:</i>
    ├ <code>🎨 StableDiffusionXL</code>
    ├ <code>🎮 Playground v2</code>
    ├ <code>✨ EnhanceImage</code>
    ├ <code>📷 Midjourney V4</code>
    ├ <code>🔥 Midjourney V6</code>
    ├ <code>📹 StableDiffusion Video</code>
    ├ <code>🖼 DALL·E 3</code>
    └ <code>🖌 TencentARC PhotoMaker</code>

    🎵 <code>Audio</code> — neuronale Netzwerke, die Audio generieren.
    <i>Liste der neuronalen Netzwerke:</i>
    ├ <code>🎤 Whisper V3</code>
    └ <code>🗣️ RachelVoice</code>

```Neuro choose```

messages-choose_neuro = ❓ <b>Wählen Sie das neuronale Netzwerk aus</b>

messages-category_text = <code>💭 ChatGPT (GPT 3.5)</code> — eines der stabilsten neuronalen Netzwerke für die Textgenerierung. Es kann Texte generieren, Code schreiben, Fragen beantworten und vieles mehr. Kann Links zu Websites verarbeiten.

    <code>☁️ Claude AI</code> — ein KI-Assistent der neuen Generation, basierend auf Anthropic-Forschung zur Schulung nützlicher, ehrlicher und harmloser KI-Systeme. Claude kann eine Vielzahl von Aufgaben bei der Verarbeitung von Gesprächen und Texten ausführen und dabei eine hohe Zuverlässigkeit und Vorhersagbarkeit beibehalten. Funktioniert hauptsächlich auf Englisch.

    <code>📱 Google AI</code> — ein neuronales Netzwerk von Google, das Texte generieren kann, hauptsächlich in Englisch.

    <code>🦙 LLaMA AI</code> — ein großes Sprachmodell (LLM), das von Meta AI im Februar 2023 veröffentlicht wurde. Modelle unterschiedlicher Größe im Bereich von 7 bis 65 Milliarden Gewichten wurden trainiert.

    <code>💻 Mistral AI (Medium)</code> — ein großes maschinelles Lernsprachmodell mit sieben Milliarden Parametern. Antworten auf dem Niveau von ChatGPT, aber mit höherer Qualität. Arbeitet hauptsächlich auf Englisch.

    <code>🌤 Solar AI</code> - ein Modell von Upstage, das führend in der HuggingFace Open LLM-Rangliste ist und eine verbesserte Version des LLaMA 2-Modells darstellt.

    <code>📚 Google Gemini Pro</code> — eines der fortschrittlichsten neuronalen Netzwerke, das von Google veröffentlicht wurde. Es kann Texte generieren, Bilder betrachten und Fragen auf Englisch und Russisch beantworten.

messages-category_image = <code>🎨 StableDiffusionXL</code> — ein neuronales Netzwerk, das Bilder auf Anfrage generieren kann. Es liefert klare und qualitativ hochwertige Bilder bei Verwendung einer guten Eingabeaufforderung.

    <code>🎮 Playground v2</code> — eines der besten neuronalen Netzwerke zur Bildgenerierung. Es kann Bilder auf Anfrage generieren.

    <code>📷 Midjourney V4</code> — ein neuronales Netzwerk, das Bilder auf Anfrage generieren kann. Es liefert klare und qualitativ hochwertige Bilder bei Verwendung einer guten Eingabeaufforderung.

    <code>🔥 Midjourney V6</code> — beste neuronale Netzwerk zur Bildgenerierung derzeit. Verbesserte Version von <code>📷 Midjourney V4</code>
    
    <code>✨ EnhanceImage</code> — ein neuronales Netzwerk, das die Qualität von Bildern verbessern kann.

    <code>📹 StableDiffusion Video</code> — ein neuronales Netzwerk, das Videos auf Grundlage eines erhaltenen Fotos generieren kann.

    <code>🖼 DALL·E 3</code> — eines der fortschrittlichsten neuronalen Netzwerke zur Bildgenerierung von OpenAI.

    <code>🖌 TencentARC PhotoMaker</code> — Ein neuronales Netzwerk, das in der Lage ist, jedes Bild mit einem beliebigen Gesicht gemäß der gegebenen Anfrage zu generieren. Ein NSFW-Filter fehlt.

messages-category_audio = <code>🎤 Whisper V3</code> — ein neuronales Netzwerk, das Audio in Text übersetzen kann.

    <code>🗣 RachelVoice</code> — ein neuronales Netzwerk, das Audio basierend auf einem gegebenen Text generieren kann.

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

    <b>Senden Sie eine Audio-Datei, die in Text übersetzt werden soll</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

messages-bender_voice = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    <b>Geben Sie den Text ein, der vertont werden soll</b> oder drücken Sie die Taste <code>⬅️ Zurück</code>, um die Anfrage abzubrechen.

```Requests```

messages-request_processing = <b>Ihre Anfrage:</b> <code>{ $request }</code>

    😌 <i>Verarbeitung der Anfrage, bitte warten...</i>

messages-request_result = <b>Ihre Anfrage:</b> <code>{ $request }</code>
    <i>Antwort des neuronalen Netzwerks:</i> { $result }

messages-image_processing = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    <b>Ihre Anfrage:</b> <code>{ $prompt }</code>

    😌 <i>Verarbeitung der Anfrage, bitte warten...</i>

messages-other_processing = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

    😌 <i>Verarbeitung der Anfrage, bitte warten...</i>

messages-image_result = 🤖 _Ausgewähltes neuronales Netzwerk:_ `{ $neuro }`

    _Ihre Anfrage:_ `{ $prompt }`

messages-other_result = 🤖 <i>Ausgewähltes neuronales Netzwerk:</i> <code>{ $neuro }</code>

messages-answer = <i>Antwort des neuronalen Netzwerks:</i> <code>{ $result }</code>

```Chat mode```

messages-starting_chat = 🔄 Erstelle einen neuen Dialog, bitte warten Sie...

messages-chat_mode = 🎉 <b>Dialog mit dem Bot gestartet.</b> Um den Dialog zu beenden, drücken Sie die Taste <code>{ $end_button }</code>.

messages-in_work = 😌 Einen Moment bitte, ich bearbeite Ihre Anfrage...

messages-chat_answer = 🤖 { $answer }

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

    Netzwerke zur Textgenerierung:
    ├ ChatGPT: <code>{ $gpt }</code>
    ├ Claude AI: <code>{ $claude }</code>
    ├ Google AI: <code>{ $google }</code>
    ├ LLaMA AI: <code>{ $llama }</code>
    ├ Mistral AI (Medium): <code>{ $mistral }</code>
    ├ Solar AI: <code>{ $solar }</code>
    └ Google Gemini Pro: <code>{ $gemini }</code>

    Netzwerke zur Generierung und Verarbeitung von Bildern:
    ├ StableDiffusionXL: <code>{ $stable }</code>
    ├ Playground v2: <code>{ $playground }</code>
    ├ EnhanceImage: <code>{ $enhance }</code>
    ├ Midjourney V4: <code>{ $midjourney }</code>
    ├ Midjourney V6: <code>{ $midjourneyv6 }</code>
    ├ StableDiffusion Video: <code>{ $sdv }</code>
    ├ DALL·E 3: <code>{ $dalle3 }</code>
    └ TencentARC PhotoMaker: <code>{ $tencentmaker }</code>

    Netzwerke zur Audiobearbeitung:
    ├ Whisper V3: <code>{ $whisper }</code>
    └ RachelVoice: <code>{ $bender }</code>