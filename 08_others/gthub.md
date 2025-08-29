```
Git-local
Github-Remote
    1.create repo
    2.git init
    3.git add README.md
      git commit -m "Initial commit"
    4.git remote add origin https://github.com/username/repo-name.git
    5.git add .
      git commit -m "Your commit message"
    6.git push origin main

```
```    
Git Commit - stores in local
Git Push - Push to the remote

Git-Local
├── Git Commit - Stores changes locally

GitHub-Remote
├── 1. Create Repository
├── 2. Initialize Git
│ └── git init
├── 3. Add README and Initial Commit
│ ├── git add README.md
│ └── git commit -m "Initial commit"
├── 4. Connect Remote Repository
│ └── git remote add origin https://github.com/username/repo-name.git

├── 5. Stage and Commit Files
│ ├── git add .
│ └── git commit -m "Your commit message"
└── 6. Push to Remote
└── git push origin main

Note:

Git Commit → Stores changes in local repository.

Git Push → Sends committed changes to GitHub (remote).

```
```
>> git commit -m "Initial commit"
>> git remote add origin https://github.com/username/repo-name.git
>> git push origin main
>>
git : The term 'git' is not recognized as 
the name of a cmdlet, function, script       
file, or operable program. Check the
spelling of the name, or if a path was       
included, verify that the path is correct    
and try again.
At line:1 char:1
+ git init
+ ~~~
    + CategoryInfo          : ObjectNotFoun  
   d: (git:String) [], CommandNotFoundExce   
  ption
    + FullyQualifiedErrorId : CommandNotFou  
   ndException

git : The term 'git' is not recognized as 
the name of a cmdlet, function, script       
file, or operable program. Check the
spelling of the name, or if a path was       
included, verify that the path is correct    
and try again.
At line:2 char:1
+ git add .
+ ~~~
    + CategoryInfo          : ObjectNotFoun  
   d: (git:String) [], CommandNotFoundExce   
  ption
    + FullyQualifiedErrorId : CommandNotFou  
   ndException

git : The term 'git' is not recognized as 
the name of a cmdlet, function, script       
file, or operable program. Check the
spelling of the name, or if a path was       
included, verify that the path is correct    
and try again.
At line:3 char:1
+ git commit -m "Initial commit"
+ ~~~
    + CategoryInfo          : ObjectNotFoun  
   d: (git:String) [], CommandNotFoundExce   
  ption
    + FullyQualifiedErrorId : CommandNotFou  
   ndException

git : The term 'git' is not recognized as 
the name of a cmdlet, function, script       
file, or operable program. Check the
spelling of the name, or if a path was       
included, verify that the path is correct    
and try again.
At line:4 char:1
+ git remote add origin
https://github.com/username/repo-name.git    
+ ~~~
    + CategoryInfo          : ObjectNotFoun  
   d: (git:String) [], CommandNotFoundExce   
  ption
    + FullyQualifiedErrorId : CommandNotFou  
   ndException

git : The term 'git' is not recognized as 
the name of a cmdlet, function, script       
file, or operable program. Check the
spelling of the name, or if a path was       
included, verify that the path is correct    
and try again.
At line:5 char:1
+ git push origin main
+ ~~~
    + CategoryInfo          : ObjectNotFoun  
   d: (git:String) [], CommandNotFoundExce   
  ption
    + FullyQualifiedErrorId : CommandNotFou  
   ndException

PS D:\learn\py> git --version
>>
git : The term 'git' is not recognized as 
the name of a cmdlet, function, script       
file, or operable program. Check the 
spelling of the name, or if a path was 
included, verify that the path is correct 
and try again.
At line:1 char:1
+ git --version
+ ~~~
    + CategoryInfo          : ObjectNotFoun  
   d: (git:String) [], CommandNotFoundExce   
  ption
    + FullyQualifiedErrorId : CommandNotFou  
   ndException

PS D:\learn\py> 
 *  History restored 

PS D:\learn\py> git --version
Reinitialized existing Git repository in D:/learn/py/.git/
PS D:\learn\py> git add .
PS D:\learn\py> git commit -m "Initial commit"
On branch main
nothing to commit, working tree clean
PS D:\learn\py> git remote add origin https://github.com/Monish1662002/learn.git
error: remote origin already exists.
PS D:\learn\py> git push origin main
To https://github.com/Monish1662002/learn.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/Monish1662002/learn.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.   
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
PS D:\learn\py> git pull --rebase origin main
>>
From https://github.com/Monish1662002/learn  
 * branch            main       -> FETCH_HEAD
Successfully rebased and updated refs/heads/main.            git push origin main
Delta compression using up to 12 threads
Compressing objects: 100% (16/16), done.
Writing objects: 100% (22/22), 1.98 KiB | 145.00 KiB/s, done.
Total 22 (delta 9), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (9/9), completed with 1 local object.
To https://github.com/Monish1662002/learn.git
   8169835..86749c0  main -> main
PS D:\learn\py>
```
```
PS D:\learn\py> git init
Reinitialized existing Git repository in D:/learn/py/.git/
PS D:\learn\py> git add errors.md 
fatal: pathspec 'errors.md' did not match any files
PS D:\learn\py> ls


    Directory: D:\learn\py


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        28-08-2025     08:19                others
-a----        28-08-2025     00:57           4895 .gitignore
-a----        28-08-2025     00:57           1084 LICENSE
-a----        28-08-2025     00:57              7 README.md


PS D:\learn\py> git add others/errors.md
PS D:\learn\py> git commit -am errtypes
[main 2d590f4] errtypes
 1 file changed, 69 insertions(+)
 create mode 100644 others/errors.md
PS D:\learn\py> git push origin main
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 1.56 KiB | 398.00 KiB/s, done.
Total 4 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Monish1662002/learn.git
   43a53cb..2d590f4  main -> main
PS D:\learn\py> 
```