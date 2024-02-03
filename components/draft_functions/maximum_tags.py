from lxml import etree as et


path: str = '/home/hellboy4/hellboyAcerman/temp_xml/market_affiliate-part-tovary-dlia-krasoty.xml'


def pars_file() -> None:
    cnt = -1
    list_of_id = []
    for event, elem in et.iterparse(path, events=('end',), tag=['offer'], recover=True):
        if event == 'end' and elem.tag == 'offer':
            child_tags = list(elem)

            for item in child_tags:
                if item.tag not in list_of_id:
                    list_of_id.append(item.tag)

    for item in list_of_id:
        print(item)

pars_file()