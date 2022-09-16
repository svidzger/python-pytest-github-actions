from http_request import get_json_data


def user_input():
    postitoimipaikka = input('Kirjoita postitoimipaikka: ')
    return postitoimipaikka


def smartpost_problem(smartpost: str):
    if ' ' in smartpost:
        return smartpost.replace(' ', '')
    else:
        return smartpost.replace('SMARTPOST', 'SMART POST')


def main(postitoimipaikka: str):
    listofkeys = []
    data = get_json_data()
    postitoimipaikka = postitoimipaikka.upper()
    smartpost_list = ['SMARTPOST', 'SMART POST']

    for key, value in data.items():
        if value == postitoimipaikka:
            listofkeys.append(key)
        if value in smartpost_list:
            if value == smartpost_problem(postitoimipaikka):
                listofkeys.append(key)

    listofkeys.sort()

    if listofkeys and len(listofkeys) >= 1:
        postinumerot = ", ".join(listofkeys)
        return postinumerot

    return False


def print_result(postinumerot: str):
    if postinumerot:
        print(f'Postinumerot: {postinumerot}')
    else:
        print('Postitoimipaikka on virhellinen!')


if __name__ == '__main__':
    postitoimipaikka = user_input()
    postinumerot = main(postitoimipaikka)
    print_result(postinumerot)
