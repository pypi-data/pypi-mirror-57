# use indexes and compute them only once
# use a tree search and only show interesting results
# implement near!
# - entity near + next finding next to it (limited to places?)

import re
import sys
import itertools
from collections import Counter
from pprint import pprint
from dateutil.relativedelta import relativedelta as rd
import numpy as np
import pandas as pd
import just

from nostalgia.base_df import DF, Results, registry, get_type_from_registry
from nostalgia.nlp import nlp_registry, get_ts, find_entities, n

find_entitites = find_entities

#

# all_res = Results.merge(*registry.values())


# days = {}
# for i in range(300):
#     days[i] = len(all_res.at_time(last_days(i), last_days(i - 1)).type.value_counts())

# option = [k for k, v in days.items() if v == max(days.values())][0]

# res = all_res.at_time(last_days(option), last_days(option - 1), sort_diff=False)

# res = all_res.at_time("2019-10-01 14:00", "2019-10-01 15:00", sort_diff=False)

# res = all_res.at_time("2019-06-19 10:00", "2019-06-19 15:00", sort_diff=False)

# questions = []
# for x in just.read("~/gits/WikiSQL/data/train.jsonl"):
#     if x["question"].lower().startswith("what") or x["question"].lower().startswith("name"):
#         continue
#     questions.append((x["question"], x["sql"]["conds"]))


# orders = emails[emails.subject.str.contains("your order", case=False, na=False)]
# payments.at_time(orders.iloc[0].timestamp, hours=2)

# start = places.travel_by_car().index.left - pd.Timedelta(minutes=5)
# end = places.travel_by_car().index.left
# tmp_locs = DF(
#     pd.DataFrame({"start": start, "end": end}, index=pd.IntervalIndex.from_arrays(start, end)),
#     "tmp",
# )
# join_time(tmp_locs, payments.at_time("this month"))

# payments.by_me().expenses.at("gas station").at_time("last month").sum()

# payments.containing("CCV").near(places.near_work())
# registering "me" and "me_email" globally

# for i in xrange(num_dims + 1):
#   for permutation in itertools.permutations(xrange(num_dims), i):

# payments.amount_between(10, 100).expenses.at_time(start, end).containing("shell|shopping")


def applier(i, start, flt):
    if not isinstance(start, DF):
        if isinstance(start, pd.Series):
            return start
        start = registry[start.tp.lower()]
    if start.df_name.endswith("places") and flt.tp == "Places":
        tmp = registry["places"]
        start = start.at(flt.cls_fn(tmp))
    elif flt.tp in ["DF", "MP"]:
        start = flt.cls_fn(start)
    # # actually, start is not there so does not work | only works when mixing types (but not even then)
    # elif start.df_name == "places" and flt.tp != "Places":
    #     # bugged / very slow
    #     tmp = flt.cls_fn(registry[flt.tp.lower()])
    #     start = tmp.when_at(start)
    elif start.df_name.lower() != flt.tp.lower():
        raise ValueError("Diff type: {} {} {}".format(start.df_name, flt.tp, flt))
    else:
        start = flt.cls_fn(start)
    return start


def apply_all(ents):
    start = ents[0]
    for i, e in enumerate(ents[1:]):
        try:
            start = applier(i, start, e)
        except (ValueError, TypeError) as e:
            print(e)
            return None
    return start


def uniquer(ents):
    seen = set()
    results = []
    for x in ents:
        key = (x.tp, x.orig_word)
        if key in seen:
            continue
        results.append(x)
        seen.add(key)
    return results


def filtering(ents, time):
    results = []
    for x in ents:
        if hasattr(x, "norm"):
            for y in x.norm:
                if y.role == time:
                    results.append(y)
        elif x.role == time:
            results.append(x)
    return uniquer(results)


def filter_expansion(filters):
    seen = set()
    results = []
    start = 1  # max(0, len(filters) - 1)
    for i in range(start, len(filters) + 1):
        for x in itertools.combinations(filters, i):
            results.append(list(x))
    # split when "supermarket" in "supermarkets"
    results2 = []
    for res in results:
        res2 = []
        seen = set()
        for x in res:
            for y in res:
                if x == y:
                    continue
                a = x.orig_word[:-1] if x.orig_word.endswith("s") else x.orig_word
                b = y.orig_word[:-1] if y.orig_word.endswith("s") else y.orig_word
                if a not in seen and a == b:
                    res2.append((x, y))
                    seen.add(a)
                    break
            else:
                res2.append(x)
                a = x.orig_word[:-1] if x.orig_word.endswith("s") else x.orig_word
                seen.add(a)
        results2.append(list(itertools.product(res2)))
    results2 = [[y[0] for y in x] for x in results2]
    results = []
    for x in results2:
        for y in x:
            if isinstance(y, tuple):
                break
        else:
            results.append(x)
    return results


def filter_generic_when_specific(results):
    # filtering X vs specific
    # return results
    seen = {}
    results2 = []
    for score, res in results:
        words = tuple([(y.orig_word) for y in res])
        seen[words] = max(score, seen.get(words, -1000))
    for score, res in results:
        if score < seen[words]:
            continue
        results2.append((score, res))
    return results2


def visualize_path(res_infos):
    objs = []
    for res_info in res_infos:
        if res_info.role == "start":
            objs.append(res_info.tp)
        else:
            cls_fn = str(res_info.cls_fn).split()[1].split(".")[-1]
            if cls_fn == "att_inner":
                fn_name = res_info.cls.split(".")[-1] + "()"
            elif cls_fn == "col_contains":
                fn_name = "col_contains({!r}, {!r})".format(res_info.orig_word, res_info.col_name)
            elif cls_fn == "at_time":
                fn_name = "at_time({!r})".format(res_info.orig_word)
            else:
                fn_name = cls_fn + "()"
            objs.append(fn_name)
    return ".".join(objs)


def smerger(text):
    ents = find_entities(text)
    results = []
    starts = filtering(ents, "start")
    filters = filtering(ents, "filter")
    ends = filtering(ents, "end")
    # think about hierarchy!?
    time_higher = bool([x for x in ends if "last" in x.orig_word])
    ends = [x for x in ends if not time_higher or x.orig_word != "when"]
    for x in starts:
        flt = []
        expansions = filter_expansion(filters)
        for filter_group in expansions:
            ys = []
            for y in filter_group:
                # if x.tp != y.tp and (
                #     x.tp not in ["DF", "MP", "Places"] and y.tp not in ["DF", "MP", "Places"]
                # ):
                #     continue
                ys.append(y)
            if ys:
                # "last" stuff at the end
                ys = sorted(ys, key=lambda x: "last" in x.orig_word)
                res = []
                for z in ends:
                    res.append([x] + ys + [z])
                if not res:
                    res.append([x] + ys)
                flt.extend(res)
        if not flt:
            # end should be type specicifc?
            for z in ends:
                flt.append([x, z])
            print("should try with mixed types?")
        results.extend(flt)
    # scoring based on purity?
    results = [(sum([y.tp != "DF" for y in x]) - len(set([y.tp for y in x])), x) for x in results]
    # filtering X vs specific
    results = filter_generic_when_specific(results)
    results = results[-10:]
    # appliers
    results = [(x, apply_all(x[1]), visualize_path(x[1])) for x in results]
    results = [x for x in results if x[1] is not None]
    # sort scoring
    results = sorted(results, key=lambda x: (bool(x[0][1]) * len([(y.orig_word) for y in x[0][1]])))
    rep = [
        (
            [(y.orig_word) for y in x[0][1]],
            x,
            (bool(x[0][1]), len([(y.orig_word) for y in x[0][1]])),
            x[2],
        )
        for x in results
    ]
    return rep


# heartrate
# no browsing
# on couch


# find_entities("what is the address of work")

# find_entities("how much did i pay in amsterdam")
# smerger("how long did i stay at work last friday")


# smerger("Show me when I visited work last")

# where have i been last week
# what phones did i see
# what laptops did i google
# what lenovo pages did i visit
# what thinkpad pages did i visit
# what were the offers for me
# how much did i spend last week
# how much did i work last year
# how much did i spend on gas last week
# how often did i visit google yesterday

# find_entities("how much did I spend")

# # does not work yet because no mixing types
# sm = smerger("when did i last go to the cinema")

# sm = smerger("when was the last time i visited utrecht")

# sm = smerger("how much did i spend last time I visited a bar")

# sm = smerger("how much did I spend at bars in novi sad last year")

# sm = smerger("when was the last time I visited a supermarket")

# text = "how many times have i been to work"
# sm = smerger(text)

# # exclude "i" since it is already in the generic keywords (being more specific)
# # maybe need to defer it

# find_entities("how much did I spend at bars in novi sad last year")

# find_entities("when was the last time I visited a supermarket")

# for e in find_entities("when was the last time I visited a supermarket"):
#     print(e)
#     for n in e.norm:
#         print(n)
#     print()

# payments.when_at(places.containing("bar")).last()

# Result.merge(pics, emails, web_history, page_visit, places)

# pics.when_at(places.containing("amsterdam"))

# payments.when_at(places.containing("bar")).last().sum()

# offers.when_at(payments.containing("bijenkorf"), days=3)

# payments.at_time("last 20 months").containing("Shopping Center")

# places[places.city == "Edinburgh"]


# (
#     payments.by_card.at_time("last 3 months")
#     .amount_between(30, 70)
#     .when_at(places.containing("Driving|Gas station"))
# )

# # # # #

# from spacy_api.tree_view import TreeView
# from spacy import load
# nlp = load("en")
# tv = TreeView(nlp)
# tv("how much did I spend at bars in novi sad last year")
# tv("when was the last time I visited a supermarket")

# (
#     payments.by_card.at_time("last 3 months")
#     .amount_between(30, 70)
#     .when_at(places.containing("Driving|Gas station"))
# ).bedrag.sum()
# payments.containing("texaco").at_time("last 3 months")
# payments.containing("gas").at_time("last 3 months")
# payments.at_time("last 3 months").containing("gas")
# payments.at_time("last 3 months")
# payments.at_time("last 3 months").containing("gas")
# payments.at_time("last 3 months").containing("bp")
# payments.containing("bp")
