from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dateutil.parser import parse
from ast import literal_eval
from .serializers import RecentUsage, BatteryUsage, TimeStamp, TimeStampSerializer
from datetime import datetime
import csv

# Create your views here.
@api_view(['POST'])
@csrf_exempt
def battery_report_data(request):   
    ru_table = False
    if request.method == 'POST':
        data = literal_eval(request.body.decode("UTF-8"))
        
        tsuid = TimeStamp.objects.filter(uid = data[0][6])
        for tsrb in tsuid:
            try:
                print("RU and BU for TS ",tsrb,"\n",tsrb.ru, tsrb.bu)
                if tsrb.ru and tsrb.bu:
                    tsrb.delete()
            except:
                print("BU & RU not available",tsrb)
        
        if 'a' in data[0][3]:
            ru_table = True

        if ru_table:
            header=['Date', 'Time', 'State', 'Source', 'Capacity_percentage', 'Capacity_remaining', 'Machine_ID']
            f = open(r"logs\ru.csv", 'a+', encoding='UTF8')
            writer = csv.writer(f)
            writer.writerow(header)
            for ie in data:
                ts = TimeStamp.objects.get_or_create(date=parse(ie[0]).date(), time=parse(ie[1]).time(), state=ie[2], uid=ie[6])
                if ie[3] == "ac":
                    RecentUsage.objects.get_or_create(timestamp=ts[0], source=ie[3], capacity_percent=int(ie[4].split(' ')[0]), capacity=int(ie[5].split(' ')[0].replace(',','')))
                    writer.writerow(ie)
            writer.writerow(["This", "Above", "CSV", "Data", "Was", "Added", "At", datetime.now()])
            writer.writerows([[],[],[]])
            f.close()
        else:
            header=['Date', 'Time', 'State', 'Duration', 'Energy_percentage', 'Energy_remaining', 'Machine_ID']
            f = open(r"logs\bu.csv", 'a+', encoding='UTF8')
            writer = csv.writer(f)
            writer.writerow(header)
            for ie in data:
                ts = TimeStamp.objects.get_or_create(date=parse(ie[0]).date(), time=parse(ie[1]).time(), state=ie[2], uid=ie[6])
                if ie[4] == '-' and ie[5] == '-':
                    BatteryUsage.objects.get_or_create(timestamp=ts[0], duration=parse(ie[3]).time(), energy_percent=0, energy=0)
                elif ie[4] == '-':
                    BatteryUsage.objects.get_or_create(timestamp=ts[0], duration=parse(ie[3]).time(), energy_percent=0, energy=int(ie[5].split(' ')[0].replace(',','')))
                elif ie[5] == '-':
                    BatteryUsage.objects.get_or_create(timestamp=ts[0], duration=parse(ie[3]).time(), energy_percent=int(ie[4].split(' ')[0]), energy=0)
                else:
                    BatteryUsage.objects.get_or_create(timestamp=ts[0], duration=parse(ie[3]).time(), energy_percent=int(ie[4].split(' ')[0]), energy=int(ie[5].split(' ')[0].replace(',','')))
                writer.writerow(ie)
            writer.writerow(["This", "Above", "CSV", "Data", "Was", "Added", "At", datetime.now()])
            writer.writerows([[],[],[]])
            f.close()

    print("RU & BU = NONE \n",TimeStamp.objects.filter(ru=None, bu=None).delete())

    return Response()

@login_required
@api_view(['GET'])
def battery_report_data_all(request):
    ts = TimeStamp.objects.all().order_by('-date')
    data = TimeStampSerializer(ts, many=True)
    return Response(data.data)

@api_view(['GET'])
def battery_report_data_user(request, uid):
    ts = TimeStamp.objects.filter(uid=uid)
    data = TimeStampSerializer(ts, many=True)
    return Response(data.data)

# @api_view(['GET'])
# def battery_report_data_user_lts(request, uid):
#     ts = TimeStamp.objects.filter(uid=uid).last()
#     data = TimeStampSerializer(ts)
#     return Response(data.data['time'])

@api_view(['GET'])
def battery_report_data_user_power(request, uid):
    ts = TimeStamp.objects.filter(uid=uid)

    ac_bu_sum = 0
    ac_bu_count = 0
    bu_capacity_sum = 0
    bu_capacity_count = 0
    ru_capacity_sum = 0
    ru_capacity_count = 0
    bu_energy_min = 999999
    bu_energy_sum = 0
    bu_duration_sum = 0
    
    for e in ts:
        if e.state == "active":
            try:
                ru_capacity_sum += e.ru.capacity
                ru_capacity_count += 1
            except:
                print("RU Null for ",e)
            try:
                duration = (e.bu.duration.hour)*3600+(e.bu.duration.minute)*60+(e.bu.duration.second)
                if duration > 0:
                    ac_bu_count += 1
                    ac_bu_sum += e.bu.energy/duration
            except:
                print("No BU  for ",e)
        elif e.state == 'connected standby':
            try:
                ru_capacity_sum += e.ru.capacity
                ru_capacity_count += 1
            except:
                print("RU Null for ",e)
            try:
                if e.bu.energy < bu_energy_min:
                    bu_energy_min = e.bu.energy
                bu_energy_sum += e.bu.energy
                bu_duration_sum += (e.bu.duration.hour)*3600+(e.bu.duration.minute)*60+(e.bu.duration.second)
            except:
                print("No BU  for ",e)

    ac_avg = ac_bu_sum/ac_bu_count
    avg_bu_cs = (bu_energy_sum - bu_energy_min)
    try:
        avg_bu_cs = avg_bu_cs/bu_duration_sum
    except:
        avg_bu_cs = avg_bu_cs/bu_energy_min
        print("\n\n\n Battery Usage Table's Duration SUM Was zero, i.e battery report of avg is wrong \n")

    tp_active = bu_capacity_sum + (bu_capacity_count*ac_avg)
    tp_cstandby = ru_capacity_sum + (avg_bu_cs * ru_capacity_count)

    data = {
        "power": round(tp_active+tp_cstandby,2),
        "carbon": round((tp_active+tp_cstandby)*0.41205*0.27778, 2)
    }

    return Response(data)
