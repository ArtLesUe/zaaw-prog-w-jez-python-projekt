git reset --hard
git clean -f -d -x
git fetch --all
git pull
cp -v ../.env.example ../.env
