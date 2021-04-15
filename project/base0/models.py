from django.db import models
from django_extensions.db import fields as extension_fields

# Create your models here.

class City(models.Model):

    # Fields 1
    title = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return f'{self.title}'


class Direction(models.Model):

    # Fields 1
    title = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.title}'


class AggregatorsType(models.Model):

    # Fields 1
    title = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Fields 2
    manufacturer = models.CharField(max_length=255, default='N/A')
    linksIn = models.IntegerField(default=0)
    linksOut = models.IntegerField(default=0)

    def __str__(self):
        return f'Агрегатор линков {self.title} by {self.manufacturer}\
         (Вх.линков {self.linksIn}/Вых.линков {self.linksOut}'


class Aggregator(models.Model):
    # Fields 1
    title = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Relationship Fields
    type = models.ForeignKey('AggregatorsType', on_delete=models.CASCADE, related_name="aggregatorsType",)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name="inCity", default='',)
    # Fields 2
    provider = models.TextField(max_length=100, blank=True)
    serial = models.TextField(max_length=100, blank=True)
    inventar = models.TextField(max_length=100, blank=True)
    address = models.TextField(max_length=100, blank=True)
    place = models.TextField(max_length=255, blank=True)
    contact = models.TextField(max_length=100, blank=True)
    person = models.TextField(max_length=100, blank=True)
    info = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.city}   {self.title} s/n {self.serial}'


class Timeslot(models.Model):

    # Fields 1
    title = models.IntegerField()
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    def __str__(self):
        return f'TS-{self.title} '


class BsInTsm(models.Model):
    # Fields 1
    title = models.CharField(max_length=100)
    tsm = models.IntegerField(default=0)
    bs = models.IntegerField(default=0)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    card = models.IntegerField(default=0)
    led = models.IntegerField(default=0)
    place = models.IntegerField(default=0)
    tx = models.BooleanField()
    plinth = models.IntegerField(default=0)
    pair = models.IntegerField(default=0)


    def __str__(self):
        return f'BS-in-{self.bs} '
    class Meta:
        unique_together = ('tsm', 'bs',)


class BsOutTsm(models.Model):
    # Fields 1
    title = models.CharField(max_length=100)
    tsm = models.IntegerField(default=0)
    bs = models.IntegerField(default=0)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    card = models.IntegerField(default=0)
    led = models.IntegerField(default=0)
    place = models.IntegerField(default=0)
    tx = models.BooleanField()
    plinth = models.IntegerField(default=0)
    pair = models.IntegerField(default=0)
    # Relationship Fields
    hw = models.ForeignKey('Iprobe', on_delete=models.PROTECT, related_name="aggregatorHW", default="", )

    def __str__(self):
        return f'BS-out-{self.bs} '
    class Meta:
        unique_together = ('tsm', 'bs',)

# class LeftSide(models.Model):
#     # Fields 1
#     title = models.CharField(max_length=30, unique=False, default="n/a")
#     slug = extension_fields.AutoSlugField(populate_from='title', blank=True, default="")
#     last_updated = models.DateTimeField(auto_now=True, editable=False)
#     # Relationship Fields
#     #hw = models.ForeignKey('Aggregator', on_delete=models.PROTECT, related_name="aggregatorHW", default="", )
#     BsTsmIn = models.OneToOneField(BsInTsm, on_delete=models.PROTECT, primary_key=True,  default="",)
#     BsTsmOut = models.OneToOneField(BsOutTsm, on_delete=models.PROTECT, unique=True,  null=True,)
    # # type = models.ForeignKey('Cros', on_delete=models.CASCADE, related_name="aggregatorHW", default="", )
    # ts_0 = models.ForeignKey('TimeSlot', on_delete=models.CASCADE, related_name="TS0", null=True, default="", )
    # ts_IN = models.ForeignKey('TimeSlot', on_delete=models.CASCADE, related_name="TSin", null=True, default="", )
    # BitStream_IN = models.ForeignKey('BitStream', on_delete=models.CASCADE, related_name="BSin", null=True,
    #                                  default="", )
    # Fields 2
    # columnIN = models.TextField(max_length=100, blank=True)
    # addressIN = models.TextField(max_length=100, blank=True)
    # plinthIN = models.TextField(max_length=100, blank=True)
    # pairIN = models.TextField(max_length=100, blank=True)
    # Fields 2
    # info = models.TextField(max_length=100, blank=True)
    # Fields out
    # plinthOUT = models.TextField(max_length=100, blank=True)
    # pairOUT = models.TextField(max_length=100, blank=True)
    # dpc = models.TextField(max_length=100)
    #
    #
    # def __str__(self):
    #     return f"  {self.BsTsmIn} {self.title} HW-{self.hw}"


class Matrix(models.Model):
    # Fields 1
    title = models.CharField(max_length=30, unique=False, default="n/a")
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True, default="")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Relationship Fields
    aggregator = models.ForeignKey('Aggregator', on_delete=models.PROTECT, related_name="aggregatorHW", default="", )
    bsTsmIn = models.OneToOneField(BsInTsm, on_delete=models.PROTECT, primary_key=True,  default="",)
    bsTsmOut = models.OneToOneField(BsOutTsm, on_delete=models.PROTECT, unique=True,  null=True,)
    info = models.TextField(max_length=100, blank=True)



    def __str__(self):
        return f"  {self.bsTsmIn} {self.title} aggregator-{self.aggregator} {self.bsTsmOut} "


class Iprobe(models.Model):
    # Fields 1
    title = models.CharField(max_length=30, unique=False, default="n/a")
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True, default="")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    CARD1 = '1'
    CARD2 = '2'
    CARD3 = '3'
    CARD4 = '4'
    CARD5 = '5'
    CARD_CHOICES = (
        (CARD1, 'card1'),
        (CARD2, 'card2'),
        (CARD3, 'card3'),
        (CARD4, 'card4'),
        (CARD5, 'card5'),
    )
    card = models.CharField(max_length=5,
                                      choices=CARD_CHOICES,
                                      default='')
    IPROBE1 = '1'
    IPROBE2 = '2'
    IPROBE3 = '3'
    IPROBE4 = '4'
    IPROBE5 = '5'
    IPROBE6 = '6'
    IPROBE7 = '7'
    IPROBE_CHOICES = (
        (IPROBE1, 'iprobe1'),
        (IPROBE2, 'iprobe2'),
        (IPROBE3, 'iprobe3'),
        (IPROBE4, 'iprobe4'),
        (IPROBE5, 'iprobe5'),
        (IPROBE6, 'iprobe6'),
        (IPROBE7, 'iprobe7'),
    )
    iprobe = models.CharField(max_length=5,
                                      choices=IPROBE_CHOICES,
                                      default='')
    # trunk = models.IntegerField(default=0)

    # Relationship Fields

    def __str__(self):
        return f"   trunk={self.title} iprobe={self.iprobe} card={self.card}   "


class Object(models.Model):
    TS_CHOICES = [(str(i), 'ts' + str(i)) for i in range(1, 32)]
    TSM_CHOICES = [(str(i), 'tsm' + str(i)) for i in range(1, 3)]
    # Fields 1
    title = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    vertical = models.CharField(max_length=255)
    plinth = models.CharField(max_length=255)
    pair = models.CharField(max_length=255)
    # Relationship Fields
    ts0 = models.CharField(max_length=2, choices=TS_CHOICES, default='')
    # streamDirection = models.OneToOneField('Direction', on_delete=models.PROTECT, related_name="stream_direction", unique=True, )
    bs = models.ForeignKey(BsInTsm, on_delete=models.PROTECT)
    ts1 = models.ForeignKey('TimeSlot', on_delete=models.PROTECT, related_name="TS1", null=True, default="", )
    tsm = models.CharField(max_length=2, choices=TSM_CHOICES, default='')
    tx1 = "1"
    tx0 = "0"
    TX_CHOICES = ((tx1, 'TX'),(tx0, 'RX'),)
    tx = models.CharField(max_length=8,choices=TX_CHOICES, default='')
    class Meta:
        unique_together = ('tsm', 'bs','ts1',)
    def __str__(self):
        return f'{self.title}--TS0={self.ts0} --> BS{self.bs} /TS1={self.ts1}'