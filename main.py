from Apishka import dnp_dev_details
from Apishka import tr_demo_calculate
from Apishka import tr_demo_details
from Apishka import live_calculate
from Apishka import dnp_dev_calculate
from Apishka import dnp_dev_mass_calculation_from_DB
from SearchBYdomain import add_domains_to_db
from SearchBYdomain import look_at_db
from SearchBYMalwareDomains import search_malware_domains
from SimateouslyEvaluationLive import calc_s
from SimateouslyEvaluationStage import DNPTRStageCalc
from SearchBYdomain import check_api_code_request

print("Print 1 for start live calculation")
print("Print 2 for start dnp dev calculation")
print("Print 3 for mass start dnp dev recalculation from DB")
print("Print 4 for start dnp dev details")
print("Print 5 for start calculation and details for one domain on DNP/TR")
print("Print 6 add domains to db from file Domainllist")
print("Print 7 search malware domains")
print("Print 8  for PRODUCTION calculation from db and file")
print("Print 9 look at DB or check response code")
print("Print x to exit")



val = int(input("Select method: "))
if val== 1:
    live_calculate()
if val == 2:
    dnp_dev_calculate()
elif val == 3:
    dnp_dev_mass_calculation_from_DB()

elif val == 4:
    dnp_dev_details()

elif val == 5:
    print("1 - calculation on stage Trustratings",
          "2 - calculation on dev Dnprotect")
    value = int(input("Select method: "))
    if value == 1:
        tr_demo_calculate()
        tr_demo_details()
    elif value == 2:
        dnp_dev_calculate()
        dnp_dev_details()
    else:
        print("undefined param")


elif val== 6:
    add_domains_to_db()

elif val== 7:
    search_malware_domains()

elif val == 8:
    print("1 - simulateously calculation on stage",
          "2 - simulateously calculation on live")
    value = int(input("Select method: "))
    if value == 1:
        DNPTRStageCalc()
    elif value == 2:
        calc_s()
    else:
        print("undefined param")

elif val == 9:
    print("1 - DB domains info",
          "2 - check for error codes")
    value = int(input("Select method: "))
    if value ==1:
        look_at_db()
    elif value==2:
        check_api_code_request()
    else:
        print("undefined param")
elif str(val)=='x':
    exit()
else:
    print("undefined param")

