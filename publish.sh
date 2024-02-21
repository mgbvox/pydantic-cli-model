poetry version patch
v=$(poetry version)
git add . ; git commit -m "publish version $v"; git push
poetry build
poetry publish
