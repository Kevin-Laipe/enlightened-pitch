from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
import pandas as pd
import urllib.request
import os

from backend.models import Bloc, Card, CardKeyword, CardReleasenote, CardStat, CardSubtype, CardSupertype, Class, Keyword, Releasenote, Stat, Subtype, Supertype, Talent, Type

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

    def addSupertypesToDatabase(self, fileName, sheetName):
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

    def addClassesToDatabase(self, fileName, sheetName):
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
    
    def addTypesToDatabase(self, fileName, sheetName):
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

    def addSubtypesToDatabase(self, fileName, sheetName):
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

    def addKeywordsToDatabase(self, fileName, sheetName):
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

    def addBlocsToDatabase(self, fileName, sheetName):
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

    def addStatsToDatabase(self, fileName, sheetName):
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

    def addCardsToDatabase(self, fileName, sheetName):
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

    def addReleaseNotesToDatabase(self, fileName, sheetName):
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

    def handle(self, *args, **options):        
        cardsFile = os.path.join('xls/', 'cards.xls')
        printingsFile = os.path.join('xls/', 'printings.xls')

        if options['nodownload']:
            self.nodownload(cardsFile, printingsFile)

        self.addTalentsToDatabase(cardsFile, 'talents')
        self.addSupertypesToDatabase(cardsFile, 'supertypes')
        self.addClassesToDatabase(cardsFile, 'classes')
        self.addTypesToDatabase(cardsFile, 'types')
        self.addSubtypesToDatabase(cardsFile, 'subtypes')
        self.addKeywordsToDatabase(cardsFile, 'keywords')
        self.addBlocsToDatabase(cardsFile, 'blocs')
        self.addStatsToDatabase(cardsFile, 'stats')
        self.addCardsToDatabase(cardsFile, 'cards')
        self.addReleaseNotesToDatabase(cardsFile, 'release_notes')
