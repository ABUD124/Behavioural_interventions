import pandas as pd
from ..helper import generate_output_file_csv
from ..constant import CM_NAME


def filter_data(df, field_of_intervention=None, intervention_type=None, building_type=None):
    filtered_df = df.copy()  # Make a copy of the original DataFrame

    # Apply filters based on user input
    if field_of_intervention and field_of_intervention.lower() != 'all':
        filtered_df = filtered_df[filtered_df['Field_of_intervention'].str.lower() == field_of_intervention.lower()]
    if intervention_type and intervention_type.lower() != 'all':
        filtered_df = filtered_df[filtered_df['Type_of_intervention'].str.lower() == intervention_type.lower()]
    if building_type and building_type.lower() != 'all':
        filtered_df = filtered_df[filtered_df['Building_type'].str.lower() == building_type.lower()]

    return filtered_df


def calculation(output_directory, inputs_parameter_selection):
    # Extract inputs from inputs_parameter_selection
    field_of_intervention = str(inputs_parameter_selection["field_of_intervention"])
    intervention_type = str(inputs_parameter_selection["intervention_type"])
    building_type = str(inputs_parameter_selection["building_type"])

    # Read the data from CSV
    df_path = 'app/api_v1/my_calculation_module_directory/Input_data/cleaned_data.csv'
    df = pd.read_csv(df_path) 

    output_csv_path1 = generate_output_file_csv(output_directory)

    # Filter the data
    filtered_data = filter_data(df, field_of_intervention=field_of_intervention, intervention_type=intervention_type,
                                building_type=building_type)

    # Save filtered data to CSV

    filtered_data.to_csv(output_csv_path1, index=False)

    result = dict()
    result['name'] = CM_NAME
    result["csv_files"] = [{"name": "filtering_behavioural_interventions", "path": output_csv_path1}]

    return result
