import math
from icecream import ic
import json
#######################################################
cards=16
total=256
incard=16
BS = [i for i in range(0,256)]
place = [i for i in range(1,257)]
dicts = {}
expdict = {}
export = []

#######################################################
def placeinbase(place,base):
    placein = place - base * math.floor(place/base)
    if placein == 0: placein = base
    return placein


for i in  range(len(BS)) :
    tx = 1
    if i >= 128:
        tx=0
    card = math.ceil(place[i]/incard)
    plinth = math.ceil(place[i]/8)
    led = placeinbase(place[i],16)
    pair = placeinbase(place[i],8)
    title = "BS"+str(i)
    BS = i
    # descr = {'title': title, 'card': card, 'led': led,'plinth': plinth,'pair': pair,}
    # dicts[i] = descr
    expdict = {
        "model": 'base0.bsintsm',
        "pk": place[i],
        "fields": {"title": title,
                   "bs": i,
                   "slug": "bs"+str(i),
                   "last_updated": "2021-04-06T12:43:58.626Z",
                   "card": card,
                   "led": led,
                   "place": place[i],
                   "tx": tx,
                   "plinth": plinth,
                   "pair": pair,
                   }
    }
    # ic(expdict)
    export.append(expdict)

# print(json.dumps(export))


# ic(export)

# ic(json.dumps(dicts))

# [{"model": "base0.bsintsm",
# "pk": 1,
# "fields":
# {"title": "bs100",
# "bs": 100,
# "slug": "bs100",
# "last_updated": "2021-04-06T12:43:58.626Z",
# "card": 1,
# "led": 1,
# "place": 1,
# "tx": "tx",
# "plinth": 1,
# "pair": 1
# }
# }]





# class BsINtsm(models.Model):
#     # Fields 1
#     title = models.CharField(max_length=100)
#     bs = models.IntegerField(default=0)
#     slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
#     last_updated = models.DateTimeField(auto_now=True, editable=False)
#     card = models.IntegerField(default=0)
#     led = models.IntegerField(default=0)
#     place = models.IntegerField(default=0)
#     tx = models.CharField(max_length=2)
#     plinth = models.IntegerField(default=0)
#     pair = models.IntegerField(default=0)
#
#     def __str__(self):
#         return f'{self.title} '