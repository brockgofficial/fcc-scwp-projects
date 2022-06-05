#Import third party modules
import sys
from pytest import main

#Import in-house modules/packages
from arithmetic_arranger import arithmetic_arranger

#Custom tests for debugging
# personal_tests = [
#     (["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False),
#     (['3801 - 2', '123 + 49'], False),
#     (["320 + 698", "3801 - 384", "45 + 43", "32 + 457", "120 - 67"], True)
# ]

# for item in personal_tests:
#     print(arithmetic_arranger(item[0], item[1]))
#     print("\n")

#Run unit tests automatically
sys.exit(main())