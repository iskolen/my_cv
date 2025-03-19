AUTHOR = 'Вадим Петров'
SITENAME = 'Резюме'
SITEURL = 'https://iskolen.github.io/my_cv'

PATH = 'content'
TIMEZONE = 'Europe/Moscow'
DEFAULT_LANG = 'ru'

THEME = 'resume'
CSS_FILE = 'main.css'

NAME = 'Вадим'
TAGLINE = 'Студент ПС-42'
PIC = 'profile.jpg'

EMAIL = 'iskolen@mail.ru'
PHONE = '+7 (902) 743-22-89'
GITHUB = 'iskolen'

CAREER_SUMMARY = 'Студент 4 курса программной инженерии, увлечён программированием.'

SKILLS = [
    {'title': 'Python', 'level': '20'},
    {'title': 'C++', 'level': '10'},
    {'title': 'HTML5 & CSS', 'level': '8'},
    {'title': 'React', 'level': '5'},
    {'title': 'SQL', 'level': '5'},
    {'title': 'Docker', 'level': '2'},
]

PROJECT_INTRO = 'Ниже приведены репозитории, разработанные и изученные в рамках 4 курсов университета, демонстрирующие практическое применение теоретических знаний и развитие навыков программирования.'
PROJECTS = [
    {
        'title': 'Алгоритмы и структуры данных',
        'tagline': 'Репозиторий с реализациями основных алгоритмов и структур данных, изученных в курсе, включая сортировки, деревья и графы.'
    },
    {
        'title': 'Распределённое программирование',
        'tagline': 'Репозиторий, посвящённый изучению принципов распределённых вычислений, алгоритмам распределения задач и синхронизации процессов.'
    },
    {
        'title': 'Контроль качества',
        'tagline': 'Проекты, связанные с методами обеспечения качества ПО, автоматизированным тестированием и анализом результатов тестирования.'
    },
    {
        'title': 'Параллельное программирование',
        'tagline': 'Набор примеров и проектов, демонстрирующих применение многопоточности и параллельных алгоритмов для повышения производительности.'
    },
    {
        'title': 'Объектно-ориентированное программирование',
        'tagline': 'Репозиторий с примерами и практическими заданиями по принципам ООП для создания модульного и масштабируемого ПО.'
    }
]

LANGUAGES = [
    {'name': 'Русский', 'description': 'Родной'},
    {'name': 'Английский', 'description': 'Средний'},
]

INTERESTS = ['Программирование', 'Чтение', 'Музыка']

EXPERIENCES = []

EDUCATIONS = [
    {
        'degree': 'Бакалавр программной инженерии',
        'meta': 'ПГТУ',
        'time': '2020-2025'
    },
]
