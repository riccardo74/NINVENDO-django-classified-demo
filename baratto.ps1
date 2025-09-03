# PowerShell Script per fare il merge del branch baratto in master
# Salva come: merge-baratto.ps1

param(
    [switch]$Force,
    [switch]$DeleteBranch
)

# Colori per output
function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    } else {
        $input | Write-Output
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

function Write-Success { Write-ColorOutput Green $args }
function Write-Warning { Write-ColorOutput Yellow $args }
function Write-Error { Write-ColorOutput Red $args }
function Write-Info { Write-ColorOutput Cyan $args }

# 1. Vai nella directory del progetto
Write-Info "=== NAVIGATING TO PROJECT DIRECTORY ==="
$ProjectPath = "C:\Users\riki_\Documents\GitHub\NINVENDO-django-classified-demo"

if (Test-Path $ProjectPath) {
    Set-Location $ProjectPath
    Write-Success "✅ Changed to: $ProjectPath"
} else {
    Write-Error "❌ Project directory not found: $ProjectPath"
    exit 1
}

# 2. Verifica lo stato corrente
Write-Info "`n=== CURRENT STATUS ==="
try {
    Write-Output "Current directory: $(Get-Location)"
    git status --porcelain
    if ($LASTEXITCODE -ne 0) { throw "Git status failed" }
    
    Write-Output "`nAvailable branches:"
    git branch -a
} catch {
    Write-Error "❌ Error checking git status: $_"
    exit 1
}

# 3. Controlla se ci sono modifiche non committate
$gitStatus = git status --porcelain
if ($gitStatus -and -not $Force) {
    Write-Warning "⚠️  You have uncommitted changes:"
    Write-Output $gitStatus
    $response = Read-Host "`nDo you want to continue anyway? (y/N)"
    if ($response -notmatch '^[Yy]$') {
        Write-Info "Merge cancelled by user"
        exit 0
    }
}

# 4. Passa al branch master
Write-Info "`n=== SWITCHING TO MASTER ==="
try {
    git checkout master
    if ($LASTEXITCODE -ne 0) { throw "Failed to checkout master" }
    Write-Success "✅ Switched to master branch"
} catch {
    Write-Error "❌ Error switching to master: $_"
    exit 1
}

# 5. Aggiorna master (se hai un remote)
Write-Info "`n=== UPDATING MASTER BRANCH ==="
try {
    git pull origin master 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Success "✅ Master updated from remote"
    } else {
        Write-Warning "⚠️  No remote origin found or pull failed, continuing..."
    }
} catch {
    Write-Warning "⚠️  Could not update from remote, continuing..."
}

# 6. Verifica che il branch baratto esista
Write-Info "`n=== CHECKING BARATTO BRANCH ==="
$barattoBranch = git branch --list baratto
if (-not $barattoBranch) {
    Write-Error "❌ Branch 'baratto' not found!"
    Write-Output "Available branches:"
    git branch -a
    exit 1
} else {
    Write-Success "✅ Branch 'baratto' found"
}

# 7. Esegui il merge
Write-Info "`n=== MERGING BARATTO INTO MASTER ==="
$commitMessage = @"
Merge branch 'baratto' into master

- Add complete trade/barter system
- Integration with django-classified  
- User authentication and social login
- FSM state management for trades
- Feedback and messaging system
- Template integration and UI
- Enhanced user experience with crispy forms
- Real-time trade status management
"@

try {
    git merge baratto --no-ff -m $commitMessage
    if ($LASTEXITCODE -ne 0) { throw "Merge failed" }
    Write-Success "✅ MERGE COMPLETED SUCCESSFULLY!"
} catch {
    Write-Error "❌ MERGE FAILED!"
    Write-Warning "Check for conflicts and resolve them manually:"
    git status
    Write-Info "`nTo resolve conflicts:"
    Write-Info "1. Edit conflicted files"
    Write-Info "2. Run: git add ."
    Write-Info "3. Run: git commit"
    exit 1
}

# 8. Mostra il risultato
Write-Info "`n=== MERGE RESULT ==="
Write-Output "Recent commits:"
git log --oneline -5 --graph

# 9. Push su remote (se esiste)
Write-Info "`n=== PUSHING TO REMOTE ==="
try {
    git push origin master 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Success "✅ Changes pushed to remote"
    } else {
        Write-Warning "⚠️  Could not push to remote (no remote configured?)"
    }
} catch {
    Write-Warning "⚠️  Could not push to remote"
}

# 10. Opzione per eliminare il branch baratto
if ($DeleteBranch) {
    Write-Info "`n=== DELETING BARATTO BRANCH ==="
    try {
        git branch -d baratto
        Write-Success "✅ Branch 'baratto' deleted locally"
        
        # Elimina anche dal remote se esiste
        git push origin --delete baratto 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Success "✅ Branch 'baratto' deleted from remote"
        }
    } catch {
        Write-Warning "⚠️  Could not delete branch 'baratto'"
    }
} else {
    Write-Info "`n=== CLEANUP OPTION ==="
    $response = Read-Host "Do you want to delete the 'baratto' branch? (y/N)"
    if ($response -match '^[Yy]$') {
        try {
            git branch -d baratto
            Write-Success "✅ Branch 'baratto' deleted locally"
            
            # Chiedi se eliminare anche dal remote
            $remoteResponse = Read-Host "Delete from remote too? (y/N)"
            if ($remoteResponse -match '^[Yy]$') {
                git push origin --delete baratto 2>$null
                if ($LASTEXITCODE -eq 0) {
                    Write-Success "✅ Branch 'baratto' deleted from remote"
                } else {
                    Write-Warning "⚠️  Could not delete from remote"
                }
            }
        } catch {
            Write-Warning "⚠️  Could not delete branch 'baratto': $_"
        }
    } else {
        Write-Info "Branch 'baratto' preserved"
    }
}

# 11. Status finale
Write-Info "`n=== FINAL STATUS ==="
Write-Output "Current branches:"
git branch

Write-Output "`nRecent commits:"
git log --oneline -3

Write-Success "`n🎉 MERGE PROCESS COMPLETED!"
Write-Info "Your Django classified project now includes the complete bartering system!"

# Suggerimenti finali
Write-Info "`n=== NEXT STEPS ==="
Write-Output "1. Run migrations: python manage.py migrate"
Write-Output "2. Collect static files: python manage.py collectstatic"  
Write-Output "3. Test the application: python manage.py runserver"
Write-Output "4. Check trade functionality at /trade/"