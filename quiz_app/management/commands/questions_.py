# quiz/quiz_app/management/commands/questions_.py

questions_and_answers = {
    "Какая функция в Python используется для вывода текста на экран?": [
        [
            "print()",
            "input()",
            "len()",
            "range()"
        ],
        1  # Уровень сложности
    ],
    "Какой символ используется для обозначения комментариев в Python?": [
        [
            "#",
            "&",
            "$",
            "!"
        ],
        1  # Уровень сложности
    ],
    "Какой тип данных в Python используется для хранения целых чисел?": [
        [
            "int",
            "str",
            "float",
            "list"
        ],
        1  # Уровень сложности
    ],
    "Как создать пустой список в Python?": [
        [
            "my_list = []",
            "my_list = {}",
            "my_list = [1, 2, 3]",
            "my_list = (1, 2, 3)"
        ],
        1  # Уровень сложности
    ],
    "Какой оператор используется для выполнения целочисленного деления в Python?": [
        [
            "//",
            "/",
            "%",
            "**"
        ],
        1  # Уровень сложности
    ],
    "Какой принцип SOLID гласит, что классы должны быть открыты для расширения, но закрыты для модификации?": [
        [
            "Open/Closed Principle.",
            "Single Responsibility Principle.",
            "Liskov Substitution Principle.",
            "Dependency Inversion Principle."
        ],
        2  # Уровень сложности
    ],
    "Что означает принцип Interface Segregation в SOLID?": [
        [
            "Клиенты не должны быть вынуждены реализовывать интерфейсы, которыми они не пользуются.",
            "Все интерфейсы должны быть универсальными и подходить для всех классов.",
            "Классы могут иметь только один интерфейс.",
            "Интерфейсы должны быть закрыты для расширения."
        ],
        2  # Уровень сложности
    ],
    "Что означает принцип KISS?": [
        [
            "Система или дизайн должны оставаться как можно проще.",
            "Каждый класс должен иметь только одну функцию.",
            "Сохранять зависимости между классами на минимальном уровне.",
            "Избегать использования наследования."
        ],
        2  # Уровень сложности
    ],
    "Какой принцип утверждает, что более высокоуровневые модули не должны зависеть от низкоуровневых модулей?": [
        [
            "Dependency Inversion Principle.",
            "Single Responsibility Principle.",
            "Open/Closed Principle.",
            "Liskov Substitution Principle."
        ],
        2  # Уровень сложности
    ],
    "Какие два принципа SOLID наиболее сосредоточены на управлении зависимостями?": [
        [
            "Dependency Inversion Principle и Interface Segregation Principle.",
            "Single Responsibility Principle и Open/Closed Principle.",
            "Liskov Substitution Principle и Single Responsibility Principle.",
            "Open/Closed Principle и Liskov Substitution Principle."
        ],
        2  # Уровень сложности
    ],
    "Что означает принцип Single Responsibility в SOLID?": [
        [
            "Класс должен иметь только одну причину для изменения.",
            "Класс должен реализовывать все возможные функции.",
            "Класс должен зависеть от других классов.",
            "Класс должен быть написан в одной строке кода."
        ],
        3  # Уровень сложности
    ],
    "Какой из этих принципов наиболее акцентирует внимание на разделении интерфейса?": [
        [
            "Interface Segregation Principle.",
            "Dependency Inversion Principle.",
            "Single Responsibility Principle.",
            "Open/Closed Principle."
        ],
        3  # Уровень сложности
    ],
    "Какое из следующих утверждений лучше всего описывает принцип KISS?": [
        [
            "Сложные системы работают лучше, когда их держат как можно проще.",
            "Каждый класс должен стремиться к выполнению только одной задачи.",
            "Все зависимости в системе должны быть явными и легко трассируемыми.",
            "Интерфейсы должны быть разделены так, чтобы классы не зависели от методов, которые они не используют."
        ],
        3  # Уровень сложности
    ],
    "В чем основное отличие между принципами KISS и DRY?": [
        [
            "KISS фокусируется на простоте, а DRY на избежании дублирования.",
            "KISS касается управления проектом, а DRY - процесса разработки.",
            "KISS направлен на клиентскую часть, а DRY - на серверную.",
            "KISS относится к интерфейсам, а DRY к реализации."
        ],
        3  # Уровень сложности
    ],
    "Какой из этих принципов наиболее подчеркивает важность создания модульного кода с четко определенными абстракциями?": [
        [
            "Dependency Inversion Principle.",
            "Liskov Substitution Principle.",
            "Interface Segregation Principle.",
            "Single Responsibility Principle."
        ],
        3  # Уровень сложности
    ],
    "Какой принцип SOLID утверждает, что производные классы должны быть способны заменять базовые классы?": [
        [
            "Liskov Substitution Principle.",
            "Interface Segregation Principle.",
            "Dependency Inversion Principle.",
            "Open/Closed Principle."
        ],
        4  # Уровень сложности
    ],
    "Что означает принцип DRY?": [
        [
            "Каждая часть знаний в системе должна иметь единственное, недвусмысленное и авторитетное представление.",
            "Повторять логику программы как можно чаще.",
            "Разделять код на максимальное количество мелких частей.",
            "Использовать глобальные переменные для упрощения доступа к данным."
        ],
        4  # Уровень сложности
    ],
    "Как принцип Single Responsibility влияет на тестирование кода?": [
        [
            "Упрощает написание тестов, так как классы с одной ответственностью легче тестировать.",
            "Затрудняет тестирование, так как требует написания большего количества тестов.",
            "Не оказывает никакого влияния на процесс тестирования.",
            "Делает написание тестов необязательным."
        ],
        4  # Уровень сложности
    ],
    "Какой из следующих примеров лучше всего иллюстрирует принцип Open/Closed?": [
        [
            "Расширение функциональности класса через наследование без изменения исходного класса.",
            "Добавление новых методов непосредственно в класс.",
            "Изменение существующих методов класса для добавления новой функциональности.",
            "Полное переписывание класса для внесения изменений."
        ],
        4  # Уровень сложности
    ],
    "Почему следование принципу Single Responsibility важно для тестирования?": [
        [
            "Упрощает написание тестов, так как изменения в одной части системы меньше влияют на другие части.",
            "Позволяет использовать больше моков и заглушек в тестах.",
            "Уменьшает необходимость в интеграционном тестировании.",
            "Делает тесты более сложными и тем самым улучшает качество кода."
        ],
        4  # Уровень сложности
    ],
    "Что такое Dependency Inversion Principle в SOLID?": [
        [
            "Модули высокого уровня не должны зависеть от модулей низкого уровня. Оба типа модулей должны зависеть от абстракций.",
            "Зависимости внутри системы должны быть строго фиксированы и не изменяемы.",
            "Все зависимости должны быть напрямую встроены в код.",
            "Абстракции не должны зависеть от деталей."
        ],
        5  # Уровень сложности
    ],
    "Какой из следующих примеров наиболее точно отражает принцип Liskov Substitution?": [
        [
            "Функции, которые используют базовый тип, должны уметь использовать подтипы базового типа, не зная об этом.",
            "Подклассы не должны требовать от пользователей знаний о различиях между ними и базовыми классами.",
            "Подклассы должны напрямую заменять базовые классы.",
            "Базовый класс должен содержать все методы, которые могут потребоваться его подклассам."
        ],
        5  # Уровень сложности
    ],
    "Какой принцип помогает предотвратить 'кода-спагетти' за счет ограничения распространения изменений?": [
        [
            "Open/Closed Principle.",
            "Liskov Substitution Principle.",
            "Interface Segregation Principle.",
            "Single Responsibility Principle."
        ],
        5  # Уровень сложности
    ],
    "Чем полезен принцип DRY в процессе разработки программного обеспечения?": [
        [
            "Сокращает дублирование кода, упрощая поддержку и модификацию.",
            "Гарантирует, что классы легко расширяемы новыми функциями.",
            "Убеждает разработчиков писать код, который легко переиспользуется в других частях приложения.",
            "Помогает определить, какие классы должны быть абстрактными, а какие - конкретными."
        ],
        5  # Уровень сложности
    ],
    "Как применение SOLID принципов влияет на масштабируемость приложения?": [
        [
            "Облегчает добавление новой функциональности и адаптацию к изменяющимся требованиям без изменения существующего кода.",
            "Требует от разработчиков использовать более сложные алгоритмы для выполнения задач.",
            "Приводит к увеличению количества кода, который необходимо поддерживать.",
            "Ограничивает возможности для использования наследования и полиморфизма."
        ],
        5  # Уровень сложности
    ], 
}

text_questions_and_answers = {
    "Как называется переменная, которая может использоваться везде в вашем приложении?": [
        "глобальная",
        1  # Уровень сложности
    ],
    "Как называется метод, который автоматически вызывается при создании объекта класса?": [
        "конструктор",
        2  # Уровень сложности
    ],
    "Какое ключевое слово используется для определения базового класса в Python?": [
        "super",
        3  # Уровень сложности
    ],
    "Какое ключевое слово в Python используется для определения анонимной функции?": [
        "lambda",
        4  # Уровень сложности
    ],
    "Какой метод HTTP используется для получения данных с сервера?": [
        "GET",
        5  # Уровень сложности
    ]
}
