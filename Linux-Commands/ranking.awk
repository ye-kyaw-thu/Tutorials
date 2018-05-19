#demo of awk script file

BEGIN {OFS=", "; print "### Rank of Restaurants ###\n";}
$1 ~ /Restaurant$/ {print NR, $1, $5}
END {print "\n===== End of list ===== "}
