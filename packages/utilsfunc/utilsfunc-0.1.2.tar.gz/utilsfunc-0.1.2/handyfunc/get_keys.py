

def getKeysByValue(dictOfElements, valueToFind):
    """
    Get a list of keys from dictionary which has the given value
    """
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for key, val in listOfItems:
        if val == valueToFind:
            listOfKeys.append(key)
    return listOfKeys


def getKeysByValues(dictOfElements, listOfValues):
    """
    Get a list of keys from dictionary which
    has value that matches with any value in given list of values
    """
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for key, val in listOfItems:
        if val in listOfValues:
            listOfKeys.append(key)
    return listOfKeys


if __name__ == '__main__':
    dictOfWords = {
        "hello": 0.56,
        "at": 0.23,
        "test": 0.43,
        "this": 0.97,
        "here": 0.43,
        "now": 0.97,
        "another": 0.12,
        "test": 0.34,
        "is": 0.67,
        "here": 0.89
    }

    print("Original Dictionary")
    print(dictOfWords)

    # Get list of keys with value 43
    listOfKeys = getKeysByValue(dictOfWords, 43)
    print("Keys with value equal to 43")
    # Iterate over the list of keys
    for key in listOfKeys:
        print(key)

    # Get list of keys with any of the given values
    print("Keys with value equal to any one from the list [43, 97] ")
    listOfKeys = getKeysByValues(dictOfWords, [43, 97])
    # Iterate over the list of values
    for key in listOfKeys:
        print(key)

    result_sim = list(dictOfWords.values())
    result_dict = {i: str(v) for i, v in enumerate(result_sim)}

    result_sim_new = sorted(result_sim, reverse=True)
    q_index_uniq = []
    for q in result_sim_new[:5]:
        q_index_list = getKeysByValue(result_dict, str(q))
        q_index_uniq += q_index_list
        q_index_uniq = list(set(q_index_uniq))
        print(q_index_uniq)
            # result_list_new.append(lp_fullcate_txtvec[k]+(result_sim_new[q],))
