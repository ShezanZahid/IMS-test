from django.shortcuts import redirect, render
from .models import Activenumber,Result
from django.http import HttpResponse
from django.db.models import F
import  csv
from datetime import timedelta

from .form import MyForm
# Create your views here.

def imsSetupFilter(request):
    Result.objects.all().delete()
   
    comission_sim =Activenumber.objects.all()
    total= comission_sim.count()
    comission_sim_beforchange=comission_sim
    comission_sim_diff = Activenumber.objects.none()
    regions=request.POST.getlist('region')
    product_code=request.POST.getlist('product_code')
    if regions :
        comission_sim_beforchange=comission_sim
        comission_sim= Activenumber.objects.filter(region__in=(regions))
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        
        for item in comission_sim_diff:
            item.remarks = "Region Not Matched"

        Result.objects.bulk_create(comission_sim_diff)

    if product_code:
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(product_code__in=(product_code))
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "Product code do Not Matched"

        Result.objects.bulk_create(comission_sim_diff)

    active_start_date= request.POST.get('active_start_date')
    active_end_date= request.POST.get('active_end_date')
    if active_start_date or  active_end_date :
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(activation_date__range=[active_start_date,active_end_date])
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "Activation date do not matched"

        Result.objects.bulk_create(comission_sim_diff)
    

    
    qcpass_start_date= request.POST.get('qcpass_start_date')
    qcpass_end_date= request.POST.get('qcpass_end_date')
    if qcpass_start_date or  qcpass_end_date :
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(qcpass_date__range=[qcpass_start_date,qcpass_end_date])
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "QC pass date do not match"

        Result.objects.bulk_create(comission_sim_diff)

    qcpass_days_end = request.POST.get('qcpass_days_end')
   
    if qcpass_days_end:
        qcpass_days_end = int(qcpass_days_end)
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(qcpass_date__lt=F('activation_date')+timedelta(days=qcpass_days_end))
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "QC Pass days Range Not Matched"

        Result.objects.bulk_create(comission_sim_diff)

    lift_start_date= request.POST.get('lift_start_date')
    lift_end_date= request.POST.get('lift_end_date')
    if lift_start_date or  lift_end_date :
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(lifting_date__range=[lift_start_date,lift_end_date])
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "lifting date do not matched"

        Result.objects.bulk_create(comission_sim_diff)

    usage_start_date= request.POST.get('usage_start_date')
    usage_end_date= request.POST.get('usage_end_date')
    if usage_start_date or  usage_end_date :
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(usage_date__range=[usage_start_date,usage_end_date])
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "Usage date  do not match"

        Result.objects.bulk_create(comission_sim_diff)

    usage_days_start = request.POST.get('usage_days_start')
    usage_days_end =request.POST.get('usage_days_end') 
    if usage_days_start or usage_days_end:
        usage_days_start = int(usage_days_start)
        usage_days_end =int(usage_days_end) 
        comission_sim_beforchange=comission_sim
       
        comission_sim= comission_sim.filter(usage_date__lt=F('activation_date')+timedelta(days=usage_days_end)).filter(usage_date__gte=F('activation_date')+timedelta(days=usage_days_start))
        #comission_sim= comission_sim.filter(usage_date__range=[F('activation_date')+timedelta(days=2),F('activation_date')+timedelta(days=10)])
    
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "Usage days Range Not Matched"

        Result.objects.bulk_create(comission_sim_diff)

    usage_value_start = request.POST.get('usage_value_start')
    usage_value_end = request.POST.get('usage_value_end')
    if usage_value_start or  usage_value_end :
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(usage_value__gte=usage_value_start,usage_value__lte=usage_value_end)
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "Usage Amount do not match"

        Result.objects.bulk_create(comission_sim_diff)
    
   

    usage_3g_value_start = request.POST.get('usage_3g_value_start')
    usage_3g_value_end = request.POST.get('usage_3g_value_end')
    if usage_3g_value_start or  usage_3g_value_end :
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(net_3g_usage_value__gte=usage_3g_value_start,net_3g_usage_value__lte=usage_3g_value_end)
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "3g Usage amount do not match"

        Result.objects.bulk_create(comission_sim_diff)
    
    usage_4g_value_start = request.POST.get('usage_4g_value_start')
    usage_4g_value_end = request.POST.get('usage_4g_value_end')
    if usage_4g_value_start or  usage_4g_value_end :
        comission_sim_beforchange=comission_sim
        comission_sim= comission_sim.filter(net_4g_usage_value__gte=usage_4g_value_start,net_4g_usage_value__lte=usage_4g_value_end)
        comission_sim_diff= comission_sim_beforchange.difference(comission_sim)
        for item in comission_sim_diff:
            item.remarks = "4G Usage Amount do not match"

        Result.objects.bulk_create(comission_sim_diff)

    for item in comission_sim:
            item.remarks = "Successfully got comission"
    Result.objects.bulk_create(comission_sim)

    
    comission_sim_count = comission_sim.count()
    comission_sim_beforchange = comission_sim_beforchange.count()
    comission_sim_def_count = comission_sim_diff.count()
    context={
        'comission_sim':comission_sim,
        'comission_sim_count':comission_sim_count,
        'comission_sim1_count':comission_sim_beforchange,
        'comission_sim_def_count':comission_sim_def_count,
        'total':total,
        'disqualified':total-comission_sim_count
    }

    return render(request,'core/ims-result-filter.html',context)


def itemFilter(request):
    form = MyForm()
    regions= Activenumber.objects.all().order_by('region').values('region').distinct()
    product_codes = Activenumber.objects.all().order_by('product_code').values('product_code').distinct()
    return render(request,'core/filter-item-form.html',{'form':form,'regions':regions,'product_codes':product_codes })

def export(request):
    response =HttpResponse(content_type ='text/csv')
    fields =Result._meta.fields
    final_names =[field.name for field in fields]
    writer = csv.writer(response)
    writer.writerow(final_names)

    for item in Result.objects.all().values_list():
     writer.writerow(item)

    response['Content-Disposition'] = 'attachment; filename="result.csv"'

    

    return response

def clearData(request):
    Result.objects.all().delete()
    response= HttpResponse("Successfully Cleared the table")
    return redirect ('/filter-item-form')
