def csv_maker(post):
    dump_id = post['id']
    created = post['created']
    cit_1 = post['cit_1']
    cit_2 = post['cit_2']
    cit_3 = post['cit_3']
    cit_4 = post['cit_4']
    cit_5 = post['cit_5']
    temp_1 = post['temp_1']
    temp_2 = post['temp_2']
    temp_3 = post['temp_3']
    temp_4 = post['temp_4']
    temp_5 = post['temp_5']
    f_l_1 = post['f_l_1']
    f_l_2 = post['f_l_2']
    f_l_3 = post['f_l_3']
    f_l_4 = post['f_l_4']
    f_l_5 = post['f_l_5']
    con_1 = post['con_1']
    con_2 = post['con_2']
    con_3 = post['con_3']
    con_4 = post['con_4']
    con_5 = post['con_5']

    return f'Created: {created}, Dump #{dump_id}\n_City_, _t ℃_, _Feel like ℃_, _Condition_\n' \
           f'{cit_1},{temp_1},{f_l_1},{con_1}\n' \
           f'{cit_2},{temp_2},{f_l_2},{con_2}\n' \
           f'{cit_3},{temp_3},{f_l_3},{con_3}\n' \
           f'{cit_4},{temp_4},{f_l_4},{con_4}\n' \
           f'{cit_5},{temp_5},{f_l_5},{con_5}'
