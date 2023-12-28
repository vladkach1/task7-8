from yandex_tracker_client import TrackerClient

client = TrackerClient(token="y0_AgAAAAASyb3FAAsP9AAAAAD2OH8GaAgI--51SBC8_xBwYR2HI9icPnc", cloud_org_id='bpf458dtgel2lumnc190')

issues = client.issues.get_all()
last_issue = str(issues[0])

try:
    client.issues.create(queue='TEAMCITYBUILDFA', summary=f"Issue № {last_issue[len(last_issue) - 2]}",
                         type={'name': 'Task'})
except Exception as ex:
    print("exception:\n", ex)