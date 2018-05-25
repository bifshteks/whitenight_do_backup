from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.contrib import messages
from main.models import Bid, Item, Callback
from .forms import OrderForm, CallbackForm


class Index(TemplateView):
	template_name = 'index.html'

# class FakeCatalog(TemplateView):

# 	template_name = 'fake_catalog.html'

# 	def get_context_data(self, **kwargs):

# 		context = super(FakeCatalog, self).get_context_data(**kwargs)

# 		context['items'] = Item.objects.all()


# 		return context

# class FakeContacts(TemplateView):
# 	template_name = 'fake_contacts.html'

class Catalog(CreateView):
	model = Bid
	form_class = OrderForm
	template_name = 'catalog.html'
	success_url = '/catalog/'

	def get_context_data(self, **kwargs):

		context = super(Catalog, self).get_context_data(**kwargs)

		context['items'] = Item.objects.all()
		if self.request.session.get('catalog_order', False) and \
			not self.request.session.get('catalog_order_saw', False):
			context['need_show_popup'] = True
			self.request.session['catalog_order_saw'] = True

		else:
			context['need_show_popup'] = False
		# context['success_url'] = self.success_url

		return context

	def form_valid(self, form):


		self.object = form.save()
		# self.request.session['bids_id'] = self.object.id
		self.request.session['catalog_order'] = True
		self.request.session['catalog_order_saw'] = False
		# messages.success(self.request, "Ваша заявка успешно отправлена! Мы обязательно перезвоним в указанное время!")
		form.send_email()

		return super(Catalog, self).form_valid(form)

class ItemDetails(CreateView):
	model = Bid
	template_name = 'item.html'
	form_class = OrderForm
	success_url = '/catalog/'

	def get_context_data(self, **kwargs):
		context = super(ItemDetails, self).get_context_data(**kwargs)

		context['item'] = Item.objects.get(id=self.kwargs.get('pk'))
		# context['success_url'] = self.success_url
		# if self.request.session.get('item_order', False) and \
		# 	not self.request.session.get('item_order_saw', False):

		# 	context['need_show_popup'] = True
		# 	self.request.session['item_order_saw'] = True

		# else:
		# 	context['need_show_popup'] = False

		return context

	def form_valid(self, form):


		self.object = form.save()
		# self.request.session['bids_id'] = self.object.id

		# messages.success(self.request, "Your password is changed")
		self.request.session['catalog_order'] = True
		self.request.session['catalog_order_saw'] = False
		form.send_email()

		return super(ItemDetails, self).form_valid(form)


class Contacts(CreateView):
	template_name = 'contacts.html'
	model = Callback
	form_class = CallbackForm
	success_url = '/contacts/'

	def get_context_data(self, **kwargs):
		context = super(Contacts, self).get_context_data(**kwargs)

		# context['success_url'] = self.success_url
		if self.request.session.get('callback_order', False) and \
			not self.request.session.get('callback_order_saw', False):

			context['need_show_popup'] = True
			self.request.session['callback_order_saw'] = True

		else:
			context['need_show_popup'] = False

		return context

	def form_valid(self, form):

		self.object = form.save()
		# self.request.session['bids_id'] = self.object.id
		
		# messages.success(self.request, "")
		self.request.session['callback_order'] = True
		self.request.session['callback_order_saw'] = False
		form.send_email()

		return super(Contacts, self).form_valid(form)

class Thanks(TemplateView):
	template_name = 'thanks.html'

	def get_context_data(self, **kwargs):
		context = super(Thanks, self).get_context_data(**kwargs)

		context['bids_id'] = self.request.session['bids_id']

		return context

def test(request):

	return HttpResponse("it's a test")



