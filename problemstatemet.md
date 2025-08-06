# 📦 Business Problem  

A FMCG company has entered into the instant noodles business two years back.  
The higher management has noticed that there is a mismatch in the demand and supply.  

- Where the demand is high, supply is pretty low  
- Where the demand is low, supply is pretty high  

In both cases, it results in an **inventory cost loss** to the company.  
Hence, the higher management wants to optimize the **supply quantity** in each and every warehouse across the country.  

# 📑 Data Dictionary  

| **Variable** | **Business Definition** |
|--------------|--------------------------|
| Ware_house_ID | Product warehouse ID |
| WH_Manager_ID | Employee ID of warehouse manager |
| Location_type | Warehouse location (city or village) |
| WH_capacity_size | Storage capacity size of the warehouse |
| zone | Zone of the warehouse |
| WH_regional_zone | Regional zone of the warehouse under each zone |
| num_refill_req_l3m | Number of times refilling was done in the last 3 months |
| transport_issue_l1y | Transport issues (accident or theft) reported in the last 1 year |
| Competitor_in_mkt | Number of instant noodles competitors in the market |
| retail_shop_num | Number of retail shops selling the product |
| wh_owner_type | Warehouse ownership type (company-owned or rented) |
| distributor_num | Number of distributors between warehouse and retail shops |
| flood_impacted | Indicator: Warehouse located in a flood-impacted area |
| flood_proof | Indicator: Flood-proof warehouse |
| electric_supply | Indicator: Electric backup (e.g., generator) available |
| dist_from_hub | Distance (km) from warehouse to production hub |
| workers_num | Number of workers in the warehouse |
| wh_est_year | Year the warehouse was established |
| storage_issue_reported_l3m | Storage issues reported in the last 3 months (e.g., rat, fungus) |
| temp_reg_mach | Indicator: Temperature regulating machine available |
| approved_wh_govt_certificate | Type of government-issued certificate |
| wh_breakdown_l3m | Number of breakdowns in the last 3 months (e.g., strike, flood, power failure) |
| govt_check_l3m | Number of government inspections in the last 3 months |
| product_wg_ton | Product shipped in the last 3 months (in tons) |
