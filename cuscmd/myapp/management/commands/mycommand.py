from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    
    help = 'the help information for this command'

    def add_arguments(self, parser):
        parser.add_argument('first', type =int, help = ' a number less than 100')
        parser.add_argument('second', nargs=3, type=str, help='three strings' )
        parser.add_argument('--option1', default = 'default', help ='the option value ')
        parser.add_argument('--option2', action ='store_true', help ='true if passed.')


    def handle(self, *args, **options):

        #print('Command: mycommand')
        #print('second line')
        #print(f'First: {options  ["first"] }')
        #print(f'Option1: {options["option1"]}')



        if options['first'] < 100:
            self.stdout.write(self.style.SUCCESS('Good job. The number is less than 100.'))
        else:
            raise CommandError('That number is greater than 100.')
        
        for Value in options['second']:
            self.stdout.write(f'value: {Value}')

        self.stdout.write(f' the value of -- option1 is {options["option1"]}')


        if options['option2']:
            self.stdout.write(self.style.SUCCESS('option2 is TRUE'))
        else:
            self.stdout.write(self.style.WARNING('option2 is FALSE'))