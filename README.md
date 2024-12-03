# Business questions

Your analytical and business skills are needed to provide clarity in the following aspects:

- How should products be classified into different categories to simplify reports and analysis?
- What is the distribution of product prices across different categories?
-----
### How many products are being discounted?
1. Number of discounted products: 48,741
2. Number of non-discounted products: 128,473
3. Percentage of discounted products: 27.50% 
-----
- How big are the offered discounts as a percentage of the product prices?
- How do seasonality and special dates (Christmas, Black Friday) affect sales?

-----
### How could data collection be improved?

1. Ensure Data Completeness
- Current Observation: Missing or incomplete values can lead to inaccurate analysis, as seen in columns like price, promo_price, and date in your dataset.
- Improvement Suggestion:
Implement validation checks during data entry to ensure all fields are filled.
Use default or estimated values for mandatory fields (e.g., assign a default price for missing products based on category).

2. Improve Data Consistency
- Current Observation: Inconsistent data formats (e.g., price and promo_price as strings instead of numeric) required coercion and cleaning.
- Improvement Suggestion:
Standardize formats for dates, numeric values, and categorical data at the source (e.g., ensuring numeric fields only accept numbers).
Use dropdowns or predefined options for categorical fields like event, type, or state.

-----

