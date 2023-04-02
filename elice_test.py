def trump_tweet(text):
    dic ={'hash' : [], 'mention' : [], 'text' : []}
    for i in list(text.split()):
        if i[0] == '#':
            dic['hash'].append(i[1:])
        elif i[0] == '@':
            dic['mention'].append(i[1:])
        else:
            dic['text'].append(i)
    print("""\
hash list : {0}
mention list : {1}
text list : {2}\
    """.format(dic['hash'], dic['mention'], dic['text']))

text = input()
trump_tweet(text)
