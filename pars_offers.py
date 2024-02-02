from lxml import etree as et

path: str = '/home/hellboy4/hellboyAcerman/temp_xml/market_affiliate-part-tovary-dlia-krasoty.xml'

list_of_id: list[str] = []

API_KEY: str = '0c8bd89c2e517164204ceb1dfee65289a659b4bcffee'


def pars_file() -> None:
    cnt = 0
    for event, elem in et.iterparse(path, events=('end',), tag=['offer'], recover=True):
        if event == 'end' and elem.tag == 'offer':
            group_id: str = elem.find('group_id').text.strip()
            # sci_id: str = elem.get('id')
            link: str = (f'http://market.apisystem.name/models/{group_id}/specification?&format=json&api_key={API_KEY}')
            list_of_id.append(link)
            cnt += 1
        if cnt == 500:
            break


def add_to_file() -> None:
    with open('data/IDs.txt', 'w', encoding='utf-8') as file:
        for id_temp in list_of_id:
            file.write(f'{id_temp}\n')


def main() -> None:
    pars_file()
    print('parsed the file')
    add_to_file()
    print('done')


if __name__ == '__main__':
    main()
