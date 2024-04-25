import pandas as pd

def filter_data(df, field_of_intervention=None, intervention_type=None, space_filter=None):
    filtered_df = df.copy()  # Make a copy of the original DataFrame

    # Apply filters based on user input
    if field_of_intervention:
        filtered_df = filtered_df[filtered_df['Field_of_intervention'].str.lower() == field_of_intervention.lower()]
    if intervention_type:
        filtered_df = filtered_df[filtered_df['Type_of_intervention'].str.lower() == intervention_type.lower()]
    if space_filter:
        for col in ['Residential', 'Office', 'Educational', 'Other']:
            if space_filter.get(col) == 'Y':
                filtered_df = filtered_df[filtered_df[col].str.lower() == 'y']

    # Convert filtered data to JSON
    filtered_json = filtered_df.to_json(orient='records')

    return filtered_json