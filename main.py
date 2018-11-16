from pymongo import MongoClient
import datetime


# Inserts of the Collection 1 (queries 1, 3 and 4)
# _id = orderkey
def insertsCol1():
    db.drop_collection("col1")
    r = [{
        "_id": 1,
        "orderkey": 1,
        "c_mktsegment": "abcdefghij",
        "o_order_date": datetime.datetime(2018, 11, 18),
        "o_ship_priority": 1,
        "n_name": "France",
        "r_name": "region1",
        "lineitems": [{
            "l_extendedprice": 10,
            "l_discount": 0.6,
            "l_returnflag": 0,
            "l_linestatus": 0,
            "l_quantity": 12,
            "l_shipdate": datetime.datetime(2018, 11, 20),
            "l_tax": 0.2
        },
        {
            "l_extendedprice": 6,
            "l_discount": 0.4,
            "l_returnflag": 1,
            "l_linestatus": 1,
            "l_quantity": 4,
            "l_shipdate": datetime.datetime(2018, 11, 25),
            "l_tax": 1.4
        }],
    },
    {
        "_id": 2,
        "orderkey": 2,
        "c_mktsegment": "segmentno5",
        "o_order_date": datetime.datetime(2020, 5, 19),
        "o_ship_priority": 2,
        "n_name": "France",
        "r_name": "region1",
        "lineitems": [{
            "l_extendedprice": 5,
            "l_discount": 0.2,
            "l_returnflag": 1,
            "l_linestatus": 1,
            "l_quantity": 4,
            "l_shipdate": datetime.datetime(2020, 11, 20),
            "l_tax": 0.2
        },
        {
            "l_extendedprice": 24,
            "l_discount": 0.4,
            "l_returnflag": 0,
            "l_linestatus": 1,
            "l_quantity": 1,
            "l_shipdate": datetime.datetime(2020, 7, 13),
            "l_tax": 1.1
        }],
    },
    {
        "_id": 3,
        "orderkey": 3,
        "c_mktsegment": "segmentno5",
        "o_order_date": datetime.datetime(2019, 8, 15),
        "o_ship_priority": 1,
        "n_name": "Spain",
        "r_name": "region2",
        "lineitems": [{
            "l_extendedprice": 6,
            "l_discount": 0.2,
            "l_returnflag": 0,
            "l_linestatus": 0,
            "l_quantity": 2,
            "l_shipdate": datetime.datetime(2018, 2, 10),
            "l_tax": 1.5
        },
        {
            "l_extendedprice": 10,
            "l_discount": 0.1,
            "l_returnflag": 0,
            "l_linestatus": 1,
            "l_quantity": 2,
            "l_shipdate": datetime.datetime(2018, 2, 10),
            "l_tax": 1.3
        }],
    },
    {
        "_id": 4,
        "orderkey": 4,
        "c_mktsegment": "jaiopambja",
        "o_order_date": datetime.datetime(2020, 5, 19),
        "o_ship_priority": 2,
        "n_name": "Portugal",
        "r_name": "region2",
        "lineitems": [{
            "l_extendedprice": 13,
            "l_discount": 0.1,
            "l_returnflag": 1,
            "l_linestatus": 0,
            "l_quantity": 5,
            "l_shipdate": datetime.datetime(2020, 11, 20),
            "l_tax": 1.1
        },
        {
            "l_extendedprice": 12,
            "l_discount": 0,
            "l_returnflag": 1,
            "l_linestatus": 0,
            "l_quantity": 1,
            "l_shipdate": datetime.datetime(2020, 7, 13),
            "l_tax": 2.5
        }],
    },
    {
        "_id": 5,
        "orderkey": 5,
        "c_mktsegment": "segmentno5",
        "o_order_date": datetime.datetime(2019, 7, 15),
        "o_ship_priority": 1,
        "n_name": "France",
        "r_name": "region1",
        "lineitems": [{
            "l_extendedprice": 6,
            "l_discount": 0.2,
            "l_returnflag": 0,
            "l_linestatus": 0,
            "l_quantity": 4,
            "l_shipdate": datetime.datetime(2019, 2, 16),
            "l_tax": 2
        },
        {
            "l_extendedprice": 11,
            "l_discount": 0.13,
            "l_returnflag": 1,
            "l_linestatus": 1,
            "l_quantity": 6,
            "l_shipdate": datetime.datetime(2020, 7, 13),
            "l_tax": 5.2
        }]
    }]
    return r

# Inserts of the Collection 2 (query 2)
def insertsCol2():
    db.drop_collection("col2")
    r = [{
        "_id": 1,
        "suppkey": 1,
        "s_acctbal": 1.2,
        "s_name": "supplier1",
        "s_address": "carrer a",
        "s_phone": "936120614",
        "s_comment": "comment1",
        "n_name": "France",
        "r_name": "Europe",
        "parts": [{
            "partkey": 1,
            "p_mfgr": "mfgr1",
            "p_size": 2,
            "p_type": "type1",
            "ps_supplycost": 3.5
        },
        {
            "partkey": 2,
            "p_mfgr": "mfgr2",
            "p_size": 2,
            "p_type": "type1",
            "ps_supplycost": 3.5
        }]
    },
    {
        "_id": 2,
        "suppkey": 2,
        "s_acctbal": 2.2,
        "s_name": "supplier2",
        "s_address": "carrer b",
        "s_phone": "9361208568",
        "s_comment": "comment2",
        "n_name": "Catalonia",
        "r_name": "Europe",
        "parts": [{
            "partkey": 3,
            "p_mfgr": "mfgr3",
            "p_size": 2,
            "p_type": "type1",
            "ps_supplycost": 3.5
        },
        {
            "partkey": 4,
            "p_mfgr": "mfgr4",
            "p_size": 2,
            "p_type": "type2",
            "ps_supplycost": 11
        }]
    },
    {
        "_id": 3,
        "suppkey": 3,
        "s_acctbal": 5.1,
        "s_name": "supplier3",
        "s_address": "carrer c",
        "s_phone": "9361246457",
        "s_comment": "comment3",
        "n_name": "Andorra",
        "r_name": "Europe",
        "parts": [{
            "partkey": 5,
            "p_mfgr": "mfgr5",
            "p_size": 4,
            "p_type": "type1",
            "ps_supplycost": 3.5
        },
        {
            "partkey": 6,
            "p_mfgr": "mfgr2",
            "p_size": 2,
            "p_type": "type2",
            "ps_supplycost": 3.5
        }]
    },
    {
        "_id": 4,
        "suppkey": 4,
        "s_acctbal": 5.2,
        "s_name": "supplier4",
        "s_address": "carrer 4",
        "s_phone": "93612025352",
        "s_comment": "comment4",
        "n_name": "Swaziland",
        "r_name": "Africa",
        "parts": [{
            "partkey": 7,
            "p_mfgr": "mfgr6",
            "p_size": 2,
            "p_type": "type1",
            "ps_supplycost": 3.5
        },
        {
            "partkey": 8,
            "p_mfgr": "mfgr8",
            "p_size": 2.42,
            "p_type": "type2",
            "ps_supplycost": 52
        }]
    }
    ]
    return r


mclient = MongoClient('mongodb://localhost:27017/')
db = mclient['test-database']
db.col1.insert(insertsCol1())
db.col2.insert(insertsCol2())

# $unwind = subdocuments
# $match = where
# $group = select amb operacions
# _id de $group = group by
# $sort = order by asc(1) or desc(-1)
# $project = includes (1) or suppresses (0) fields

# query 1
# _id = l_returnflag, l_linestatus (group by)

date = datetime.datetime(2019, 2, 16)
result_q1 = db.col1.aggregate([
    {"$unwind": "$lineitems"},
    {"$match": {"lineitems.l_shipdate": {"$lte": date}}},
    {"$group": {
        "_id": {"l_returnflag": "$lineitems.l_returnflag", "l_linestatus": "$lineitems.l_linestatus"},
        "sum_qty": {"$sum": "$lineitems.l_quantity"},
        "sum_base_price": {"$sum": "$lineitems.l_extendedprice"},
        "sum_disc_price": {"$sum":
                               {"$multiply": ["$lineitems.l_extendedprice", {"$subtract": [1, "$lineitems.l_discount"]}]}
                           },
        "sum_charge": {"$sum": {
            "$multiply": [{"$multiply":
                           ["$lineitems.l_extendedprice", {"$subtract": [1, "$lineitems.l_discount"]}]},
                          {"$add": [1, "$lineitems.l_tax"]}]
        }},
        "avg_qty":  {"$avg": "$lineitems.l_quantity"},
        "avg_price": {"$avg": "$lineitems.l_extendedprice"},
        "avg_discount": {"$avg": "$lineitems.l_discount"},
        "count_order": {"$sum": 1}
    }},
    {"$project": {
        "_id": 0,
        "l_returnflag": "$_id.l_returnflag",
        "l_linestatus": "$_id.l_linestatus",
        "sum_qty": 1, "sum_base_price": 1, "sum_disc_price": 1, "sum_charge": 1,
        "avg_qty": 1, "avg_price": 1, "avg_discount": 1, "count_order": 1
    }},
    {"$sort": {"l_returnflag": 1, "l_linestatus": 1}}
])

print("Query 1:")
print(list(result_q1))

# query 2
region2 = "Europe"
result_qaux = db.col2.aggregate([
    {"$unwind": "$parts"},
    {"$match": {"r_name": region2}},
    {"$group": {"_id": 0, "ps_supplycost": {"$min": "$parts.ps_supplycost"}}}
])

minim = list(result_qaux)[0]['ps_supplycost']
size = 2
type1 = "type1"
result_q2 = db.col2.aggregate([
    {"$unwind": "$parts"},
    {"$match": {"parts.p_size": size, "parts.p_type": {"$regex": type1},
                "r_name": region2, "parts.ps_supplycost": minim}
    },
    {"$project": {
        "_id": 0,
        "s_acctbal": 1,
        "s_name": 1,
        "n_name": 1,
        "partkey": "$parts.partkey",
        "p_mfgr": "$parts.p_mfgr",
        "s_address": 1,
        "s_phone": 1,
        "s_comment": 1
    }},
    {"$sort": {"s_acctbal": -1, "n_name": 1, "s_name": 1, "partkey": 1}}
])
print("Query 2:")
print(list(result_q2))

# query 3
segment = "segmentno5"
date1 = datetime.datetime(2020, 2, 16)
date2 = datetime.datetime(2018, 1, 10)
result_q3 = db.col1.aggregate([
    {"$unwind": "$lineitems"},
    {"$match": {"c_mktsegment": segment, "o_order_date": {"$lt": date1}, "lineitems.l_shipdate": {"$gt": date2}}},
    {"$group": {
        "_id": {"orderkey": "$orderkey", "o_order_date": "$o_order_date", "o_ship_priority": "$o_ship_priority"},
        "revenue": {"$sum": {"$multiply": ["$lineitems.l_extendedprice", {"$subtract": [1, "$lineitems.l_discount"]}]}},
    }},
    {"$project": {
        "_id": 0,
        "orderkey": "$_id.orderkey",
        "revenue": 1,
        "o_order_date": "$_id.o_order_date",
        "o_ship_priority": "$_id.o_ship_priority"
    }},
    {"$sort": {"revenue": -1, "o_order_date": 1}}
])
print("Query 3:")
print(list(result_q3))

# query 4
date4 = datetime.datetime(2019, 6, 1)
region = "region2"
result_q4 = db.col1.aggregate([
    {"$unwind": "$lineitems"},
    {"$match": {
        "r_name": region,
        "o_order_date": {"$gte": date4, "$lt": (date4.replace(year=date4.year + 1))}
    }},

    {"$group": {
        "_id": {"n_name": "$n_name"},
        "revenue": {"$sum": {"$multiply": ["$lineitems.l_extendedprice", {"$subtract": [1, "$lineitems.l_discount"]}]}}
    }},
    {"$project": {
        "_id": 0,
        "n_name": "$_id.n_name",
        "revenue": 1
    }},
    {"$sort": {"revenue": -1}}
])
print("Query 4:")
print(list(result_q4))