from colorama import Fore, Style, init

# Эта библиотека нужна для изменения цвета текста в терминале

init()  

print(Fore.RED + "Это красный текст")
print(Fore.GREEN + "Это зеленый текст")
print(Fore.YELLOW + "Это желтый текст")

print(Style.RESET_ALL + "Обычный текст")