from lhub_extractors import feature_extractor

@feature_extractor
def feature_extractor_func(node_metadata, node_output_table):
    '''
    Extract out feature from node_output_table
    :param str column1: Column String
    :param int column2: Column Number
    '''

    # feature_extraction code
    col1_is_valid = False
    col1 = node_output_table['column1']
    for col in col1:
      # check data in col1
      col1_is_valid = True

    col2_is_valid = False
    col2 = node_output_table['column2']
    for col in col2:
       # check data in col2
       col2_is_valid = True

    feature_result = {
      'feature': col1_is_valid and col2_is_valid
    }

    return feature_result
