from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import urllib.request
import os

from backend.models import Keyword, Subtype, Supertype, Talent

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

    def handle(self, *args, **options):        
        cardsFile = os.path.join('xls/', 'cards.xls')
        printingsFile = os.path.join('xls/', 'printings.xls')

        if options['nodownload']:
            self.nodownload(cardsFile, printingsFile)

        self.addTalentsToDatabase(cardsFile, 'talents')
        self.addSupertypesToDatabase(cardsFile, 'supertypes')
