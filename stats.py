def get_num_words(text):
    words = text.split()
    return len(words)


def kind_of_letters(text):
    dic = {}
    lower_case_text = text.lower()
    for a in lower_case_text:
        for b in a:
            dic[b] = dic.get(b,0)+1
    del dic[" "]
    del dic["\n"]
    return dic

def sorting(dic):
    pretty_dic = ''
    for k in dic:
        pretty_dic += f'{k}: {dic[k]} \n'
    return pretty_dic
