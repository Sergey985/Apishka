from Apishka import dnp_dev_details
from Apishka import dnp_dev_calculate
from Apishka import start_evaluation_calculate
from SearchBYdomain import add_domains_to_db
from SearchBYdomain2 import search_malware_domains
from SimateouslyEvaluation import start_evaluation


print("Print 1 for start dnp dev recalculation")
print("Print 2 for mass start dnp dev recalculation from DB")
print("Print 3 for start dnp dev details")
print("Print 4 for start dnp dev recalculation and details")
print("Print 5 add domains to db")
print("Print 6 search malware domains")

print("Print 8 for exit")



val = int(input("Select method: "))
if val == 1:
    dnp_dev_calculate()
elif val == 2:
    start_evaluation_calculate()

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
    start_evaluation()
elif val == 8:
    exit()
else:
    print("undefined param")

