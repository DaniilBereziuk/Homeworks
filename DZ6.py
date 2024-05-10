from colorama import Fore, Back, Style

print(f'Function Fore do TEXT with diffrent colors like {Fore.RED + 'red text'}{Fore.RESET + ' this or'} {Fore.BLUE + 'blue text'}{Fore.RESET + ' this'}')
print(f'Function Back do BACK TEXT with diffrent colors like {Back.YELLOW + 'yellow back'}{Back.RESET + ' this or'} {Back.WHITE + 'white back'}{Back.RESET + ' this'}')
print(f'Function Style do STYLE OF TEXT with diffrent size like {Style.DIM + "'small text'"} this or {Style.BRIGHT + "'BIG text'"} this')

print(Style.RESET_ALL)

print('Fore have: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.')
print('Back have: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.')
print('Style have: DIM, NORMAL, BRIGHT, RESET_ALL.')

print(Style.RESET_ALL)