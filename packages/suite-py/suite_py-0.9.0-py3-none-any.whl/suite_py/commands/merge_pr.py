from __future__ import print_function, unicode_literals
from ..lib.handler.youtrack_handler import YoutrackHandler
from ..lib.handler.github_handler import GithubHandler
from ..lib.handler.captainhook_handler import CaptainHook
from ..lib.config import Config
from ..lib.logger import Logger
from ..lib.handler import prompt_utils
from ..lib.qainit import qainit_shutdown
from ..lib.handler import git_handler as git
from ..lib.handler import drone_handler as drone
import os
import sys
import re

youtrack = YoutrackHandler()
github = GithubHandler()
logger = Logger()
lock = CaptainHook()
config = Config().load()


def entrypoint(args):
    stop_if_master_locked(args.project)

    pr = select_pr(args.project)
    branch_name = pr.head.ref

    if not pr.mergeable or pr.mergeable_state != "clean":
        logger.error("Impossibile fare il merge. Controlla che le review siano positive o che la build non sia fallita. {}".format(pr.html_url))
        sys.exit(-1)

    logger.info("Eseguo il merge...")

    merge_status = pr.merge(
        commit_title="{} (#{})".format(pr.title, pr.number), commit_message='', merge_method='squash')

    if not merge_status.merged:
        logger.error("Si è verificato un errore durante il merge.")
        sys.exit(-1)

    drone_build = get_drone_build(args.project, merge_status.sha)

    if drone_build:
        logger.info(
            "Pull request mergiata su master! Puoi seguire lo stato della build su {}".format(drone_build))
    else:
        logger.info("Pull request mergiata su master!")

    logger.info("Cancello il branch da github...")

    if git.delete_remote_branch(args.project, branch_name):
        logger.info("Branch remoto eliminato.")
    else:
        logger.error("Si è verificato un errore durante la cancellazione del branch remoto.")
        logger.error("Elimina il branch manualmente da {}".format(pr.html_url))

    if prompt_utils.ask_confirm("Vuoi bloccare staging? (Necessario se bisogna testare su staging)".format(args.project), default=False):
        lock.lock_project(args.project)

    logger.info("Aggiorno lo stato della card su youtrack...")
    if update_card(branch_name):
        logger.info("Card aggiornata")
    else:
        logger.warning("Non sono riuscito a trovare una issue YouTrack nel nome del branch o la issue indicata non esiste.\
            Nessuna card aggiornata su YouTrack")

    logger.info("Spengo il qa, se esiste")
    qainit_branch = "{}_{}".format(git.get_git_username(), branch_name)
    qainit_shutdown(qainit_branch)

    logger.info("Tutto fatto!")
    sys.exit()


def select_pr(project):
    prs = github.get_list_pr(project)

    choices = [{"name": "{} {}".format(i.number, i.title), "value": i} for i in prs]
    return prompt_utils.ask_choices('Seleziona PR: ', choices)


def stop_if_master_locked(project):
    request = lock.status(project)
    if request.status_code != 200:
        logger.error("Impossibile determinare lo stato del lock su master.")
        sys.exit(-1)

    if request.json()["locked"]:
        logger.error("Il progetto è lockato su master. Impossibile continuare.")
        sys.exit(-1)


def get_drone_build(project, sha):
    drone_build = drone.get_pr_build_url(
        project, sha)
    if drone_build != "":
        return drone_build
    return None


def update_card(branch_name):
    id_card = youtrack.get_card_from_name(branch_name)

    if id_card:
        youtrack.update_state(id_card, config["youtrack"]["merged_state"])
        return True
    else:
        return False
