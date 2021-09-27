from Apishka import dnp_dev_details
from Apishka import dnp_dev_calculate
from Apishka import dnp_dev_mass_calculation_from_DB
from SearchBYdomain import add_domains_to_db
from SearchBYdomain2 import search_malware_domains
from SimateouslyEvaluation import calc_s

print("Print 1 for start dnp dev recalculation")
print("Print 2 for mass start dnp dev recalculation from DB")
print("Print 3 for start dnp dev details")
print("Print 4 for start dnp dev re-calculation and details for one domain")
print("Print 5 add domains to db from file Domainllist")
print("Print 6 search malware domains")
print("Print 7  for PRODUCTION calculation from db and file")
print("Print 8 for exit")



val = int(input("Select method: "))
if val == 1:
    dnp_dev_calculate()
elif val == 2:
    dnp_dev_mass_calculation_from_DB()

elif val == 3:
    dnp_dev_details()

elif val == 4:
    dnp_dev_calculate()
    dnp_dev_details()

elif val== 5:
    add_domains_to_db()

elif val== 6:
    search_malware_domains()

elif val == 7:
    calc_s()

elif val == 8:
    exit()
else:
    print("undefined param")

