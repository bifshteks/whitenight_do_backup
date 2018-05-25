from django import forms
from .models import Bid, Callback
from datetime import *

from django.core.mail import send_mail

now_date = date.today()

def get_select_date(delta_days):
	res_date = now_date + timedelta(days=int(delta_days))

	return res_date

MONTH = {
	1: 'января',
	2: 'февраля',
	3: 'марта',
	4: 'апреля',
	5: 'мая',
	6: 'июня',
	7: 'июля',
	8: 'августа',
	9: 'сентября',
	10: 'октября',
	11: 'ноября',
	12: 'декабря',
}

TIME = [
	('12:00', '12:00'),
	('12:30', '12:30'),
	('13:00', '13:00'),
	('13:30', '13:30'),
	('14:00', '14:00'),
	('14:30', '14:30'),
	('15:00', '15:00'),
	('15:30', '15:30'),
	('16:00', '16:00'),
	('16:30', '16:30'),
	('17:00', '17:00'),
	('17:30', '17:30'),
	('18:00', '18:00'),
	('18:30', '18:30'),
	('19:00', '19:00'),
	('19:30', '19:30'),
	('20:00', '20:00'),
]

DAYS = [(
		str(get_select_date(str(x)).day) + ' ' + MONTH[get_select_date(str(x)).month],
		str(get_select_date(str(x)).day) + ' ' + MONTH[get_select_date(str(x)).month]
	) for x in range(7)]



class OrderForm(forms.ModelForm):

	details = forms.CharField(label='Подробности заявки:', widget=forms.Textarea(attrs={'class': 'col-md-10 col-sm-10 col-xs-10', 'cols': '1000', 'rows': '8'}), max_length=100, required=False)
	name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name', 'placeholder': 'Имя:'}), max_length=255)
	phone = forms.CharField(widget=forms.TextInput(attrs={'id': 'phone', 'placeholder': 'Телефон:'}), max_length=20)
	time_from = forms.ChoiceField(widget=forms.Select(attrs={'id': 'time_from'}), choices=TIME)
	time_to = forms.ChoiceField(widget=forms.Select(attrs={'id': 'time_to'}), choices=TIME, initial='20:00')
	date = forms.ChoiceField(widget=forms.Select(attrs={'id': 'date'}), choices=DAYS)
	item_name = forms.CharField(widget=forms.HiddenInput(attrs={'name': 'id', 'id': 'hidden_input'}))

	

	class Meta:
		model = Bid
		fields = '__all__'


	def send_email(self):

		name = self.cleaned_data['name']
		phone = self.cleaned_data['phone']
		item_name = self.cleaned_data['item_name']
		date = self.cleaned_data['date']
		time_from = self.cleaned_data['time_from']
		time_to = self.cleaned_data['time_to']
		details = self.cleaned_data['details']
		subject = 'Новая заявка с сайта whitenight.info'
		message = '''
		Информация по заявке:\n
		Имя: {}\n
		Телефон: {}\n
		Товар: {}\n
		Совершить звонок {} с {} до {}\n
		Детали заявки: {}
		'''.format(name, phone, item_name, date, time_from, time_to, details)

		sender = 'whitenight.info@mail.ru'
		receiver = 'artem.pif@mail.ru'

		send_mail(
			subject,
			message,
			sender,
			[receiver],
			fail_silently=True
		)



class CallbackForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name', 'placeholder': 'Имя:'}), max_length=255)
	phone = forms.CharField(widget=forms.TextInput(attrs={'id': 'phone', 'placeholder': 'Телефон:'}), max_length=20)
	time_from = forms.ChoiceField(widget=forms.Select(attrs={'id': 'time_from'}), choices=TIME)
	time_to = forms.ChoiceField(widget=forms.Select(attrs={'id': 'time_to'}), choices=TIME, initial='20:00')
	date = forms.ChoiceField(widget=forms.Select(attrs={'id': 'date'}), choices=DAYS)
	
	class Meta:
		model = Callback
		fields = '__all__'

	def send_email(self):

		name = self.cleaned_data['name']
		phone = self.cleaned_data['phone']
		date = self.cleaned_data['date']
		time_from = self.cleaned_data['time_from']
		time_to = self.cleaned_data['time_to']		
		subject = 'Новый заказ звонка с сайта whitenight.info'
		message = '''
		Информация по заказу:\n
		Имя: {}\n
		Телефон:{}\n
		Совершить звонок {} с {} до {}\n
		'''.format(name, phone, date, time_from, time_to)

		sender = 'whitenight.info@mail.ru'
		receiver = 'artem.pif@mail.ru'

		send_mail(
			subject,
			message,
			sender,
			[receiver],
			fail_silently=True
		)