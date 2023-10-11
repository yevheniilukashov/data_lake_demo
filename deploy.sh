REGION=eu-west-1
BRANCH=master
NAME=cloud-data-lake-demo

sam validate && \
sam build --use-container && \
sam deploy --stack-name "$NAME-$BRANCH-$REGION"\
           --region "$REGION"\
           --parameter-overrides "ParameterKey=REGION,ParameterValue=$REGION"\
                                 "ParameterKey=BRANCH,ParameterValue=$BRANCH"\
                                 "ParameterKey=NAME,ParameterValue=$NAME"\
           --capabilities CAPABILITY_NAMED_IAM\
           --resolve-s3