function sleep(d){
  for(var t = Date.now();Date.now() - t <= d;);
}

var amqp = require('amqp');  
  
var connection = amqp.createConnection({url: "amqp://hardchain:pswHd@localhost:5672/%2F"});  
// Wait for connection to become established.
connection.on('ready', function () {  
    var callbackCalled = false;  
    exchange = connection.exchange('xxx', {type: 'direct',autoDelete:false});  
    connection.queue("electron3",{autoDelete:false}, function(queue){  
        queue.bind('xxx','electron3', function() {  
            exchange.publish('electron3', 'this is message is testing ......');  
             callbackCalled = true;  
        });  
      
        queue.subscribe(function (message) {  
          console.log('At 5 second recieved message is:'+ message.data);  
        });  
      
    });  
});  
