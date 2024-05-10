#!/usr/bin/env python

def get_best_word(points:tuple[int, ...] , words:list[str]) -> int:
    best_word:str = ""
    highest_score:int = 0

    for word in words:
        if len(best_word) == 0:
            best_word = word
            highest_score = get_word_score(word, points)
            continue
        
        word_score = get_word_score(word, points)
        if word_score > highest_score: 
            best_word = word
            highest_score = word_score
        elif word_score == highest_score:
            if len(word) < len(best_word):
                best_word = word

    return words.index(best_word)


def get_word_score(word:str, points:tuple[int, ...]) -> int:
    score:int = 0

    for x in enumerate(word):
        index = get_alphabet_index(x[1])
        score += points[index]

    return score


def get_alphabet_index(alphabet:str) -> int:
    index:int = ord(alphabet.lower()) - 97
    return index


if __name__ == "__main__":
    points = (1,3,3,2,1,4,2,4,1,8,10,1,2,1,1,3,8,1,1,1,1,4,10,10,10,10)

    assert get_best_word(points, ["WHO","IS","THE","BEST","OF","US"]) == 0
    assert get_best_word(points, ["AABCDEF", "WHO","IS","THE","BEST","OF","US"]) == 1
    assert get_best_word(points, ["NOQ","TXAY","S","OM","ESFT","CJUKQ","QL","QO","ASTK","Y"]) == 5
    assert get_best_word(points, ["N","AO","TQGZW","P","OBTP","CLWXB","Y","JQGFJ","Q","RP","OC","MRQCZ","ZWN","ZRT","OIRYH","GWPMSZP","LQRYUKQ","LBM","LFEI","VHUX","RTALLIC","JEMUPS","XUW","X","ZLXFMWS","LFAGR","HJ","RTUAI","JRBNG","ZUYSC","CIEYV","FUY","B","EJS","CINBTQS","JEAC","JX","LLILSEK","W","KLUV"]) == 16
    assert get_best_word(points, ["SVWLIDP","FCPKTHW","EREMN","NFEF","PQ","FSC","ZYPOSXJ","BOR","YCGG","RC","DVPE","VAOE","OIGK","OTQE","REJFUFD","FVBCSSB","VHJ","BEC","MWZQ","WX","L","ZPCB","JKLHE","RYFTY","NKP","ID","O","KA","VRXX","NTDB","OERKPC","YFLUI","SKQCJ","PXDSW","ITYWD","TC","LOIDQEJ","NE","YND","VJHOCEC","RPRANZ","BQ","STM","RGVBFW","SMWUYLW","KT","SXHY","XCE","T","SC","UDJU","CHDR","UGXNQ","CQOOBA","O","NWW","V","L","BAQ","AZN","LBTR","N","QSURR","KADPH","M","LCBEAKM","ZHEVXS","F","TVAIQCY","MF","KCI","YQ","RCG","AKYPCP","WJXG","RQXOI","SJI","TWXZ","J","HIKCGHV","EAAXGG","AETSH","EO","BUET","TDIQCO","TKL","FJCRY","ZHAJLK","OLMCVA","F"]) == 6
    assert get_best_word(points, ["RBBL","ZJ","ZOFXE","LMBFCFX","O","JG","SYRYE","VXG","EU","DAIFZR","BQUNZHH","WKO","TFPHPLX","SWLG","CY","JYQNDSM","ITPS","B","UVSDMWR","LCPS"]) == 15
    assert get_best_word(points, ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG']) == 5
