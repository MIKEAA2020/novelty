#!/usr/bin/env bash
# Bootstrap GitHub access for the novelty project — survives session resets.
# The PAT is stored OUTSIDE git in /home/z/my-project/secrets/ (chmod 600).
# Run this at the start of any future session that needs GitHub access.
set -e
BASE=/home/z/my-project
SECRETS=$BASE/secrets
TOKEN=$(cat $SECRETS/github_pat.txt)
REPO=MIKEAA2020/novelty

# 1. Restore git identity + credential helper (points at the persistent store).
git config --global credential.helper "store --file=$SECRETS/git-credentials"
git config --global user.name "MIKEAA2020"
git config --global user.email "63320461+MIKEAA2020@users.noreply.github.com"

# 2. Ensure the clone exists and its remote carries the token.
if [ ! -d "$BASE/novelty/.git" ]; then
  git clone "https://MIKEAA2020:${TOKEN}@github.com/${REPO}.git" "$BASE/novelty"
fi
git -C "$BASE/novelty" remote set-url origin "https://MIKEAA2020:${TOKEN}@github.com/${REPO}.git"

# 3. Pull latest (the repo may have been updated externally, e.g. new alien readings).
git -C "$BASE/novelty" pull --ff-only origin main || true

# 4. Verify the token still works.
curl -s -m 20 -H "Authorization: Bearer ${TOKEN}" https://api.github.com/user | grep -m1 '"login"' || echo "WARNING: token failed verification"

echo "GitHub access restored. Clone: $BASE/novelty"
