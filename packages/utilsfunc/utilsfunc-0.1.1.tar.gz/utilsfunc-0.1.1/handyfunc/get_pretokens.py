import nltk
import re


def transform_text(text):
    '''Transform text aid to split phrase from raw pharse'''
    character_map = {
        " / ": "/",
        " x ": 'x',
        " + ": '+',
        " * ": '*',
        " - ": '-',
        " - ": '-',
        " ~ ": '~',
        " & ": '&'}
    for origin, new in character_map.items():
        text = text.replace(origin, new)
    return text


def preprocess_titles(title):
    # 删除特殊字符和头尾空格
    r = '[!$@|(){}[\\]=<>_,:;?★、…【】《》^⚡☠❤•✅⭐ツ丿灬●❗✪✨✦✖✔✓⚾♪♥♛☕★☀►▲Ø✌▶]+'
    title = transform_text(title)
    title_lower = title.lower()
    return re.sub(r, '', title_lower).strip(' ').rstrip('#~+-*$')


def get_title_parse(raw):
    # 词性正则表达式
    grammar = r"""
            CP:{<CD><NN|JJ><NN|JJ>}
            DP:{<CD><NNS|NN>}
            DPP:{<IN><NNS|NN>+}
            CN:{<CD><:><CD>}
            CJJ:{<CD><''|POS><NN><NN|FW>?}
            CPOS:{<CD><''|POS|VBG>}
            CM:{<CD><''><JJ>{2}<''|POS>}
            NP:{<JJ|NN><POS|IN>?<NN>}
            PP:{<NN|NNS|NNP|NNPS>}
            """
    text_token = nltk.word_tokenize(raw)
    text_pos = nltk.pos_tag(text_token)
    rp = nltk.RegexpParser(grammar)
    return rp.parse(text_pos)


def preprocess_chunk(chunk):
    character_map = {
            " '": "'",
            " \"": "\"",
            " %": "%"}
    for origin, new in character_map.items():
            chunk = chunk.replace(origin, new)
    return chunk.rstrip(" ~*&×/-+#$").lstrip(" */~")


def preprocess_in(title_chunk_list):
    title_chunk_dict = {key: value
                        for value, key in enumerate(title_chunk_list)}
    new_title_chunk = []
    index = -1
    try:
        for key, value in title_chunk_dict.items():
            if value != index:
                if key in {'for', 'in'}:
                    new_title_chunk.append(
                        ' '.join(title_chunk_list[value: value + 2]))
                    index = value + 1
                elif key in {'or', 'and', 'of'}:
                    del(new_title_chunk[-1])
                    new_title_chunk.append(
                        ' '.join(title_chunk_list[value - 1: value + 2]))
                    index = value + 1
                else:
                    new_title_chunk.append(title_chunk_list[value])
        return new_title_chunk
    except Exception:
        return title_chunk_list


def get_chunk(title):
    title = preprocess_titles(title)
    text_parse = get_title_parse(title)
    title_chunk_list = []
    k = -1
    try:
        for i in range(len(text_parse)):

            if isinstance(text_parse[i], nltk.tree.Tree):
                strings = ''
                if i > 0:

                    if (text_parse[i - 1][0] == '#' or
                            text_parse[i - 1][0] == '$'):

                        strings = text_parse[i - 1][0]

                for j in range(len(text_parse[i])):

                    strings = strings + text_parse[i][j][0] + ' '
                title_chunk_list.append(strings)

            else:
                if len(text_parse[i][0]) > 1 and i != k:

                    title_chunk_list.append(text_parse[i][0])
                else:
                    if (text_parse[i][0] == '#' or
                            text_parse[i][0] == '$'):

                        if isinstance(text_parse[i + 1][0], tuple):
                            continue

                        else:
                            title_chunk_list.append(
                                [text_parse[i][0] + text_parse[i + 1][0]][0])

                            k = i + 1

        new_title_chunk = preprocess_in(title_chunk_list)

        return [preprocess_chunk(chunk)
                for chunk in new_title_chunk
                if len(chunk.strip(' ')) > 1 and not chunk.isdigit()]

    except Exception:
        return []


if __name__ == "__main__":
    title = "100-Pak =RESEALABLE= Plastic Wrap CD Sleeves for 10.4mm Jewel Cases!"
    print(get_chunk(title))




