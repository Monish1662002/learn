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
