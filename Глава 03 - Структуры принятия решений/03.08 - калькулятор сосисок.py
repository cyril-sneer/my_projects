SAUSAGES_IN_PACK = 10
BUNS_IN_PACK = 8

while True:
    people = int(input('Введите количество людей (0 - выход):\t'))
    if people == 0: break
    hotdogs_pp = int(input('Количество хот-догов на рыло:\t\t\t'))
    hotdogs_total = people * hotdogs_pp

    packs_of_sausages = hotdogs_total / SAUSAGES_IN_PACK
    if packs_of_sausages % 1 !=0:
        packs_of_sausages = packs_of_sausages // 1 + 1

    packs_of_cookies = hotdogs_total / BUNS_IN_PACK
    if packs_of_cookies % 1 != 0:
        packs_of_cookies = packs_of_cookies // 1 + 1

    print(f'Мин кол-во пакетов сосисек:\t{packs_of_sausages:.0f}')
    print(f'Останется сосисек:\t\t\t{packs_of_sausages * SAUSAGES_IN_PACK - hotdogs_total:.0f}')
    print(f'Мин кол-во пакетов булочек:\t{packs_of_cookies:.0f}')
    print(f'Останется булочек:\t\t\t{packs_of_cookies * BUNS_IN_PACK - hotdogs_total:.0f}')

