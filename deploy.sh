sam validate && \
sam build --use-container && \
sam deploy --stack-name "data-platform" \
           --resolve-s3 \
           --capabilities CAPABILITY_NAMED_IAM 
           