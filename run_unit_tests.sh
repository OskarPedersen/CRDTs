find unit_test_*enc -execdir encorec {} \;
find unit_test_* -not -name "*.enc" -execdir {} \;
find unit_test_* -not -name "*.enc" -execdir rm {} \;
