var AWS = require('aws-sdk');
var aws_region = "us-east-1";

//add function name
var function_name = '';

//add your access and secret access key
var creds = new AWS.Credentials({ accessKeyId: '', secretAccessKey: ''});


AWS.config.update({ region: aws_region });

var lambda = new AWS.Lambda({apiVersion: '2015-03-31'});

// sample payload
var payload_obj = { name: "John", age: 30, city: "New York" };
var payload_json = JSON.stringify(payload_obj);



var params = {
                 FunctionName: function_name,
                 InvocationType: 'RequestResponse',
                 LogType: 'Tail',
                 Payload: payload_json
             };

lambda.invoke(params, function(err, data) {
if (err) console.log(err, err.stack); // an error occurred
else     console.log(data);           // successful response
});
