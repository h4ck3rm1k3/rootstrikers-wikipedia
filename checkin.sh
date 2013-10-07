pathname=$1
filename=$2

pushd $pathname
echo "commit (${pathname},${filename})"
git add $filename
git commit -m "adding in new data file ${pathname}${filename}"
#git push  dont push every file, it will overload the github servers
popd
