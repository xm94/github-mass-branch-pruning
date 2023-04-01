# github-mass-branch-pruning

This is a small python script made for the purpose of pruning leftover branches by using the [PyGithub library](https://github.com/PyGithub/PyGithub) (be sure to check them out!)

Note: Be sure to install the `PyGithub` library, not `github`


## Usage

The following config file is read from to determine how branches/PRs are removed

```
{
    "github_token": "<your_token>",
    "target_repo": "org/repo",
    "branch_list": ["main","master","dev","develop","development","stable","prod","production"],
    "delete_prs": false
}
```

The keys in the json correspond with the following:

- **github_token:** This is your github Personal Access Token. To generate one, see [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) in the GitHub docs.
- **target_repo:** The repo you wish to delete branches/PRs from.
- **branch_list:** A list of protected brances you do not wish to have deleted. If the key does not exist in the config file then the following branches will be skipped:
    - `main`,`master`,`dev`,`develop`,`development`,`stable`,`prod`,`production`
- **delete_prs:** A boolean that designates whether you want all open PRs to be closed as well - currently this option does not discriminate based of the branches it is merging to/from, so only set this to true if you want to nuke everything.

To run the script, simply type `python3 prune_branches.py` into the terminal of your choice with the config file propery set-up.