# Custom package
import custom_package
# Depth level 1 sub-directory
from sub.a import a
# Depth level 2 sub-directory
from subs.sub1.b import b
# From direct file
from c import c

custom_package.foo.foo_script.foo()
# custom_package.foo.foo_script.bar() NOT VISIBLE OR CALLABLE

# custom_package.bar.bar_script.bar() VISIBLE BUT NOT CALLABLE

a()
b()
c()
