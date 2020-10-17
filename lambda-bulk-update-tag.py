import boto3

'''
The code below will add the specified tags to Lambda function in a region.

'''
###############################################################################
REGION = "eu-west-1"
ACCESS_KEY = ""
SECRET_KEY = ""
TAG_KEY = ""
TAG_VALUE = ""
###############################################################################

client = boto3.client('lambda', region_name=REGION,aws_access_key_id=ACCESS_KEY,aws_secret_access_key=SECRET_KEY)


def add_tag(function_arn):
    try:
        add_tag = client.tag_resource(
            Resource=function_arn,
            Tags={
                TAG_KEY: TAG_VALUE
            }
        )
    except:
        print('ERROR! : Could not add tags for function {}'.format(function_arn.split(':')[-1]))

def show_tag(function_arn):
    all_tags = client.list_tags(
        Resource=function_arn
    )

    function_name = function_arn.split(':')[-1]

    try:
        tag_value = all_tags['Tags'][TAG_KEY]
        if tag_value == TAG_VALUE:
            status = True
        else:
            status = False
    except:
        status = False

    if status:
        print('Tag was added to function {}'.format(function_name))
    else:
        print('Tag was not added to function {}'.format(function_name))


all_functions = client.list_functions()

next_marker = ''

while next_marker != '':
    next_marker= ''

    for function in all_functions['Functions']:
        function_arn = function['FunctionArn']
        #print(function_arn)
        add_tag(function_arn)
        show_tag(function_arn)

        if 'NextMarker' in all_functions:
                next_marker = all_functions['NextMarker']
                all_functions = client.list_functions(Marker=next_marker)
