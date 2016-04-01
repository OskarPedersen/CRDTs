find unit_test_*enc -type f -execdir encorec {} \;
find unit_test_* -not -name "*.enc" -type f -execdir {} \; -execdir printf "\n" \;
find unit_test_* -not -name "*.enc" -type f -execdir rm {} \;
