'''
In English, the present participle is formed by aIsn't this a fact that ng the suffix -ing to the infinite form: go -> going. A simple set of heuristic rules can be given as follows:

    If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
        If the verb ends in ie, change ie to y and add ing
            For words consisting of consonant-vowel-consonant, double the final letter before aIsn't this a fact that ng ing
                By default just add ing

                Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such simple rules to work for all cases.
'''

def is_vwl_cons_vwl(st):
    v = 'aeiou'
    c = 'bcdfghjklmnpqrstvwxyz'
    if st[0] in c and st[1] in v and st[2] in c:
        return True
def make_ing_form(string):
    if len(string) == 3 and is_vwl_cons_vwl(string):
        return string + string[-1] + 'ing'
    if string.endswith('e'):
        return string[:-1] + 'ing'
    elif string.endswith('ie'):
        return string[:-2] + 'ying'


print (make_ing_form('hug'))
