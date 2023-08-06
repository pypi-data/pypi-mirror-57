

# pytest -v test_autocomplete_me.py

import pytest
import autocomplete_me
#import os
# os.chdir('C:/Users/dell/Documents/s750/assignments-junyi-zhu/autocomplete-me')


##############################################################################
################################ SLOWCOMPLETE ################################
##############################################################################

def test_read_terms_slow():
    assert type(autocomplete_me.read_terms_slow("Data/test.txt")) == list
    assert type(autocomplete_me.read_terms_slow("Data/pokemon.txt")) == list
    assert type(autocomplete_me.read_terms_slow("Data/baby-names.txt")) == list
    assert type(autocomplete_me.read_terms_slow("Data/mandarin.txt")) == list
    assert type(autocomplete_me.read_terms_slow("Data/trademarks.txt")) == list
    assert [(607, 'sabzoo'), (308, 'chris'), (830, 'angus'), \
            (424, 'cmupreeya'), (925, 'cmugunho')] == autocomplete_me.read_terms_slow("Data/test.txt")

# ranked by file size
test_slow = autocomplete_me.read_terms_slow("Data/test.txt")
pokemon_slow = autocomplete_me.read_terms_slow("Data/pokemon.txt")
babies_slow = autocomplete_me.read_terms_slow("Data/baby-names.txt")
mandarin_slow = autocomplete_me.read_terms_slow("Data/mandarin.txt")
trademarks_slow = autocomplete_me.read_terms_slow("Data/trademarks.txt")

##############################################################################
############################### slowcomplete() ###############################

def test_slowcomplete():
    # test_slow.txt
    assert [(607,'sabzoo')] == autocomplete_me.slowcomplete(test_slow, "sab", 5)
    assert [(925,'cmugunho'),(424,'cmupreeya')] == autocomplete_me.slowcomplete(test_slow, "cmu", 5)
    assert [(925,'cmugunho'),(424,'cmupreeya'),(308,'chris')] == autocomplete_me.slowcomplete(test_slow, "c", 5)
    # pokemon.txt"
    assert [(32501,'Pikachu'),(8681,'Pinsir'),(5271,'Piloswine')] == autocomplete_me.slowcomplete(pokemon_slow, "Pi", 3)
    assert [(1892,'Delibird'),(1109,'Delcatty'),(0,'Delphox')] == autocomplete_me.slowcomplete(pokemon_slow, "Del", 3)
    assert [(141026,'Zapdos'), (116998,'Zoroark'),(11688,'Zangoose')] == autocomplete_me.slowcomplete(pokemon_slow, "Z", 3)
    # baby-names.txt"
    assert [(22175,'Sophia'),(20811,'Emma'),(18949,'Isabella'),(18936,'Mason'),(18925,'Jacob')] == autocomplete_me.slowcomplete(babies_slow, "", 5)
    assert [(240,'Saylor'),(88,'Saydee'),(68,'Saya'),(64,'Sayuri'),(31,'Sayra')] == autocomplete_me.slowcomplete(babies_slow, "Say", 5)
    assert [(54,'Seanna'),(16,'Seana'),(9,'Seanmichael'),(5,'Seann')] == autocomplete_me.slowcomplete(babies_slow, "Sean", 5)
    # mandarin.txt"
    assert [(20865,'我的'),(1495,'我喜'),(811,'我自己'),(690,'我爸')] == autocomplete_me.slowcomplete(mandarin_slow, "我", 4)
    assert [(110,'爱丽丝'),(71,'爱着'),(61,'爱尔兰'),(51,'爱过')] == autocomplete_me.slowcomplete(mandarin_slow, "爱", 4)
    assert [(19363,'你的'),(1011,'你自己'),(931,'你好'),(288,'你家')] == autocomplete_me.slowcomplete(mandarin_slow, "你", 4)
    # trademarks.txt"
    assert [(85890184,'Shaheen & Gordon, P.A.'),(85889354,'Shumaker, Loop & Kendrick')] == autocomplete_me.slowcomplete(trademarks_slow, "Sh", 2)
    assert [(85890402,'Antoinette M. Tease, P.L.L.C.'),(85855608,'Antero & Tormey LLP')] == autocomplete_me.slowcomplete(trademarks_slow, "An", 2)
    assert [(85885062,'HOME DYNAMIX LLC.'),(85884297,'HOME BOX OFFICE, INC.')] == autocomplete_me.slowcomplete(trademarks_slow, "HOME", 2)
    # edge cases
    assert [(292828,'我')] == autocomplete_me.slowcomplete(mandarin_slow, "", 1)
    assert "No words match with the given prefix." == autocomplete_me.slowcomplete(mandarin_slow, "invalidprefix", 1)


##############################################################################
################################ AUTOCOMPLETE ################################
##############################################################################

def test_insertWord():
    # Build a trie for testing. 
    nn = autocomplete_me.Node()
    nn.insertWord(10, "can")
    nn.insertWord(15, "cat")
    nn.insertWord(5, "actor")
    nn.insertWord(20, "act")
    nn.insertWord(5, "in")
    nn.insertWord(20, "inn")
    # tests for weights, maxweights
    assert -1 == nn.children["c"].weight
    assert 10 == nn.children["c"].children["a"].children["n"].weight
    assert 10 == nn.children["c"].children["a"].children["n"].maxweight
    assert 20 == nn.children["a"].maxweight
    assert -1 == nn.children["a"].children["c"].weight
    assert 5 == nn.children["i"].children["n"].weight
    assert 20 == nn.children["i"].children["n"].maxweight
    # tests for fullword
    assert 'in' == nn.children["i"].children["n"].fullword
    assert None == nn.children["a"].fullword
    assert 'can' == nn.children["c"].children["a"].children["n"].fullword


def test_read_terms_auto():
    assert type(autocomplete_me.read_terms_auto("Data/test.txt").children) == dict
    assert type(autocomplete_me.read_terms_auto("Data/pokemon.txt").children) == dict
    assert type(autocomplete_me.read_terms_auto("Data/baby-names.txt").children) == dict
    assert type(autocomplete_me.read_terms_auto("Data/mandarin.txt").children) == dict
    assert type(autocomplete_me.read_terms_auto("Data/trademarks.txt").children) == dict

    assert type(autocomplete_me.read_terms_auto("Data/test.txt").children["a"].weight) == int
    assert type(autocomplete_me.read_terms_auto("Data/pokemon.txt").children["C"].maxweight) == int
    assert type(autocomplete_me.read_terms_auto("Data/baby-names.txt").children["A"].children["v"].children["a"].fullword) == str


# ranked by file size
test_auto = autocomplete_me.read_terms_auto("Data/test.txt")
pokemon_auto = autocomplete_me.read_terms_auto("Data/pokemon.txt")
babies_auto = autocomplete_me.read_terms_auto("Data/baby-names.txt")
mandarin_auto = autocomplete_me.read_terms_auto("Data/mandarin.txt")
trademarks_auto = autocomplete_me.read_terms_auto("Data/trademarks.txt")

def test_searchTrie():
    assert autocomplete_me.Trie(test_auto).searchTrie("cmugunh").children["o"].fullword == 'cmugunho'
    assert autocomplete_me.Trie(test_auto).searchTrie("cm").children["u"].weight == -1
    assert autocomplete_me.Trie(test_auto).searchTrie("cm").children["u"].maxweight == 925

    assert autocomplete_me.Trie(mandarin_auto).searchTrie("时间").fullword == '时间'
    assert autocomplete_me.Trie(mandarin_auto).searchTrie("是不是").weight == 2158
    assert autocomplete_me.Trie(mandarin_auto).searchTrie("是").maxweight == 116019

    assert autocomplete_me.Trie(pokemon_auto).searchTrie("Po").fullword == None
    assert autocomplete_me.Trie(pokemon_auto).searchTrie("Porygon").weight == 533
    assert autocomplete_me.Trie(pokemon_auto).searchTrie("Porygon").maxweight == 156945
    
    assert autocomplete_me.Trie(trademarks_auto).searchTrie("PEPSICO, INC.").fullword == 'PEPSICO, INC.'
    assert autocomplete_me.Trie(trademarks_auto).searchTrie("BLANK").weight == -1
    assert autocomplete_me.Trie(trademarks_auto).searchTrie("BLANK").maxweight == 85892501

    assert autocomplete_me.Trie(trademarks_auto).searchTrie("invalidprefix") == False

##############################################################################
############################### autocomplete() ###############################

def test_autocomplete():
    assert autocomplete_me.slowcomplete(test_slow, "sab", 1) == autocomplete_me.autocomplete(test_auto, "sab", 1)
    assert autocomplete_me.slowcomplete(test_slow, "c", 3) == autocomplete_me.autocomplete(test_auto, "c", 3)
    assert autocomplete_me.slowcomplete(test_slow, "invalidprefix", 5) == autocomplete_me.autocomplete(test_auto, "invalidprefix", 5)

    assert autocomplete_me.slowcomplete(pokemon_slow, "Z", 1) == autocomplete_me.autocomplete(pokemon_auto, "Z", 1)
    assert autocomplete_me.slowcomplete(pokemon_slow, "Po", 3) == autocomplete_me.autocomplete(pokemon_auto, "Po", 3)
    assert autocomplete_me.slowcomplete(pokemon_slow, "  BLAH", 5) == autocomplete_me.autocomplete(pokemon_auto, "  BLAH", 5)

    assert autocomplete_me.slowcomplete(babies_slow, "H", 1) == autocomplete_me.autocomplete(babies_auto, "H", 1)
    assert autocomplete_me.slowcomplete(babies_slow, "Her", 3) == autocomplete_me.autocomplete(babies_auto, "Her", 3)
    assert autocomplete_me.slowcomplete(babies_slow, "Sabrin", 5) == autocomplete_me.autocomplete(babies_auto, "Sabrin", 5)

    assert autocomplete_me.slowcomplete(mandarin_slow, "", 1) == autocomplete_me.autocomplete(mandarin_auto, "", 1)
    assert autocomplete_me.slowcomplete(mandarin_slow, "永久", 3) == autocomplete_me.autocomplete(mandarin_auto, "永久", 3)
    assert autocomplete_me.slowcomplete(mandarin_slow, "Hermione", 5) == autocomplete_me.autocomplete(mandarin_auto, "Hermione", 5)

    assert autocomplete_me.slowcomplete(trademarks_slow, "HOME", 1) != autocomplete_me.autocomplete(trademarks_auto, "Home", 1)
    assert autocomplete_me.slowcomplete(trademarks_slow, "", 3) == autocomplete_me.autocomplete(trademarks_auto, "", 3)
    assert autocomplete_me.slowcomplete(trademarks_slow, "invalidprefix", 5) == autocomplete_me.autocomplete(trademarks_auto, "invalidprefix", 5)


##############################################################################
#################### ADD TERM, CHANGE WEIGHT, DELETE TERM #################### 
##############################################################################

test2_auto = autocomplete_me.read_terms_auto("Data/test2.txt")

def test_add_term():
    # test2_auto
    autocomplete_me.add_term(test2_auto, "hermione", 919)
    assert autocomplete_me.Trie(test2_auto).searchTrie("hermion").children["e"].fullword == "hermione"
    assert autocomplete_me.Trie(test2_auto).searchTrie("hermione").weight == 919
    assert autocomplete_me.Trie(test2_auto).searchTrie("her").maxweight == 919
    assert autocomplete_me.Trie(test2_auto).searchTrie("her").weight == 67
    assert autocomplete_me.autocomplete(test2_auto, "he", 3) == [(919,'hermione'),(67,'her')]
    # babies_auto
    autocomplete_me.add_term(babies_auto, "Ron", 19800301)
    assert autocomplete_me.autocomplete(babies_auto, "Ro", 3) == [(19800301,'Ron'),(6882,'Robert'),(2562,'Roman')]
    assert autocomplete_me.Trie(babies_auto).searchTrie("Ron").weight == 19800301
    assert autocomplete_me.Trie(babies_auto).searchTrie("Ro").maxweight == 19800301
    assert autocomplete_me.Trie(babies_auto).searchTrie("Ro").weight == -1


def test_insert_or_update():
    # updating existing words
    autocomplete_me.insert_or_update(test2_auto, "can", 23)
    assert autocomplete_me.Trie(test2_auto).searchTrie("can").weight == 16
    assert autocomplete_me.Trie(test2_auto).searchTrie("ca").maxweight == 16
    autocomplete_me.insert_or_update(test2_auto, "cat", 100)
    autocomplete_me.insert_or_update(test2_auto, "cat", 1000)
    # make sure the maxweight is updated as well
    assert autocomplete_me.Trie(test2_auto).searchTrie("cat").weight == 17
    assert autocomplete_me.Trie(test2_auto).searchTrie("ca").maxweight == 17

    # inserting new words
    # test2_auto
    autocomplete_me.insert_or_update(test2_auto, "hermione", 919)
    assert autocomplete_me.autocomplete(test2_auto, "her", 1) == [(920,'hermione')]
    assert autocomplete_me.autocomplete(test2_auto, "he", 3) == [(920,'hermione'),(67,'her')]
    assert autocomplete_me.Trie(test2_auto).searchTrie("her").maxweight == 920
    assert autocomplete_me.Trie(test2_auto).searchTrie("her").weight == 67
    # pokemon_auto
    autocomplete_me.insert_or_update(pokemon_auto, "jinhowchong", 19960308)
    assert autocomplete_me.autocomplete(pokemon_auto, "jin", 5) == [(19960308,'jinhowchong')]
    assert autocomplete_me.Trie(pokemon_auto).searchTrie("jinh").maxweight == 19960308
    assert autocomplete_me.Trie(pokemon_auto).searchTrie("jinhowchong").weight == 19960308


def test_delete_term():
    # test2_auto
    # case 1: node has no children
    assert autocomplete_me.Trie(test2_auto).searchTrie("in").maxweight == 20
    autocomplete_me.delete_term(test2_auto, "inn")
    assert autocomplete_me.autocomplete(test2_auto, "i", 50) == [(5,'in')]
    assert autocomplete_me.Trie(test2_auto).searchTrie("inn") == False
    assert autocomplete_me.Trie(test2_auto).searchTrie("in").maxweight == 5

    # pokemon_auto
    # case 2: node has children
    autocomplete_me.delete_term(pokemon_auto, "Porygon2")
    assert autocomplete_me.autocomplete(pokemon_auto, "Pory", 2) == [(83878,"Porygon-Z"), (533, "Porygon")]
    assert autocomplete_me.Trie(pokemon_auto).searchTrie("Porygon2") == False
    assert autocomplete_me.Trie(pokemon_auto).searchTrie("Porygon").maxweight == 83878
    autocomplete_me.delete_term(pokemon_auto, "Porygon-Z")
    assert autocomplete_me.autocomplete(pokemon_auto, "Pory", 2) == [(533, "Porygon")]



def test_change_weight():
    # update functions
    def func1(weight): return (weight + 1)
    def func2(weight): return (weight * 6)
    def func3(weight): return (weight//10000)

    # test2_auto
    autocomplete_me.change_weight(test2_auto, "cat", func2)
    assert autocomplete_me.Trie(test2_auto).searchTrie("cat").weight == 17 * 6
    assert autocomplete_me.Trie(test2_auto).searchTrie("c").maxweight == 17 * 6
    autocomplete_me.change_weight(test2_auto, "cat", func3)
    assert autocomplete_me.Trie(test2_auto).searchTrie("cat").weight == 0
    assert autocomplete_me.Trie(test2_auto).searchTrie("ca").maxweight == 16

    # trademarks_auto
    autocomplete_me.change_weight(trademarks_auto, "NORVELL IP LLC", func3)
    autocomplete_me.change_weight(trademarks_auto, "NORVELL IP LLC", func1)
    assert autocomplete_me.Trie(trademarks_auto).searchTrie("NORVELL IP LLC").weight == 85890111//10000 + 1
    assert autocomplete_me.Trie(trademarks_auto).searchTrie("NORVELL IP LLC").maxweight == 85890111//10000 + 1

    
def test_prune_and_rescale():
    def rescalefunc(weight): return (weight//10)
    def rescalefunc2(weight): return (weight-1)
    def rescalefunc3(weight): return (weight//2)

    # test2_auto
    autocomplete_me.prune_trie(test2_auto, 20)
    assert autocomplete_me.autocomplete(test2_auto, "", 5) == [(920, "hermione"), (67, "her")]
    autocomplete_me.rescale_weight(test2_auto, rescalefunc)
    assert autocomplete_me.autocomplete(test2_auto, "", 5) == [(92, "hermione"), (6, "her")]
    assert autocomplete_me.Trie(test2_auto).searchTrie("her").maxweight == 92

    # babies_auto
    autocomplete_me.prune_trie(babies_auto, 300)
    assert autocomplete_me.autocomplete(babies_auto, "Gio", 5) == [(3086, "Giovanni"), (372, "Giovani")]
    assert autocomplete_me.autocomplete(babies_auto, "Ayl", 5) == [(1284, "Ayla"), (673, "Aylin"), (379, "Ayleen")]
    autocomplete_me.rescale_weight(babies_auto, rescalefunc2)
    assert autocomplete_me.autocomplete(babies_auto, "Sab", 5) == [(1174, "Sabrina")]
    assert autocomplete_me.autocomplete(babies_auto, "Sel", 5) == [(1043, "Selena"), (570, "Selah")]
    
    # mandarin_auto
    autocomplete_me.prune_trie(mandarin_auto, 4000)
    assert autocomplete_me.autocomplete(mandarin_auto, "不", 5) == [(15666, "不是"), (7167, "不要"), (6942, "不能"), (6892, "不知道"), (4256, "不起")]
    assert autocomplete_me.autocomplete(mandarin_auto, "好", 5) == [(6171, "好了"), (5391, "好吧"), (5170, "好的")]
    autocomplete_me.rescale_weight(mandarin_auto, rescalefunc3)
    assert autocomplete_me.autocomplete(mandarin_auto, "意", 5) == "No words match with the given prefix."
    assert autocomplete_me.autocomplete(mandarin_auto, "我", 5) == [(20865, "我的")]


