from __future__ import print_function, unicode_literals
from ..lib.handler.youtrack_handler import YoutrackHandler
from ..lib.handler.github_handler import GithubHandler
from ..lib.handler import git_handler as git
from ..lib.config import Config
from ..lib.logger import Logger
from ..lib.handler import prompt_utils

import re

youtrack = YoutrackHandler()
github = GithubHandler()
logger = Logger()
config = Config().load()


def entrypoint(args):
    git.is_dirty(args.project)

    if args.card:
        issue = youtrack.get_issue(args.card)
    else:
        slug = ask_project_slug()
        issue = select_card(slug)

    checkout_branch(args.project, issue)

    youtrack.assign_to(issue["id"], "me")

    youtrack.update_state(issue["id"], config["youtrack"]["picked_state"])


def ask_project_slug():
    return prompt_utils.ask_questions_input(
        'Inserisci slug progetto Youtrack: ', config["youtrack"]["default_project_prefix"])


def ask_board():
    boards = youtrack.get_boards()
    choices = [{"name": i["name"], "value": i["name"]} for i in boards]
    return prompt_utils.ask_choices(
        'Seleziona board: ', choices, config["youtrack"]["default_board_name"])


def select_card(slug):
    board = ask_board()
    issues = youtrack.get_issues(
        slug,
        "Board {}: {{Current Sprint}}".format(
            board
        ),
        0,
        100
    )
    choices = [{"name": issue_label(i), "value": i} for i in issues if i["State"] in ["ToDo", "In Progress"]]
    return prompt_utils.ask_choices(
        'Seleziona card: ', choices)


def issue_label(issue):
    return "{} {}".format(issue["id"], issue["summary"])


def checkout_branch(project, issue):
    branch_name = prompt_utils.ask_questions_input("Inserisci nome del branch: ", re.sub(
        r'([\s\\.~\^:\[\]"\'?]|[^\x00-\x7F])+', "-", issue["summary"]
    ).lower())

    parent_branch_name = prompt_utils.ask_questions_input(
        "Inserisci branch iniziale: ", "master")

    branch_type = issue["Type"].lower().replace(" ", "-")

    branch_name = "{}/{}/{}".format(
        branch_type, branch_name, issue["id"]
    )

    git.checkout(project, parent_branch_name)

    git.checkout(project, branch_name)
