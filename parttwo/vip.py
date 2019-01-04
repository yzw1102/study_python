def _dimond_vip(lv):
    print('dimond vip,welcome')
    return 'DimondVIP' + str(lv)

def _gold_vip(lv):
    print('gold vip,welcome')
    return 'GoldVIP' + str(lv)

def vip_lv_name(lv):
    if lv == 1:
        print(_gold_vip(lv))
    if lv == 2:
        print(_dimond_vip(lv))

vip_lv_name(2)
