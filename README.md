
# Prerequisites:
- `git`
- ['uv'](https://docs.astral.sh/uv/getting-started/installation/)
- an `ssh` key (`ssh-keygen`) on POSIX systems, (idx on Windows, will edit whenever I get a Win machine to mess around with) linked to your GitHub account, so you can push and pull to and from this repository. 

# Part 1 Instructions:
- `git clone` this repository
- `checkout` your own branch from this repository using `git checkout -b <name of your branch>`
Uh oh! There seems to be a `.env` with company secrets! We might lose $0.03 if this stays in the repository! Quick! 
- First, remove the file from git with `git rm .env`

- Then, commit this change with `git commit -m "<some message indicating you saved our company's life>"`
- Finally, push this to your branch! Fast! Use `git push`
- Wait... It only exists on your device. Use `git push --set-upstream origin <name of your branch>` to create a remote branch and push this to it!. 
Let's make a backup, just in case. Can't be too careful!. 

- `git tag backup-before-cleanup`
Great. But someone could just click on commits and take a peek at that key. Let's remove that. 
Secret methods: 
- `git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch .env' --prune-empty HEAD`

Whoa. That's a LOT of text. What does this do? 
Well:
- `--force` overwrites the current backup
- `--index filter` goes through the git index for each commit 
- `git rm --cached --ignore-unmatch .env` will remove the `.env` from each index, and will ignore it if it doesn't exist
- `--prune-empty` will remove commits that are empty after filtering
- `HEAD` is current branch only (your branch, basically instead of the main branch). You should be pushing only to this with the `--force` flag. 
Speaking of which, let's do that. 

- `git push origin --force <your branch name>`
Phew. Done. Now, to avoid this, again, let's add the `.env` to a special file for git called the `.gitignore`. 

You can either copy this into your terminal, use the `.sh` script I've included, or the `.bat` file (untested, use at your own risk...)

```
echo ".env" >> .gitignore
git add .gitignore
git commit -m "I'm a big dummy and forgot to gitignore my .env"
git push 
```
# Part 2 Instructions (If Time)

# Extra Notes:
- DO NOT EDIT THE `DO_NOT_EDIT.py` FILE (There's nothing really interesting in there). Feel free to take a look in there, since there is a helpful function you will be using in there. 

- In `main.py`
