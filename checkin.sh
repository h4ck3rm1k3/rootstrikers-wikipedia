cd fech_yaml
filename=`echo $1 | sed -e's/fech_yaml\//\.\//' `
echo commit $filename
git add $filename
git commit -m "adding in new data file $filename"
git push 
