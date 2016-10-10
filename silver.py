words_list = []
bad_list = []

def read_input():
    global words_list
    f = open('input_silver.txt', 'r')
    input_content = f.read()
    words_list = list(input_content.split(' '))
    f.close()
    return words_list

def read_badwords():
    global bad_list
    f = open('badwords.txt', 'r')
    badwords_content = f.read()
    bad_list = list(badwords_content.split(' '))
    f.close()
    return bad_list

def search_input(input, badwords):
    f = open('clean_output.txt', 'w')
    output = []
    for word in words_list:
        if word in bad_list:
            output.append("*" * len(word))
        else:
            output.append(word)
    f.write(' '.join(output))
    f.close()


def swear_shield():
    input = read_input()
    badwords = read_badwords()
    search_input(input, badwords)

swear_shield()