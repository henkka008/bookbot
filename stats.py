def get_num_words(text):
    words = text.split()
    return len(words)


def kind_of_letters(text):
    dic = {}
    lower_case_text = text.lower()
    for a in lower_case_text:
        for b in a:
            dic[b] = dic.get(b,0)+1
    return dic
