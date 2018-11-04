"""
With mask Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""
import os
from persian_wordcloud.wordcloud import PersianWordCloud
import multidict
from PIL import Image
import numpy as np
from arabic_reshaper import arabic_reshaper
from bidi.algorithm import get_display
from wordcloud import get_single_color_func
from photography.models import thumbnail
from app.models import Config
import random
import string
from datetime import datetime
import time
from .tasks import photo_remove
from django.conf import settings
from django.core.cache import cache
from django.utils.crypto import get_random_string
from contextlib import suppress

CACHE_TTL = getattr(settings, 'CACHE_TTL')
COUNTDOWN = getattr(settings, 'COUNTDOWN')

class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping
       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.
       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        # self.word_to_color = {color: word
        #                       for (color, words) in color_to_words.items()
        #                       for word in words}
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)


# class GroupedColorFunc(object):
#     """Create a color function object which assigns DIFFERENT SHADES of
#        specified colors to certain words based on the color to words mapping.
#        Uses wordcloud.get_single_color_func
#        Parameters
#        ----------
#        color_to_words : dict(str -> list(str))
#          A dictionary that maps a color to the list of words.
#        default_color : str
#          Color that will be assigned to a word that's not a member
#          of any value from color_to_words.
#     """
#
#     def __init__(self, color_to_words, default_color):
#         self.color_func_to_words = [
#             (get_single_color_func(color), set(words))
#             for (color, words) in color_to_words.items()]
#
#         self.default_color_func = get_single_color_func(default_color)
#
#     def get_color_func(self, word):
#         """Returns a single_color_func associated with the word"""
#         try:
#             color_func = next(
#                 color_func for (color_func, words) in self.color_func_to_words
#                 if word in words)
#         except StopIteration:
#             color_func = self.default_color_func
#
#         return color_func
#
#     def __call__(self, word, **kwargs):
#         return self.get_color_func(word)(word, **kwargs)

# def name_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
def name_generator(size=6, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



def create_photo(id, content, colormap, font, word1, word2, color1, color2, main_color, bg_color, user):

    now = str(datetime.now().second)
    name = now + get_random_string(length=10) + name_generator(6, time.strftime("%s")) + '.jpeg'
    if cache.get('conf') is not None:
        conf = cache.get('conf')

    else:
        config = Config.objects.get(status=1)
        word_stop = config.content
        url_pre = config.url_pre
        save_place = config.save_place
        watermark = str(config.watermark)
        conf = {'config': config, 'word_stop': word_stop, 'url_pre': url_pre, 'save_place': save_place, 'watermark': watermark}
        cache.set('conf', conf, timeout=CACHE_TTL)
    pho_conf = 'photo_conf' + str(id)
    if cache.get(pho_conf) is not None:
        photo_conf = cache.get(pho_conf)

    else:
        image = thumbnail.objects.get(id=id)
        min_word = image.photo_Mask.min_word
        medium_word = image.photo_Mask.medium_word
        max_word = image.photo_Mask.max_word
        path_mask = str(image.photo_Mask.url)
        path_photo = str(image.photo_main.url)
        photo_conf = {'photo_conf': image, 'min_word': min_word, 'medium_word': medium_word, 'max_word': max_word\
                      , 'path_mask': path_mask, 'path_photo': path_photo
        }
        # photo_conf = {'photo_conf': image, 'path_mask': path_mask, 'path_photo': path_photo}
        cache.set(pho_conf, photo_conf, timeout=CACHE_TTL)

    image_watermark = Image.open('media/' + conf['watermark'])
    save_path = conf['save_place'] + name
    word_stop = conf['word_stop']
    url_pre = conf['url_pre']
    min_word = photo_conf['min_word']
    medium_word = photo_conf['medium_word']
    max_word = photo_conf['max_word']
    path_mask = photo_conf['path_mask']
    path_photo = photo_conf['path_photo']

    stop_words_reshape = get_display(arabic_reshaper.reshape(word_stop))
    STOPWORDS = set([x.strip() for x in stop_words_reshape.split('\n')])
    mask_ptoto = np.array(Image.open('media/' + path_mask))
    main_photo = Image.open('media/' + path_photo)
    text = get_display(arabic_reshaper.reshape(content))
    array_txt = text.split(" ")
    array_txt2 = array_txt[-10:]
    len_array = len(array_txt2)
    if len_array < 4:
        ln_word = min_word
        # ln_word = 400
    elif len_array < 7:
        ln_word = medium_word
        # ln_word = 300
    else:
        ln_word = max_word
    #     ln_word = 200
    #ln_word = 400
    words = multidict.MultiDict()
    color_to_words = {}
    # if Certainـwords != None:
    #     w1 = get_display(arabic_reshaper.reshape(Certainـwords))
    #     sword1 = w1.split(" ")
    #     sword2 = sword1[-3:]
    #     for item in sword2:
    #         words.add(item, np.random.randint(1, ln_word))
    #         color_to_words[item] = [colorـCertainـwords]

    if word1 != None:
        w1 = get_display(arabic_reshaper.reshape(word1))
        sword1 = w1.split(" ")
        words.add(sword1[0], np.random.randint(1, ln_word))
        color_to_words[color1] = [w1]

    if word2 != None:
        w2 = get_display(arabic_reshaper.reshape(word2))
        sword2 = w2.split(" ")
        words.add(sword2[0], np.random.randint(1, ln_word))
        color_to_words[color2] = [w2]

    # if word2 != None:
    #     sword2 = word2.split(" ")
    #     w2 = get_display(arabic_reshaper.reshape(sword2[0]))
    #     words.add(w2, np.random.randint(1, ln_word))
    #     color_to_words[color2] = [w2]

    for item in array_txt2:
        for i in range(ln_word):
            words.add(item, np.random.randint(1, 5))

    # the regex used to detect words is a combination of normal words, ascii art, and emojis
    # 2+ consecutive letters (also include apostrophes), e.x It's
    normal_word = r"(?:\w[\w']+)"
    # 2+ consecutive punctuations, e.x. :)
    ascii_art = r"(?:[{punctuation}][{punctuation}]+)".format(punctuation=string.punctuation)
    # a single character that is not alpha_numeric or other ascii printable
    emoji = r"(?:[^\s])(?<![\w{ascii_printable}])".format(ascii_printable=string.printable)
    regexp = r"{normal_word}|{ascii_art}|{emoji}".format(normal_word=normal_word, ascii_art=ascii_art,
                                                         emoji=emoji)
    # colormap = {1:"jet", 2:"hsv",3:"hot", 4:"cool", 5:"spring", 6:"summer", 7:"autumn", 8:"winter",
    #             9:"gray",10:"copper", 11:"pink", 12:"lines"}
    # FONT_PATH = os.environ.get('FONT_PATH', os.path.join(FILE, 'DroidSansMono.ttf'))

    Font_Path = {'a': 'B_Nazanin_Regular.ttf', 'b': 'Mj_Nazila_Gol.ttf', 'c': 'B_Fantezy.ttf',
                 'd': 'B_Kaj.ttf', 'e': 'B_Moj.ttf', 'f': 'B_Majid_Shadow.ttf', 'j': 'B_Esfehan_Bold.ttf',
                 'h': 'B_Koodak_Outline.ttf', 'i': 'Mj_Anoosh.ttf', 'g': 'B_Chini.ttf', 'k': 'Mj_Pashtu_Outline.ttf'
                 , 'l': 'ChopinScript.otf', 'm': 'BrushScriptStd.otf', 'n': 'DirtyFox.ttf',
                 'o': 'AlexBrush-Regular.ttf', 'p': 'BlackoakStd.otf'}

    with suppress(FileNotFoundError):
        Font = 'media/config/font/'+Font_Path[font]
    print(colormap)
    recolor = 'no'
    if colormap == 'null':
        colormap = 'cool'
        recolor = 'yes'
        print(colormap)
    wc = PersianWordCloud(
        # font_path=Font_Path,
        max_words=400,
        stopwords=STOPWORDS,
        margin=0,
        width=700,
        height=700,
        min_font_size=4,
        colormap=colormap,
        font_path=Font,
        regexp=regexp,
        max_font_size=150,
        random_state=False,
        background_color=bg_color,
        mask=mask_ptoto
    ).generate_from_frequencies(words)
    if recolor == 'yes':
        grouped_color_func = SimpleGroupedColorFunc(color_to_words, main_color)
        wc.recolor(color_func=grouped_color_func)
    save_url = {}
    image = wc.to_image()
    image.paste(main_photo, (0, 0), main_photo)
    image.paste(image_watermark, (0, 0), image_watermark)
    if not os.path.exists(conf['save_place']):
        os.makedirs(conf['save_place'])

    image.save(save_path)
    print(datetime.now())
    url = url_pre + name
    save_url['url'] = url
    # when = datetime.now() + timedelta(minutes=1)
    # image_remove.apply_async(args=[save_place], eta=when)
    photo_remove.apply_async(args=[save_path, user], countdown=COUNTDOWN)
    return save_url
