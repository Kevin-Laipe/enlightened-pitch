from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
import pandas as pd
import urllib.request
import os

from backend.models import Bloc, Card, CardKeyword, CardReleasenote, CardStat, CardSubtype, CardSupertype, Class, Finish, Keyword, Printing, Rarity, Releasenote, Set, Stat, Subtype, Supertype, Talent, Type

class Command(BaseCommand):
    help = 'Download the .xls file with all cards and printings data and updates the database accordingly'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nodownload',
            default=True,
            action='store_false',
            help='Updates the database without downloading xls files',
        )

    def nodownload(self, cardsFile, printingsFile):
        if not os.path.exists('xls/'):
            os.mkdir('xls')

        if os.path.exists(cardsFile):
            os.remove(cardsFile)

        if os.path.exists(printingsFile):
            os.remove(printingsFile)

        cardsUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR29Sp0PHojzlOIULsrzwrXW9fCFwgFkNIoIEVWIvQPaetZYIXnQbhZ8msHd_PR2JwViA-2BNmK2Y3u/pub?output=xlsx'
        printingsUrl = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ8yCwmw7g7JW5WGzp7m_aPydcy7H6O7q1Pr6w91Dzdy3yP9Y1IxppiQriEBEtT31ZhgMcsdYwD3v1r/pub?output=xlsx'
        urllib.request.urlretrieve(cardsUrl, cardsFile)
        urllib.request.urlretrieve(printingsUrl, printingsFile)

    def addTalentsToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add talents from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        talents = df.to_dict(orient='records')
        for talent in talents:
            try:
                t = Talent.objects.create(id=talent['ID'], name=talent['Name'])
                t.save()
            except:
                existingTalent = Talent.objects.get(id=talent['ID'])
                existingTalent.name = talent['Name']
                existingTalent.save()

        self.stdout.write(self.style.SUCCESS("Talents added successfully !"))

    def addSupertypesToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add supertypes from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        supertypes = df.to_dict(orient='records')
        for supertype in supertypes:
            try:
                s = Supertype.objects.create(id=supertype['ID'], name=supertype['Name'])
                s.save()
            except:
                existingSupertype = Supertype.objects.get(id=supertype['ID'])
                existingSupertype.name = supertype['Name']
                existingSupertype.save()

        self.stdout.write(self.style.SUCCESS("Supertypes added successfully !"))

    def addClassesToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add classes from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        classes = df.to_dict(orient='records')
        for _class in classes:
            try:
                c = Class.objects.create(id=_class['ID'], name=_class['Name'])
                c.save()
            except:
                existingClass = Class.objects.get(id=_class['ID'])
                existingClass.name = _class['Name']
                existingClass.save()

        self.stdout.write(self.style.SUCCESS("Classes added successfully !"))
    
    def addTypesToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add types from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        types = df.to_dict(orient='records')
        for _type in types:
            try:
                t = Type.objects.create(id=_type['ID'], name=_type['Name'])
                t.save()
            except:
                existingType = Type.objects.get(id=_type['ID'])
                existingType.name = _type['Name']
                existingType.save()

        self.stdout.write(self.style.SUCCESS("Types added successfully !"))

    def addSubtypesToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add subtypes from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        subtypes = df.to_dict(orient='records')
        for subtype in subtypes:
            try:
                s = Subtype.objects.create(id=subtype['ID'], name=subtype['Name'])
                s.save()
            except:
                existingSubtype = Subtype.objects.get(id=subtype['ID'])
                existingSubtype.name = subtype['Name']
                existingSubtype.save()

        self.stdout.write(self.style.SUCCESS("Subtypes added successfully !"))

    def addKeywordsToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add keywords from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        keywords = df.to_dict(orient='records')
        for keyword in keywords:
            try:
                k = Keyword.objects.create(id=keyword['ID'], name=keyword['Name'], description=keyword['Description'], notes=keyword['Notes'])
                k.save()
            except:
                existingKeyword = Keyword.objects.get(id=keyword['ID'])
                existingKeyword.name = keyword['Name']
                existingKeyword.description = keyword['Description']
                existingKeyword.notes = keyword['Notes']
                existingKeyword.save()

        self.stdout.write(self.style.SUCCESS("Keywords added successfully !"))

    def addBlocsToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add blocs from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        blocs = df.to_dict(orient='records')
        for bloc in blocs:
            try:
                b = Bloc.objects.create(id=bloc['ID'], name=bloc['Name'], description=bloc['Description'])
                b.save()
            except:
                existingBloc = Bloc.objects.get(id=bloc['ID'])
                existingBloc.name = bloc['Name']
                existingBloc.description = bloc['Description']
                existingBloc.save()

        self.stdout.write(self.style.SUCCESS("Blocs added successfully !"))

    def addStatsToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add stats from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        stats = df.to_dict(orient='records')
        for stat in stats:
            try:
                s = Stat.objects.create(id=stat['ID'], name=stat['Name'])
                s.save()
            except:
                existingStat = Stat.objects.get(id=stat['ID'])
                existingStat.name = stat['Name']
                existingStat.save()

        self.stdout.write(self.style.SUCCESS("Stats added successfully !"))

    def addCardsToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add cards from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        cards = df.to_dict(orient='records')
        for card in cards:
            try:
                c = Card.objects.create(
                    id=card['ID'],
                    name=card['Name'],
                    talent=Talent.objects.get(name=card['Talent']) if card['Talent'] else None,
                    _class=Class.objects.get(name=card['Class']) if card['Class'] else None,
                    _type=Type.objects.get(name=card['Type']),
                    text=card['Effect'],
                    bloc=Bloc.objects.get(name=card['Bloc']),
                    is_banned_cc=True if card['Banned CC'] == 'TRUE' else False,
                    is_banned_blitz=True if card['Banned Blitz'] == 'TRUE' else False
                )
                c.save()
                self.stdout.write(self.style.SUCCESS("Card '%s' successfully created !" % c))
            except:
                existingCard = Card.objects.get(id=card['ID'])
                existingCard.name = card['Name']
                existingCard.talent = Talent.objects.get(name=card['Talent']) if card['Talent'] else None
                existingCard._class = Class.objects.get(name=card['Class']) if card['Class'] else None
                existingCard._type = Type.objects.get(name=card['Type'])
                existingCard.text = card['Effect']
                existingCard.bloc = Bloc.objects.get(name=card['Bloc'])
                existingCard.is_banned_cc=True if card['Banned CC'] == 'TRUE' else False
                existingCard.is_banned_blitz=True if card['Banned Blitz'] == 'TRUE' else False
                existingCard.save()
                self.stdout.write(self.style.SUCCESS("Card '%s' successfully updated !" % existingCard))

            for supertype in card['Super-Types'].split():
                if supertype != '':
                    try:
                        CardSupertype.objects.create(card=Card.objects.get(id=card['ID']), supertype=Supertype.objects.get(name=supertype))
                    except IntegrityError:
                        pass

            for subtype in card['Sub-Types'].split():
                if subtype != '':
                    try:
                        CardSubtype.objects.create(card=Card.objects.get(id=card['ID']), subtype=Subtype.objects.get(name=subtype))
                    except IntegrityError:
                        pass

            for keyword in card['Keywords'].split('\n'):
                if keyword != '':
                    try:
                        CardKeyword.objects.create(card=Card.objects.get(id=card['ID']), keyword=Keyword.objects.get(name=keyword))
                    except IntegrityError:
                        pass

            if card['Cost'] != '':
                try:
                    CardStat.objects.create(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Cost'), value=card['Cost'])
                except IntegrityError:
                    cs = CardStat.objects.get(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Cost'))
                    cs.value = card['Cost']
                    cs.save()

            if card['Pitch'] != '':
                try:
                    CardStat.objects.create(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Pitch'), value=card['Pitch'])
                except IntegrityError:
                    cs = CardStat.objects.get(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Pitch'))
                    cs.value = card['Pitch']
                    cs.save()

            if card['Power'] != '':
                try:
                    CardStat.objects.create(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Power'), value=card['Power'])
                except IntegrityError:
                    cs = CardStat.objects.get(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Power'))
                    cs.value = card['Power']
                    cs.save()

            if card['Defense'] != '':
                try:
                    CardStat.objects.create(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Defense'), value=card['Defense'])
                except IntegrityError:
                    cs = CardStat.objects.get(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Defense'))
                    cs.value = card['Defense']
                    cs.save()

            if card['Intellect'] != '':
                try:
                    CardStat.objects.create(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Intellect'), value=card['Intellect'])
                except IntegrityError:
                    cs = CardStat.objects.get(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Intellect'))
                    cs.value = card['Intellect']
                    cs.save()

            if card['Life'] != '':
                try:
                    CardStat.objects.create(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Life'), value=card['Life'])
                except IntegrityError:
                    cs = CardStat.objects.get(card=Card.objects.get(id=card['ID']), stat=Stat.objects.get(name='Life'))
                    cs.value = card['Life']
                    cs.save()
        
        self.stdout.write(self.style.SUCCESS("Cards added successfully !"))

    def addReleaseNotesToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add release notes from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        releaseNotes = df.to_dict(orient='records')
        for releaseNote in releaseNotes:
            try:
                r = Releasenote.objects.create(id=releaseNote['ID'], text=releaseNote['Text'])
                r.save()
            except:
                existingReleasenote = Releasenote.objects.get(id=releaseNote['ID'])
                existingReleasenote.text = releaseNote['Text']
                existingReleasenote.save()

            try:
                cardsQueryset = Card.objects.filter(name__regex=releaseNote['Name'])
                for card in cardsQueryset:
                    cr = CardReleasenote.objects.create(card=card, releasenote=Releasenote.objects.get(id=releaseNote['ID']))
                    cr.save()
            except:
                pass

        self.stdout.write(self.style.SUCCESS("Release notes added successfully !"))

    def addFinishesToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add finishes from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        finishes = df.to_dict(orient='records')
        for finish in finishes:
            try:
                f = Finish.objects.create(id=finish['ID'], name=finish['Name'])
                f.save()
            except:
                existingFinish = Finish.objects.get(id=finish['ID'])
                existingFinish.name = finish['Name']
                existingFinish.save()

        self.stdout.write(self.style.SUCCESS("Finishes added successfully !"))

    def addRaritiesToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add rarities from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        rarities = df.to_dict(orient='records')
        for rarity in rarities:
            try:
                r = Rarity.objects.create(id=rarity['ID'], name=rarity['Name'], tag=rarity['Tag'])
                r.save()
            except:
                existingRarity = Rarity.objects.get(id=rarity['ID'])
                existingRarity.name = rarity['Name']
                existingRarity.tag = rarity['Tag']
                existingRarity.save()

        self.stdout.write(self.style.SUCCESS("Rarities added successfully !"))

    def addSetsToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add sets from .xls file...")
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        sets = df.to_dict(orient='records')
        for set in sets:
            try:
                s = Set.objects.create(id=set['ID'], name=set['Name'])
                s.save()
            except:
                existingSet = Set.objects.get(id=set['ID'])
                existingSet.name = set['Name']
                existingSet.save()

        self.stdout.write(self.style.SUCCESS("Sets added successfully !"))
    
    def addPrintingsToDatabase(self, fileName, sheetName):
        self.stdout.write("Starting to add printings from .xls file (sheet '%s')..." % sheetName)
        df = pd.read_excel(fileName, sheet_name=sheetName)
        df = df.fillna('')

        printings = df.to_dict(orient='records')
        for printing in printings:
            try:
                p = Printing.objects.create(
                    uid=printing['uid'],
                    image=printing['Image'],
                    card=Card.objects.get(name=printing['Name']),
                    finish=Finish.objects.get(name=printing['Finish']),
                    flavour_text=printing['Flavour Text'],
                    rarity=Rarity.objects.get(name= printing['Rarity']),
                    set=Set.objects.get(id=printing['Set Tag']),
                    is_first_edition=printing['First Edition']
                )
                p.save()
            except:
                existingPrinting = Printing.objects.get(uid=printing['uid'])
                existingPrinting.image = printing['Image']
                existingPrinting.card = Card.objects.get(name=printing['Name'])
                existingPrinting.finish = Finish.objects.get(name=printing['Finish'])
                existingPrinting.falvour_text = printing['Flavour Text']
                existingPrinting.rarity = Rarity.objects.get(name=printing['Rarity'])
                existingPrinting.set = Set.objects.get(id=printing['Set Tag'])
                existingPrinting.is_first_edition = printing['First Edition']
                existingPrinting.save()

        self.stdout.write(self.style.SUCCESS("Printings from '%s' added successfully !" % sheetName))
 
    def handle(self, *args, **options):        
        cardsFile = os.path.join('xls/', 'cards.xls')
        printingsFile = os.path.join('xls/', 'printings.xls')

        if options['nodownload']:
            self.nodownload(cardsFile, printingsFile)

        # self.addTalentsToDatabase(cardsFile, 'talents')
        # self.addSupertypesToDatabase(cardsFile, 'supertypes')
        # self.addClassesToDatabase(cardsFile, 'classes')
        # self.addTypesToDatabase(cardsFile, 'types')
        # self.addSubtypesToDatabase(cardsFile, 'subtypes')
        # self.addKeywordsToDatabase(cardsFile, 'keywords')
        # self.addBlocsToDatabase(cardsFile, 'blocs')
        # self.addStatsToDatabase(cardsFile, 'stats')
        # self.addCardsToDatabase(cardsFile, 'cards')
        # self.addReleaseNotesToDatabase(cardsFile, 'release_notes')
        # self.addFinishesToDatabase(cardsFile, 'finishes')
        # self.addRaritiesToDatabase(cardsFile, 'rarities')
        # self.addSetsToDatabase(cardsFile, 'sets')

        xl = pd.ExcelFile(printingsFile)
        for printing_sheet in xl.sheet_names:
            self.addPrintingsToDatabase(printingsFile, printing_sheet)
