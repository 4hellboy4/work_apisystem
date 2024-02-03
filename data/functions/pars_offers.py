from lxml import etree as et

path: str = '/home/hellboy4/hellboyAcerman/temp_xml/market_affiliate-part-tovary-dlia-krasoty.xml'

API_KEY: str = '0c8bd89c2e517164204ceb1dfee65289a659b4bcffee'


def pars_file() -> None:
    cnt = 0
    list_of_id: list[str] = []
    for event, elem in et.iterparse(path, events=('end',), tag=['offer'], recover=True):
        if event == 'end' and elem.tag == 'offer':
            temp = {}

            try:
                temp['name_feed'] = elem.find('name').text.strip()
            except:
                temp['name_feed'] = 'NULL'

            try:
                temp['category_id_feed'] = elem.find('categoryId').text.strip()
            except:
                temp['category_id_feed'] = 'NULL'

            try:
                temp['picture_feed'] = elem.find('picture').text.strip()
            except:
                temp['picture_feed'] = 'NULL'

            try:
                temp['picture_feed'] = elem.find('picture').text.strip()
            except:
                temp['picture_feed'] = 'NULL'




            group_id: str = elem.find('group_id').text.strip()
            # sci_id: str = elem.get('id')
            if group_id not in group_id:
                link: str = (f'http://market.apisystem.name/models/{group_id}/specification?&format=json&api_key={API_KEY}')

            cnt += 1
        if cnt == 500:
            break


def add_to_file() -> None:
    with open('../IDs.txt', 'w', encoding='utf-8') as file:
        for id_temp in list_of_id:
            file.write(f'{id_temp}\n')
