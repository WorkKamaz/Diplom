<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Мой сайт</title>
    <style>
        /* CSS стили */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.9;
        }
        
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        
        nav {
            background-color: #34495e;
            padding: 0.5rem;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }
        
        nav ul li {
            margin: 0 1rem;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        
        nav ul li a:hover {
            background-color: #2c3e50;
        }

        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }

        .t-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Блок IM10 */
        .im10-block {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            margin: 60px 0;
        }
        
        .im10-image-col {
            width: 50%;
            padding: 0 15px;
            box-sizing: border-box;
        }
        
        .im10-content-col {
            width: 50%;
            padding: 0 15px;
            box-sizing: border-box;
        }
        
        .im10-image-wrapper {
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        
        .im10-image {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.3s ease;
        }
        
        .im10-image-wrapper:hover .im10-image {
            transform: scale(1.03);
        }
        
        .im10-content {
            padding: 30px;
        }
        
        .im10-subtitle {
            font-size: 16px;
            color: #666;
            font-weight: 500;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .im10-title {
            font-size: 32px;
            font-weight: 700;
            line-height: 1.3;
            margin-bottom: 20px;
            color: #333;
        }
        
        .im10-text {
            font-size: 18px;
            line-height: 1.6;
            color: #555;
            margin-bottom: 30px;
        }
        
        .im10-btn {
            display: inline-block;
            padding: 12px 30px;
            background-color: #4a6bff;
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: 600;
            transition: all 0.3s ease;
            border: 2px solid transparent;
        }
        
        .im10-btn:hover {
            background-color: #3a56d4;
            transform: translateY(-2px);
        }
        
        /* Адаптивность */
        @media (max-width: 768px) {
            .im10-image-col,
            .im10-content-col {
                width: 100%;
            }
            
            .im10-image-col {
                margin-bottom: 30px;
            }
            
            .im10-title {
                font-size: 26px;
            }
            
            .im10-text {
                font-size: 16px;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>TresogaStop</h1>
    </header>
    
    <nav>
        <ul>
            <li><a href="index.html">Главная</a></li>
            <li><a href="#">Упражнения</a></li>
            <li><a href="form.html">Статьи</a></li>
            <li><a href="test.html">Тесты</a></li>
        </ul>
    </nav>

    <div class="t-container">
        <div class="im10-block">
            <div class="im10-image-col">
                <div class="im10-image-wrapper">
                    <img src="C:\Users\HUAWEI\Downloads\indoor-shot-shocked-scared-frustrated-young-woman-covering-face-with-hands-her-eyes-full-terror-panic-scaled.jpg" alt="Изображение" class="im10-image">
                </div>
            </div>
            <div class="im10-content-col">
                <div class="im10-content">
                    <div class="im10-subtitle">О тревожности</div>
                    <h2 class="im10-title">Ваш результат</h2>
                    <p class="im10-text">
                        У вас довольно хороший результат, хотя могло быть и лучше. У вас присутствуют некоторые соматические признаки тревоги, но учитывая их относительную выраженность, но пока не перешли грань допустимого.
                    </p>
                    <p class="im10-text"></p>
                        Исходя из результатов у вас большая склонность к ситувтивной тревоге, а значит вы предрасположены надумывать, что любое непредвиденная ситуация обязательно выбьет у вас почву из под ног, даже если это обьяктивнно не так. Вы не можете рационально смотрети на ситуацию. Вы смотрите тольео тереч призмк эмоций и ироцианальности, которые отлично подкармливает ваша тревога.
                    </p>
                    <p class="im10-text"></p>
                        Стоит ли этого бояться? Нет конечно. Ситуативная тревога самая распостраненая. Вам достаточно просто освоить техники для того чтобы отвлекатися от совего круговорота мыслей.
                    </p>
                </div>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2025 Дипломная работа студента Качмазовай СС.</p>
    </footer>
</body>