# get input
f = open('day_2\input.text', 'r')

# convert each line to list of ints and store
reports = []
for row in f.readlines():
    report = row.split(' ')
    report_ints = list(map(int, report))
    reports.append(report_ints)

# define function to determine safety
def determine_safety(report):
    status = 'safe'
    direction = 'asc' if report[1] - report[0] >= 1 else 'desc'
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if direction == 'asc' and (diff <= 0 or diff > 3):
            status = 'unsafe'
            break
        if direction == 'desc' and (diff >= 0 or diff < -3):
            status = 'unsafe'
            break
    return status

# loop through reports and determine safety status
safe_reports = 0

for i in range(len(reports)):
    report_status = determine_safety(reports[i])
    if report_status == 'safe':
        safe_reports += 1

print(safe_reports)

