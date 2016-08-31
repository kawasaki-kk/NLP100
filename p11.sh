cat hightemp.txt
echo --------sed------------
sed -e "s/\t/ /g" hightemp.txt

echo ---------tr--------------
cat hightemp.txt
cat hightemp.txt | tr '\t' ' '


echo ---------expand--------------
cat hightemp.txt
expand -t 1 hightemp.txt
