from jira.client import JIRA
from credentials import username, password

options = {'server': 'https://jira.b2xcare.com'}

jira = JIRA(options, basic_auth=(username, password))
projects = jira.projects()
#print(projects)

# issues = jira.search_issues('assignee='+username)
# print(issues)

ticketName = str(input("Enter the ticket name: "))
issue = jira.issue(ticketName)

command = str(input("Enter option for following task: 1. Get a story into current sprint 2. Move Story 3. Update Story Points 4. Read Story's Description & comments 5. Add work log to specific ticket "))

if command == "1":
    boards = jira.boards()
    # print('boards ', boards)
    board_id = 220
    sprints = jira.sprints(board_id)
    # for sprint in sprints:
    #     print('%s: %s ' % (sprint.id, sprint.name))
    sprintId = sprints[-1].id
    # print(sprints[-1].name)
    # jira.add_issues_to_sprint(220, sprintId)
    # jira.assign_issue(issue.id, username)
    # storyPoints = int(input("Enter story points: "))
    # issue.update(fields={'customfield_10021': storyPoints})         # --> Story Points
    # issue.update(fields={'customfield_10904': {'id': "11568"}})     # --> Team
elif command == "2":
    print(issue.id)

    # transitions = jira.transitions(issue)
    # ticketStatus = str(input("What you want to do with it: "))
    #
    # if ticketStatus != "inprogress" and ticketStatus != "resolve":
    #     print("Please enter proper status")
    # else:
    #     print([(t['id'], t['name']) for t in transitions])
    #     # print(issue.fields.status)
    #     if ticketStatus == "inprogress":
    #         jira.transition_issue(issue, '4')
    #     elif ticketStatus == "resolve":
    #         jira.transition_issue(issue, '5')
    #     else:
    #         print("Something went wrong!!")


    # issues = jira.search_issues('project=PP')
    #
    # for issue in issues:
    #     print (issue.key, 'Status: ',issue.fields.status)
elif command == "3":
    # for field_name in issue.raw['fields']:
    #     print("Field:", field_name, "Value:", issue.raw['fields'][field_name])

    storyPoints = int(input("Enter story points: "))
    # print(storyPoints)
    issue.update(fields={'customfield_10021': storyPoints})
elif command == "4":
    print("Description ")
    print(issue.raw['fields']['description'])
    print("========================================================================")
    print("Comments ")
    print(issue.fields.comment.comments)
elif command == "5":
    timeSpent = str(input("Please enter the time you want to log (eg. 3w 4d 12h 30m): "))
    jira.add_worklog(issue, timeSpent=timeSpent, timeSpentSeconds=None, adjustEstimate=None, newEstimate=None,
                     reduceBy=None, comment=None, started=None, user=None)
else:
    print("Invalid input")