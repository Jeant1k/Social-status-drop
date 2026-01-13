#### Этап 1: Hard Data & Logic (Фундамент)
*Прежде чем писать текст, нужно собрать «мясо» проекта.*
1.  **AI-Research 2.0:** Использовать AI (Perplexity / GPT-4o с браузером) не для общего поиска, а как узкого специалиста.
    *   *Задача:* Найти актуальные ставки утильсбора (с 1 декабря 2025 правила ужесточились), стоимость автовоза из Европа/Китая/ОАЭ, стоимость аренды лофта для вечеринки и т.д.
2.  **Excel Financial Model:** Создание финмодели.
    *   *AI:* Попроси AI сгенерировать структуру P&L (Profit and Loss) и Cash Flow для автодилера.
    *   *Результат:* Таблица, где видно маржу с одной машины с учетом маркетинга (вечеринки).

Не спрашивай «как привезти авто?». Спрашивай как брокер:
> **Prompt:** "Act as a senior logistics broker for luxury cars relying on the latest Russian customs regulations. Calculate the exact landed cost for a BMW M5 (G90) 2025 bought in Europe for $105,000. Include: customs duty, excise tax, recycling fee (util-sbor) for a legal entity vs individual, broker fees, logistics to Moscow. Output as a table."
> *Зачем:* Чтобы жюри увидело, что ты знаешь про разницу оформления на физ/юр лицо.

> **Action:** Создай файл `finance_logic.md` в Cursor.
> **Prompt (в Cursor):** "Based on the logistics costs we found, help me structure a Unit Economics model for selling one car. Unit Price: 15M RUB. COGS: [Insert Data]. Marketing CAC: [Calculate based on Influencer price]. Event Cost: 100k RUB per car. Calculate Marginal Profit. Prepare formulas for Excel."
> *Совет:* Обязательно учти, что вечеринка для каждого клиента «съедает» маржу. Покажи, что ты это понимаешь.


#### Этап 2: Visual Concept (Упаковка "Мечты")
*Люкс покупают глазами. Нам нужны доказательства твоих УТП.*
1.  **AI-Design (Midjourney / Flux / DALL-E 3):**
    *   Сгенерировать рендеры: «Автомобиль Lamborghini Revuelto в кастомном футуристичном обвесе», «Вечеринка зумеров при вручении авто в неоновом стиле», «Интерфейс приложения, где AI подбирает тюнинг».
    *   Эти картинки пойдут и в бизнес-план, и в презентацию.

Для раздела «AI-дизайн кастомизации»:
> **Prompt:** "Futuristic luxury car showroom, wide shot, Gen Z aesthetics, neon purple and acid green lighting, a Lamborghini Revuelto being customized by a holographic AI interface, hyper-realistic, 8k, unreal engine 5 render --ar 16:9"


#### Этап 3: Drafting in Cursor (Сборка смыслов)
*Здесь используем твою силу — Markdown и структуры.*
1.  **Сборка БП:** Пишешь текст по структуре (разделы 1-8).
2.  **Интеграция:** Вставляешь ссылки на локальные картинки (из этапа 2) и скриншоты таблиц (из этапа 1).
3.  **Контекст:** Используй Cursor Composer, скормив ему все найденные данные, чтобы он писал фактурно, а не «водой».

Используй режим *Composer* (Cmd+I или Ctrl+I), чтобы он мог редактировать несколько файлов.
> **Prompt:** "You are an expert business consultant. Write Section 3 'Market Analysis' based on the data in `research_notes.md`. Focus on the problem of 'Boring Luxury' for Gen Z. Use professional business terminology (SAM/SOM, CAGR). Keep sentences punchy."


#### Этап 4: Presentation "Hybrid" (Презентация)
*Отказываемся от чистого LaTeX в пользу гибрида или MD-to-PPTX с ручной доработкой.*
1.  **Structure:** Генерируешь структуру слайдов и тезисы в Cursor.
2.  **Design:** Используешь Gamma.app (импорт текста) или экспорт в PPTX, но затем **вручную** накладываешь «дорогой» дизайн. Для направления «Шаг в бизнес» презентация — это 50% успеха. Она должна продавать.

Если ты фанат кода, используй **Marp** (Markdown Presentation Ecosystem) в VS Code/Cursor. Он позволяет писать слайды в MD и сразу видеть превью, но дает больше контроля над CSS, чем LaTeX.
*Но я настаиваю:* Экспортируй PDF и добавь «глянец» поверх, если Marp покажется слишком простым.


#### Этап 5: Текст для презентации (Cursor Composer/Chat)


#### Этап 6: Defense Simulator (Репетиция)
1.  **AI-Judge:** Загружаешь свой готовый текст в кэш AI и просишь его «уничтожить» твой проект каверзными вопросами.


#### 7. Паспорт проекта
Паспорт — это сухая выжимка.
> **Prompt:** "Based on the full `business_plan.md`, fill out the 'Project Passport' template strictly limiting word count per section. Extract key metrics: ROI, Paybox period, Break-even point."
