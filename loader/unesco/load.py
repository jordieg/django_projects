import csv 

from unesco.models import Category, States, Region, Iso, Site

fhand = open('unesco/load.csv')
reader = csv.reader(fhand)

Category.objects.all().delete()
States.objects.all().delete()
Region.objects.all().delete()
Iso.objects.all().delete()
Site.objects.all().delete()

# name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso

for row in reader:
   # print(row)
    
############## Category

    # name for Category
    try:
        c_name = string(row[7])
    except:
        c_name = None

    c  = Category(name=c_name)
    c.save()


################ Region

    # name for Region
    try:
        r_name = string(row[9])
    except: 
        r_name = None

    # latitude for Region
    try:
        latitude = float(row[5])
    except:
        latitude = None

    # longitude for Region 4
    try: 
        longitude = float(row[4])
    except:
        longitude = None

    r = Region(name=r_name, latitude=latitude, longitude=longitude)
    r.save()


################ ISO
    # name for Iso
    try:
        iso = string(row[10])
    except: 
        iso = None

    i = Iso(name=iso)
    i.save() 


############### States 
    # name for States
    try:
        s_name = string(row[8])
    except:
        s_name = None

    st = States(name=s_name, iso=i, region=r) 
    st.save()

############### Site

    try:
        name = string(row[0])
        print(name)
    except:
        name = None
    
    try:
        d = string(row[1])
    except:
        d = None

    # justification for Site
    try:
        j = string(row[2])
    except:
        j = None

    # year for Site
    try:
        y = int(row[3])
    except:
        y = None

    try:
        area_hectares = int(row[6])
    except:
        area_hectares = None    
    
    s = Site(name=name, description=d, justification=j, 
                 year=y, category=c, states=st, area_hectares=area_hectares)
    s.save()












    # name for Site
    # try:
    #     s = Site.objects.get(name=row[0])
    # except:
    #     print("Inserting Site name",row[0])
    #     s = Site(name=row[0])
    #     s.save()
