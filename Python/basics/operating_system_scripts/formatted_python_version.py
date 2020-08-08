import sys

v_info = sys.version_info

tuple_v = v_info[:3]

v = list(tuple_v)

test_list = [str(i) for i in v]

print('.'.join(test_list))
