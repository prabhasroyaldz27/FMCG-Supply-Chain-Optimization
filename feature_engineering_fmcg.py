import pandas as pd

df = pd.read_csv('your_dataset.csv')

# Demand Supply Ratio
df['demand_supply_ratio'] = df['num_refill_req_l3m'] / (df['product_wg_ton'] + 1)

# Warehouse Capacity Utilization
df['warehouse_capacity_utilization'] = df['product_wg_ton'] / df['WH_capacity_size']

# Demand per Retail Shop
df['demand_per_retail_shop'] = df['num_refill_req_l3m'] / (df['retail_shop_num'] + 1)

# Transport Issues Impact
df['transport_issues_impact'] = df['transport_issue_l1y'] * df['num_refill_req_l3m']

# Competitor Influence
df['competitor_influence'] = df['Competitor_in_mkt'] / (df['num_refill_req_l3m'] + 1)

# Distance to Production Hub
df['distance_to_production_hub'] = df['dist_from_hub']

# Supply Chain Efficiency
df['supply_chain_efficiency'] = (df['retail_shop_num'] + df['distributor_num']) / ((df['transport_issue_l1y'] + 1) * (df['num_refill_req_l3m'] + 1))

df.to_csv('feature_engineered_dataset.csv', index=False)
