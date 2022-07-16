#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# TODO: Общие:
#  1) пройдись black или аналогичным и посмотри, где не так по отступам
#  2) Раздели по папочкам drf штуки
#  3) Создай README (не пустой)
#  4) Прилепи сюда нарисованную схему ДБ
#  5) Почисти не нужные пустые файлы
#  6) Я не очень уверен, что в chat нам нужны формы
