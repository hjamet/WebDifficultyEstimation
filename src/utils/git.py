import git
import os


def get_repo_root():
    """Get the root directory of the git repository."""
    repo = git.Repo(os.path.dirname(__file__), search_parent_directories=True)
    return repo.git.rev_parse("--show-toplevel")
