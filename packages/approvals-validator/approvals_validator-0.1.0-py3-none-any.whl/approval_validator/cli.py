from typing import Tuple

import click

import cli_utils
from change_set import ChangeSet


@click.command(context_settings={'help_option_names': ['-h', '--help']},
               options_metavar="REQUIRED_FLAGS")
@click.option("--approvers",
              "-a",
              required=True,
              type=cli_utils.UsernameList(),
              help="Username(s) of approvals.")
@click.option("--changed-files",
              "-c",
              required=True,
              type=cli_utils.FileList(),
              help="File paths.")
def validate_approvals(approvers: Tuple[str], changed_files: Tuple[str]):
    """
    Validate that the correct approvals have been received to approve changes
    to the given files.

    Note: Multiple approvers and/or changed files can be passed as CSV strings.

    Example:

      validate_approvals --approvers alovelace,eclarke \\
                           --changed-files src/com/twitter/follow/Follow.java
    """
    changes = ChangeSet(approvers, changed_files)
    if changes.approved:
        click.secho("Approved", fg="green")
    else:
        click.secho("Insufficient approvals", fg="red")


if __name__ == "__main__":
    validate_approvals()
