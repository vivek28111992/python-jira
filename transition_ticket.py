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

command = str(input("Enter option for following task: \n 1. Get a story into current sprint \n 2. Move Story \n 3. Update Story Points \n 4. Read Story's Description & comments \n 5. Add work log to specific ticket \n 6. Assign Ticket To Me \n 7. Create sub-task of this issue \n"))

if command == "1":
    boards = jira.boards()
    # print('boards ', boards)
    board_id = 220
    sprints = jira.sprints(board_id)
    # for sprint in sprints:
    #     print('%s: %s ' % (sprint.id, sprint.name))
    sprintId = int(sprints[-1].id)
    issueId = str(issue.id)
    issueIdList = list()
    issueIdList.append(issueId)    
    # print(issue.id)
    # print("issue key ", issueIdList)
    jira.assign_issue(issue.id, username)
    jira.add_issues_to_sprint(sprintId, issueIdList)
    storyPoints = int(input("Enter story points: "))
    issue.update(fields={'customfield_10021': storyPoints})         # --> Story Points
    issue.update(fields={'customfield_10904': {'id': "11568"}})     # --> Team
elif command == "2":
    # print(issue.id)

    transitions = jira.transitions(issue)
    print([(t['id'], t['name']) for t in transitions])
    print(issue.fields.status)
    ticketStatus = str(input("What you want to do with this issue: \n 1. Inprogress \n 2. Resolve \n 3. Reopen Issue \n"))
    
    if ticketStatus != "1" and ticketStatus != "2":
        print("Please enter proper status")
    else:
        if ticketStatus == "1":
            jira.transition_issue(issue, '4')
        elif ticketStatus == "2":
            jira.transition_issue(issue, '5')
        elif ticketStatus == "3":
            jira.transition_issue(issue, '3')
        else:
            print("Please select option either 1, 2 or 3")


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
    print("========================================================================")
    print("Description ")
    print(issue.raw['fields']['description'])
    print("========================================================================")
    print("Comments ")
    print(issue.fields.comment.comments)
elif command == "5":
    timeSpent = str(input("Please enter the time you want to log (eg. 3w 4d 12h 30m): "))
    jira.add_worklog(issue, timeSpent=timeSpent, timeSpentSeconds=None, adjustEstimate=None, newEstimate=None, reduceBy=None, comment=None, started=None, user=None)
elif command == "6":
    jira.assign_issue(issue.id, username)
elif command == "7":
    summary = str(input("Please enter summary: "))
    description = str(input("Plese enter description: "))

    rootnn_dict = {
    'summary' : summary,
    'description' : description,
    'issuetype' : { 'name' : 'Sub-task' },
    'parent' : { 'id' : issue.id},
    }

    jira.create_issue(fields=rootnn_dict)
else:
    print("Invalid input")