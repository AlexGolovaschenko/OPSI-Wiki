from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from partners.models import Contractor, Supplier, Comment
from partners.forms import ContractorUpdateForm, SupplierUpdateForm


def partners_list(request):
	contractors = Contractor.objects.all().order_by('-rating')
	suppliers = Supplier.objects.all().order_by('-rating')
	context = {
		'contractors': contractors,
		'suppliers': suppliers
	}
	return render(request, 'partners/partners_list.html', context)


def contractor_detail(request, id):
	partner = get_object_or_404(Contractor, pk = id)
	comments = partner.comments.all()
	context = {'company': partner, 'comments': comments}
	return render(request, 'partners/contractor_detail.html', context)


def supplier_detail(request, id):
	partner = get_object_or_404(Supplier, pk = id)
	comments = partner.comments.all()
	context = {'company': partner, 'comments': comments}
	return render(request, 'partners/supplier_detail.html', context)



@permission_required('pages.change_page')
def update_contractor(request, id=None):
	if id:
		# update existing company
		company_instance = get_object_or_404(Contractor, pk=id)
	else:
		# create new company
		company_instance = None

	if request.method == "POST":
		company_form = ContractorUpdateForm(request.POST, request.FILES, instance = company_instance)
		if company_form.is_valid():
			company = company_form.save()
			messages.success(request, f'Данные компании успешно изменены!')
			return redirect('partners:contractor_detail', company.id)
		else:
			messages.warning(request, f'Возникла ошибка при редактировании данных компании!')
			if id:
				return redirect('partners:contractor_detail', str(id))
			else:
				return redirect('partners:partners_list')
	else:
		company_form = ContractorUpdateForm(instance = company_instance)

	context = {'form': company_form, 'company_id': id}
	return render(request, 'partners/update_contractor_form.html', context)


@permission_required('pages.change_page')
def update_supplier(request, id=None):
	if id:
		# update existing company
		company_instance = get_object_or_404(Supplier, pk=id)
	else:
		# create new company
		company_instance = None

	if request.method == "POST":
		company_form = SupplierUpdateForm(request.POST, request.FILES, instance = company_instance)

		if company_form.is_valid():
			company = company_form.save()
			messages.success(request, f'Данные компании успешно изменены!')
			return redirect('partners:supplier_detail', company.id)
		else:
			messages.warning(request, f'Возникла ошибка при редактировании данных компании!')
			if id:
				return redirect('partners:supplier_detail', str(id))
			else:
				return redirect('partners:partners_list')
	else:
		company_form = SupplierUpdateForm(instance = company_instance)

	context = {'form': company_form, 'company_id': id}
	return render(request, 'partners/update_supplier_form.html', context)


@permission_required('pages.change_page')
def delete_contractor(request, id):
	company = get_object_or_404(Contractor, pk=id)
	company_name = company.company_name
	company.delete()
	messages.info(request, f'Субподрядчик {company_name} удален!')
	return redirect('partners:partners_list')


@permission_required('pages.change_page')
def delete_supplier(request, id):
	company = get_object_or_404(Supplier, pk=id)
	company_name = company.company_name
	company.delete()
	messages.info(request, f'Поставщик {company_name} удален!')
	return redirect('partners:partners_list')



@login_required
def leave_comment(request):
	try:
		object_name = request.POST['object_name']
		object_id = request.POST['object_id']
		if Contractor.__name__ == object_name:
			company = Contractor.objects.get(id=object_id)
		elif Supplier.__name__ == object_name:
			company = Supplier.objects.get(id=object_id)
		else:
			raise ValueError
	except:
		raise Http404("Компания не найдена")

	Comment.objects.create(author = request.user, text = request.POST['text'], content_object=company)

	try:
		next = request.POST['next']
		return HttpResponseRedirect(next) 
	except:
		return HttpResponseRedirect( reverse('partners:partners_list') ) 


@login_required
def delete_comment(request, id):
	comment = get_object_or_404(Comment, pk=id)
	if request.user.has_perm('pages.change_page') or comment.author == request.user:
		comment.delete()
	else:
		messages.warning(request, f'Не достаточно прав для удаления комментария!')

	next = request.GET.get('next', reverse('partners:partners_list'))
	return HttpResponseRedirect(next)