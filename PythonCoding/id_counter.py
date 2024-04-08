# 9) Counter.
# We have a list with identifiers of form “id-SITE”. Calculate how many ids we have per site.

# 10) Top counter.
# We have a list with identifiers of form “id-SITE”. Show the top 3 sites. You can break ties in any way you want.

ids = [
    'xgc8wnman8sh3-ID',
    'bnh9chddv8ik2-IN',
    'jsn8wnman9sh3-IN',
    'ofk8okshd7lf7-PL',
    'ovf8ujedn6sh3-PL',
    'yhv8wnman8sh1-PL',
    'vfj8pskdn3uj5-UA'
]


def id_counter(elements: list) -> dict:
    counter = dict()
    for elem in elements:
        site = elem[-2:]
        counter[site] = counter.get(site, 0) + 1
    return counter


print(id_counter(ids))


def top_counter(elements: list) -> dict:
    counter_dict = id_counter(elements)
    sorted_key_3 = sorted(counter_dict, reverse=True, key=counter_dict.get)[:3]
    return {key: counter_dict[key] for key in sorted_key_3}


print(top_counter(ids))
