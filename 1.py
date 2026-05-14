<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>Сахар и здоровье: влияние на организм | Доказательная информация</title>
    <meta name="description" content="Узнайте, как сахар воздействует на мозг, сердце, печень и вес. Научные факты, скрытые источники и советы по снижению потребления.">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: system-ui, 'Segoe UI', 'Inter', 'Roboto', 'Helvetica Neue', sans-serif;
            background-color: #fefcf5;
            color: #1e2a2e;
            line-height: 1.5;
            scroll-behavior: smooth;
        }

        /* Typography */
        h1, h2, h3 {
            font-weight: 600;
            letter-spacing: -0.02em;
        }

        h2 {
            font-size: 2rem;
            margin-bottom: 1.5rem;
            position: relative;
            display: inline-block;
        }
        h2:after {
            content: '';
            position: absolute;
            bottom: -8px;
            left: 0;
            width: 60px;
            height: 3px;
            background: #e67e22;
            border-radius: 2px;
        }

        /* Layout */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 24px;
        }

        section {
            padding: 4rem 0;
            border-bottom: 1px solid #f0e4d0;
        }

        section:last-child {
            border-bottom: none;
        }

        /* Hero */
        .hero {
            background: linear-gradient(135deg, #fff4e6 0%, #ffe6d5 100%);
            padding: 4rem 0 5rem 0;
            border-bottom: 1px solid #f0e0cc;
        }
        .hero-content {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 2rem;
            justify-content: space-between;
        }
        .hero-text {
            flex: 1.2;
        }
        .hero-text h1 {
            font-size: 3.2rem;
            line-height: 1.2;
            margin-bottom: 1rem;
            color: #b45f2b;
        }
        .hero-text p {
            font-size: 1.2rem;
            color: #3a3a3a;
            max-width: 90%;
            margin-bottom: 1.8rem;
        }
        .hero-badge {
            background-color: #e67e22;
            color: white;
            display: inline-block;
            padding: 0.25rem 1rem;
            border-radius: 40px;
            font-size: 0.8rem;
            font-weight: 500;
            margin-bottom: 1rem;
        }
        .hero-image {
            flex: 0.8;
            background: #f5e2d0;
            border-radius: 36px;
            padding: 1rem;
            text-align: center;
            box-shadow: 0 20px 30px -10px rgba(0,0,0,0.05);
        }
        .hero-image svg {
            max-width: 100%;
            height: auto;
        }

        /* Cards grid */
        .grid-2, .grid-3 {
            display: grid;
            gap: 2rem;
            margin-top: 1rem;
        }
        .grid-2 {
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        }
        .grid-3 {
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        }
        .card {
            background: white;
            border-radius: 1.5rem;
            padding: 1.6rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.03), 0 2px 6px rgba(0,0,0,0.05);
            transition: all 0.2s ease;
            border: 1px solid #f3e5d6;
        }
        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -12px rgba(0,0,0,0.1);
            border-color: #eedcc9;
        }
        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        .card h3 {
            font-size: 1.4rem;
            margin-bottom: 0.75rem;
            color: #b85c1a;
        }
        .stat-number {
            font-size: 2.2rem;
            font-weight: 800;
            color: #e67e22;
            line-height: 1;
            margin-right: 0.3rem;
        }
        .stat-unit {
            font-size: 1rem;
            font-weight: normal;
            color: #5a6268;
        }

        /* highlight facts */
        .fact-badge {
            background: #f8ede3;
            border-left: 4px solid #e67e22;
            padding: 1rem 1.5rem;
            border-radius: 1rem;
            margin: 1.5rem 0;
        }

        /* hidden sugar list */
        .sugar-list {
            background: #ffffffea;
            border-radius: 1.5rem;
            padding: 1rem 0;
        }
        .sugar-item {
            display: flex;
            align-items: baseline;
            gap: 0.8rem;
            padding: 0.8rem 1rem;
            border-bottom: 1px solid #f1e2d2;
        }
        .sugar-item strong {
            min-width: 130px;
            color: #c95c0f;
        }

        .btn {
            display: inline-block;
            background: #e67e22;
            color: white;
            font-weight: 600;
            padding: 0.8rem 1.6rem;
            border-radius: 60px;
            text-decoration: none;
            transition: background 0.2s;
            border: none;
            cursor: pointer;
        }
        .btn-outline {
            background: transparent;
            border: 1px solid #e67e22;
            color: #e67e22;
        }
        .btn-outline:hover {
            background: #e67e22;
            color: white;
        }
        .btn:hover {
            background: #cf711f;
        }

        footer {
            background: #1e2a2e;
            color: #e6e2da;
            padding: 2rem 0;
            text-align: center;
            font-size: 0.85rem;
        }
        footer a {
            color: #f0bc8c;
            text-decoration: none;
        }

        @media (max-width: 760px) {
            .hero-text h1 {
                font-size: 2.3rem;
            }
            .hero-text p {
                max-width: 100%;
            }
            .hero-content {
                flex-direction: column;
            }
            section {
                padding: 2.5rem 0;
            }
            h2 {
                font-size: 1.8rem;
            }
            .sugar-item {
                flex-direction: column;
                gap: 0.3rem;
            }
            .sugar-item strong {
                min-width: auto;
            }
        }
    </style>
</head>
<body>

<main>
    <!-- Герой-секция -->
    <div class="hero">
        <div class="container hero-content">
            <div class="hero-text">
                <div class="hero-badge">⚡ Научные данные 2025</div>
                <h1>Сахар: сладкая зависимость или скрытая угроза?</h1>
                <p>Как добавленный сахар влияет на мозг, печень, сердце и обмен веществ. Разбираем факты, которые меняют взгляд на сладкое.</p>
                <a href="#facts" class="btn">Узнать главные риски →</a>
            </div>
            <div class="hero-image">
                <svg width="280" height="220" viewBox="0 0 300 220" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M150 30 L180 70 L210 60 L200 100 L230 130 L190 140 L170 180 L150 150 L130 180 L110 140 L70 130 L100 100 L90 60 L120 70 L150 30Z" fill="#F9CFA3" stroke="#E67E22" stroke-width="2"/>
                    <circle cx="150" cy="105" r="15" fill="#FFF2E0" stroke="#E67E22" stroke-width="1.5"/>
                    <path d="M135 100 L145 100 M155 100 L165 100" stroke="#A55117" stroke-width="2" stroke-linecap="round"/>
                    <path d="M140 112 L150 118 L160 112" stroke="#A55117" stroke-width="1.8" fill="none"/>
                    <text x="110" y="40" font-size="12" fill="#BF6F2C">🍬</text>
                    <text x="220" y="85" font-size="16" fill="#BF6F2C">⚠️</text>
                    <text x="60" y="150" font-size="14" fill="#BF6F2C">🧠</text>
                </svg>
            </div>
        </div>
    </div>

    <div class="container">
        <!-- Быстрые факты (статистика) -->
        <section id="facts">
            <h2>Сахар в цифрах</h2>
            <div class="grid-3">
                <div class="card">
                    <div class="card-icon">🍬</div>
                    <div><span class="stat-number">22</span><span class="stat-unit"> чайных ложек</span></div>
                    <p>среднестатистический взрослый потребляет добавленного сахара ежедневно — в 3 раза выше нормы ВОЗ (рекомендовано < 6 ч.л./день).</p>
                </div>
                <div class="card">
                    <div class="card-icon">❤️</div>
                    <div><span class="stat-number">38%</span><span class="stat-unit"> выше риск</span></div>
                    <p>развития сердечно-сосудистых заболеваний при диете с высоким содержанием добавленных сахаров (>20% калорий).</p>
                </div>
                <div class="card">
                    <div class="card-icon">🧠</div>
                    <div><span class="stat-number">2x</span><span class="stat-unit"> риск депрессии</span></div>
                    <p>Исследования показывают: высокое потребление сахара коррелирует с повышением риска депрессивных расстройств.</p>
                </div>
            </div>
            <div class="fact-badge">
                📌 ВОЗ рекомендует ограничить добавленный сахар до <strong>менее 10%</strong> от суточной калорийности, а для пользы — до <strong>5%</strong> (~25 граммов или 6 чайных ложек).
            </div>
        </section>

        <!-- Механизм воздействия (основные органы) -->
        <section>
            <h2>Как сахар влияет на организм</h2>
            <div class="grid-2">
                <div class="card">
                    <h3>🧠 Мозг и дофаминовая зависимость</h3>
                    <p>Сахар активирует центр вознаграждения в мозге, выбрасывая дофамин — подобно некоторым наркотическим веществам. Со временем рецепторы притупляются, и требуется больше сладкого для того же удовольствия. Возникает настоящая пищевая зависимость, тяга к сладкому и синдром отмены.</p>
                </div>
                <div class="card">
                    <h3>🫀 Сердце и сосуды</h3>
                    <p>Избыток фруктозы стимулирует синтез триглицеридов и повышает уровень "плохого" холестерина (ЛПНП). Повышается артериальное давление, риск атеросклероза, инфарктов и инсультов. Газированные напитки особенно опасны из-за быстрого всасывания.</p>
                </div>
                <div class="card">
                    <h3>🫁 Печень и жировая болезнь</h3>
                    <p>Избыточная фруктоза метаболизируется исключительно в печени, превращаясь в жир. Это главная причина неалкогольной жировой болезни печени (НАЖБП), которая затрагивает до 25% взрослых в мире и не связана с алкоголем.</p>
                </div>
                <div class="card">
                    <h3>⚖️ Ожирение и метаболический синдром</h3>
                    <p>Сахар калориен, но не насыщает. Жидкие калории (соки, кола) не вызывают чувства сытости, провоцируя переедание. Хроническое потребление ведет к инсулинорезистентности и диабету 2 типа.</p>
                </div>
            </div>
        </section>

        <!-- Скрытые источники сахара (самое шокирующее) -->
        <section>
            <h2>Где прячется сахар? ⚠️</h2>
            <p style="margin-bottom: 1.5rem;">Добавленный сахар есть не только в десертах. Проверьте эти продукты — на этикетках они скрываются за 50+ названиями.</p>
            <div class="sugar-list">
                <div class="sugar-item"><strong>🍞 Белый хлеб / булки</strong> — до 4-6 г сахара на 2 кусочка</div>
                <div class="sugar-item"><strong>🥫 Томатные соусы и кетчуп</strong> — 1 ст. ложка = ~1 ч.л. сахара</div>
                <div class="sugar-item"><strong>🥣 Гранола и "полезные" батончики</strong> — до 15 г на порцию</div>
                <div class="sugar-item"><strong>🥤 Йогурты с фруктовыми добавками</strong> — 17-20 г на 150 г</div>
                <div class="sugar-item"><strong>🌾 Растворимые каши и мюсли</strong> — до 12 г сахара</div>
                <div class="sugar-item"><strong>🍔 Фастфуд (бургеры, маринады)</strong> — даже несладкие блюда содержат сахар для вкуса</div>
                <div class="sugar-item"><strong>💊 Скрытые имена: сироп агавы, декстроза, мальтодекстрин, тростниковый сок, фруктоза, концентраты...</strong></div>
            </div>
            <div class="fact-badge" style="margin-top: 1.8rem;">
                🔍 Совет: Читайте этикетки. Если сахар (или его "псевдонимы") в первых трех ингредиентах — лучше отказаться.
            </div>
        </section>

        <!-- Научная связь с хроническими болезнями -->
        <section>
            <h2>Сахар и хронические заболевания</h2>
            <div class="grid-2">
                <div class="card">
                    <h3>🩸 Диабет 2 типа</h3>
                    <p>Постоянно высокий уровень глюкозы перегружает поджелудочную железу, инсулин перестает работать эффективно. Риск растет даже у людей без ожирения — так называемый "тощий диабет" из-за сахарной нагрузки.</p>
                </div>
                <div class="card">
                    <h3>🦷 Кариес и здоровье полости рта</h3>
                    <p>Бактерии во рту питаются сахаром и вырабатывают кислоту, разрушающую эмаль. Более 2 млрд человек страдают от кариеса, главный провокатор — частое употребление сладких напитков и закусок.</p>
                </div>
                <div class="card">
                    <h3>🧠 Когнитивные нарушения</h3>
                    <p>Хронически высокий сахар в крови связан с атрофией гиппокампа (центр памяти), ускоряя когнитивное старение и увеличивая риск болезни Альцгеймера ("диабет 3 типа").</p>
                </div>
                <div class="card">
                    <h3>👨‍🦰 Акне и воспаления кожи</h3>
                    <p>Сахар повышает уровень IGF-1 и андрогенов, стимулируя выработку кожного сала и закупорку пор. Диета с высоким гликемическим индексом — триггер акне у подростков и взрослых.</p>
                </div>
            </div>
        </section>

        <!-- Как сократить сахар - практические шаги -->
        <section>
            <h2>Как снизить потребление сахара: руководство без стресса</h2>
            <div class="grid-2" style="margin-top: 1rem;">
                <div>
                    <ul style="list-style-type: none; padding-left: 0;">
                        <li style="margin-bottom: 1rem;">✔️ <strong>Постепенно уменьшайте количество</strong> — резкий отказ может вызвать тягу; снижайте сахар в чае/кофе на 1/4 ложки каждые 3 дня.</li>
                        <li style="margin-bottom: 1rem;">✔️ <strong>Замените сладкие напитки</strong> на воду с мятой, лимоном, имбирем или несладкий травяной чай. Газировки — главный враг.</li>
                        <li style="margin-bottom: 1rem;">✔️ <strong>Выбирайте цельные фрукты</strong> вместо соков и смузи: клетчатка замедляет усвоение фруктозы.</li>
                        <li style="margin-bottom: 1rem;">✔️ <strong>Готовьте сами</strong> — соусы, заправки, десерты на основе фиников, бананов и без белого сахара.</li>
                        <li style="margin-bottom: 1rem;">✔️ <strong>Белковая закуска</strong> при тяге к сладкому (орехи, йогурт без добавок) стабилизирует сахар крови.</li>
                    </ul>
                </div>
                <div class="card" style="background: #fff7ef;">
                    <h3 style="margin-top: 0;">📊 Примерный дневной лимит</h3>
                    <p>Для взрослого при норме 2000 ккал: <strong>не более 25-30 г добавленного сахара</strong> (~6 чайных ложек). Одна банка колы (330 мл) содержит ≈ 35 г — уже превышение!</p>
                    <hr style="margin: 1rem 0; border-color: #eedbc9;">
                    <div style="font-size: 0.9rem;">🍏 Замените сладкий перекус на горсть миндаля, яблоко или ложку натурального арахисового масла — через 2 недели рецепторы привыкнут к естественному вкусу.</div>
                </div>
            </div>
            <div style="text-align: center; margin-top: 2rem;">
                <a href="#" class="btn btn-outline" style="background: white;" onclick="alert('Начните с малого: замените один сладкий напиток водой сегодня. Спасибо, что заботитесь о здоровье! 💚'); return false;">📘 Получить чек-лист на день (простой старт)</a>
            </div>
        </section>

        <!-- Мифы vs реальность -->
        <section>
            <h2>Мифы о сахаре: развенчиваем</h2>
            <div class="grid-2">
                <div class="card">
                    <h3>❌ «Коричневый сахар полезнее белого»</h3>
                    <p>По химическому составу и влиянию на метаболизм коричневый сахар почти идентичен белому — это тот же сахарозный песок с примесью патоки. Калорийность и риски те же.</p>
                </div>
                <div class="card">
                    <h3>❌ «Мед — здоровая альтернатива, можно без ограничений»</h3>
                    <p>Мед содержит антиоксиданты, но это все еще концентрированный сахар (фруктоза+глюкоза). Переизбыток меда также ведет к ожирению и кариесу. Норма — не более 1-2 ч.л. в день.</p>
                </div>
                <div class="card">
                    <h3>❌ «Фруктоза безопасна для диабетиков»</h3>
                    <p>Избыток фруктозы нагружает печень сильнее глюкозы, усугубляя инсулинорезистентность. Сиропы и "диабетические" сладости на фруктозе не рекомендуются.</p>
                </div>
                <div class="card">
                    <h3>✅ «Умеренность работает»</h3>
                    <p>Истина: полностью исключать сахар не нужно. Позволяйте себе десерт после полноценного приема пищи, но сократите скрытый сахар в повседневных продуктах.</p>
                </div>
            </div>
        </section>

        <!-- Вдохновение: истории успеха / вывод -->
        <section>
            <div style="background: #e9f0e6; border-radius: 2rem; padding: 2.5rem 2rem; text-align: center; border: 1px solid #cfdac5;">
                <span style="font-size: 3rem;">🌿</span>
                <h2 style="color: #2c5f2d; margin-top: 0.5rem;">Свобода от сахарной зависимости реальна</h2>
                <p style="max-width: 700px; margin: 1rem auto;">Многие люди замечают улучшение энергии, ясность ума и нормализацию веса уже через 2-3 недели снижения добавленного сахара. Слушайте свой организм — он отблагодарит вас здоровьем.</p>
                <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-top: 1.5rem;">
                    <span style="background: #fff; border-radius: 40px; padding: 0.3rem 1rem; font-size: 0.9rem;">✨ Уходит усталость после еды</span>
                    <span style="background: #fff; border-radius: 40px; padding: 0.3rem 1rem; font-size: 0.9rem;">✨ Меньше тяги к сладкому</span>
                    <span style="background: #fff; border-radius: 40px; padding: 0.3rem 1rem; font-size: 0.9rem;">✨ Кожа становится чище</span>
                </div>
            </div>
        </section>
    </div>

    <footer>
        <div class="container">
            <p>© 2025 — Влияние сахара на здоровье. Информационно-образовательный проект на основе рекомендаций ВОЗ, данных Гарвардской школы общественного здоровья и мета-анализов.</p>
            <p style="margin-top: 0.6rem;">Этот сайт не является медицинской консультацией. При проблемах со здоровьем обращайтесь к врачу.<br>
            <a href="#">Политика осознанного потребления</a></p>
        </div>
    </footer>
</main>

<!-- Дополнительный скрипт для плавного перехода по ссылке, и интерактива -->
<script>
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
</script>
</body>
</html>