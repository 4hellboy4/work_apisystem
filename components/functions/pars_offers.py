from lxml import etree as et
from components.functions.process_link import process_link
from components.classes.json_list import JsonList, add_to_json_list

path: str = '/home/hellboy4/hellboyAcerman/temp_xml/market_affiliate-part-tovary-dlia-krasoty.xml'


def pars_file(jsons_class: JsonList) -> None:
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
                temp['categoryId_feed'] = elem.find('categoryId').text.strip()
            except:
                temp['categoryId_feed'] = 'NULL'

            try:
                temp['picture_feed'] = elem.find('picture').text.strip()
            except:
                temp['picture_feed'] = 'NULL'

            try:
                temp['price_feed'] = elem.find('price').text.strip()
            except:
                temp['price_feed'] = 'NULL'

            try:
                temp['currencyId_feed'] = elem.find('currencyId').text.strip()
            except:
                temp['currencyId_feed'] = 'NULL'

            try:
                temp['url_feed'] = elem.find('url').text.strip()
            except:
                temp['url_feed'] = 'NULL'

            try:
                temp['groupId_feed'] = elem.find('group_id').text.strip()
            except:
                temp['groupId_feed'] = 'NULL'

            try:
                temp['vendor_feed'] = elem.find('vendor').text.strip()
            except:
                temp['vendor_feed'] = 'NULL'

            try:
                temp['description_feed'] = elem.find('description').text.strip()
            except:
                temp['description_feed'] = 'NULL'

            try:
                temp['barcode_feed'] = elem.find('barcode').text.strip()
            except:
                temp['barcode_feed'] = 'NULL'

            try:
                temp['oldprice_feed'] = elem.find('oldprice').text.strip()
            except:
                temp['oldprice_feed'] = 'NULL'

            try:
                temp['param_feed'] = elem.find('param').text.strip()
            except:
                temp['param_feed'] = 'NULL'

            if temp['groupId_feed'] not in list_of_id:
                cnt += 1
                list_of_id.append(temp['groupId_feed'])
                add_to_json_list(process_link(temp['groupId_feed'], temp), jsons_class)
        if cnt == 500:
            break


# def add_to_file() -> None:
#     with open('../IDs.txt', 'w', encoding='utf-8') as file:
#         for id_temp in list_of_id:
#             file.write(f'{id_temp}\n')
