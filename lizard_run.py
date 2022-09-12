import lizard
import pandas as pd
import flask

cc = lizard.analyze_file("lizard_test.py")

print(cc.CCN)
