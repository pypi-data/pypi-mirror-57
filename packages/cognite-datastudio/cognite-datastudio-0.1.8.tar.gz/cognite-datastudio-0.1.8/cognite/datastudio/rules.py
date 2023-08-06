import numpy as np
import pandas as pd
import regex as re


def _doRow(row: pd.Series):
    X = row["predicted"]
    Y = row["input"]

    pattern = "[A-Za-z]+|[0-9]+"
    Yalpha = pd.Series(re.findall(pattern, Y))
    Ysepa = pd.Series(re.split(pattern, Y))
    Xalpha = pd.Series(re.findall(pattern, X))
    Xsepa = pd.Series(re.split(pattern, X))
    common, ixX, ixY = np.intersect1d(Xalpha, Yalpha, return_indices=True)
    ixX = pd.Series(ixX)
    ixY = pd.Series(ixY)

    YN = pd.Series(["D" if a.isdigit() else "L" for a in Yalpha])
    YN.loc[ixY] = "[" + YN.loc[ixY] + (1 + ixY.index).astype(str) + "]"
    YNN = [Ysepa[i] + YN[i] for i in range(len(YN))]

    XN = pd.Series(["D" if a.isdigit() else "L" for a in Xalpha])
    XN.loc[ixX] = "[" + XN.loc[ixX] + (1 + ixX.index).astype(str) + "]"
    XNN = [Xsepa[i] + XN[i] for i in range(len(XN))]

    PY = "".join(YNN)
    PX = "".join(XNN)
    return [PY, PX]


def _calcRules(M: pd.DataFrame):
    rule = []
    VAL_Y = M["PY"].value_counts()
    for vc in VAL_Y.index:
        Mred = M[M["PY"] == vc]
        VAL_X = Mred.PX.value_counts()
        for vx in VAL_X.index:
            Mrred = Mred[Mred.PX == vx]
            score = Mrred.score.mean()
            rule.append([vc, vx, VAL_X.loc[vx], score, Mrred.index])

    return pd.DataFrame(
        columns=["Y Pattern", "X Pattern", "num_matches", "avg_score", "match_ix"], data=rule
    ).sort_values(by="num_matches", ascending=False)


def calc_regex_rules(matches: pd.DataFrame):
    A = matches[["predicted", "input"]].apply(_doRow, axis=1, result_type="expand")
    A.columns = ["PY", "PX"]
    A["score"] = matches.score

    return _calcRules(A)
