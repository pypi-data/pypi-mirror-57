# mypy_boto3

Mypy-friendly type annotations for `boto3 1.10.40`.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy_boto3](#mypyboto3)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)
  - [Submodules](#submodules)

## How to use

This package by itself is not very useful, it just gives you access to all
underlying `boto3` services type annotations.

It is the biggest package, so if you want to save 4 MB of space, install
service packages directly, e.g. `pip install mypy-boto3-s3 mypy-boto3-ec2`

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for services that you use to get type checking working.

```bash
# You can find a full list of modules below
python -m pip install boto3-stubs[s3,ec2]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import s3
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_s3 as s3

# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("s3")
client: s3.EC2Client = boto3.client("s3")

# Oh, it must be `Bucket`... Thanks, mypy!
client.create_bucket(bucket="bucket")
```

### Code auto-complete

Not a single Python IDE supports `Literal` type overloads yet (but in `VSCode` support is just around the corner).
Meanwhile, to have a nice auto-complete you can explicitly set types to help your IDE to get methods, arguments etc.

```python
import boto3_name

from mypy_boto3 import ec2

# this is the only place where you have to set types explicitly
client: ec2.EC2Client = boto3.client("ec2")
resource: ec2.EC2ServiceResource = boto3.resource("ec2")

# now you have auto-complete for methods, arguments and even return types
```

### Build services index

This packages provides a CLI to build services index for `boto3-stubs`.

```bash
# Use this command when you add or remove service packages
python -m mypy_boto3
```

## How it works

Fully automated [builder](https://github.com/vemel/mypy_boto3) carefully generates
type annotations for each service, patiently waiting for `boto3` updates. It delivers
a drop-in type annotations for you and makes sure that:

- Latest version of `boto3` is used.
- Each public class and method of every `boto3` service gets valid type annotations
  extracted from latest documentation (blame `botocore` docs if types are incorrect).
- Type annotations include up-to-date documentation.
- Code is processed by [black](https://github.com/psf/black) for readability.

## Submodules

- `boto3-stubs[essential]` - Type annotations for `cloudformation`, `dynamodb`, `ec2`, `lambda`, `rds`, `s3` and `sqs` services.
- `boto3-stubs[accessanalyzer]` - Type annotations for `accessanalyzer` service.
- `boto3-stubs[acm]` - Type annotations for `acm` service.
- `boto3-stubs[acm-pca]` - Type annotations for `acm-pca` service.
- `boto3-stubs[alexaforbusiness]` - Type annotations for `alexaforbusiness` service.
- `boto3-stubs[amplify]` - Type annotations for `amplify` service.
- `boto3-stubs[apigateway]` - Type annotations for `apigateway` service.
- `boto3-stubs[apigatewaymanagementapi]` - Type annotations for `apigatewaymanagementapi` service.
- `boto3-stubs[apigatewayv2]` - Type annotations for `apigatewayv2` service.
- `boto3-stubs[appconfig]` - Type annotations for `appconfig` service.
- `boto3-stubs[application-autoscaling]` - Type annotations for `application-autoscaling` service.
- `boto3-stubs[application-insights]` - Type annotations for `application-insights` service.
- `boto3-stubs[appmesh]` - Type annotations for `appmesh` service.
- `boto3-stubs[appstream]` - Type annotations for `appstream` service.
- `boto3-stubs[appsync]` - Type annotations for `appsync` service.
- `boto3-stubs[athena]` - Type annotations for `athena` service.
- `boto3-stubs[autoscaling]` - Type annotations for `autoscaling` service.
- `boto3-stubs[autoscaling-plans]` - Type annotations for `autoscaling-plans` service.
- `boto3-stubs[backup]` - Type annotations for `backup` service.
- `boto3-stubs[batch]` - Type annotations for `batch` service.
- `boto3-stubs[budgets]` - Type annotations for `budgets` service.
- `boto3-stubs[ce]` - Type annotations for `ce` service.
- `boto3-stubs[chime]` - Type annotations for `chime` service.
- `boto3-stubs[cloud9]` - Type annotations for `cloud9` service.
- `boto3-stubs[clouddirectory]` - Type annotations for `clouddirectory` service.
- `boto3-stubs[cloudformation]` - Type annotations for `cloudformation` service.
- `boto3-stubs[cloudfront]` - Type annotations for `cloudfront` service.
- `boto3-stubs[cloudhsm]` - Type annotations for `cloudhsm` service.
- `boto3-stubs[cloudhsmv2]` - Type annotations for `cloudhsmv2` service.
- `boto3-stubs[cloudsearch]` - Type annotations for `cloudsearch` service.
- `boto3-stubs[cloudsearchdomain]` - Type annotations for `cloudsearchdomain` service.
- `boto3-stubs[cloudtrail]` - Type annotations for `cloudtrail` service.
- `boto3-stubs[cloudwatch]` - Type annotations for `cloudwatch` service.
- `boto3-stubs[codebuild]` - Type annotations for `codebuild` service.
- `boto3-stubs[codecommit]` - Type annotations for `codecommit` service.
- `boto3-stubs[codedeploy]` - Type annotations for `codedeploy` service.
- `boto3-stubs[codeguru-reviewer]` - Type annotations for `codeguru-reviewer` service.
- `boto3-stubs[codeguruprofiler]` - Type annotations for `codeguruprofiler` service.
- `boto3-stubs[codepipeline]` - Type annotations for `codepipeline` service.
- `boto3-stubs[codestar]` - Type annotations for `codestar` service.
- `boto3-stubs[codestar-notifications]` - Type annotations for `codestar-notifications` service.
- `boto3-stubs[cognito-identity]` - Type annotations for `cognito-identity` service.
- `boto3-stubs[cognito-idp]` - Type annotations for `cognito-idp` service.
- `boto3-stubs[cognito-sync]` - Type annotations for `cognito-sync` service.
- `boto3-stubs[comprehend]` - Type annotations for `comprehend` service.
- `boto3-stubs[comprehendmedical]` - Type annotations for `comprehendmedical` service.
- `boto3-stubs[compute-optimizer]` - Type annotations for `compute-optimizer` service.
- `boto3-stubs[config]` - Type annotations for `config` service.
- `boto3-stubs[connect]` - Type annotations for `connect` service.
- `boto3-stubs[connectparticipant]` - Type annotations for `connectparticipant` service.
- `boto3-stubs[cur]` - Type annotations for `cur` service.
- `boto3-stubs[dataexchange]` - Type annotations for `dataexchange` service.
- `boto3-stubs[datapipeline]` - Type annotations for `datapipeline` service.
- `boto3-stubs[datasync]` - Type annotations for `datasync` service.
- `boto3-stubs[dax]` - Type annotations for `dax` service.
- `boto3-stubs[detective]` - Type annotations for `detective` service.
- `boto3-stubs[devicefarm]` - Type annotations for `devicefarm` service.
- `boto3-stubs[directconnect]` - Type annotations for `directconnect` service.
- `boto3-stubs[discovery]` - Type annotations for `discovery` service.
- `boto3-stubs[dlm]` - Type annotations for `dlm` service.
- `boto3-stubs[dms]` - Type annotations for `dms` service.
- `boto3-stubs[docdb]` - Type annotations for `docdb` service.
- `boto3-stubs[ds]` - Type annotations for `ds` service.
- `boto3-stubs[dynamodb]` - Type annotations for `dynamodb` service.
- `boto3-stubs[dynamodbstreams]` - Type annotations for `dynamodbstreams` service.
- `boto3-stubs[ebs]` - Type annotations for `ebs` service.
- `boto3-stubs[ec2]` - Type annotations for `ec2` service.
- `boto3-stubs[ec2-instance-connect]` - Type annotations for `ec2-instance-connect` service.
- `boto3-stubs[ecr]` - Type annotations for `ecr` service.
- `boto3-stubs[ecs]` - Type annotations for `ecs` service.
- `boto3-stubs[efs]` - Type annotations for `efs` service.
- `boto3-stubs[eks]` - Type annotations for `eks` service.
- `boto3-stubs[elastic-inference]` - Type annotations for `elastic-inference` service.
- `boto3-stubs[elasticache]` - Type annotations for `elasticache` service.
- `boto3-stubs[elasticbeanstalk]` - Type annotations for `elasticbeanstalk` service.
- `boto3-stubs[elastictranscoder]` - Type annotations for `elastictranscoder` service.
- `boto3-stubs[elb]` - Type annotations for `elb` service.
- `boto3-stubs[elbv2]` - Type annotations for `elbv2` service.
- `boto3-stubs[emr]` - Type annotations for `emr` service.
- `boto3-stubs[es]` - Type annotations for `es` service.
- `boto3-stubs[events]` - Type annotations for `events` service.
- `boto3-stubs[firehose]` - Type annotations for `firehose` service.
- `boto3-stubs[fms]` - Type annotations for `fms` service.
- `boto3-stubs[forecast]` - Type annotations for `forecast` service.
- `boto3-stubs[forecastquery]` - Type annotations for `forecastquery` service.
- `boto3-stubs[frauddetector]` - Type annotations for `frauddetector` service.
- `boto3-stubs[fsx]` - Type annotations for `fsx` service.
- `boto3-stubs[gamelift]` - Type annotations for `gamelift` service.
- `boto3-stubs[glacier]` - Type annotations for `glacier` service.
- `boto3-stubs[globalaccelerator]` - Type annotations for `globalaccelerator` service.
- `boto3-stubs[glue]` - Type annotations for `glue` service.
- `boto3-stubs[greengrass]` - Type annotations for `greengrass` service.
- `boto3-stubs[groundstation]` - Type annotations for `groundstation` service.
- `boto3-stubs[guardduty]` - Type annotations for `guardduty` service.
- `boto3-stubs[health]` - Type annotations for `health` service.
- `boto3-stubs[iam]` - Type annotations for `iam` service.
- `boto3-stubs[imagebuilder]` - Type annotations for `imagebuilder` service.
- `boto3-stubs[importexport]` - Type annotations for `importexport` service.
- `boto3-stubs[inspector]` - Type annotations for `inspector` service.
- `boto3-stubs[iot]` - Type annotations for `iot` service.
- `boto3-stubs[iot-data]` - Type annotations for `iot-data` service.
- `boto3-stubs[iot-jobs-data]` - Type annotations for `iot-jobs-data` service.
- `boto3-stubs[iot1click-devices]` - Type annotations for `iot1click-devices` service.
- `boto3-stubs[iot1click-projects]` - Type annotations for `iot1click-projects` service.
- `boto3-stubs[iotanalytics]` - Type annotations for `iotanalytics` service.
- `boto3-stubs[iotevents]` - Type annotations for `iotevents` service.
- `boto3-stubs[iotevents-data]` - Type annotations for `iotevents-data` service.
- `boto3-stubs[iotsecuretunneling]` - Type annotations for `iotsecuretunneling` service.
- `boto3-stubs[iotthingsgraph]` - Type annotations for `iotthingsgraph` service.
- `boto3-stubs[kafka]` - Type annotations for `kafka` service.
- `boto3-stubs[kendra]` - Type annotations for `kendra` service.
- `boto3-stubs[kinesis]` - Type annotations for `kinesis` service.
- `boto3-stubs[kinesis-video-archived-media]` - Type annotations for `kinesis-video-archived-media` service.
- `boto3-stubs[kinesis-video-media]` - Type annotations for `kinesis-video-media` service.
- `boto3-stubs[kinesis-video-signaling]` - Type annotations for `kinesis-video-signaling` service.
- `boto3-stubs[kinesisanalytics]` - Type annotations for `kinesisanalytics` service.
- `boto3-stubs[kinesisanalyticsv2]` - Type annotations for `kinesisanalyticsv2` service.
- `boto3-stubs[kinesisvideo]` - Type annotations for `kinesisvideo` service.
- `boto3-stubs[kms]` - Type annotations for `kms` service.
- `boto3-stubs[lakeformation]` - Type annotations for `lakeformation` service.
- `boto3-stubs[lambda]` - Type annotations for `lambda` service.
- `boto3-stubs[lex-models]` - Type annotations for `lex-models` service.
- `boto3-stubs[lex-runtime]` - Type annotations for `lex-runtime` service.
- `boto3-stubs[license-manager]` - Type annotations for `license-manager` service.
- `boto3-stubs[lightsail]` - Type annotations for `lightsail` service.
- `boto3-stubs[logs]` - Type annotations for `logs` service.
- `boto3-stubs[machinelearning]` - Type annotations for `machinelearning` service.
- `boto3-stubs[macie]` - Type annotations for `macie` service.
- `boto3-stubs[managedblockchain]` - Type annotations for `managedblockchain` service.
- `boto3-stubs[marketplace-catalog]` - Type annotations for `marketplace-catalog` service.
- `boto3-stubs[marketplace-entitlement]` - Type annotations for `marketplace-entitlement` service.
- `boto3-stubs[marketplacecommerceanalytics]` - Type annotations for `marketplacecommerceanalytics` service.
- `boto3-stubs[mediaconnect]` - Type annotations for `mediaconnect` service.
- `boto3-stubs[mediaconvert]` - Type annotations for `mediaconvert` service.
- `boto3-stubs[medialive]` - Type annotations for `medialive` service.
- `boto3-stubs[mediapackage]` - Type annotations for `mediapackage` service.
- `boto3-stubs[mediapackage-vod]` - Type annotations for `mediapackage-vod` service.
- `boto3-stubs[mediastore]` - Type annotations for `mediastore` service.
- `boto3-stubs[mediastore-data]` - Type annotations for `mediastore-data` service.
- `boto3-stubs[mediatailor]` - Type annotations for `mediatailor` service.
- `boto3-stubs[meteringmarketplace]` - Type annotations for `meteringmarketplace` service.
- `boto3-stubs[mgh]` - Type annotations for `mgh` service.
- `boto3-stubs[migrationhub-config]` - Type annotations for `migrationhub-config` service.
- `boto3-stubs[mobile]` - Type annotations for `mobile` service.
- `boto3-stubs[mq]` - Type annotations for `mq` service.
- `boto3-stubs[mturk]` - Type annotations for `mturk` service.
- `boto3-stubs[neptune]` - Type annotations for `neptune` service.
- `boto3-stubs[networkmanager]` - Type annotations for `networkmanager` service.
- `boto3-stubs[opsworks]` - Type annotations for `opsworks` service.
- `boto3-stubs[opsworkscm]` - Type annotations for `opsworkscm` service.
- `boto3-stubs[organizations]` - Type annotations for `organizations` service.
- `boto3-stubs[outposts]` - Type annotations for `outposts` service.
- `boto3-stubs[personalize]` - Type annotations for `personalize` service.
- `boto3-stubs[personalize-events]` - Type annotations for `personalize-events` service.
- `boto3-stubs[personalize-runtime]` - Type annotations for `personalize-runtime` service.
- `boto3-stubs[pi]` - Type annotations for `pi` service.
- `boto3-stubs[pinpoint]` - Type annotations for `pinpoint` service.
- `boto3-stubs[pinpoint-email]` - Type annotations for `pinpoint-email` service.
- `boto3-stubs[pinpoint-sms-voice]` - Type annotations for `pinpoint-sms-voice` service.
- `boto3-stubs[polly]` - Type annotations for `polly` service.
- `boto3-stubs[pricing]` - Type annotations for `pricing` service.
- `boto3-stubs[qldb]` - Type annotations for `qldb` service.
- `boto3-stubs[qldb-session]` - Type annotations for `qldb-session` service.
- `boto3-stubs[quicksight]` - Type annotations for `quicksight` service.
- `boto3-stubs[ram]` - Type annotations for `ram` service.
- `boto3-stubs[rds]` - Type annotations for `rds` service.
- `boto3-stubs[rds-data]` - Type annotations for `rds-data` service.
- `boto3-stubs[redshift]` - Type annotations for `redshift` service.
- `boto3-stubs[rekognition]` - Type annotations for `rekognition` service.
- `boto3-stubs[resource-groups]` - Type annotations for `resource-groups` service.
- `boto3-stubs[resourcegroupstaggingapi]` - Type annotations for `resourcegroupstaggingapi` service.
- `boto3-stubs[robomaker]` - Type annotations for `robomaker` service.
- `boto3-stubs[route53]` - Type annotations for `route53` service.
- `boto3-stubs[route53domains]` - Type annotations for `route53domains` service.
- `boto3-stubs[route53resolver]` - Type annotations for `route53resolver` service.
- `boto3-stubs[s3]` - Type annotations for `s3` service.
- `boto3-stubs[s3control]` - Type annotations for `s3control` service.
- `boto3-stubs[sagemaker]` - Type annotations for `sagemaker` service.
- `boto3-stubs[sagemaker-a2i-runtime]` - Type annotations for `sagemaker-a2i-runtime` service.
- `boto3-stubs[sagemaker-runtime]` - Type annotations for `sagemaker-runtime` service.
- `boto3-stubs[savingsplans]` - Type annotations for `savingsplans` service.
- `boto3-stubs[schemas]` - Type annotations for `schemas` service.
- `boto3-stubs[sdb]` - Type annotations for `sdb` service.
- `boto3-stubs[secretsmanager]` - Type annotations for `secretsmanager` service.
- `boto3-stubs[securityhub]` - Type annotations for `securityhub` service.
- `boto3-stubs[serverlessrepo]` - Type annotations for `serverlessrepo` service.
- `boto3-stubs[service-quotas]` - Type annotations for `service-quotas` service.
- `boto3-stubs[servicecatalog]` - Type annotations for `servicecatalog` service.
- `boto3-stubs[servicediscovery]` - Type annotations for `servicediscovery` service.
- `boto3-stubs[ses]` - Type annotations for `ses` service.
- `boto3-stubs[sesv2]` - Type annotations for `sesv2` service.
- `boto3-stubs[shield]` - Type annotations for `shield` service.
- `boto3-stubs[signer]` - Type annotations for `signer` service.
- `boto3-stubs[sms]` - Type annotations for `sms` service.
- `boto3-stubs[sms-voice]` - Type annotations for `sms-voice` service.
- `boto3-stubs[snowball]` - Type annotations for `snowball` service.
- `boto3-stubs[sns]` - Type annotations for `sns` service.
- `boto3-stubs[sqs]` - Type annotations for `sqs` service.
- `boto3-stubs[ssm]` - Type annotations for `ssm` service.
- `boto3-stubs[sso]` - Type annotations for `sso` service.
- `boto3-stubs[sso-oidc]` - Type annotations for `sso-oidc` service.
- `boto3-stubs[stepfunctions]` - Type annotations for `stepfunctions` service.
- `boto3-stubs[storagegateway]` - Type annotations for `storagegateway` service.
- `boto3-stubs[sts]` - Type annotations for `sts` service.
- `boto3-stubs[support]` - Type annotations for `support` service.
- `boto3-stubs[swf]` - Type annotations for `swf` service.
- `boto3-stubs[textract]` - Type annotations for `textract` service.
- `boto3-stubs[transcribe]` - Type annotations for `transcribe` service.
- `boto3-stubs[transfer]` - Type annotations for `transfer` service.
- `boto3-stubs[translate]` - Type annotations for `translate` service.
- `boto3-stubs[waf]` - Type annotations for `waf` service.
- `boto3-stubs[waf-regional]` - Type annotations for `waf-regional` service.
- `boto3-stubs[wafv2]` - Type annotations for `wafv2` service.
- `boto3-stubs[workdocs]` - Type annotations for `workdocs` service.
- `boto3-stubs[worklink]` - Type annotations for `worklink` service.
- `boto3-stubs[workmail]` - Type annotations for `workmail` service.
- `boto3-stubs[workmailmessageflow]` - Type annotations for `workmailmessageflow` service.
- `boto3-stubs[workspaces]` - Type annotations for `workspaces` service.
- `boto3-stubs[xray]` - Type annotations for `xray` service.
