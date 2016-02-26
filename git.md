
# Git Tutorial

## 1. Create a directory to host your files.
```bash
mkdir BI028
cd BI028
```

## 2. Initiate the repository
```bash
git init
```

## 3. Add files
```bash
git add README.md
```

## 4. See status
```bash
git status
```

## 5. Commit
```bash
git commit -m "Add README.md"
```

## 6. Roll back
```bash
git reset --hard HEAD^
# git reset --hard ee568
```

## 7. Roll forward
```bash
git reflog
git reset --hard ee568
```


## 8. delete the file
```bash
git rm README.md
git commit -m "Delete README.md"
## get back the file from the repository
git checkout -- README.md
```

## 9. submit to online repository
```bash
#git remote rm bi028
git remote add bi028 git@git.com:ricket-sjtu/BI028
git push -u bi028 master
```
