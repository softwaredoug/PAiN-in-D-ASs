import pandas as pd

def get_kids(fam: pd.DataFrame) -> pd.DataFrame:
    return fam[fam['age'] <= 18]

def pay_allowance(kids: pd.DataFrame) -> pd.DataFrame:
    """Use poor pandas code to give kids money."""

    def give_kid_money(kid: pd.Series, bonus_per_kid: dict) -> pd.Series:
        kid['moneyz'] = 0
        if kid.at['name'].startswith('Ian'):
            kid['moneyz'] += 5 + bonus_per_kid['Ian']
        elif kid.at['name'].startswith('Murray'):
            kid['moneyz'] += 5 + bonus_per_kid['Murray']

        return kid

    # should just be a merge, but trying to demonstrate a point ;)
    return pd.DataFrame(kids.apply(give_kid_money, axis=1, bonus_per_kid={'Ian': 10000, 'Murray': 5000}))



if __name__ == "__main__":

    family = pd.DataFrame([{"age": 22, "name": "Doug Turnbull"},
                           {"age": 22, "name": "Khara Turnbull"},
                           {"age": 10, "name": "Ian Turnbull"},
                           {"age": 6,  "name": "Murray Turnbull"}])
    print(family.groupby('age')['age'].sum())
    print(family.max(axis=1))
    kids = get_kids(family)
    kids_with_moneyz = pay_allowance(kids)
    print(kids_with_moneyz)
