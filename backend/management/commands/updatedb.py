from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import urllib.request
import os

from backend.models import Keyword

class Command(BaseCommand):
    help = 'Download the .xlsx file with all cards and printings data and updates the database accordingly'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nodownload',
            default=True,
            action='store_false',
            help='Updates the database without downloading xls files',
        )

    def handle(self, *args, **options):        
        cardsFile = os.path.join('xls/', 'cards.xls')
        printingsFile = os.path.join('xls/', 'printings.xls')

        if options['nodownload']:
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

        df = pd.read_excel(cardsFile, sheet_name='keywords')
        df = df.fillna('')

        keyword_dict = df.to_dict(orient='records')
        for keyword in keyword_dict:
            try:
                Keyword.objects.create(name=keyword['Name'], description=keyword['Description'], notes=keyword['Notes'])
            except:
                existingKeyword = Keyword.objects.get(name=keyword['Name'])
                existingKeyword.description = keyword['Description']
                existingKeyword.notes = keyword['Notes']
                existingKeyword.save()